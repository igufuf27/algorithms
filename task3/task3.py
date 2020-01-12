import sys

data_file_name = ['Cash1.txt', 'Cash2.txt', 'Cash3.txt', 'Cash4.txt', 'Cash5.txt']
initial_data = []
hours = []

# Take names of txt files, create matrix with initial info
path = sys.argv[1]
for i in range(5):
    file = open(path + "\\" + data_file_name[i], 'r')
    initial_data.insert(i, file.read())
    file.close()
    hours.insert(i, initial_data[i].split('\n'))


# Calculate max customers qty, return interval number (index + 1)
def interval(hours):
    total_num = [0 for i in range(16)]
    for i in range(16):
        for j in range(5):
            total_num[i] = total_num[i] + float(hours[j][i])
    return (int(total_num.index(max(total_num)) + 1))

print(interval(hours))
