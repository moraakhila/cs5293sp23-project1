# cs5293sp23-project1
# The Redactor

Whenever sensitive information is shared with the public, the data must go through a redaction process. That is, all sensitive names, places, and other sensitive information must be hidden. Documents such as police reports, court transcripts, and hospital records all contain sensitive information. Redacting this information is often expensive and time consuming.
From Enrom email dataset, few files were used for testing the project. The sensitive information like names, date, phone numbers, address, gender are redacted. The redacted information is stored in a new directory. Also, all the statistics of the redacted data is stored in stats file.

## Author Details
* Name: Akhila Mora
* Email: akhila.mora@ou.edu
* Student ID: 113531532

## Demo Video


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
* Run the project using main.py
```
pipenv run python project1/redactor.py --input '*.txt'  --names --dates --phones --genders --address --output 'files/' --stats stderr
```
or
```
pipenv run python project1/redactor.py --input '*.txt'  --names --dates --phones --genders --address --output 'files/' --stats stats
```
* By running the program using above command, it will generate redacted files with an extension .redacted and save all the files in files/ folder. Screenshot of redacted files folder:
* ![image](https://user-images.githubusercontent.com/113566461/229969365-2b808578-c0a2-45d4-9df1-c3b51573c786.png)
* Run pytests using below command:
```
pipenv run python -m pytest -v
```

### Functions
There is one file named redactor.py which consists of all the logic for redacting the input files:
* arg_function
   * It takes arguments using args parameter. It extracts input_file, name, date, phone, gender, address, ouput_dir, stats_file from args parameter. It creates an output directory and uses glob to search for file paths. It calls redactor_function to redact sensitive information.
* name_redact
   * This function redacts names that are present in the file using nltk, spacy and en_web_core_md module.  It returns redacted text and also writes statistics of redacted data to stats file. Most of the names are redacted as nltk and spacy are used.
* gender_redact
   * This function redacts gender based on gender list. This list consists of all the words that are used to identify gender. It uses nltk to tokenize words, sentences and then identify gender. It returns redacted text and also writes statistics of redacted data to stats file. I considered maximum of the words that are used to classify gender. If any other word that represents gender is missing, that will not be redacted.
* date_redact
   * This function redacts dates that are present in the file using spacy, en_web_core_md module and regex pattern. It returns redacted text and also writes statistics of redacted data to stats file. Almost all commonly used date formats were considered, and if any format is missing, it is not possible to redact those dates.
* phone_redact
   * This function redacts phone numbers that are present in the file using regex patterns. If a phone number matches any pattern in the list, it will be redacted. It returns redacted text and also writes statistics of redacted data to stats file. Almost all commonly used phone number formats were considered, and if any format is missing, it is not possible to redact those phone numbers.
* address_redact
   * This function redacts address that are present in the file using regex and a list that contains all US states. It returns redacted text and also writes statistics of redacted data to stats file.
* store_output
   * This function takes output directory, output data and file name as parameters. It stores an output in the output directory. It changes the output filename and adds .redacted to it. It writes all the redacted data to output file.
* redactor_function
   * This function takes file; name, gender, date, phone, address flags; output and stats as parameters. It calls all the above listed functions and redacts each file present in the docs directory. It also updates stats file based on the input given to stats. If stats is given as stderr, it stores error array as stderr. Else it stores statistics to stats file.
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
