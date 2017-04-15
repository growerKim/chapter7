'''
Created on 2017. 4. 14.

@author: david
'''

import os

def run(**args):
    print "[*] In dirlister module."
    files = os.listdir(".")
    
    return str(files)

