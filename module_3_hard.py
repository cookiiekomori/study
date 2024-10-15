data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    hui = 0
    for i in data_structure:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            hui += calculate_structure_sum(i)
        elif isinstance(i, int):
            hui += i
        elif isinstance(i, str):
            hui += len(i)
        elif isinstance(i, dict):
            for k in i.items():
                hui += calculate_structure_sum(k)
    return hui

result = calculate_structure_sum(data_structure)
print(result)
