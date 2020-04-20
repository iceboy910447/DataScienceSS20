import sys

class ListKeeper:
    def __init__(self):
        self.combined{"example":[1,2,3,4,5]}        #creating new dictionary
        """
        self.names = [example]
        self.lists = [[1,2,3,4,5]]
        temp = zip(self.names,self.lists)           #combining both Lists to one
        self.combined = dict(temp)                  #using combined List to create Dictonary
        """
    def show(self):
        return list(self.combined.keys())
        # return self.names
    def add(self,name, liste):
        self.combined[name] = liste                 #adding list to dictionary with key
        """
        self.names = self.names + name
        self.lists.append(list)
        temp = zip(self.names,self.lists)           #combining both Lists to one
        self.combined = dict(temp)                  #using combined List to create Dictonary
        """
    def delete(self,name):
        self.combined.pop(name)

        #Ind_Num = self.names.index(name)
        #self.lists.pop(Ind_Num)
    def append(self,name,liste):
        self.combined[name].extend(liste)
    def sort(self,name):
        return self.combined[name].sort()

        
