class StringReverse(object):
    """ 
    输入一个字符串，将其逆转并输出
    """
    def solution(self,string):
        return False if len(string) == 0 else string[::-1]

if __name__ == '__main__':
    print(StringReverse().solution("hello"))
        