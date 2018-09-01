def swapLexOrder(str, pairs):

    # first find the connected components in the pairs
    connected_components = []

    set_pairs = [set([x-1, y-1]) for x, y in pairs]
    return_string = list(str)

    while set_pairs:
        connected_component = set_pairs.pop()
        while True:
            anyChange = False
            for pair in set_pairs:
                if connected_component.intersection(pair):
                    connected_component = connected_component.union(pair)
                    set_pairs.remove(pair)
                    anyChange = True
            if anyChange:
                pass
            else:
                break
        ordered = sorted([return_string[i] for i in connected_component], reverse=True) # sort letters descending
        for indx, i in enumerate(sorted(connected_component)): #sort index positions ascending
            return_string[i] = ordered[indx]
    return "".join(return_string)
