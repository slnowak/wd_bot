__author__ = 'novy'


class Grade(object):
    def __init__(self, mark, date):
        self.mark, self.date = mark, date

    def __key(self):
        return self.mark, self.date

    def __eq__(self, y):
        return self.__key() == y.__key()

    def __hash__(self):
        return hash(self.__key())

    def __unicode__(self):
        return 'Mark: ' + unicode(self.mark) + '\t' + 'Date: ' + self.date
