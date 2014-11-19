# coding=utf-8
from enum import Enum

__author__ = 'novy'


class GradeType(Enum):
    recitation = 1
    laboratory = 2
    exam = 3
    final = 4
    language_course = 5

    def __unicode__(self):
        return self._name_.title().replace('_', ' ')

    @staticmethod
    def from_translated_str(name):
        names = {
            u'Ćwiczenia laboratoryjne': GradeType.laboratory,
            u'Ćwiczenia audytoryjne': GradeType.recitation,
            u'Egzamin': GradeType.exam,
            u'Ocena końcowa': GradeType.final,
            u'Lektorat': GradeType.language_course
        }
        return names[name]