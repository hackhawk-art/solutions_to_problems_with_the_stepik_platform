from collections import defaultdict

def best_sender(messages, senders):
    my_dict = defaultdict(int)
    for i in range(len(messages)):
        my_dict[senders[i]] += len(messages[i].split(" "))
    #return max(my_dict, key=lambda x: max(x) if min(my_dict.values()) == max(my_dict.values()) else max(my_dict.keys()))
    for k, v in my_dict.items():
        if v == max(my_dict.values()) and min(my_dict.values()) != max(my_dict.values()):
            return k
        elif v == max(my_dict.values()) and min(my_dict.values()) == max(my_dict.values()):
            return max(my_dict.keys())

messages = ['bu bu da', 'bu bu da', 'bu bu da', 'bu bu da', 'bu bu da', 'bu bu net']
senders = ['dima', 'anri', 'timur', 'timur', 'anri', 'dima']

print(best_sender(messages, senders))
