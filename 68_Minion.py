# from itertools import combinations
S = input()
letter_list = [a for a in S]
l = len(letter_list)
Stuart = []
Kevin = []

# # Combinations
all_word = [letter_list[start:end+1] for start in range(l) for end in range(start, l)]

# Playing in Progress
for i in range(0,len(all_word)):
    word = all_word[i][0]
    if (word == 'A'or word == 'E'or word == 'I'or word == 'O'or word == 'U'):
        Kevin.append(all_word[i])
    else:
        Stuart.append(all_word[i])

# Winner Winner Chicken Dinner
if len(Kevin) > len(Stuart):
    print('Kevin',len(Kevin))
elif len(Kevin) == len(Stuart):
    print('Draw')
else:
    print('Stuart',len(Stuart))
