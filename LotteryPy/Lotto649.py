import json
import numpy
import time


def lotto649():

    start = (time.time()*1000)

    lotterylist = json.load(open("Lotto649.json"))
    test = []

    for i in range(0, len(lotterylist["Lotto649"])):
        test.append(lotterylist["Lotto649"][i]["Numbers"])

    # flatten list into a single list instead of list of lists.
    flat_list = [item for sublist in test for item in sublist]

    # # use collections to count frequency of elements in flattened list.
    # ctr = collections.Counter(flat_list)
    # print(ctr)

    # use numpy to pull frequency from flattened list
    vals, counts = numpy.unique(flat_list, return_counts=True)
    # print(vals, counts)

    # zip the results into a dictionary of value, frequency
    results = dict(zip(vals, counts))

    # sorts by descending order by count
    sorted_by_value = sorted(results.items(), key=lambda kv: kv[1], reverse=True)
    # print(sorted_by_value)

    # Uses pandas to pull a frequency table.
    # furthertest = pandas.Series(flat_list).value_counts().sort_index()
    # print(furthertest)

    with open("649Singles.txt", "w") as f:
        f.write('\n'.join('Number: %s, Frequency: %s' % x for x in sorted_by_value))
    end = (time.time()*1000)
    print(f"Lotto649 Time to Execute: {end - start} ms\n")

    # Home System - ~350 - 400 ms
