from abc import ABC

class Abstract(ABC):
    address=None

    def __init__(self, address):
        self.address=address

    def calculateFreqs(self):
        pass
class ListCount(Abstract):

    def calculateFreqs(self):
        na = 1
        count = 0
        oList = list()
        holder = list()
        list2 = list()
        with open(self.address, 'r') as file:
            a = file.read()
            for char in a:
                if char.isalpha():
                    char = char.lower()
                    list2.append(char)
                    if char not in holder:
                        holder.append(char)
                        holder.sort()
            for charr in holder:
                for uniqueChar in list2:
                    if charr == uniqueChar:
                        count += 1
                if na == 1:
                    oList.append(f"List-> {charr}"+"  "+f"Resulting List -> {charr} = {count}")
                else:
                    oList.append(f"       {charr}" + "  " + f"                  {charr} = {count}")
                na = 0
                count = 0
        for items in oList:
            print(items)
class DictCount(Abstract):

    def calculateFreqs(self):
        holder = dict()
        with open(self.address, 'r') as file:
            content = file.read()
            for char in content:
                if char.isalpha():
                    char = char.lower()
                    if char in holder:
                        holder[char] += 1
                    else:
                        holder[char] = 1
        number = 1
        sorted_char = sorted(holder.keys())
        for sChar in sorted_char:
                if number == 1:
                    print(f"Dict -> {sChar}" + "  " + f"Updated Dist -> {sChar} = {holder[sChar]}")
                else:
                    print(f"        {sChar}" + "  " + f"                {sChar} = {holder[sChar]}")
                number = 0
file_adress = "weirdWords.txt"
listCo = ListCount(file_adress)
dictCo = DictCount(file_adress)
listCo.calculateFreqs()
print("-------------------------------------------------")
dictCo.calculateFreqs()
