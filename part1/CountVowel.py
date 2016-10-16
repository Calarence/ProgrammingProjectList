from collections import defaultdict
class VowelCount(object):
	"""统计元音字母——输入一个字符串，
	统计处其中元音字母的数量。
	更复杂点的话统计出每个元音字母的数量
	特殊输入:空字符串、大小写
	"""
	def __init__(self):
		self.vowelDictionary = defaultdict(int)
		self.vowel = ('a','e','i','o','u')

	def countVowel(self,string):
		if len(string) > 0:
			for element in string:
				if element.lower() in self.vowel:
				    self.vowelDictionary[element] += 1
				else:
					continue
		else:
			self.vowelDictionary
		return self.vowelDictionary

	def format(self,result):
		if len(result) == 0:
			print("vowel not found")
		else:
			for key, value in result.items():
				print(key,'-->',value)


if __name__ == '__main__':
	vowelCount = VowelCount()
	result = vowelCount.countVowel("")
	vowelCount.format(result)

		