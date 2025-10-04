from importlib import resources

import student
from config.csvconf.configuration import FILENAME
from student.load import load_from_csv
from student.save import save_to_csv
from student.show import display_student_information

print("Welcome to Data Migration App")


'''
    #Test Code : save_to_csv
    L = [[101, 'AAA', 60], [102, 'BBB', 70], [103, 'CCC', 80]]
    save_to_csv(FILENAME, L)
    
    #Test Code : load_from_csv
    L = load_from_csv(FILENAME)
    display_student_information(L)    
    
'''
