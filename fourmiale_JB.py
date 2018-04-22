import pants
import math
import random
import csv
import matplotlib.pyplot as plt
import gpxpy.geo

# Variable initialization
pubNodes = []

# Recovery of csv file data and selection of latitude row(6) and longitude row(7)
with open('open_pubs.csv', newline='') as csvfile:
    pubRow = csv.reader(csvfile)
    for row in pubRow:
        try:
            x = float(row[6])
            y = float(row[7])
            pubNodes.append((x, y))
        except:
            continue
print(pubNodes)

# Selection of the first 100 ads on the list
maximum = 100
pubNodes2 = pubNodes[0:maximum]

# Sorts duplicates
pubCoordinate = list(set(pubNodes2))

# Calculating distance with latitude and longitude with gpxpy function
def distancePub(a, b):
    dist = gpxpy.geo.haversine_distance(a[0], b[0], a[1], b[1])

# Solver and World Instanciation
world = pants.World(pubCoordinate, distancePub)
solver = pants.Solver()

# Solution
solution = solver.solve(world)

# Distance and tour
print('Distance = ', solution.distance, 'km')
print(solution.tour)

# Initialization of the graphical coordinates
X = []
Y = []

# Graph function
for node in solution.tour: 
    X.append(node[0])
    Y.append(node[1])
plt.plot(X, Y)

# Display of the graph
plt.show()