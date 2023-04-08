# cs5293sp23-project1
# The Redactor

Whenever sensitive information is shared with the public, the data must go through a redaction process. That is, all sensitive names, places, and other sensitive information must be hidden. Documents such as police reports, court transcripts, and hospital records all contain sensitive information. Redacting this information is often expensive and time consuming.
From Enrom email dataset, few files were used for testing the project. The sensitive information like names, date, phone numbers, address, gender are redacted. The redacted information is stored in a new directory. Also, all the statistics of the redacted data is stored in stats file.

## Author Details
* Name: Akhila Mora
* Email: akhila.mora@ou.edu
* Student ID: 113531532

## Demo Video
![Final](https://user-images.githubusercontent.com/113566461/229979723-38b96010-38ef-4b7c-9064-d14640feec78.gif)

## Getting Started

Below are the starting steps which needs to be done before starting the project:
* In Ubuntu, connect to the VM instance using the following command:
```
ssh -i [path-to-private-key] [username]@[instance-external-ip]
```
* Create a tree structure as shown below in VM instance:
* ![image](https://user-images.githubusercontent.com/113566461/229966821-0577dc91-024a-4856-a767-0d4d0c130712.png)
* We need to have python installed in the instance. If not, install it using below command:
```
sudo apt-get install python3
```
* To redact data, five sample files were taken from Enrom email dataset files and are stored in docs/ folder as File 1.txt, File 2.txt, File 3.txt, File 4.txt, File 5.txt

### Packages

* spacy
* nltk
* os
* sys
* re
* glob
* argparse

## Executing program

Below is the detailed explanation on how to run the project:
* Clone the project into your instance:
```
git clone https://github.com/moraakhila/cs5293sp23-project1.git
```
* Change the current working directory to cloned repository:
```
cd cs5293sp23-project1
```
* Create a virtual environment
```
pipenv install
```
* Activate virtual environment
```
pipenv shell
```
* Install necessary packages
```
pipenv install nltk
pipenv install spacy
pipenv run python -m spacy download en_core_web_md
pipenv install pytest
```
* Run the project using readctor.py
```
pipenv run python redactor.py --input '*.txt'  --names --dates --phones --genders --address --output 'files/' --stats stderr
```
or
```
pipenv run python redactor.py --input '*.txt'  --names --dates --phones --genders --address --output 'files/' --stats stats
```
* By running the program using above command, it will generate redacted files with an extension .redacted and save all the files in files/ folder. Screenshot of redacted files folder:
* ![image](https://user-images.githubusercontent.com/113566461/229969365-2b808578-c0a2-45d4-9df1-c3b51573c786.png)
* Run pytests using below command:
```
pipenv run python -m pytest -v
```

## Functions
There is one file named redactor.py which consists of all the logic for redacting the input files:
* arg_function()
   * It takes arguments using args parameter. It extracts input_file, name, date, phone, gender, address, ouput_dir, stats_file from args parameter. It creates an output directory and uses glob to search for file paths. It calls redactor_function to redact sensitive information.
* name_redact()
   * This function redacts names that are present in the file using nltk, spacy and en_web_core_md module.  It returns redacted text and also writes statistics of redacted data to stats file. Most of the names are redacted as nltk and spacy are used.
* gender_redact()
   * This function redacts gender based on gender list. This list consists of all the words that are used to identify gender. It uses nltk to tokenize words, sentences and then identify gender. It returns redacted text and also writes statistics of redacted data to stats file. I considered maximum of the words that are used to classify gender. If any other word that represents gender is missing, that will not be redacted.
* date_redact()
   * This function redacts dates that are present in the file using spacy, en_web_core_md module and regex pattern. It returns redacted text and also writes statistics of redacted data to stats file. Almost all commonly used date formats were considered, and if any format is missing, it is not possible to redact those dates.
* phone_redact()
   * This function redacts phone numbers that are present in the file using regex patterns. If a phone number matches any pattern in the list, it will be redacted. It returns redacted text and also writes statistics of redacted data to stats file. Almost all commonly used phone number formats were considered, and if any format is missing, it is not possible to redact those phone numbers.
* address_redact()
   * This function redacts address that are present in the file using regex and a list that contains all US states. It returns redacted text and also writes statistics of redacted data to stats file.
* store_output()
   * This function takes output directory, output data and file name as parameters. It stores an output in the output directory. It changes the output filename and adds .redacted to it. It writes all the redacted data to output file.
* redactor_function()
   * This function takes file; name, gender, date, phone, address flags; output and stats as parameters. It calls all the above listed functions and redacts each file present in the docs directory. It also updates stats file based on the input given to stats. If stats is given as stderr, it stores error array as stderr. Else it stores statistics to the file name given through command prompt.For example:
   * Here, stderr stores error data 
   ```
   pipenv run python redactor.py --input '*' --dates --output 'files/' --stats stderr
   ```
   * Here, stats stores statistics of the data
   ```
   pipenv run python redactor.py --input '*' --dates --output 'files/' --stats stats
   ```
* __main__ function()
   * Atleast one of the redaction flags must be given to run the program. It is not necessary to give all the redaction flags. Below is the command to redact only dates:
   ```
   pipenv run python redactor.py --input '*' --dates --output 'files/' --stats stderr
   ```
## Test Cases
For the purpose of testing, I have stored a file(File1.txt) in tests folder. test_redactor.py was used to write test cases of all functions
* test_name_redact(info): This function is used to test name_redact() function. It returns true if names are redacted.
* test_gender_redact(info): This function is used to test gender_redact() function. It returns true if genders are redacted.
* test_date_redact(info): This function is used to test date_redact() function. It returns true if dates are redacted.
* test_phone_redact(info): This function is used to test phone_redact() function. It returns true if phone numbers are redacted.
* test_address_redact(info): This function is used to test address_redact() function. It returns true if addresses are redacted.
* test_redact_filefunc_and_outputfile(): This function checks if the redacted files are stored in the output path or not. If it exist, it returns True.
* There is no test code for arg_function() as it won't return anything. This function is mainly used to extract arguments. 

## Assumptions
For this project, I have made below assumptions:
* I used spacy and nltk to redact names. So, almost all the names are redacted. I believe that, with spacy is redaction is performing correctly.
* All the files must be .txt and all the flags(names, gender, date, phone, address) are not present in every file.
* All the flags must to given while running the program.
* Dates are redacted based on US date format. Dates are redacted based on regex for almost all formats.
* Gender are redacted based on a list which consists of almost all words that are used to define genders. Only these words are redacted.
* There may be names which are not recognized by spacy or nltk. Also, some names are recognized as names by spacy or nltk though they are not names.
* Address is redacted based on the regex. If addres is in the define format, it will be redacted.

## Bugs
There might be some bugs if the assumptions are not correct:
* The output after redacting name is sent as an input to gender function and so on. The redacted files are sent to following functions. This may cause some issues while redacting.
* Some names are considered as names though they are not correct and are redacted by name_redact function.
* If there are no required packages, an error will occur.
* If the address is in different formats, it may not not be redacted.
* If the phone numbers are in any other format apart from US, it will not be redacted.
* There should not be any duplicates in the virtual environments, else it might cause an error.
* I only selected some files from huge dataset. This may not contain all the required flags. 

## Acknowledgments
Below are the resources which I used for this project
* [Github Readme template](https://github.com/matiassingers/awesome-readme)
* [NLTK](https://www.nltk.org/)
* [spacy](https://spacy.io/usage/spacy-101#whats-spacy)
* [US states](https://www.faa.gov/air_traffic/publications/atpubs/cnt_html/appendix_a.html)
* [Regular Expression](https://www.w3schools.com/python/python_regex.asp)
* [spacy](https://realpython.com/natural-language-processing-spacy-python/)
