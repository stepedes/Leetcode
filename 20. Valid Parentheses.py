class Solution:
    def isValid(self, s: str) -> bool:
        #if str len is odd
        if len(s)%2!=0:
            return False
        
        pairs = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        
        for i in s:
            #if char is valid
            if i in pairs.keys():
                print(i)
                stack.append(i)
            else:
                if stack == []:
                    return False
                #move from stack to a
                a = stack.pop()
                print(a)
                #if i doesnt match the pair
                if i!=pairs[a]:
                    return False
        return stack == []