def groupingDishes(dishes):
    ret_dict = {}
    for i in dishes:
        for j in range(len(i)):
            if j == 0:
                pass
            else:
                if i[j] not in ret_dict:
                    ret_dict[i[j]] = [i[0]]
                else:
                    ret_dict[i[j]].append(i[0])
    
    length_keys = len(ret_dict)
    return_array = []
    
    for i in ret_dict:
        temp_array = []
        if (len(ret_dict[i]) >= 2):
            temp_array.append(i)
            temp_array.extend(ret_dict[i])
            return_array.append(temp_array)
            
    
    return_array.sort(key=lambda lst : lst[0])
    for i in range(len(return_array)):
        to_sort = return_array[i][1:]
        to_sort.sort()
        return_array[i][1:] = to_sort

    return return_array
        
