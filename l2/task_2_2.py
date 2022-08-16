# task_2_2
user_tokens = ['в', '5', 'часов', '17', 'минут',
               'температура', 'воздуха', 'была', '+5', 'градусов']
len_list0 = len(user_tokens)

c = 0  # loop counter
while c < len_list0:
    # loop for every char in list item
    for c_chr in user_tokens[c]:
        if c_chr.isdigit() and '.' not in user_tokens[c]:
            len_list0 += 2  # list increment
            user_tokens.insert(c, '"')
            user_tokens.insert(c+2, '"')
            c += 1
            break
    c += 1  # loop increment

len_list1 = len(user_tokens)  # list lenth for string items handling
i = 0  # counter for loop below
# loop for the list items:
while i < len_list1:
    # loop for chars in the string item:
    for i_chr in user_tokens[i]:
        # check if char is digit and the item has no signs of float type:
        if i_chr.isdigit() and '.' not in user_tokens[i]:
            # fetch index of current char:
            i_chr_pos = user_tokens[i].index(i_chr)
            # check that second position has no digit (one-digit number):
            if not user_tokens[i][i_chr_pos+1:].isdigit():
                # insert 0 for one-digit number in the item
                user_tokens[i] = user_tokens[i][:i_chr_pos] + \
                    '0' + \
                    user_tokens[i][i_chr_pos:]
            break
    i += 1  # increment for main loop iteration
# format the output:
f_string = ' '.join(user_tokens)
print(f_string)
