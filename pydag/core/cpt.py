from pydag.core.orderedSet import OrderedSet


class CPT:

    """
    The CPT class represents a Conditional Probability Table (CPT) - a discrete probability distribution in a tabular format.
    A CPT will be denoted as P(X|Y), where X and Y are list of *Variables*. Moreover, X can be called *head* and *Y* tail.
    The CPT itself and its operations follows the CPT structure [C.J. Butz, W. Yan, P. Lingras and Y.Y. Yao, The CPT Structure of Variable Elimination in Discrete Bayesian Networks, Advances in Intelligent Information Systems, SCI 265, Z.W. Ras and L.S. Tsay (Eds.), Springer, 245-257, 2010.], meaning that the 'bar' is always kept. For instance, P(a|b,c) * P(b|c) = P(a,b|c).
    Among other common operations with a CPT, this class implements multiplication, division and marginalization.
    """

    def __init__(self):
        """
        Input: (None)
        Output: (None)
        Description: The constructor only creates the members of the class. The *head* is a list with *Variable*, representing the left hand side (LHS) of a CPT. The *tail* is also a list with *Variable*, representing the right hand side (RHS) of a CPT. A *table* is a *dictionary* where the keys are *tuples* representing rows (configurations or combinations) of domain values. For example, P(a|b) with head Variable("a") and tail Variable("b"), both binary, could have a table {(0,0): 0.7, (0,1): 0.3, (1,0):0.2, (1,1):0.8}.
        """
        self.head = OrderedSet()
        self.tail = OrderedSet()
        self.table = {}

    def __str__(self):
        """
        Input: (None)
        Output: printStr (str)
        Description: Special function in Python called when a CPT is passed to "print" function. Then, it beautifully prints a CPT, showing the head and tail variables as well as its table.
        """
        printStr = ""
        printHead = ""
        for v in self.getHead():
            printHead = printHead + v.__str__() + " "
        printHead.strip()
        printTail = ""
        for v in self.getTail():
            printTail = printTail + v.__str__() + " "
        printTail.strip()
        if len(printTail) == 0:
            printStr = printStr + "P (" + printHead + ")"
        else:
            printStr = printStr + "P (" + printHead + "| " + printTail + ")"
        printStr = printStr + "\n"
        table = ""
        for key in self.getTable():
            table = table + \
                key.__str__() + " => " + self.getTable()[key].__str__()
            table = table + "\n"
        printStr = printStr + table
        return printStr

    def __len__(self):
        """
        Input: (None)
        Output: (int)
        Description: Special function in Python called when a CPT is passed to "len" function. The number of rows (keys of the dictionary) in the *table* is the length of the CPT.
        """
        return len(self.getTable())

    def __eq__(self, other):
        trueFlag = True
        trueFlag = trueFlag and (len(self.getHead()) == len(other.getHead()))
        trueFlag = trueFlag and (len(self.getTail()) == len(other.getTail()))
        trueFlag = trueFlag and (
            len([v for v in self.getHead() if v in other.getHead()]) == self.getHead())
        trueFlag = trueFlag and (
            len([v for v in self.getTail() if v in other.getTail()]) == self.getTail())
        trueFlag = trueFlag and (self.getTable() == other.getTable())
        return trueFlag

    def __hash__(self):
        head = tuple(v for v in self.getHead())
        tail = tuple(v for v in self.getTail())
        return hash(head + tail)

    def copy(self):
        """
        Input: (None)
        Output: copiedCPT (CPT)
        Description: Creates a copy of a CPT by coping its head, tail and table into a new instance of a CPT.
        """
        copiedCPT = CPT()
        copiedCPT.head = self.getHead()[:]
        copiedCPT.tail = self.getTail()[:]
        copiedCPT.table = self.getTable().copy()
        return copiedCPT

    def add(self, key, value):
        """
        Input: key (tuple), value (float)
        Output: (None)
        Description: Add one row to the table by creating a new key to value entry in the dictionary of the table.
        """
        self.table[key] = value

    def get(self, key):
        """
        Input: key (tuple)
        Output: (float)
        Description: Return the value of a given row on the *table*.
        """
        return self.getTable()[key]

    def set(self, key, value):
        """
        Input: value (tuple)
        Output: (None)
        Description: Set the value of a given row on the *table*.
        """
        self.table[key] = value

    def setHead(self, head):
        """
        Input: head (list[Variable])
        Output: (None)
        Description: Set a new *head*.
        """
        self.head = head

    def getHead(self):
        """
        Input: (None)
        Output: (list[Variable])
        Description: Returns the current *head*.
        """
        return self.head[:]

    def getHeadAsVarsTuple(self):
        """
        Input: (None)
        Output: (tuple)
        Description: Return a *tuple* containing the name (str) of all variables in the *head*.
        """
        return tuple([v.getName() for v in self.getHead()])

    def setTail(self, tail):
        """
        Input: tail (list[Variable])
        Output: (None)
        Description: Set a new *tail*.
        """
        self.tail = tail

    def getTail(self):
        """
        Input: (None)
        Output: (list[Variable])
        Description: Returns the current *tail*.
        """
        return self.tail[:]

    def getVariables(self):
        """
        Input: (None)
        Output: (list[Variable])
        Description: Returns all variables in the CPT by concatening the *head* and the *tail*. This is useful when trying to use a global reference indice for the variable. For example, if head = [Variable("a")] and tail = [Variable("b"),Variable("c")] in a global reference for Variable("b") would be 1, since *variables* = (Variable("a"),Variable("b"),Variable("c")).
        """
        return self.getHead()[:] + self.getTail()[:]

    def hasVariable(self, variable):
        """
        Input: variable (Variable)
        Output: (None)
        Description: Check if given variable is within the CPT.
        """
        return (variable in self.getHead()) or (variable in self.getTail())

    def getTable(self):
        """
        Input: (None)
        Output: table (dict[tuple] = float)
        Description: Returns the current *table*.
        """
        return self.table.copy()

    def setTable(self, table):
        """
        Input: table (dict[tuple] = float)
        Output: (None)
        Description: Set a new *table*.
        """
        self.table = table

    def getGlobalReferenceVarInd(self, variable):
        """
        Input: variable (Variable)
        Output: result (int)
        Description: Return the index of a variable on a global reference of the table, that is the index after putting head and tail variables together.
        For example: if head = [Variable("a")] and tail = [Variable("b"),Variable("c")], the global reference index of Variable("b") is 1.
        """
        result = -1
        try:
            result = self.getVariables().index(variable)
        except ValueError:
            pass
        return result

    def __mul__(self, other):
        """
        Input: other (CPT)
        Output: cptResult (CPT)
        Description: Special function in Python called when a CPT is multiplied by another one using the * operator. The idea of the multiplication is given as follows. First, find the global reference index of matching variables between the two CPTs. Given one row of the first CPT and one of the second CPT, we verify if the values of for each respective matching index is the same. If all of them are the same, we can proceed with the multiplication by calling *constructNewKeyAndValueTableForMul*, which return the new row (key) and multiplied value. If no matching index, that is no matching variables between the tables, is found all rows are multiplied. After the multiplication, the *head* and *tail* of the resultant CPT is constructed by calling *constructNewHeadAndTailForMult*.
        """
        # find matching columns (common variables)
        matchingVarIndexes = [(self.getVariables().index(v), other.getVariables().index(
            v)) for v in self.getVariables() if v in other.getVariables()]
        # helps to keep track of the index for a matching variable on the head
        # in the *other* CPT.
        matchingOtherHeadVarIndexes = [other.getHead().index(
            v) for v in other.getHead() if ((v in self.getHead()) or (v in self.getTail()))]
        # helps to keep track of the index for a matching variable on the tail
        # in the *other* CPT.]
        matchingOtherTailVarIndexes = [len(other.getHead()) + other.getTail().index(
            v) for v in other.getTail() if ((v in self.getHead()) or (v in self.getTail()))]
        # construct the resultant cpt
        cptResult = CPT()
        # multiply each row that has matching domain values for all matching
        # variable columns
        for selfRow in self.getTable():
            for otherRow in other.getTable():
                if len(matchingVarIndexes) > 0:
                    # verify if tables has common variables, if yes, just
                    # multiply on common rows. If not, multiply them all
                    allMatchingVarsHasSameValue = True
                    for matchingVarIndex in matchingVarIndexes:
                        allMatchingVarsHasSameValue = allMatchingVarsHasSameValue and (selfRow[matchingVarIndex[0]] == otherRow[matchingVarIndex[1]])
                    if allMatchingVarsHasSameValue:
                        newKeyAndValue = self.constructNewKeyAndValueTableForMul(other, selfRow, otherRow, matchingOtherHeadVarIndexes, matchingOtherTailVarIndexes)
                        cptResult.add(newKeyAndValue["newKey"], newKeyAndValue["newValue"])
                else:
                    newKeyAndValue = self.constructNewKeyAndValueTableForMul(other, selfRow, otherRow, matchingOtherHeadVarIndexes, matchingOtherTailVarIndexes)
                    cptResult.add(newKeyAndValue["newKey"], newKeyAndValue["newValue"])
        # reorganize the head and tail variables
        newHeadAndTail = self.constructNewHeadAndTailForMult(other)
        cptResult.setHead(newHeadAndTail["newHead"])
        cptResult.setTail(newHeadAndTail["newTail"])
        return cptResult

    def constructNewKeyAndValueTableForMul(self, other, selfRow, otherRow, matchingOtherHeadVarIndexes, matchingOtherTailVarIndexes):
        """
        Input: other (CPT), selfRow (tuple(Variable)), otherRow (tuple(Variable), matchingOtherHeadVarIndexes (list[int]), matchingOtherTailVarIndexes (list[int]))
        Output: (dict[str] = (tuple)/float)
        Description: A helper function that do the multiplication first by creating a new row (configuration). This new combination is done by first concatening the values related to the head of *self* CPT with the ones related to the tail of *other* CPT. Later, we also concatane the tail of *self* CPT and the tail of *other*. Finally, the new value is obtained by multiplying the values of *self* and *other* rows.
        """
        listSelfRow = list(selfRow)
        listOtherRow = list(otherRow)
        newKey = []
        varsInHead = []
        for (counter, value) in enumerate(self.getHead()):
            newKey.append(listSelfRow[counter])
            varsInHead.append(value)
        for (counter, value) in enumerate(other.getHead()):
            if value not in varsInHead:
                newKey.append(listOtherRow[counter])
                varsInHead.append(value)
        varsInTail = []
        for (counter, value) in enumerate(self.getTail()):
            if value not in varsInHead:
                newKey.append(listSelfRow[counter + len(self.getHead())])
                varsInTail.append(value)
        for (counter, value) in enumerate(other.getTail()):
            if (value not in varsInTail) and (value not in varsInHead):
                newKey.append(listOtherRow[counter + len(other.getHead())])
                varsInTail.append(value)
        newKey = tuple(newKey)
        # multiply to get the new value
        newValue = self.get(selfRow) * other.get(otherRow)
        return {"newKey": newKey, "newValue": newValue}

    def constructNewHeadAndTailForMult(self, other):
        """
        Input: other (CPT)
        Output: (dict[str] = [Variable])
        Description: A helper function that construct the head and tail of the resultant CPT from a multiplication. The head is done by concatening the first the head of the first CPT (*self*) then later the second CPT (*other*). The *tail* also is done by concatening first the tail of the *self* CPT and later the *other*, but ignoring variables already in the *head*.
        """
        newHead = self.getHead() + other.getHead()
        newTailSelf = [v for v in self.getTail() if v not in newHead]
        # an extra check if the variable was already added to the tail because
        # it's on the tail of the *self* CPT.
        newTailOther = [v for v in other.getTail() if (
            (v not in newHead) and (v not in newTailSelf))]
        newTail = newTailSelf + newTailOther
        return {"newHead": newHead, "newTail": newTail}

    def constructNewHeadAndTailForDiv(self, other):
        """
        Input: other (CPT)
        Output: (dict[str] = [Variable])
        Description: A helper function that construct the head and tail of the resultant CPT from a division. The head is done by selecting all variables in the *head* of the first CPT (*self*) but not in the *head* of the second CPT (*other*). The *tail* is done by concatening first the head of the *self* CPT, then the tail of the *self* CPT, and finally the tail of the *other* CPT, but ignoring variables already in the *head*.
        """
        newHead = [v for v in self.getHead() if v not in other.getHead()]
        newTailSelf = [v for v in (self.getHead() + self.getTail()) if v not in newHead]
        newTailOther = [v for v in (other.getHead() + other.getTail()) if ((v not in newHead) and (v not in newTailSelf))]
        newTail = newTailSelf + newTailOther
        return {"newHead": newHead, "newTail": newTail}

    def __div__(self, other):
        """
        Input: other (CPT)
        Output: cptResult (CPT)
        Description: Special function in Python called when a CPT is divided by another one using the / operator. Here, the idea is to replace each value of each row of the second CPT by the value divided by one. Later, we proceed with normal multiplication between the first (*self*) CPT and the second (*other*) CPT.
        """
        tempDivCpt = CPT()
        tempDivCpt.setHead(other.getHead())
        tempDivCpt.setTail(other.getTail())
        # divide other rows by 1
        for key in other.getTable():
            newValue = 0
            if other.getTable()[key] != 0:
                newValue = 1.0 / other.getTable()[key]
            tempDivCpt.add(key, newValue)
        cptResult = self * tempDivCpt
        # reorganize the head and tail variables
        newHeadAndTail = self.constructNewHeadAndTailForDiv(other)
        cptResult.setHead(newHeadAndTail["newHead"])
        cptResult.setTail(newHeadAndTail["newTail"])
        return cptResult

    def marginalize(self, variables):
        """
        Input: variables (list[Variables] or Variable)
        Output: cptResult (CPT)
        Description: Marginalize a CPT on the given variables. Given the variables to be summed out (given by taking all variables and removing the ones to be marginalized), the idea is to remove every column (a position in a tuple) of each configuration (row) from the table. Next, we sum the rows that are equal.
        """
        if type(variables) != OrderedSet:
            variables = OrderedSet(variables)
        # a copy of the current CPT that can be modified.
        cptResult = self.copy()
        # find out variables to be summed out, in order to construct the new
        # table
        sumOutVars = [v for v in self.head if v not in variables]
        for v in sumOutVars:
            # index of the column to be removed in each configuration (row)
            vInd = cptResult.getGlobalReferenceVarInd(v)
            newTable = {}
            for row in cptResult.getTable():
                listRow = list(row)
                del listRow[vInd]
                tupleRow = tuple(listRow)
                # Sum the rows which are equal.
                if tupleRow in newTable:
                    newTable[tupleRow] = newTable[
                        tupleRow] + cptResult.get(row)
                else:
                    newTable[tupleRow] = cptResult.get(row)
            cptResult.setTable(newTable)
            # re construct the head variables
            newHead = cptResult.getHead()
            newHead.remove(v)
            cptResult.setHead(newHead)
        return cptResult

    def removeRows(self, evidence):
        """
        Input: evidence (dict[Variable] = str/int)
        Output: (None)
        Description: Remove all rows from this CPT that has given value for given variable.
        """
        for evidenceVar in evidence:
            varInd = self.getGlobalReferenceVarInd(evidenceVar)
            for row in self.getTable():
                if row[varInd] == evidence[evidenceVar]:
                    del self.table[row]

    def keepRows(self, evidence):
        """
        Input: evidence (dict[Variable] = str/int)
        Output: (None)
        Description: Keeps all rows from this CPT that has given value for given variable. All other ones are removed.
        """
        for evidenceVar in evidence:
            varInd = self.getGlobalReferenceVarInd(evidenceVar)
            for row in self.getTable():
                if row[varInd] != evidence[evidenceVar]:
                    del self.table[row]

    def removeColumns(self, columnIndices):
        """
        Input: columnIndices (OrderedSet(int))
        Output: (None)
        Description: Remove all column in each row of the table of given indices.
        """
        for i in columnIndices:
            self.removeColumn(i)

    def removeColumn(self, columnInd):
        """
        Input: columnInd (int)
        Output: (None)
        Description: Remove a column in each row of the table of given indice.
        """
        newTable = {}
        for row in self.getTable():
            rowList = list(row)
            del rowList[columnInd]
            newTable[tuple(rowList)] = self.get(row)
        self.setTable(newTable)

    def removeTailVariable(self, variable):
        """
        Input: variable (Variable)
        Output: (None)
        Description: Remove a variable from Tail.
        """
        self.tail.remove(variable)

    def removeHeadVariable(self, variable):
        """
        Input: variable (Variable)
        Output: (None)
        Description: Remove a variable from Head.
        """
        self.head.remove(variable)
