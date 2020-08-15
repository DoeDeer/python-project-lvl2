# Diff generator  

[![Maintainability](https://api.codeclimate.com/v1/badges/1c074cc4be9a3a0739d5/maintainability)](https://codeclimate.com/github/DoeDeer/python-project-lvl2/maintainability)
[![Build Status](https://travis-ci.org/DoeDeer/python-project-lvl2.svg?branch=master)](https://travis-ci.org/DoeDeer/python-project-lvl2)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1c074cc4be9a3a0739d5/test_coverage)](https://codeclimate.com/github/DoeDeer/python-project-lvl2/test_coverage)

##
Compare to files for differences.
##

## Usage
#### Console:
gendiff [-h] [-f FORMAT] first_file second_file

Positional arguments:  
`first_file`: source file with original keys  
`second_file`: changed file with updated keys

Optional arguments:  
`-h or --help`: show help message  
`-f FORMAT or --format FORMAT`:  set format of output message. Available choices
are: json, json-like and plain. Json-like is pretty formatted json dict with 
`+` and `-` that shows changed, removed and added keys. Json - is valid json 
string with info dict about all keys. Plain is just test describing keys change.  

#### In code:
```
from gendiff import gendiff

diff = gendiff(path_to_first_file, path_to_second_file, mode)
```