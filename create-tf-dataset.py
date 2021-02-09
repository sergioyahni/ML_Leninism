import os
import tarfile

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

def create_dts(txt, code):
    #read text   
    f = open(txt)
    lines = list(f.readlines())
    f.close()
    
    '''
    Process the text 
    (1) Clean out non alphanumeric characters
    (2) Clean out stop-words
    (3) Save each line into a separate folder
    '''
    counter = 0
    for line in lines:
        if line != '\n':
            text = clean_text(line)
            save_file(text, code, counter)
        counter += 1

def clean_text(text):
    '''
    Credit: https://machinelearningmastery.com/clean-text-machine-learning-python/
    '''
    # nltk.download('punkt')

    # load text. Optional
    '''
    filename = 'lenin_clean.txt'
    file = open(filename, 'rt')
    text = file.read()
    file.close()
    '''
    # split into words by white space
    tokens = word_tokenize(text)
    
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    
    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    
    return ' '.join(words)
    
def save_file(content, fcode, counter):
    if fcode == 1: 
        folder = "/home/sergio/Dev/Lenin Project/dataset/lenin_language_dataset/pos/"
    elif fcode == 0: 
        folder = "/home/sergio/Dev/Lenin Project/dataset/lenin_language_dataset/neg/"
    
    file_to_save = folder + str(counter) + '.txt'
    f = open(file_to_save, "w")
    f.write(content)
    f.close()

def tardir(path="/home/sergio/Dev/Lenin Project/dataset/lenin_language_dataset", tar_name="lenin_dataset.tar.gz"):
    # Create tar file
    with tarfile.open(tar_name, "w:gz") as tar_handle:
        for root, dirs, files in os.walk(path):
            for file in files:
                tar_handle.add(os.path.join(root, file))

# Create folders
os.mkdir(os.path.join('/home/sergio/Dev/Lenin Project/dataset', 'lenin_language_dataset'))
os.mkdir(os.path.join('/home/sergio/Dev/Lenin Project/dataset/lenin_language_dataset', 'pos'))
os.mkdir(os.path.join('/home/sergio/Dev/Lenin Project/dataset/lenin_language_dataset', 'neg'))

# Call create dataset function
create_dts('is_lenin', 1)
create_dts('not_lenin', 0)

# Call tar function
# Optional
# tardir()


