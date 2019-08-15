'''
    Given the dataset and the ID of an individual in the dataset
    Return the individual's earliest known ancestor
        1. the one at the farthest distance from the input individual.
        2. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.
        3. If the input individual has no parents, the function should return -1.

    * The input will not be empty.
    * There are no cycles in the input.
    * There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
    * IDs will always be positive integers.
    * A parent may have any number of children.

    Example input:
    6

    Parent  Child
    1        3
    2        3
    3        6
    5        6
    5        7
    4        5
    4        8
    8        9
    11       8
    10       1
    Example output:
    10
'''
from util import Queue
dataset = [
    (1,3),
    (2,3),
    (3,6),
    (5,6),
    (5,7),
    (4,5),
    (4,8),
    (8,9),
    (11,8),
    (10,1)
]
def earliest_ancestor(ancestors, starting_node):
    family_tree = {}

    for person in ancestors:
        parent = person[0]
        child = person[1]
        if child in family_tree:
            family_tree[child].append(parent)
        else:
            family_tree[child] = [parent]            
        if parent not in family_tree:
            family_tree[parent] = []

    q = Queue()
    q.enqueue([ starting_node ])
    longest_path = [ starting_node ]

    while q.size() >= 1:
        path = q.dequeue()
        latest = path[-1]

        if len(longest_path) < len(path) or len(longest_path) == len(path) and latest < longest_path[-1]:
            longest_path = path

        for ancestor in family_tree[latest]:
            new_path = path.copy()
            new_path.append(ancestor)
            q.enqueue(new_path)
    
    return longest_path[-1] if len(longest_path) > 1 else -1