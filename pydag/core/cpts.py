from pydag.core.orderedSet import OrderedSet


class CPTs():

    def __init__(self, cpts=OrderedSet()):
        self.iterCounter = -1
        self.cpts = cpts

    def __str__(self):
        toPrint = ""
        toPrint = toPrint + "{ "
        for cpt in self.cpts:
            toPrint = toPrint + "P("
            for h in cpt.getHead():
                toPrint = toPrint + h.__str__() + ","
            toPrint = toPrint[0:-1]
            toPrint = toPrint + "|"
            for t in cpt.getTail():
                toPrint = toPrint + t.__str__() + ","
            toPrint = toPrint[0:-1]
            toPrint = toPrint + ")"
            toPrint = toPrint + ","
        toPrint = toPrint[0:-1]
        toPrint = toPrint + " }"
        return toPrint

    def __iter__(self):
        return self

    def next(self):
        if self.iterCounter < len(self.cpts) - 1:
            self.iterCounter += 1
            return self.cpts[self.iterCounter]
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self.cpts[key]

    def __len__(self):
        return len(self.cpts)

    def copy(self):
        copiedCPTs = CPTs()
        copiedCPTs.setCPTs(self.getCPTs().copy())
        return copiedCPTs

    def add(self, cpt):
        self.cpts.add(cpt)

    def remove(self, cpt):
        self.cpts.remove(cpt)

    def removeCPTs(self, cpts):
        for cpt in cpts:
            self.remove(cpt)

    def removeCPTsByAllHeadVariables(self, headVariables):
        for v in headVariables:
            self.removeCPTsByHeadVariables([v])

    def removeCPTsByHeadVariables(self, head):
        cpts = self.getCPTsByHead(head)
        for c in cpts:
            self.remove(c)

    def setCPTs(self, cpts):
        self.cpts = cpts

    def getCPTs(self):
        return self.cpts

    def getCPTsByHead(self, head):
        return CPTs(OrderedSet([cpt for cpt in self.getCPTs() if cpt.getHead() == head]))

    def getCPTsByTail(self, tail):
        return CPTs(OrderedSet([cpt for cpt in self.getCPTs() if cpt.getTail() == tail]))

    def getCPTsByVariable(self, variable):
        return CPTs(OrderedSet([cpt for cpt in self.getCPTs() if (variable in cpt.getHead()) or (variable in cpt.getTail())]))

    def getVariables(self):
        result = []
        for cpt in self.getCPTs():
            result.extend(cpt.getVariables())
        return OrderedSet(result)
