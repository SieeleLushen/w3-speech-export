import os
import msvcrt

# read dict
ids_dict = open(r'ids_dict.txt', 'r', encoding='utf-8').readlines()
ids_dict = [l.strip().split(':') for l in ids_dict]
ids_dict = dict((l[0], l[1]) for l in ids_dict)

path = os.getcwd() + '\\speech_files'

for f in os.listdir(path):
    hex_id = f[:f.rfind('.')] 
    dec_id = str(int(hex_id, 16))
    
    if ' ' in hex_id: # already changed
        continue # skip
        
    if dec_id not in ids_dict.keys():
        actor = 'UNKNOWN'
    else:
        actor = ids_dict[dec_id]
        
    newfilename = '{} {}{}'.format(dec_id.zfill(10), actor, f[f.rfind('.'):])
    
    print(f'{f} -> {newfilename}')
    
    os.rename(path + '\\' + f, path + '\\' + newfilename)
    
print('Press any key to exit')

msvcrt.getch()
