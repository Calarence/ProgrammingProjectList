from collections import deque
class TextMatch(object):
	"""docstring for TextMatch
	对一系列文本行做简单的文本匹配操作，
	当发现有匹配时就输出当前的匹配行以及最后检查过的N行文本
	"""
	def search(self,lines,pattern,history=5):
		previous_lines = deque(maxlen=5)
		for line in lines:
			if pattern in line:
				yield line, previous_lines
			previous_lines.append(line)

if __name__ == '__main__':
	test = TextMatch()
	with open('somefile.txt') as f:
		for line,prevlines in test.search(f,"python",5):
			for pline in prevlines:
				print(pline,end='')
			print(line,end='')
			print('-'*20)
		