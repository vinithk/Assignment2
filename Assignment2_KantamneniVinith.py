#Central Tendency

example_data = [0, 5, 24, 18, 30, 5]

length = len(example_data)

#MEAN
mean = sum(example_data) / length

print("Mean: " + str(mean))

#MEDIAN
if length / 2 == 0:
  median = example_data[length // 2]
else:
  median = (example_data[length // 2] + example_data[length // 2 - 1]) / 2

print("Median: " + str(median))

#MODE 
mode = max(example_data, key = example_data.count)
print("Mode: " + str(mode))