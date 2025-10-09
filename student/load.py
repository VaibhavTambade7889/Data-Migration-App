import csv

from myio.myinput import get_rno, get_name, get_per


def load_from_csv(filepath):
    L =[]
    fr = open(filepath, "r")
    reader = csv.reader(fr)
    L = list(reader)      #list() method reads from object which is pointing to student.csv and returens list of list
    del L[0]        #here I am deleting Header row ["RNO", "NAME", "PER"]
    fr.close()
    return L

#Preparing List of List Student records from user
def load_from_user(n):
    L =[]

    for i in range(n):
        rno  = get_rno()
        name = get_name()
        per  = get_per()
        TL = [rno , name, per] # Packing of List TL=[101, 'AAA', 60]

        L.append(TL)

    return L