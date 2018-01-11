import sys
print(sys.path)
def run():
    key_obj = open('key.py','r')
    key = key_obj.read().rstrip()
    key_obj.close()
    return key
