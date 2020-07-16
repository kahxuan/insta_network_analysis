# Instagram network clustering and visualisation

This project helps us to better understand our Instagram network by partitioning our Instagram friends into clusters. We can identify the social groups in our network and gain insight into the closeness between different social groups.

[Click here](https://instaclustering.herokuapp.com) for my interactive network graph.

![Network graph example](https://github.com/kahxuan/insta_clustering/blob/master/assets/example.png)

## Data collection

Follower and followee lists are collected using [Instaloader](https://instaloader.github.io). Two users are considered to be connected when they are following each other so that the graph is non-directional. My network only includes users whom I connect with.

## Clustering detection

Hierarchical k-means clustering is used, with the distance metric being the shortest path between users, i.e. the minimum number of profiles a user has to visit before the target user's profile can be reached. Each user is initialised to be an independent cluster, then in each iteration, clusters that are close to each other are merged, and clusters having at least one pair of users with distance higher than some threshold are split into two. 

This algorithm cannot detect users that belong to more than one social group, and they might act as a bridge that connects two social group into one clusters.

## Visualisation

The network graph is created using [NetworkX](https://networkx.github.io) and [Plotly](https://github.com/plotly).
