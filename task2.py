import os
import sys

folder = sys.argv[1]
ext = sys.argv[2]

def get_files(folder,ext):
    result = []
    for root,folders,files in os.walk(folder):
        for i in files:
            if i.endswith(ext):
                result.append(i)
    return result

print get_files(folder, ext)


