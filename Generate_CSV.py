import os, glob, wave
from os import walk
from scipy.io import wavfile as wav
import csv

path = 'C:/Users/Muhammad/Desktop/REU19/Talker_Speaker.csv'
audio_location = 'C:/Users/Muhammad/Desktop/REU19/lombardgrid/audio'

with open(path, 'a') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0

    names = []
    duration = []

    # adds file name to list names
    for (dirpath, dirnames, filenames) in walk(audio_location):
        names.extend(filenames)

    # gets rid of file extension 
    names = [os.path.splitext(x)[0] for x in names]
        
    # for each file in directory, add duration to list
    for soundfiles in glob.glob(os.path.join(audio_location, '*.wav')):
        (freq, sig) = wav.read(soundfiles)
        nframes = sig.size
        length_of_file = nframes/freq
        duration.append(length_of_file)

    print(names)
    print(duration)
    print('Length of f:       ', len(names))
    print('Length of duration:', len(duration))

    # clears csv
    clear_csv = open(path, 'w+')
    clear_csv.close()

    # names the first row
    fieldnames = ['File_Name', 
                  'Speaker_1', 
                  'Speaker_2', 
                  'Speaker_3', 
                  'Speaker_4', 
                  'Speaker_5', 
                  'Speaker_6', 
                  'File_Name_Out_S1', 
                  'File_Name_Out_S2', 
                  'File_Name_Out_S3', 
                  'File_Name_Out_S4', 
                  'File_Name_Out_S5',
                  'File_Name_Out_S6', 
                  'Duration']
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames, lineterminator = '\n')
    writer.writeheader()

    for i in range(len(names)):
        writer.writerow({'File_Name' : names[i], 
                         'Speaker_1' : 'N', 
                         'Speaker_2' : 'N', 
                         'Speaker_3' : 'N', 
                         'Speaker_4' : 'N', 
                         'Speaker_5' : 'N', 
                         'Speaker_6' : 'N', 
                         'File_Name_Out_S1' : names[i] + '_speaker_1', 
                         'File_Name_Out_S2' : names[i] + '_speaker_2', 
                         'File_Name_Out_S3' : names[i] + '_speaker_3', 
                         'File_Name_Out_S4' : names[i] + '_speaker_4', 
                         'File_Name_Out_S5' : names[i] + '_speaker_5',
                         'File_Name_Out_S6' : names[i] + '_speaker_6',
                         'Duration' : duration[i]})

    

    