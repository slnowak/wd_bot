__author__ = 'novy'
# coding=utf-8


class GradeBookEntry:
    def __init__(self, subject, lecturer, grade_type, final_grade, grades):
        self.subject, self.lecturer, self.grade_type = subject, lecturer, grade_type
        self.final_grade, self.grades = final_grade, grades

    def __key(self):
        return self.subject, self.lecturer, self.grade_type, self.final_grade, self.grades

    def __eq__(self, y):
        return self.__key() == y.__key()

    def __hash__(self):
        return hash(self.__key())

    def __unicode__(self):
        str_repr = 'Subject: ' + self.subject + '\n'
        str_repr += ('Type: ' + unicode(self.grade_type) + '\n')
        str_repr += ('Lecturer: ' + self.lecturer + '\n\n')

        str_repr += ('Final note:\t\t\t' + unicode(self.final_grade) + '\n')
        for (grade, attempt) in zip(self.grades, xrange(1, 4)):
            if grade is not None:
                str_repr += ('Attempt ' + unicode(attempt) + ':\t\t\t' + unicode(grade) + '\n')

        return str_repr


