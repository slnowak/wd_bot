import pickle

__author__ = 'novy'


class Serializer(object):
    @staticmethod
    def serialize(filename, objects):
        with open(filename, 'wb+') as f:
            pickle.dump(objects, f)

    @staticmethod
    def deserialize(filename):
        try:
            f = open(filename, 'rb')
            data = pickle.load(f)
            f.close()
            return data
        except IOError:
            return set()
