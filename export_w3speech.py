import os
import subprocess
import msvcrt
import time

# set game dir
dir_w3 = r'C:\Program Files (x86)\Steam\steamapps\common\The Witcher 3'
# language
lang = 'en'

if not os.path.exists('speech_files'):
    os.makedirs('speech_files')

for i in range(13): #content0 - content12
    process = subprocess.Popen(['w3unpack.exe', '-u', f'{dir_w3}\\content\\content{str(i)}\\{lang}pc.w3speech',
                                'speech_files'])
    process.wait()  
    

process = subprocess.Popen(['w3unpack.exe', '-u', f'{dir_w3}\\dlc\\bob\\content\\{lang}pc.w3speech',
                            'speech_files'])
process.wait()   

process = subprocess.Popen(['w3unpack.exe', '-u', f'{dir_w3}\\dlc\\ep1\\content\\{lang}pc.w3speech',
                            'speech_files'])
process.wait()   
   

path = os.getcwd() + '\\speech_files'

print('\nRenaming...')
for f in [fl for fl in os.listdir(path) if '.wav' in fl]:
    print(f)
    os.rename(path + '\\' + f, path + '\\' + f.replace('.wav', '.wem'))
    process = subprocess.Popen([os.getcwd() + '\\vgmstream-cli.exe',
                                path + '\\' + f.replace('.wav', '.wem'), '-o',
                                path + '\\' + f])
    process.wait()  
   
print('\nPress any key to continue...')   

msvcrt.getch()
