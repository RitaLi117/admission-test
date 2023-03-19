def count(input):
    input = input1
    count_char = {}

    for char in input:
        if char not in count_char:
            count_char[char] = 0
        count_char[char] += 1

    return count_char


input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


def group_by_key(input):
    input = input2
    group = {}

    for key in input:
        if key['key'] not in group:
            group[key['key']] = key['value']
        else:
            group[key['key']] += key['value']

    return group


input2 = [
{'key': 'a', 'value': 3}, {'key': 'b', 'value': 1}, {'key': 'c', 'value': 2}, {'key': 'a', 'value': 3}, {'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}