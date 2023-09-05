class Solution:
    
#0 need to get user input and create an instance of Solution to output
#1 store_list = [] to hold qualifying substrings
#2 cannot have any repeating characters > loop for this
#3 1 character also qualifies
#4 get the max length element in store_list

    # pwwkew is returning pwke
    # so when it reaches pww, your while loop does not end up breaking,
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
    
        if max_val == " ":
            return 1
        else:
            max_length = len(max_val)
            return max_length

'''
        #(return 0 bc get value error is max() is ran on empty list)
        if not store_list:
            return 0
        else:
            return max_length
       
# ohh so in this code: "pwwkew" is outputting "pwke" as one of the substrings
# returning 4 instead of what should be 3
# basically my program here is not going in order and breaking in between
# it keeps on going to get all the unique chars loll.


#s = input("s = ") ... oh in leetcode you don't specify this
s2 = s.replace('"', '')
solution = Solution()
print(solution.lengthOfLongestSubstring(s2))
'''
