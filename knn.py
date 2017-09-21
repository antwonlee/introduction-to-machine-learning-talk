from math import sqrt

# K-Nearest Neighbor
# Euclidean Distance Example

plot1 = [1, 3]
plot2 = [2, 5]

euclidean_distance = sqrt( (plot1[0] - plot2[0])**2 + (plot1[1] - plot2[1])**2 )

print(euclidean_distance)
