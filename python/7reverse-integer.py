def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sx = str(x)
    sx = sx[::-1]
    if sx[-1] == '-':
        sx = sx[:-1]    #去掉最后一位
        sx = '-' + sx
        
    r_int = int(sx)     #int()方法只保留非零数字
    if r_int <= 2 ** 31 - 1 and r_int >= -(2 ** 31):   #存储32位有符号整数 [−2^31,  2^31 − 1]
        return r_int
    else:
        return 0

print(reverse(-123400))
