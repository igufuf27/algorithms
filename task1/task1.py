import sys
import math
import functools
import statistics as stat

# Take the name of txt file, create a list, change items type, sorting
data_file_name = sys.argv[1]
file = open(data_file_name, 'r')
initial_data = file.read()
file.close()
initial_data_list = initial_data.split('\n')
initial_data_list = [int(item) for item in initial_data_list]
initial_data_list.sort()


# Find the percentile
def percentile(list, percent, key=lambda x: x):
    if not list:
        return None
    k = (len(list)-1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(list[int(k)])
    d0 = key(list[int(f)]) * (c-k)
    d1 = key(list[int(c)]) * (k-f)
    return d0+d1


# 2 numbers after dot
def adjast(value):
    return '%.2f' % round(value, 4)

# Create a list with answers, change items type
answers = [adjast(percentile(initial_data_list, 0.9)), adjast(percentile(initial_data_list, 0.5)),
adjast(max(initial_data_list)), adjast(min(initial_data_list)), adjast(stat.mean(initial_data_list))]
answers = [str(item) for item in answers]

# Print answer with /n separator
print('\n'.join(answers))
