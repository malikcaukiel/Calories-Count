########## Calories Count ##############

import numpy as np

# importing a csv file
calorie_stats = np.genfromtxt('cereal.csv',delimiter = ',')
print(calorie_stats)

# Average calorie count of available specimen
average_calories = np.mean(calorie_stats)
print(average_calories)

# Sorting into sequence
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

# Central point
median_calories = np.median(calorie_stats)   # python auto-sorts
print(median_calories)
                                                                                                
# Percentile value greater than 60
nth_percentile = np.percentile(calorie_stats, 4)
print(nth_percentile)
nth_percentile = 4

# Calories greater
more_calories = 100-nth_percentile
print(more_calories)

# st. dev
calorie_std = np.std(calorie_stats)
print(calorie_std)

####################################################################################################

