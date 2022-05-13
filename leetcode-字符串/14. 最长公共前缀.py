def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    从左到右，并行扫描，当某一位置的所有字符都相等时，公共字符串长度+1，继续扫描下一位。    
    """
    
    result = ''
    i = 0
    while(True):
        char = ''
        for s in strs: # 每个i都遍历一遍所有字符串
            if i < len(s):
                if char == '': # 说明是strs[0][i]，直接赋值
                    char = s[i]
                elif char != s[i]: # 说明s[i] != strs[0][i]，程序可以终止了
                    char = ''
                    break
            else:
                char = ''
                break
        if char == '':
            break
        else:
            result += char
            i += 1
    return result

def longestCommonPrefix2(strs):
    """
    :type strs: List[str]
    :rtype: str
    改进版。仍然是从左到右并行扫描，但是这次以最短字符串为基准，只要与最短字符串不相同，则算法结束。
    免去了判断是否溢出和字符相加的过程。
    """
    
    if not strs:
        return ''
    
    short = min(strs, key=len) # 取出最短字符串
    
    for i in range(len(short)):
        char = short[i]
        for s in strs:
            if s[i] != char: # 只要遇到不相等的位置，则算法终止
                return short[:i]
        
    return short

if '__main__' == __name__:
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix2(strs))