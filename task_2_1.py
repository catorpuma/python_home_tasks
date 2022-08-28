# This is a python script for task2 lesson1.
# calculating the odd numbers, and it's cubes:

cube_list = []  # store for cubes of odd numbers
i = 0  # counter
while i < 1000:  # range of iteration
    if i % 2 != 0:
        rem_list = i ** 3
        cube_list.append(rem_list)
    i += 1

cube_list17 = []  # list for cubes of odd numbers +17
sum_of_cubes = []  # list to keep the sum of digits where %7 == 0

# code below iterate list of cubes by it members
for cube in cube_list:
    cube_list17.append(cube+17)  # keep the sum with 17 in the list for following calculations
    cube_digits = []  # list for digits

    while cube > 0:
        cube_digits.append(cube % 10)
        cube = cube // 10

    if (sum(cube_digits) % 7) == 0:
        s = sum(cube_digits)  # auxiliary
        sum_of_cubes.append(s)

print('required sum for the fist list is :', sum(sum_of_cubes))

sum_of_cubes17 = []
for cube17 in cube_list17:
    cube_digits17 = []  # list for digits

    while cube17 > 0:
        cube_digits17.append(cube17 % 10)
        cube17 = cube17 // 10

    if (sum(cube_digits17) % 7) == 0:
        s17 = sum(cube_digits17)  # auxiliary
        sum_of_cubes17.append(s17)

print('required sum for the second list (cube_of_odd_num+17) is :', sum(sum_of_cubes17))
