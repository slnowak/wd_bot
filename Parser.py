# coding=utf-8
from Grade import Grade
from GradeBookEntry import GradeBookEntry
from GradeType import GradeType

__author__ = 'novy'
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, html_content, serializer, filename, notifier):
        self.html_content, self.serializer, self.filename = html_content, serializer, filename
        self.notifier = notifier

    def get_table_rows(self):
        soup = BeautifulSoup(self.html_content)
        rows = [row for row in soup.find_all('tr', {'class': 'gridDane'}) if row.contents[1].text != u'Wykład']
        return [row for row in rows if row.contents[2].text.rstrip()]

    def parse_single_grade(self, text):
        if text.strip():
            mark, date = text[0:3], text[3:]
            return Grade(mark, date)
        return None

    def parse_grades(self, row):
        final_grade = self.parse_single_grade(row.contents[2].text)
        grades = tuple([self.parse_single_grade(row.contents[i].text) for i in xrange(3, 6)])
        return final_grade, grades

    def parse_grade_book_entry(self, row):
        subject, grade_type = row.contents[0].text, GradeType.from_translated_str(row.contents[1].text)
        final_grade, grades = self.parse_grades(row)
        lecturer = row.contents[6].text
        return GradeBookEntry(subject, lecturer, grade_type, final_grade, grades)

    def parse(self):
        rows = self.get_table_rows()
        grade_book_entry_dict = self.serializer.deserialize(self.filename)
        grade_book_entry_list = []

        for row in rows:
            grade_book_entry = self.parse_grade_book_entry(row)

            if not grade_book_entry in grade_book_entry_dict:
                self.notifier.notify_about_new_grade(grade_book_entry)
            grade_book_entry_list.append(grade_book_entry)

        grade_book_entry_dict.update(grade_book_entry_list)
        self.serializer.serialize(self.filename, grade_book_entry_dict)





