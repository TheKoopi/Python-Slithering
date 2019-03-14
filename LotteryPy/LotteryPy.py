#Lottery Py

import json
import pandas
import numpy
import collections


lotterylist = json.load(open(r"H:\Coding\Lotto Numbers\649\649.json"))
test = []
cutest = []
a = 0

for i in range(0,len(lotterylist["Lotto649"])):
    test.append(lotterylist["Lotto649"][i]["Numbers"])

# flatten list into a single list instead of list of lists.
flat_list = [item for sublist in test for item in sublist]

# use collections to count frequency of elements in flattened list.
ctr = collections.Counter(flat_list)
print(ctr)

# use numpy to pull frequency from flattened list
vals, counts = numpy.unique(flat_list, return_counts=True)
#print(vals, counts)

# zip the results into a dictionary of value, frequency
results = dict(zip(vals, counts))

# sorts by descending order by count
sorted_by_value = sorted(results.items(), key=lambda kv: kv[1], reverse = True)
#print(sorted_by_value)

# Uses pandas to pull a frequency table.
furthertest = pandas.Series(flat_list).value_counts().sort_index()
print(furthertest)