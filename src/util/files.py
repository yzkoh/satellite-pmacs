from os import path

# Directory
ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)) )

# Folder
DATA_FOLDER = 'data'

# File names
LLA_POS_7 = 'lla_pos_7_days.txt'
LLA_POS_1 = 'lla_pos_1_day.txt'

# Join path
def join_path(*args):
    res = ''
    for i in args:
        res = path.join(res,i)
    return res
