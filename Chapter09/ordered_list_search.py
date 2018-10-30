
def search(ordered_list, term):
    ordered_list_size = len(ordered_list)
    for i in range(ordered_list_size):
        if term == ordered_list[i]:
            return i
        elif ordered_list[i] > term:
            return None

    return None



scores = [2, 3, 4, 6, 7]

search_term = 5
position = search(scores, search_term)

if position is None:
    print("{} not found".format(search_term))
else:
    print("{} found at position {}".format(search_term, position))


search_term = 2
position = search(scores, search_term)
if position is None:
    print("{} not found".format(search_term))
else:
    print("{} found at position {}".format(search_term, position))