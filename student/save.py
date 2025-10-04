import csv
'''
    This method Save student infomation in CSV File 
    Input : filepath - Tts path where file is created 
    L - List of List  which has students infromation 
    Output : None    
'''

def save_to_csv(filepath, list_of_list):
    fw = open(filepath, 'w', newline='')
    writer = csv.writer(fw)

    header = ['RNO', 'NAME', 'PER']
    writer.writerow(header)

    for row in list_of_list:
        writer.writerow(row)

    fw.close()
    print(f"Data is Saved Successfully in '{filepath}'")