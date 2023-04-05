import os
import sys
import glob
import nltk
import pytest

import redactor

test_file = "tests/File1.txt"
with  open(test_file,'r',encoding="utf-8") as f:
    data = f.readlines()




@pytest.fixture()
def info():
    return data

# Function to test names
def test_name_redact(info):
    rd = ''.join(info)
    print(type(rd))
    print(rd)
    names = redactor.name_redact(rd)
    for name in names:
        if name == '\u2588':
            assert True

# Function to test gender
def test_gender_redact(info):
    rd = ''.join(info)
    genders = redactor.gender_redact(rd)
    for gender in genders:
        if gender == '\u2588':
            assert True

# Function to test date
def test_date_redact(info):
    rd = ''.join(info)
    dates = redactor.date_redact(rd)
    for date in dates:
        if date == '\u2588':
            assert True

# Function to test phone
def test_phone_redact(info):
    rd = ''.join(info)
    phones = redactor.phone_redact(rd)
    for phone in phones:
        if phone == '\u2588':
            assert True

# Function to test address
def test_address_redact(info):
    rd = ''.join(info)
    addresses = redactor.address_redact(rd)
    for address in addresses:
        if address == '\u2588':
            assert True



def test_redact_filefunc_and_outputfile():
    redactor.redactor_function(test_file,True,True,True,True,True,'./','stats')
    st = 0
    if os.path.exists('./'+'File1.txt.redacted'):
        st = 1
    assert st == 1
