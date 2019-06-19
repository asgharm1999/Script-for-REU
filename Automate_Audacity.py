import pywinauto
import time
from pywinauto.application import Application
import csv
import pandas as pd

path = 'C:/Users/Muhammad/Desktop/REU19/Talker_Speaker.csv'

def calc_coord(x_coord, y_coord):
    x_coord = int(x_coord * 1.25)
    y_coord = int(y_coord * 1.25)
    return (x_coord, y_coord)

change_proj_rate_button = calc_coord(81, 784)
correct_rate_button = calc_coord(87, 662)
change_mic_button = calc_coord(314, 113)
line_button = calc_coord(304, 176)
channel_button = calc_coord(520, 110)
change_channel_button = calc_coord(513, 236)
record_button = calc_coord(297, 71)
stop_button = calc_coord(139, 70)
file_button = calc_coord(15, 33)
export_button = calc_coord(60, 176)
export_multiple_button = calc_coord(296, 308)
choose_button = calc_coord(947, 257)
desktop_button = calc_coord(501, 412)
reu_button = calc_coord(727, 418)
lombardgrid_button = calc_coord(728, 419)
lomabrd_audio_out_button = calc_coord(680, 390)
select_folder_button = calc_coord(988, 662) 
name_prefix_button = calc_coord(930, 538)   
export_confirm = calc_coord(925, 607)
clear_button = calc_coord(1007, 451)
ok_button = calc_coord(983, 590)
confim_ok_button = calc_coord(770, 576)
close_button = calc_coord(1505, 12)
confim_close_button = calc_coord(806, 416)


# def rec_audio(path, keyboard):

# fields = []
# rows = []
# columns = []

# # load the CSV files
# csv_df = pd.read_csv(path, sep = ',', index_col = 0)
# print(csv_df.shape)
# print(csv_df)

with open(path, 'r') as csv_file:
    # csv_reader = csv_file.readlines()

    
    # csv_reader = csv.reader(csv_file, delimiter = ',')
    # line_count = 0


    # for line in csv_reader:
    #     S = line.split(",")
    #     print(S)

    # convert to dataframe pandas
    csv_df = pd.read_csv(path , sep = ',')
    print(csv_df.shape)

    # rows = []
    
    # fields = next(csv_reader)

    # print('Field names are: ' + ', '.join(field for field in fields))

    # S1 = [(str(line['Speaker_1']),str(line['File_Name_Out_1'])) for line in csv.DictReader(csv_file)]
    # print(S1)

    file_name_out_df = csv_df[['File_Name_Out_S1', 'File_Name_Out_S2', 'File_Name_Out_S3', 'File_Name_Out_S4', 'File_Name_Out_S5', 'File_Name_Out_S6']]

    for i in range(len(file_name_out_df)):
        file_name = file_name_out_df.loc[i, '{}'.format('File_Name_Out_S1', 'File_Name_Out_S2', 'File_Name_Out_S3', 'File_Name_Out_S4', 'File_Name_Out_S5', 'File_Name_Out_S6')]
    # for label, content in file_name_out_df.iteritems(): 
        
        # def file_name(content):
        #     for i in content:
        #         print(content[i])

        # print(file_name(content))

        app = Application(backend = "uia").start("C:/Program Files (x86)/Audacity/audacity.exe")
        time.sleep(3)

        pywinauto.mouse.move(change_proj_rate_button)
        pywinauto.mouse.click(button = 'left', coords = change_proj_rate_button)
        # time.sleep(1)

        pywinauto.mouse.move(correct_rate_button)
        pywinauto.mouse.click(button = 'left', coords = correct_rate_button)
        # time.sleep(1)

        pywinauto.mouse.move(change_mic_button)
        pywinauto.mouse.click(button = 'left', coords = change_mic_button)
        # time.sleep(1)

        pywinauto.mouse.move(line_button)
        pywinauto.mouse.click(button = 'left', coords = line_button)
        # time.sleep(1)

        pywinauto.mouse.move(channel_button)
        pywinauto.mouse.click(button = 'left', coords = channel_button)
        # time.sleep(1)

        pywinauto.mouse.move(change_channel_button)
        pywinauto.mouse.click(button = 'left', coords = change_channel_button)
        # time.sleep(1)

        pywinauto.mouse.move(record_button)
        pywinauto.mouse.click(button = 'left', coords = record_button)
        time.sleep(6)
        
        pywinauto.mouse.move(stop_button)
        pywinauto.mouse.click(button = 'left', coords = stop_button)
        time.sleep(1)
        
        pywinauto.mouse.move(file_button)
        pywinauto.mouse.click(button = 'left', coords = file_button)
        # time.sleep(1)
        

        pywinauto.mouse.move(export_button)
        pywinauto.mouse.click(button = 'left', coords = export_button)
        # time.sleep(1)


        pywinauto.mouse.move(export_multiple_button)
        pywinauto.mouse.click(button = 'left', coords = export_multiple_button)
        # time.sleep(1)
        

        pywinauto.mouse.move(choose_button)
        pywinauto.mouse.click(button = 'left', coords = choose_button)
        # time.sleep(1)
        

        pywinauto.mouse.move(desktop_button)
        pywinauto.mouse.click(button = 'left', coords = desktop_button)
        # time.sleep(1)
       

        pywinauto.mouse.move(reu_button)
        pywinauto.mouse.double_click(button = 'left', coords = reu_button)
        time.sleep(1)
        

        pywinauto.mouse.move(lombardgrid_button)
        pywinauto.mouse.double_click(button = 'left', coords = lombardgrid_button)
        # time.sleep(1)
        

        pywinauto.mouse.move(lomabrd_audio_out_button)
        pywinauto.mouse.double_click(button = 'left', coords = lomabrd_audio_out_button)
        # time.sleep(1)
        

        pywinauto.mouse.move(select_folder_button)
        pywinauto.mouse.click(button = 'left', coords = select_folder_button)
        # time.sleep(1)
        

        pywinauto.mouse.move(name_prefix_button)
        pywinauto.mouse.click(button = 'left', coords = name_prefix_button)
        print(file_name)
        pywinauto.keyboard.send_keys('{}'.format(file_name))
        time.sleep(1)
        

        pywinauto.mouse.move(export_confirm)
        pywinauto.mouse.click(button = 'left', coords = export_confirm)
        time.sleep(1)
        
        count = 0
        while count < 7:
            pywinauto.mouse.move(clear_button)
            pywinauto.mouse.click(button = 'left', coords = clear_button)
            # time.sleep(1)
        
            pywinauto.mouse.move(ok_button)
            pywinauto.mouse.click(button = 'left', coords = ok_button)
            # time.sleep(3)

            count = count + 1
        

        pywinauto.mouse.move(confim_ok_button)
        pywinauto.mouse.click(button = 'left', coords = confim_ok_button)
        # time.sleep(1)
        

        pywinauto.mouse.move(close_button)
        pywinauto.mouse.click(button = 'left', coords = close_button)
        time.sleep(1)
        

        pywinauto.mouse.move(confim_close_button)
        pywinauto.mouse.click(button = 'left', coords = confim_close_button)
        time.sleep(1)

        print(i)

        
        



    
    
    # for row in csv_reader:
    #     rows.append(row[7:13]) # keeps only file names out
    #     print(len(rows[1:2]))
    

    # for row in rows[1:]: # get rid of first row
    #     for column in rows[1:]:



    
    # next(csv_reader) # skips the first header row
    # for row in csv_reader: # skips the first column
    #     row[1:]

   
    # Speaker_1 = []
    # Speaker_2 = []
    # Speaker_3 = []
    # Speaker_4 = []
    # Speaker_5 = []
    # Speaker_6 = []



    # for row in csv_reader:
    #     Speaker_1.append(row)
        # Speaker_2.append(row[1])
        # Speaker_3.append(row[2])
        # Speaker_4.append(row[3])
        # Speaker_5.append(row[4])
        # Speaker_6.append(row[5])
        # print(Speaker_1)


        
     

# for i in range(len(names)):
#         writer.writerow({'File_Name' : names[i])}

# for index, row in csv_df.iterrows():
    

    # for row in csv_reader:
    #     rows.append(row)
        
    # for column in row:
    #     columns.append(column)

    # fields = csv_reader.next()
    # print('Field names are: ' + ','.join(field for field in fields))

    # print(rows)
    # print(columns)
    # for row in rows[1:]: # get rid of first row
    #     for column in rows[1:]:


    # for row in csv_reader:
    #     if row{}
    #     for column in row:
    #         print(column)
    #         if column == 'Speaker_1':
    #             print('hi')
    # next(csv_reader) # skips the first header row
    # for row in csv_reader: # skips the first column
    #     print(row[1:])
    # line_count = 0

    # for i, line in enumerate(csv_reader):
        
    #     print('Line[{}] = {}'.format(i, line))
            
            #  in csv_reader:
            # if line_count == 0:
                
            #     line_count += 1
        

        # data = list(csv.reader(csv_file))
        # print(data[1][11])

            