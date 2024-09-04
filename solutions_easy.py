# 1945: Sum of Digits of String After Convert
def getlucky(s, k):
    initsum = str()
    
    for i in s.lower():
        initsum += str(ord(i) - 96)

    for j in range(k):
        sum = 0
        for x in initsum:
            sum += int(x)
            initsum = str(sum)
    return sum

#s = "leetcode"
#k = 2
#getlucky(s, k)


# 9: Palindrome Number
def isPalindrome(x):
    if x < 0:
        return False
    elif len(str(x)) == 1:
        return True
    else:
        for i in range(len(str(x)) // 2):
            if str(x)[i] == str(x)[-(i + 1)]:
                continue
            else:
                return False
        return True

#x = 2147447412
#isPalindrome(x)


