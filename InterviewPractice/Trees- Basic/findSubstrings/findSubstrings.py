class Trie:
    def __init__(self, char):
        self.char = char
        self.end = False
        self.next = {}
        
def addToTrie(root, part):
    curr = root
    for char in part:
        if char not in curr.next:
            curr.next[char] = Trie(char)
        curr = curr.next[char]
    
    curr.end = True

def findParts(word, root):
    trackLongest = 0
    indxLongest = 0
    
    #start from an index pos in each word
    for indx1 in range(len(word)):
        curr = root
        # iterate ahead of each index to see if it fits part
        for indx2 in range(indx1, len(word)):
            char = word[indx2]
            if char not in curr.next:
                break
            else:
                curr = curr.next[char]
                tempLength = indx2 - indx1 + 1
                #  if the part exists in word and its length is the longest in word
                if curr.end == True and tempLength > trackLongest:
                    trackLongest = tempLength
                    indxLongest = indx1
    
    if trackLongest > 0:
        indxBrackets = indxLongest + trackLongest
        return word[0:indxLongest] + "[" + word[indxLongest:indxBrackets] + "]" + word[indxBrackets:]
    else:
        return word 

# Not much to this function 
# It just ties everything else together
def findSubstrings(words, parts):
    #  add parts to Trie
    root = Trie('')
    for part in parts:
        addToTrie(root, part)
    
    #iterate over each word and replace in array
    returnArray = []
    for indx, word in enumerate(words):
        words[indx] = findParts(word, root)
    return words
