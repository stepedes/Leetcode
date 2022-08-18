class Solution:
    def romanToInt(self, s: str) -> int:
        i,j,sum = 0,0,0
        s += " "
        while i < len(s):
            print("i="+str(i))
            if s[i]=="I":
                if s[i+1]=="V":
                    sum += 4    
                    print ("IV = 4")
                    j += 1
                elif s[i+1]=="X":
                    sum += 9
                    print ("IX = 9")
                    j += 1
                else:
                    sum += 1
                    print ("I = 1")
            elif s[i]=="V":
                sum += 5
                print ("V = 5")
            elif s[i]=="X":
                if s[i+1]=="L":
                    sum += 40
                    print ("XL = 40")
                    j += 1
                elif s[i+1]=="C":
                    sum += 90
                    print("XC = 90")
                    j += 1
                else:
                    sum += 10
                    print ("X = 10")
            elif s[i]=="L":
                sum += 50
                print ("L = 50")
            elif s[i]=="C":
                if s[i+1]=="D":
                    sum += 400 
                    print ("CD = 400")
                    j += 1
                elif s[i+1]=="M":
                    sum += 900
                    print ("CM = 900")
                    j += 1
                else:
                    sum += 100
                    print ("C = 100")
            elif s[i]=="D":
                sum += 500
                print ("D = 500")
            elif s[i]=="M":
                sum += 1000
                print ("M = 1000")
            i += 1
            i += j
            j = 0
        print(sum)
        return(sum)