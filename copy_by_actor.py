import os
import shutil
import msvcrt

# short name from filenames
actor_name = 'LMBT' 
# Destination folder
new_folder = r'M:\_test\lambert_lines'


path = os.getcwd() + '\\speech_files'

for f in os.listdir(path):
    if f[f.find(' ') + 1 : f.rfind('.')].strip() == actor_name:
        print(f)
        shutil.copy(path + '\\' + f, new_folder + '\\' + f)
        
print('Press any key to exit')

msvcrt.getch()        