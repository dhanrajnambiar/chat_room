import os
from riot_chat.settings.base import BASE_DIR

def run():
    path_file = os.path.join(BASE_DIR,'key.py')
    key_obj = open(path_file,'r')
    key = key_obj.read().rstrip()
    key_obj.close()
    return key
