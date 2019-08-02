class Lyrics(object):
	def __init__(self, text):
		self.text = text
	
	def paragraphs(self):
		return self.text.split('\n\n')

	def __str__(self):
	 return self.text