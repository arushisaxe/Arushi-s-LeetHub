class Solution:

# Initial Thought Process:
# store_list = [] to hold qualifying substrings
# cannot have any repeating characters > loop for this
# 1 character also qualifies
# get the max length element in store_list

# Error: (Loop was not actually breaking at a repeated char)
# ("abc" worked b/c those were the only 2 unique chars as well)

# Error: "pwwkew" is returning "pwke"
# so when it reaches pww, while loop does not end up breaking..
# it just says "in store_val" so continue through "j iteration for loop"
# basically need a way to break out of the j for loop
# OR combine the for loop with the while loop and then append
    
    @staticmethod
    def lengthOfLongestSubstring(s: str):
        store_list = []
        
        for i in range(len(s)):
            
            store_val = s[i]
            
            for j in range(i+1, len(s)):
                
                if s[j] in store_val: #(pwke fix)
                    break #(pwke fix)
                
                #add onto store_val until we reach a match
                while s[j] not in store_val:
                    store_val += s[j]
                
            store_list.append(store_val)
                
        #return store_list (testing purposes)
        
        #handles case if store_list is empty & program will break here
        if not store_list:
            return 0
  
        max_val = max(store_list, key=lambda x: len(x))
    
        '''
        # *don't like this brute force sort of approach
            # more code for "" and " "..
        # *find a shorter solution later!
        '''  
        
        if max_val == " ":
            return 1
        else:
            max_length = len(max_val)
            return max_length

'''
#s = input("s = ") ... oh in leetcode you don't specify this
s2 = s.replace('"', '')
solution = Solution()
print(solution.lengthOfLongestSubstring(s2))
'''
