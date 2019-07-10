from pywinauto.application import Application
from scipy.io import wavfile as wav
from scipy.io.wavfile import read
from os import walk
import os, glob, wave
import pandas as pd
import numpy as np
import pywinauto
import winsound
import time
import csv

csv_path = 'C:/Users/Muhammad/Desktop/REU19/Talker_Speaker.csv'
lombardgrid_audio_path = 'C:/Users/Muhammad/Desktop/REU19/lombardgrid/audio'

def calc_coord(x_coord, y_coord):
    x_coord = int(x_coord * 1.25)
    y_coord = int(y_coord * 1.25)
    return (x_coord, y_coord)

change_proj_rate_button = calc_coord(81, 784)
correct_rate_button = calc_coord(87, 662)
x_button = calc_coord(14, 169)
change_mic_button = calc_coord(314, 113)
line_button = calc_coord(304, 176)
channel_button = calc_coord(727, 110)
change_channel_button = calc_coord(729, 129)
record_button = calc_coord(297, 71)
stop_button = calc_coord(139, 70)
audio_track_button = calc_coord(77, 170)
split_to_mono_button = calc_coord(78, 478)
file_button = calc_coord(15, 33)
export_button = calc_coord(60, 176)
export_multiple_button = calc_coord(296, 308)
choose_button = calc_coord(947, 257)
desktop_button = calc_coord(496, 412)
reu_button = calc_coord(727, 418)
lombardgrid_button = calc_coord(726 , 392)
lomabrd_audio_out_button = calc_coord(726, 392)
select_folder_button = calc_coord(988, 662) 
name_prefix_button = calc_coord(930, 538)   
export_confirm = calc_coord(925, 607)
clear_button = calc_coord(1007, 451)
ok_button = calc_coord(983, 590)
confim_ok_button = calc_coord(770, 576)
close_button = calc_coord(1505, 12)
confim_close_button = calc_coord(806, 416)

with open(csv_path, 'r') as csv_file:
    csv_df = pd.read_csv(csv_path, sep = ',')
    print(csv_df.shape)

    file_name_out_df = csv_df[['File_Name_Out_S1', 'File_Name_Out_S2', 'File_Name_Out_S3', 'File_Name_Out_S4', 'File_Name_Out_S5', 'File_Name_Out_S6']]
    print(file_name_out_df)

    speakers = ['File_Name_Out_S6']

    directories = []

    for (dirpath, dirnames, filenames) in walk(lombardgrid_audio_path):
        for i in filenames:
            directories.append(dirpath + '/' + i)

    # random.shuffle(directories)
    # print(directories)

    app = Application(backend = "uia").start("C:/Program Files (x86)/Audacity/audacity.exe")
    time.sleep(2)

    # pywinauto.mouse.move(change_proj_rate_button)
    # pywinauto.mouse.click(button = 'left', coords = change_proj_rate_button)
    
    # pywinauto.mouse.move(correct_rate_button)
    # pywinauto.mouse.click(button = 'left', coords = correct_rate_button)

    for filename in speakers:
        for i in range(len(file_name_out_df)):

            file_name = file_name_out_df.loc[i, '{}'.format(filename)]
          
            # pywinauto.mouse.move(change_mic_button)
            # pywinauto.mouse.click(button = 'left', coords = change_mic_button)
          
            # pywinauto.mouse.move(line_button)
            # pywinauto.mouse.click(button = 'left', coords = line_button)
          
            # pywinauto.mouse.move(channel_button)
            # pywinauto.mouse.click(button = 'left', coords = channel_button)
          
            # pywinauto.mouse.move(change_channel_button)
            # pywinauto.mouse.click(button = 'left', coords = change_channel_button)
                
            pywinauto.mouse.move(record_button)
            pywinauto.mouse.click(button = 'left', coords = record_button)
            time.sleep(1)
            # play sound
            winsound.PlaySound(directories[i], winsound.SND_FILENAME)
            time.sleep(2)
            
            pywinauto.mouse.move(stop_button)
            pywinauto.mouse.click(button = 'left', coords = stop_button)
            # time.sleep(1)

            pywinauto.mouse.move(audio_track_button)
            pywinauto.mouse.click(button = 'left', coords = audio_track_button)

            pywinauto.mouse.move(split_to_mono_button)
            pywinauto.mouse.click(button = 'left', coords = split_to_mono_button)
            # time.sleep(1)

            pywinauto.mouse.move(file_button)
            pywinauto.mouse.click(button = 'left', coords = file_button)
          
            pywinauto.mouse.move(export_button)
            pywinauto.mouse.click(button = 'left', coords = export_button)
          
            pywinauto.mouse.move(export_multiple_button)
            pywinauto.mouse.click(button = 'left', coords = export_multiple_button)
          
            # pywinauto.mouse.move(choose_button)
            # pywinauto.mouse.click(button = 'left', coords = choose_button)
            # time.sleep(1)
                   
            # pywinauto.mouse.move(desktop_button)
            # pywinauto.mouse.click(button = 'left', coords = desktop_button)
            # time.sleep(1)
          
            # pywinauto.mouse.move(reu_button)
            # pywinauto.mouse.double_click(button = 'left', coords = reu_button)
                   
            # pywinauto.mouse.move(lombardgrid_button)
            # pywinauto.mouse.double_click(button = 'left', coords = lombardgrid_button)
        
            # pywinauto.mouse.move(lomabrd_audio_out_button)
            # pywinauto.mouse.double_click(button = 'left', coords = lomabrd_audio_out_button)
        
            # pywinauto.mouse.move(select_folder_button)
            # pywinauto.mouse.click(button = 'left', coords = select_folder_button)
        
            pywinauto.mouse.move(name_prefix_button)
            pywinauto.mouse.click(button = 'left', coords = name_prefix_button)
            print(file_name)
            pywinauto.keyboard.send_keys('{}'.format(file_name))
            time.sleep(1)
            
            pywinauto.mouse.move(export_confirm)
            pywinauto.mouse.click(button = 'left', coords = export_confirm)
            # time.sleep(1)
            
            # count = 0
            # while count < 8:
            #     pywinauto.mouse.move(clear_button)
            #     pywinauto.mouse.click(button = 'left', coords = clear_button)
        
            #     pywinauto.mouse.move(ok_button)
            #     pywinauto.mouse.click(button = 'left', coords = ok_button)
        
            #     count = count + 1
        
            pywinauto.mouse.move(confim_ok_button)
            pywinauto.mouse.click(button = 'left', coords = confim_ok_button)

            count = 0
            while count < 8:
                pywinauto.mouse.move(x_button)
                pywinauto.mouse.click(button = 'left', coords = x_button)
                
                count = count + 1
        

            # pywinauto.mouse.move(close_button)
            # pywinauto.mouse.click(button = 'left', coords = close_button)
            # time.sleep(1)
        
            # pywinauto.mouse.move(confim_close_button)
            # pywinauto.mouse.click(button = 'left', coords = confim_close_button)
            # time.sleep(1)

            print(i)