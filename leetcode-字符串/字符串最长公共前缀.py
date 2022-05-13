import sys
def longestCommonPrefix(strs):
    if not strs:
            return 0
        
    short = min(strs, key=len) # 取出最短字符串

    for i in range(len(short)):
        char = short[i]
        for s in strs:
            if s[i] != char: # 只要遇到不相等的位置，则算法终止
                return len(short[:i])

    return len(short)

if '__main__' == __name__:
    n=int(input())
    strss=[]
    for _ in range(n):
        strss.append(input())
    while True:
        strs=[]
        line = sys.stdin.readline()
        if not line:
            break
        x, y = (int(i) for i in line.split())
        strs.append(strss[x-1])
        strs.append(strss[y-1])
        print(longestCommonPrefix(strs))