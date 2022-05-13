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

if '__main__' == __name__:
    arr = input()
    strs = [n for n in arr.split(',')]
    print(longestCommonPrefix(strs))