'''
Author : Aiman
Date : 09/12/2019
This function is to generate md5 checksum for a file
'''


import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


#print(md5("C:\\Users\\aiman\\PycharmProjects\\checksum\\binary\\test.txt"))
