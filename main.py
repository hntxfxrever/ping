#мой ад!

from random import choice
class Doctor():
    def __init__ (self, name, pat, illnes):
        self.name = name
        self.pat = pat
        self.illnes = illnes

    def info (self):
        print ('Врач', self.name, ',', self.pat )
    def diff (self):
        print (self.pat - self.illnes)
    def SCF ():
        a = [ "The puppet is dead." , "However, if he wasn't completely dead, it would be sure sign that he was still alive.", "The puppet is still alive.", "However, if hewere not alive, it would be a sure sign that he was actually dead."]
        s = choice(a)
    def tp (self, nameP):
        if len(nameP) %2 == self.pat % 2:
            print (True)
            self.pat = self.pat + 1
        else:
            print (False)

d = Doctor('Raven', 3, 5)
d.info()
d.diff()
d.SCF()
d.tp('Pinoccio')
d.tp('Punch')
h.info()



