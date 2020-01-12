import sys

# Take name of txt file, open it, create matrix with initial info
file_name = sys.argv[1]
file = open(file_name, 'r')
initial_data = file.read()
file.close()
intervals = initial_data.split('\n')
intervals = [item.split(' ') for item in intervals]

# Create 2 lists with entering and leaving time, convert time format into minutes
for i in range(len(intervals)):
    for j in range(2):
        for k in range(2):
            if i == 0 and j == 0 and k == 0:
                intervals_min_start = [(int(intervals[i][j].split(':')[k]) *
                60 + int(intervals[i][j].split(':')[k+1])) for i in range(len(intervals))]
            elif i == len(intervals) - 1 and j == 1 and k == 0:
                intervals_min_final = [(int(intervals[i][j].split(':')[k]) *
                60 + int(intervals[i][j].split(':')[k+1])) for i in range(len(intervals))]


# Create a whole day - cycle, calculate how much people inside the building each minute,
# find max qty, create rush minutes list, find start and last intervals minutes, reconvert answer
def rush_interval(list1, list2):
    whole_day = [0 for i in range(1440)]
    rush_min = []
    rush_int = []
    for min in range(1440):  # let it be whole day 0:00-24:00
        for i in range(len(list1)):
            if int(intervals_min_start[i]) <= min and int(intervals_min_final[i]) > min:
                whole_day[min] = whole_day[min] + 1
    for i in range(1440):
        if int(whole_day[i]) == int(max(whole_day)):
            rush_min.append(i)  # create a rush minutes list
            
    # take out start and final minutes of rush minutes intervals, adjust final minutes
    for i in range(len(rush_min)):
        if i == 0 or i == len(rush_min) - 1:
            rush_int.append(rush_min[i])
        elif rush_min[i - 1] != int(rush_min[i]) - 1:
            rush_int.append(rush_min[i - 1])
            rush_int.append(rush_min[i])
    for i in range(len(rush_int)):
        if i % 2 == 1:
            rush_int[i] = rush_int[i] + 1

    # reconvert answer back into "mm:ss" form
    for i in range(len(rush_int)):
        if rush_int[i] % 60 == 0:
            rush_int[i] = str(rush_int[i] // 60) + ":0" + str(rush_int[i] % 60)
        else:
            rush_int[i] = str(rush_int[i] // 60) + ":" + str(rush_int[i] % 60)
    result = ""

    # adjust form answer
    for i in range(len(rush_int)):
        if i % 2 == 1:
            result = result + rush_int[i] + "\n"
        else:
            result = result + rush_int[i] + " "
    return result


print(rush_interval(intervals_min_start, intervals_min_final))
