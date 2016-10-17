from collections import defaultdict
import string
class wordsCount:
	"""docstring for countWord
	统计字符串中的单词数目——统计字符串中单词的数目
	TODO:从一个文本中读出字符串并生成单词数目统计结果。参考http://zzuwxf.iteye.com/blog/366370
	"""
	def __init__(self):
		self.words = defaultdict(int)

	def countWords(self,line):
		strip = string.whitespace + string.punctuation + string.digits + "\"'"
		for word in line.split():
			word = word.strip(strip)
			if len(word) >=2 :
				self.words[word] += 1
		for word, num in self.words.items():
			print("{0} occurs {1} times".format(word,num))

if __name__ == '__main__':
	wordsCount().countWords(" strip = string. whitespace + string. punctuation + string. digits")		