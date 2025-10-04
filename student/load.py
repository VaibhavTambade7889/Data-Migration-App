import csv


def load_from_csv(filepath):
    L =[]
    fr = open(filepath, "r")
    reader = csv.reader(fr)
    L = list(reader)      #list() method reads from object which is pointing to student.csv and returens list of list
    del L[0]        #here I am deleting Header row ["RNO", "NAME", "PER"]
    fr.close()
    return L
