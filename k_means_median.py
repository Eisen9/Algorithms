#########################################################################################################
# K-means
##########################################################################################################


import numpy as np
import pandas as pd
# write a code for the k-means algorithm


def k_means(points, k, max_iter=10):
    '''
    @param
    points: list of points
    k: number of clusters
    max_iter: maximum number of iterations
    '''
    centroids = [] # list of centroids
    for i in range(k): # initialize k centroids
        centroids.append(points[i]) # randomly select k points as centroids
    for iter in range(max_iter): # iterate until convergence
        clusters = [[] for i in range(k)] # create k clusters
        for point in points: # for each point in the dataset
            distances = [] # create a list of distances
            for centroid in centroids: # for each centroid
                distances.append(get_distance(point, centroid)) # calculate the distance between the point and the centroid
            clusters[distances.index(min(distances))].append(point) # add the point to the cluster with the smallest distance
        new_centroids = [] # create a list of new centroids
        for cluster in clusters: # for each cluster
            new_centroids.append(get_centroid(cluster)) # calculate the new centroid
        if(new_centroids == centroids): # if the centroids haven't changed
            break # stop iterating
        centroids = new_centroids # update the centroids
    return clusters # return the clusters


# euclidean distance between two points
def get_distance(point1, point2):
    distance = 0 # initialize distance
    for i in range(len(point1)): # for each dimension
        distance += (point1[i] - point2[i])**2 # add the squared difference
    return distance**(1/2) # return the square root of the sum

# mean


def get_centroid(points):
    centroid = [] # initialize centroid
    for i in range(len(points[0])): # for each dimension
        sum = 0 # initialize sum
        for point in points: # for each point in the cluster
            sum += point[i] # add the dimension
        centroid.append(sum / len(points)) # calculate the mean
    return centroid # return the centroid


# uncomment to print the testing on random data.
print("*****************************k-means************************************")
print("k-means")
print(k_means([[3, 5], [1, 5], [2, 5], [7, 8], [9, 8]], 2), "\n")


#########################################################################################################
# K-median
##########################################################################################################
# implement the k-median algorithm


def k_median(k, points, max_iter=10):
    '''
    @param
    k: number of clusters
    points: list of points
    max_iter: maximum number of iterations
    '''
    centroids = [] # list of centroids
    for i in range(k): # initialize k centroids
        centroids.append(points[i]) # randomly select k points as centroids
    centroids = np.array(centroids) # convert to numpy array
    for iter in range(max_iter): # iterate until convergence
        clusters = [[] for i in range(k)] # create k clusters
        for point in points: # for each point in the dataset
            distances = [] # create a list of distances
            for centroid in centroids: # for each centroid
                distances.append(get_distance_2(point, centroid)) # calculate the distance between the point and the centroid
            clusters[distances.index(min(distances))].append(point) # add the point to the cluster with the smallest distance
        new_centroids = [] # create a list of new centroids
        for cluster in clusters: # for each cluster
            new_centroids.append(get_centroid_2(cluster)) # calculate the new centroid
        new_centroids = np.array(new_centroids) # convert to numpy array
        if(np.array_equal(new_centroids, centroids)): # if the centroids haven't changed
            break # stop iterating
        centroids = new_centroids # update the centroids
    return clusters # return the clusters


# calculate the manhattan distance between two points
def get_distance_2(point1, point2):
    distance = 0 # initialize distance
    for i in range(len(point1)): # for each dimension
        distance += abs(point1[i] - point2[i]) # add the absolute difference
    return distance # return the distance

# median
def get_centroid_2(points):
    pts = np.array(points) # convert to numpy array
    return np.median(pts, axis=0) # return the median of the points


print("*****************************k-median************************************")
print("k-median")
points = [[3, 7], [2, 4], [3, 6], [7, 8], [9, 7]]
print(k_median(2, points))
