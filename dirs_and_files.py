import os
import argparse

parser = argparse.ArgumentParser(description='Util for create folders and files')
parser.add_argument("-fo", "--folder_name", dest="folder name", help="Set name for folders")
parser.add_argument("-f_n", "--folder_number", dest="folder number", help="Set number of folders")
parser.add_argument("-f_st", "--folder_start_number", dest="folder start number", help="Set start number for folder")
parser.add_argument("-fi", "--file_name", dest="file name", help="Set name for files")

args = parser.parse_args()
\
