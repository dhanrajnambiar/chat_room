import sys,os
path2 = os.path.dirname(os.path.expanduser(os.path.abspath(__file__)))
#print(path)
if path2 not in sys.path:
    sys.path.append('path2')
def run():
    key_obj = open('key.py','r')
    key = key_obj.read().rstrip()
    key_obj.close()
    return key
