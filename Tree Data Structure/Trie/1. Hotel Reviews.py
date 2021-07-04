# Given a string containing good words and a set of hotel reviews by the customers for
# different hotels. You need to count the good words (including duplicates) in the 
# given set of reviews and sort the reviews on this count. 
# If review i and review j have the same Goodness Value (count), then their original
# order would be preserved.

# Example: goodWords = "cool_ice_wifi"
# reviews = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed", "ice_and_ice_cream_is_cool"]
# return = [3, 2, 0, 1]

# Explanation: 
# good words in reviews = [[cool], [ice], [cool, wifi], [ice, ice, cool]]
# count of good words = [1, 1, 2, 3]
# return their indices (according to max no of good words) = [3, 2, 0, 1]


# Method 1: solve using list and reverse sorting according to count
def solve(a, b):
    good_words = set(a.split('_'))
    countTable = []

    for indx, string in enumerate(b):
        count = 0
        for word in string.split('_'):
            if word in good_words:
                count += 1

        countTable.append((indx, count))

    countTable.sort(key = lambda x: x[1], reverse = True)
    return [x[0] for x in countTable]


a = 'cool_ice_wifi'
b = ["water_is_cool", 'cold_ice_drink', 'cool_wifi_wpeed', 'ice_and_ice_cream_is_cool']

print(solve(a,b))


# solve using Trie, Algorithm: 
# 1. Insert all the good words in a trie.
# 2. For each review, calculate the number of good words in it by checking whether a 
#    given word exist in trie or not.
# 3. Output as needed by the solution.

from collections import defaultdict
class Solution:
    def solve(self, A, B):
        self.node = {}
        
        reviews = defaultdict(list)
        for word in A.split('_'):
            self.insert(word)
        for index, string in enumerate(B):
            count = 0
            for word in string.split('_'):
                if self.search(word):
                    count+=1
            reviews[count].append(index)
        res = sorted(reviews.keys(), reverse = True)

        return [i for score in res for i in reviews[score]]
        
    def insert(self, word):
        n = self.node
        for i in word:
            if i not in n:
                n[i] = {}
            n = n[i]
        n['end'] = True
        
    def search(self, word):
        n = self.node
        for i in word:
            if i not in n:
                return False
            n = n[i]
        if 'end' not in n:
            return False
        return True

sol = Solution()
print(sol.solve(a,b))