def simplifyPath(path):

    simple_path = []
    
    for direc in path.split("/"):
        if direc == ".":
            continue
        elif direc == "..":
            if simple_path:
                simple_path.pop()
        else:
            if direc:
                simple_path.append(direc)
    
    return "/" + "/".join(simple_path)
            
