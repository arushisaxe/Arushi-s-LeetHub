class Solution:
    
#0 need to get user input and create an instance of Solution to output
#1 store_list = [] to hold qualifying substrings
#2 cannot have any repeating characters > loop for this
#3 1 character also qualifies
#4 get the max length element in store_list

    @staticmethod
    def lengthOfLongestSubstring(s: str):
        
        max_length = 0

        for i in range(len(s)):
            store_val = s[i]
            j = i + 1

            while j < len(s) and s[j] not in store_val:
                store_val += s[j]
                j += 1

            max_length = max(max_length, len(store_val))

        return max_length
    
'''
        store_list = []
        
        for i in range(len(s)-1):
            
            store_val = s[i]
            
            for j in range(i+1, len(s)-1):
                
                #add onto store_val until we reach a match
                while s[j] not in store_val:
                    store_val += s[j]
                
            store_list.append(store_val)
                
        return store_list
    
        #max_val = max(store_list, key=lambda x: len(x))
        #max_length = len(max_val)
        
        #return max_length
        
# ohh so in this code: "pwwkew" is outputting "pwke" as one of the substrings
# returning 4 instead of what should be 3
# basically my program here is not going in order and breaking in between
# it keeps on going to get all the unique chars loll.
# use an AND statement to say 


#s = input("s = ") ... oh in leetcode you don't specify this
s2 = s.replace('"', '')
solution = Solution()
print(solution.lengthOfLongestSubstring(s2))
'''
