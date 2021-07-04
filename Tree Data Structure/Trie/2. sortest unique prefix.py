# Find shortest unique prefix to represent each word in the list.

# Example: Input: [zebra, dog, duck, dove] -->  Output: {z, dog, du, dov}

# 1. zebra = z (there is no string in input which starts with z)
# 2. dog, lets use d (but there is duck and dove in input, so we can't use d)
#        take one more char i.e do (but there is dove in input) so add one more char
#        i.e dog

# 3. duck, -> d (there is dove in input that starts with d) so take next char -> du
#              du (there is no other string that starts with du so it is ans)

# 4. similary for dove -> dov is ans  
# result = [z, dog, du, dov]


# Method: using hashtable
# Algorithm: store the frequency of each prefix of the word
# like, for dog -> {'d': 1, 'do': 1, 'dog': 1}
# now if we add dove in this dictionary, 
# then {'d': 2, 'do': 2, 'dog': 1, 'dov': 1, 'dove': 1}

def prefix(words):
    table = {}
    for word in words:
        for i in range(len(word)):
            pref = word[:i]
            if pref in table:
                table[pref] += 1
            else:
                table[pref] = 1
    
    result = []
    for word in words:
        temp = word
        for i in range(1, len(word)):
            pref = word[:i]
            freq = table[pref]
            if freq == 1:
                temp = pref
                break
        result.append(temp)
    return result
                
words = [ "zebra", "dog", "duck", "dove" ]
print(prefix(words))




# Method 2: using Trie

class TrieNode:
    def __init__(self):
        self.children = [None]* 26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        ptr = self.root
        for ch in word:
            indx = ord(ch)- ord('a')
            if not ptr.children[indx]:
                ptr.children[indx] = [TrieNode(), 1]
            else:
                new_ptr, freq = ptr.children[indx]
                ptr.children[indx] = [new_ptr, freq+1]
            ptr,_ = ptr.children[indx]
        
        ptr.isEndOfWord = True
    
    def search(self, word):
        ptr = self.root
        for ch in word:
            indx = ord(ch) - ord('a')
            if not ptr.children[indx]:
                return False
            else:
                ptr, freq = ptr.children[indx]
        
        if ptr != None and ptr.isEndOfWord == True:
            return 1
        else:
            return 0
    
    def unique_prefix(self, word):
        ptr = self.root
        pref = ""
        for ch in word:
            indx = ord(ch) - ord('a')
            ptr, freq = ptr.children[indx]
            if freq == 1:
                return (pref + ch)
            else:
                pref = pref + ch
        return ""

class Solution:
    def prefix(self, words):

        # Trie object 
        trie = Trie() 
        # Construct trie 
        for word in words: 
            trie.insert(word) 
        output = []    
        for word in words:
            output.append(trie.unique_prefix(word))
        return output

sol = Solution()
print(sol.prefix(words))