import glob
import nltk

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('words')
nltk.download('maxent_ne_chunker')
nltk.download('averaged_perceptron_tagger')

import re
import spacy
import en_core_web_md
import argparse
import os
import sys

nlp = spacy.load("en_core_web_md")

error_array = []
stats_info = []
us_states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

def arg_function(args):
    
    # extract command line arguments
    input_file = args.input
    name = args.names
    date = args.dates
    phone = args.phones
    gender = args.genders
    address = args.address
    output_dir = args.output
    stats_file = args.stats

    # remove existing stats file
    if os.path.exists(stats_file):
        os.remove(stats_file)
    
    # check if the input file exists or not
    path = os.path.join("docs/",input_file)

    # print(path)
    if not os.path.exists(path) and not input_file.startswith("*"):
        sys.stderr.write("File not found: " + path)
        error_array.append("Error! File not found: " + path)
        return 

    # create output directory
    os.makedirs(output_dir, exist_ok=True)

    # loop through input files and redact
    for file in glob.glob(path):
        # skip non-redactable files
        # print(file)
        if "stats" in file or "stderr" in file or "stdout" in file:
            print("Skipping non-redactable file:", file)
        else:
            redactor_function(file, name, gender, date, phone, address, output_dir, stats_file)

def name_redact(text):
    names = set()
    count = 0
    for sent in nltk.sent_tokenize(text):
        for ch in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(ch,'label') and ch.label() == 'PERSON':
                names.add(' '.join(c[0] for c in ch))

    doc = nlp(text)
    for token in doc.ents:
        if token.label_ == 'PERSON':
            names.add(token.text)

    stats_info.append("\n *****NAMES***** \n")
    for word in names:
        redacted_word = ''.join(u'\u2588' for _ in range(len(word)))
        text = text.replace(word, redacted_word)
        count = count + 1

        stats_info.append(word + "\n")
    stats_info.append("Name count: "+str(count) + "\n")
    return text

def gender_redact(text):
    def_genders = ['girls', 'fiancee', 'dude', 'grandmother', 'man', 'widowers', 'daughter', 'wives', 'women', 'her', 'sisters', "women's", 'goddess', 'spokesman', 'chairman', 'mothers', 'fiance', 'gentlemen', 'fathers', 'mrs', 'widows', 'female', 'himself', 'boy', 'nieces', 'grandson', "he's", 'nephews', 'widow', 'she', 'gentleman', 'daughters', "men's", 'priestess', 'priest', 'dads', 'grandma', 'boyfriends', 'uncles', 'girlfriend', 'lady', 'king', 'nephew', 'prince', 'moms', 'girl', 'herself', 'god', 'heroine', 'grandpa', 'boyfriend', 'husbands', 'brothers', 'chairwoman', 'dad', 'sister', 'princess', 'bride', 'his', 'queens', 'uncle', 'aunt', 'son', 'mother', 'ms', 'widower', 'woman', 'waitress', 'guy', 'wife', 'mom', 'niece', 'he', 'ladies', 'sons', 'spokeswoman', 'male', 'him',"her's", 'men', 'aunts', 'grandfather', "she's", 'boys', 'waiter', 'brother', 'groom', 'girlfriends', 'mr', 'actress', 'father', 'husband', 'granddaughter']
    genders_list = []
    count = 0
    for sentence in sent_tokenize(text):
        for word in word_tokenize(sentence):
            if word.lower() in def_genders:
                genders_list.append(word)
                count = count + 1

    stats_info.append("\n *****Genders***** \n")
    for word in genders_list:
        #print(word)
        exp = '\\b' + word + '\\b'
        text = re.sub(exp,'\u2588' * len(word), text)
        stats_info.append(word + "\n")
    stats_info.append("Gender count: " + str(count) + "\n")
    return text

def date_redact(text):
    count = 0
    doc = nlp(text)
    stats_info.append("\n *****Dates***** \n")
    for entity in doc.ents:
        if entity.label_ == "DATE":
            #print(entity.text)
            text = text.replace(entity.text,'\u2588' * len(entity.text))
            stats_info.append(entity.text + "\n")
            count = count + 1

    date_formats = [
        r'\d{1,2}/\d{1,2}/\d{2,4}', # MM/DD/YYYY or MM/DD/YY or DD/MM/YYYY or DD/MM/YY
        r'\d{4}-\d{1,2}-\d{1,2}', # YYYY-MM-DD or YYYY-DD-MM
        r'\d{1,2}\.\d{1,2}\.\d{2,4}', # MM.DD.YYYY or MM.DD.YY or DD.MM.YYYY or DD.MM.YY
        r'\d{1,2}-\d{1,2}-\d{2,4}' # MM-DD-YYYY or MM-DD-YY or DD-MM-YYYY or DD-MM-YY
    ]

    for date in date_formats:
        match = re.search(date,text)
        text = re.sub(date,lambda m:'\u2588' * len(m.group(0)), text)
        count = count + sum(1 for _ in re.finditer(date,text))
        if match:
            stats_info.append(match.group(0) + "\n")
    stats_info.append("Date count: " + str(count) + "\n")
    return text


def phone_redact(text):
    count = 0
    phone_formats = [
        r"\d{3}[-.]\d{3}[-.]\d{4}",  
        r"[(]\d{3}[(] \d{3}-\d{4}",  
        r"\d{3} \d{3} \d{4}",        
        r"\d{10}",      
        r"\d{3}[.]\d{3}[-.]\d{4}"   
    ]
    stats_info.append("\n *****Phones***** \n")
    for phone in phone_formats:
        matches = re.findall(phone,text)
        for match in matches:
            #print(match)
            text = text.replace(match, '\u2588' * len(match))
            count = count + 1
            stats_info.append(match + "\n")
    stats_info.append("Phone count: " + str(count) + "\n")
    return text

def address_redact(text):
    address_count = 0
    stats_info.append("\n *****Addresses***** \n")
    p1 = re.compile(r"\d{3}\s[a-zA-Z]+\s[a-zA-Z]+")
    p2 = re.compile(r"[a-zA-Z]+(,)?\s+[a-zA-Z]+\s+(?:\d{5}|\b[A-Z]{2}\b)")
    for i,line in enumerate(text.split("\n")):
        if any(k in line for k in us_states.keys()):
            address_count += 1
            text = text.replace(line, '\u2588' * len(line), 1)
        if re.search(p1, line):
            address_count += 1
            text = text.replace(line,'\u2588' * len(line),1)
        elif re.search(p2, line):
            tlist = line.split(" ")
            #print(tlist)
            if set(tlist).intersection(set(us_states.keys())):
                address_count += 1
                text = text.replace(line,'\u2588' * len(line),1)
    stats_info.append("Address count: " + str(address_count) + "\n\n")
    return text

def store_output(output_dir, output_data, file):
    output_filename = file + ".redacted"
    with open(os.path.join(output_dir,output_filename),"w",encoding = "utf-8") as f:
        f.writelines(str(s) for s in output_data)

def redactor_function(file, name, gender, date, phone, address, output, stats):

    # check if the file is non-reductable
    if "stats" in file or "stderr" in file or "stdout" in file:
            print("Skipping non-redactable file:", file)
            return

    redactable_file = os.path.basename(file)

    # Read the file content
    try:
        with open(file, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        error_array.append("Error: File not found\n")
        return
    # print(data) 

    if name:
        result = name_redact(data)
    if gender:
        result = gender_redact(result)
    if date:
        result = date_redact(result)
    if phone:
        result = phone_redact(result)
    if address:
       result = address_redact(result)

    # Write the redacted output to output directory
    store_output(output,result,redactable_file)

    # Update statistics file
    stats_array = [file, "\n", "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", "\n"]
    #print(stats_array)
    if stats == "stderr":
        with open(stats, "a", encoding="utf-8") as f:
            f.writelines(error_array)
    else:
        with open(stats,"a",encoding="utf-8") as f:
            f.writelines(stats_array)
            f.writelines(stats_info)
    stats_info.clear()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type = str, required = True, help = "Files name")
    parser.add_argument("--names", action= "store_true", help = "Names")
    parser.add_argument("--dates", action= "store_true", help = "Date")
    parser.add_argument("--phones", action= "store_true", help = "Phone")
    parser.add_argument("--genders", action= "store_true", help = "Gender")
    parser.add_argument("--address", action= "store_true", help = "Address")
    parser.add_argument("--output", type = str,required = True, help = "Output")
    parser.add_argument("--stats", type = str, required = True, help = "Status")
    args = parser.parse_args()
    if not any([args.names, args.genders, args.dates,args.phones, args.address]):
        print("Please pass atleast one redation type!")
    else:
        arg_function(args)    
