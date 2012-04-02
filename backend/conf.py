import os
import os.path

forte_path = os.path.expanduser("~/.forte")

def db_location():
    try:
        os.makedirs(forte_path + os.sep + 'db')
    except OSError, e:
        if e.errno != 17:
            raise
    return os.sep.join([forte_path, 'db', 'key_db.sqlite'])



    
