

def search(unordered_list, term):
    unordered_list_size = len(unordered_list)
    for i in range(unordered_list_size):
        if term == unordered_list[i]:
            return i

    return None



scores = [60, 1, 88, 10, 11, 600]

search_term = 65
position = search(scores, search_term)

if position is None:
    print("{} not found".format(search_term))
else:
    print("{} found at position {}".format(search_term, position))


search_term = 600
position = search(scores, search_term)
if position is None:
    print("{} not found".format(search_term))
else:
    print("{} found at position {}".format(search_term, position))