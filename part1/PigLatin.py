class PigLatin(object):
    """docstring for PigLatin
    拉丁猪文字游戏——这是一个英语语言游戏。
    基本规则是将一个英语单词的第一个辅音音素的字母移动到词尾
    并且加上后缀-ay（譬如“banana”会变成“anana-bay”）
    """
    def __init__(self):
        self.notConsonnant = ['a','e','i','o','u','y','w']
        self.temp = ''
    def solution(self,string):
        if len(string) > 0:
            container =  list(string)
            for index in range(len(container)):
                if string[index].lower not in self.notConsonnant:
                    self.temp = container[index]
                    del container[index]
                    break
            return ''.join(container)+"-"+self.temp+"ay"
        else:
            return "empty string"

if __name__ == '__main__':
    print(PigLatin().solution(""))


