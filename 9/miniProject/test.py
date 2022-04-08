from khayyam import JalaliDate
from rtl import rtl

import os
import glob


files_list = glob.glob('*')
extensions_set = set()

for each_file in files_list:
    try:
        extension = each_file.split('.')[1]
        extensions_set.add(extension)
    except:
        continue

def create_folders():    
    for ext in extensions_set:    
        if ext == 'py':
            continue    
        try:
            today = JalaliDate.today().strftime('%A %d %B %Y')
            os.makedirs(today + "/" + ext + '_files')
        except:
            continue

def move_files():
    for each_file in files_list:        
        try:
            today = JalaliDate.today().strftime('%A %d %B %Y')
            extension = each_file.split('.')[1]
            os.rename(each_file, today + "/" + extension +'_files/' + each_file)
        except:
            continue


create_folders()
move_files()
