
class entity:

	__name = ""

	def __init__(self,nm):
		self.__name = nm

	def getName(self):
		return self.__name

	def update(self):
		#do updated
		print "update "+self.__name
