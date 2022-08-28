# This is a practical task_1 for lesson 1.
duration = 400153
s = duration  # user input of seconds
div = [60, 60, 24]  # dividers
rem = []  # reminders
names_mapping = []  # mapping of time names

# building a cascade for time-splitting and mapping of time periods:
if (s % div[0]) >= 0:  # check for reminder for seconds
    rem.append(s % div[0])  # keep the reminder of seconds
    names_mapping.append('сек')  # make time name mapping for seconds
    m = int(s - (s % div[0])) / div[0]  # do the calculation of integer minutes
    if (m % div[1]) >= 0:  # check for reminder for minutes
        rem.append(int(m % div[1]))  # keep the reminder of minutes
        names_mapping.append('мин')  # make time name mapping for minutes
        h = int(m - int(m % div[1])) / div[1]  # do the calculation of integer hours
        if (h % div[2]) >= 0:  # check for reminder for hours
            rem.append(int(h % div[2]))  # keep the reminder of hours
            names_mapping.append('час')  # make time name mapping for hours
            d = int(h - int(h % div[2])) / div[2]  # do the calculation of integer days
            if d >= 0:  # check for days reminder
                rem.append(int(d))  # keep the reminder of days
                names_mapping.append('дн')  # make time name mapping for days

rem_reversed = list(reversed(rem))  # reversing of items order in the list (after cascade building)
name_reversed = list(reversed(names_mapping))  # reversing of names order in the list

# formatted output:

print('duration', duration, sep=' ')
for i in range(len(rem_reversed)):
    if rem_reversed[i] != 0:
        print(rem_reversed[i], name_reversed[i], end=' ')
