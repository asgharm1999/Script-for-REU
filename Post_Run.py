from scipy.io import wavfile as wav
from os import walk
import os, glob, wave
import csv

path = 'C:/Users/Muhammad/Desktop/REU19/Post_Run.csv'
audio_location = 'C:/Users/Muhammad/Desktop/REU19/lombardgrid/audio_out'

with open(path, 'a') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0

    names = []
    
    # adds file name to list names
    for (dirpath, dirnames, filenames) in walk(audio_location):
        names.extend(filenames)

    # gets rid of file extension 
    names = [os.path.splitext(x)[0] for x in names]
        
    print(names)
    print('Length of f:', len(names))
    
    # clears csv
    clear_csv = open(path, 'w+')
    clear_csv.close()

    # names the first row
    fieldnames = ['File_Name', 
                  'Output Speaker']

    writer = csv.DictWriter(csv_file, fieldnames = fieldnames, lineterminator = '\n')
    writer.writeheader()

    for name in names:
        s_out = name[-4:-3]

        writer.writerow({'File_Name'      : name, 
                         'Output Speaker' : s_out})