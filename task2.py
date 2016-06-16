import os

def get_files(folder,ext):
    result = []
    for root,folders,files in os.walk(folder):
        for i in files:
            if i.endswith(ext):
                result.append(i)
    return result

