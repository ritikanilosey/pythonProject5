
#Source: https://bit.ly/3eJPW8E
import stats
lst     = [26, 66, 20, 15 , 99, 84, 17, 58]
Stats   = stats.Stats

print("Average\t", Stats.average(lst))
print("MD\t", Stats.meanDeviation(lst))
print("Count 7\t", Stats.count(lst, 7))
print("Length\t", Stats.length(lst))
print("Max\t", Stats.max(lst))
print("Min\t", Stats.min(lst))
print("Range\t", Stats.range(lst))
print("Sum\t", Stats.sum(lst))
print("Sort\t", Stats.sort(lst))
print("Variance", Stats.variance(lst))
print("SD\t", Stats.standardDeviation(lst))
print("Median\t", Stats.median(lst))