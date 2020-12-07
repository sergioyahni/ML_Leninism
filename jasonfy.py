import json

'''
import text file
'''

def create_dct(year, publication, txt, is_lenin):
    lst = []
    nlst =[]
    f = open(txt)
    lines = list(f.readlines())
    f.close()
    
    '''
    clean lines
    '''
    for line in lines:
        if line != '\n': 
            line = line[:-1]
            lst.append(line)
    
    for item in lst:
        dct = {}
        dct['year'] = year
        dct['publication'] = publication
        dct['statement'] = item
        dct['is_lenin'] = is_lenin
        nlst.append(dct)
    
    return nlst

data = create_dct(1914, 'the_right_of_nations_to_self_determination', '1914_the_right_of_nations_to_self_determination', 1)


with open('lenin_smith.json', 'w') as outfile:
    json.dump(data, outfile)
