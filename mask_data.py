import os
import names
import random
from util import generate_username

data_dir = 'data'
masked_data_dir = 'hashed'

users = [file[:-4] for file in os.listdir(data_dir)]
users_to_hname = dict(zip(users, [generate_username() for _ in range(len(users))]))

for file in os.listdir(data_dir):
    
    f = open(os.path.join(data_dir, file))
    ls = []
    for line in f:
        ori = line.strip()
        if ori in users_to_hname:
            ls.append(users_to_hname[ori])
    f.close()

    username = file[:-4]
    uid = users_to_hname[username]

    f = open(os.path.join(masked_data_dir, uid + '.txt'), 'w')
    f.write('\n'.join(ls))
    f.close()

    