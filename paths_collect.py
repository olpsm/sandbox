import os
dir='D:\\fresh_dump\\voice_1_11_2017\\per_sc2k_0'
path=[os.path.join(dirpath, filename) for dirpath, dirnames, filenames in os.walk(dir) 
                                 for filename in filenames]
print(path[0:5],'\n',path[-1])						
