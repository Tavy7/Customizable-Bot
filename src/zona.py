# clasa pentru a memora zona de hover
class Zona:
	def __init__(self, coordonate):
		self.xmin = coordonate[0][0]
		self.xmax = coordonate[1][0]
		self.ymin = coordonate[0][1]
		self.ymax = coordonate[1][1]

	def __str__(self):
		return ' xmin={}\n xmax={}\n ymin={}\n ymax={}'.format(self.xmin, self.xmax, self.ymin, self.ymax)

	def onButton(self, x, y):
		cond1 = self.xmin <= x and x <= self.xmax
		cond2 = self.ymin <= y and y <= self.ymax

		return cond1 and cond2