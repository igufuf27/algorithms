import sys

# Take names of txt files, create matrices with x, y coordinates
for i in range(2):
    data_file_name = sys.argv[i+1]
    file = open(data_file_name, 'r')
    initial_data = file.read()
    file.close()
    if i == 0:
        rect_points = initial_data.split('\n')
        rect_points = [item.split(' ') for item in rect_points]
    else:
        random_points = initial_data.split('\n')
        random_points = [item.split(' ') for item in random_points]


# Based on multiplying vectors AB*BC: result > 0; < 0; = 0 =>
# point C on the left side of AB; right side; exactly on AB
def check(A, B, C):
    A = [float(item) for item in A]
    B = [float(item) for item in B]
    C = [float(item) for item in C]
    return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])


def pointlocation(P, A):
    if (check(P[0], P[1], A) > 0 or check(P[0], P[3], A) < 0 or check(P[2], P[1], A) < 0 or
    check(P[2], P[3], A) > 0):  # check outside the figure
        return 3
    elif (check(P[0], P[1], A) < 0 and check(P[0], P[3], A) > 0) and (check(P[2], P[1], A) > 0 and
    check(P[2], P[3], A) < 0):  # check  inside the figure
        return 2
    elif check(P[0], P[2], A) == 0 or check(P[1], P[3], A) == 0:
        return 0  # check corner points
    else:
        return 1  # it is a point on the figure

for point in random_points:
    print(pointlocation(rect_points, point))
