'''
Print out each element of the following array on a separate line, but this time the input array can contain arrays nested to an arbitrarily deep level:

['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]


'''

a = [
    'Bob',
    'Slack',
        ['reddit',
         '89',
         101,
            ['alacritty',
             '(brackets)',
             5,
             375
             ]
        ],
    0,
    ['{slice, owned}'],
    22]

# for element in array
    # print(element)
# for item in a:
#     print(item)

# define a function that takes an array
# if an array exists within the array perform the function on it

def print_all_items(array):
    for item in array:
        # if item is an array:
        if type(item) == list:
            print_all_items(item)
        else:
            print(item)


print_all_items(a)
