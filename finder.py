import os
import time


start_dir = '/'
_looking_for = 'log'

_found = []

try:
    for dirs, subdirs, files in os.walk(start_dir):
        for file in os.listdir(dirs):
            print(file)
            # time.sleep(0.25)
            if _looking_for in dirs:
                _path = os.path.join(dirs)
                if _path not in _found:
                    print("Found:", _path)
                    _found.append(_path)

            if _looking_for in file:
                _path = os.path.join(dirs, file)
                if _path not in _found:
                    print("Found:", _path)
                    _found.append(_path)
                    
except KeyboardInterrupt:
    print('\nSearch closed successfully...\n')
    
with open('found.txt', 'w') as found:
    _poz = 0
    for line in _found:
        _poz+=1
        found.write(f"poz_{str(_poz)}: {line}\n")
found.close()
