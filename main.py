import os
import copy
from util import *

data_dir = 'masked'
my_username = 'k_xuanlim'

connections = {}
users = [file[:-4] for file in os.listdir(data_dir)]
users_num = len(users)
id_to_name = dict(zip([i for i in range(users_num)], users))
name_to_id = dict(zip(users, [i for i in range(users_num)]))

# get connections
for file in os.listdir(data_dir):
    
    f = open(os.path.join(data_dir, file))
    ls = []
    for line in f:
        ls.append(line.strip())
    f.close()

    username = file[:-4]
    uid = name_to_id[username]
    connections[uid] = []

    shared_friends = set(ls).intersection(users)
    hashed_ff = [name_to_id[friend] for friend in shared_friends]
    connections[uid] = hashed_ff

# param
cluster_no = users_num
merge_threshold = 2

adjacencym = gen_adjacency_matrix(connections)
dist = floyd_warshall(copy.deepcopy(adjacencym), connections)
clusters = kmeans(dist, connections.keys(), cluster_no, merge_threshold)
adjacencym[adjacencym == users_num + 1] = 0

cluster_names = ['cluster ' + str(i + 1) for i in range(len(clusters))]
plot_network(adjacencym, clusters, cluster_names, id_to_name, my_username)