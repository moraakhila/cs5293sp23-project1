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
![image](https://user-images.githubusercontent.com/113566461/229966821-0577dc91-024a-4856-a767-0d4d0c130712.png)
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
![image](https://user-images.githubusercontent.com/113566461/229969365-2b808578-c0a2-45d4-9df1-c3b51573c786.png)
* Run pytests using below command:
```
pipenv run python -m pytest -v
```

### Functions
There is one file named redactor.py which consists of all the logic for redacting the input files:
* How to run the program
* Step-by-step bullets
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
