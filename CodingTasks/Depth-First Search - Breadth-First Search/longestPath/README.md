# Problem
Suppose we represent our file system as a string. For example, the string "user\n\tpictures\n\tdocuments\n\t\tnotes.txt" represents:

    user  
        pictures  
        documents  
            notes.txt       
        
The directory user contains an empty sub-directory pictures and a sub-directory documents containing a file notes.txt.

The string "user\n\tpictures\n\t\tphoto.png\n\t\tcamera\n\tdocuments\n\t\tlectures\n\t\t\tnotes.txt" represents:

    user  
        pictures  
            photo.png  
            camera  
        documents  
            lectures  
                notes.txt  
The directory user contains two sub-directories pictures and documents. pictures contains a file photo.png and an empty second-level sub-directory camera. documents contains a second-level sub-directory lectures containing a file notes.txt.

We want to find the longest (as determined by the number of characters) absolute path to a file within our system. For example, in the second example above, the longest absolute path is "user/documents/lectures/notes.txt", and its length is 33 (not including the double quotes).

Given a string representing the file system in this format, return the length of the longest absolute path to a file in the abstracted file system. If there is not a file in the file system, return 0.

Note: Due to system limitations, test cases use form feeds ('\f', ASCII code 12) instead of newline characters.

Example

For fileSystem = "user\f\tpictures\f\tdocuments\f\t\tnotes.txt", the output should be
longestPath(fileSystem) = 24.

The longest path is "user/documents/notes.txt", and it consists of 24 characters.
# Solution
```python
def longestPath(fileSystem):
    
    maxlen = 0
    pathDict = {0: 0}
    
    for file in fileSystem.split("\f"):
        depth = file.count('\t')
        name = len(file) - depth
        if '.' in file:
            # end of path
            maxlen = max(maxlen, pathDict[depth] + name)
        else:
            # not at end of path, save into dictionary and account for forward slash
            pathDict[depth+1] = pathDict[depth] + name + 1
    return maxlen
```
