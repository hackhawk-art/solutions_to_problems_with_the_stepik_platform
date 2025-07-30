from collections import defaultdict

def flip_dict(dict_of_lists):
    my_dict = defaultdict(list)
    for k, v in dict_of_lists.items():
        for i in v:
            my_dict[i].append(k)
    return my_dict

data = data = {1: ['a', 'b', 'c'], 2: ['a', 'b', 'c', 'c'], 3: ['c', 'd', 'a'], 4: ['a', 'b', 'r', 'f'], 5: ['y', 'u', 'e', 'w']}

print(flip_dict(data))