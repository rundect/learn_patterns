class SomeClass:
    def __eq__(self, other):
        if other is None:
            return True

    def __repr__(self):
        return 'Object is'

    def __str__(self):
        return 'Object is'


spam = SomeClass()
print(spam)
print(spam == None)
print(spam is None)
