class Palindrome(object):
	"""
	判断是否为回文——判断用户输入的字符串是否为回文。
	回文是指正反拼写形式都是一样的词，譬如“racecar”
	空字符串或单个字符看作回文;忽略大小写
	TODO:若含有特殊字符，忽略特殊字符，只关注字母;数字也要考虑
	solution:1.使用堆栈;2.使用双指针;这里采用双指针方法
	时间复杂度O(n),空间复杂度O(1)
	"""
	def validPalindrome(self,string):
		if not string:
			return True
		left, right = 0, len(string) - 1
		while left < right:
			if not string[left].isalnum():
				left += 1
				continue
			if not string[right].isalnum():
				left -= 1
				continue
			if string[left].lower() == string[right].lower():
				left += 1
				right -= 1
			else:
				return False
			return True
if __name__ == '__main__':
	print(Palindrome().validPalindrome("123aba321d"))
