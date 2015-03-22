import collections

class OrderedSet(collections.MutableSet):
    """
    This class was taken from http://code.activestate.com/recipes/576694
    Few methods were added: copy, union, intersection, __getitem__, and __str__
    """

    def __init__(self, iterable=None):
        self.end = end = [] 
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def get(self,key):
        itemInd = self.map.keys().index(key)
        return self.map.keys()[itemInd]

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:        
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=False):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)

    def copy(self):
        return OrderedSet(self)

    def union(self,other):
        newMap = self.map.keys() + other.map.keys()
        return OrderedSet( newMap )

    def intersection(self,other):
        newMap = [v for v in self.map.keys() if v in other.map.keys()]
        return OrderedSet( newMap )

    def __getitem__(self,key):
        return self.map.keys()[key]

    def __str__(self):
        toPrint = ""
        toPrint = toPrint + "{ "
        for elem in self.map.keys():
            if type(elem) == tuple:
                toPrint = toPrint + "("
                for i in elem:
                    toPrint = toPrint + i.__str__() + ","
                toPrint = toPrint[0:-1]
                toPrint = toPrint + ")"
            else:
                toPrint = toPrint + elem.__str__() + " "
        toPrint = toPrint + "}"
        return toPrint
    def remove(self,key):
        self.discard(key)