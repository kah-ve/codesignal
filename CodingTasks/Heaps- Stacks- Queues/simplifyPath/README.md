# Problem
Given an absolute file path (Unix-style), shorten it to the format /<dir1>/<dir2>/<dir3>/....  

Here is some info on Unix file system paths:  

/ is the root directory; the path should always start with it even if it isn't there in the given path;  
/ is also used as a directory separator; for example, /code/fights denotes a fights subfolder in the code folder in the root directory;  
this also means that // stands for "change the current directory to the current directory"  
. is used to mark the current directory;  
.. is used to mark the parent directory; if the current directory is root already, .. does nothing.  

# Solution
```python
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
```
