import sys
firstLetter = sys.stdin.readline().strip()
secondLetter = sys.stdin.readline().strip()
thirdLetter = sys.stdin.readline().strip()
s = firstLetter + secondLetter

#If the total length of the first and second lines of letters is different from that of the third line, output 'NO' directly


if len(s) != len(thirdLetter):      
    print("NO")
else:
    for i in range(len(s)):
        c = s[i]
        flag = False
        for j in range(len(thirdLetter)):
            if thirdLetter[j] == c:
                thirdLetter = thirdLetter[:j] + thirdLetter[j+1:]
                flag = True                            #Indicates that the corresponding letter of this letter in thirdLetter was found
                break
        if not flag:
            print("NO")
            break
    if flag: print("YES")
    
