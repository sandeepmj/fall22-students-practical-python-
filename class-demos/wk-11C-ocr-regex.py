## import libraries
import re
from PIL import Image
import pytesseract ## python interface for tesseract
import os ## navitage, create directories
import shutil ## to delete the image folders with their imgs
from pdf2image import convert_from_path ## to turn pdf to image
import glob ## to glob files into a list
from pathlib import Path ## to specify path to your files
from natsort import natsorted, ns ## natural sorting
from kiwano import ocr


## Single file test
## Nixon Document


## Multifile test
## Nixon docs

## run multi file kiwano on list


## glob files together

## how many files


## run kiwano ocr function. remember language and resolutions have default values.


## name of expored file


##### Back to original California finance files


## glob files together


## how many files


## run kiwano ocr function. remember language and resolutions have default values.


## name of expored file


## pull into a variable all the text


## regex to capture alcohol numbers i used \S which captures any ***non-space*** characters in case the OCR turns out strange characters



## Method 1 pattern.findall(source_text)


#print 

## check to see if equal to number of files


## regex to capture date
## i used literals for the months


## dates list and print it


## check to see if equal to number of files



## run regex within list comprehension



## convert to dataframe


## export to csv

##BACK TO JUPYTER NOTEBOOK