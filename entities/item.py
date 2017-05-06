from entity import entity

class item(entity):

	__cam_carry = False

	def __init__(self,nm,carry=False):
		entity.__init__(self,nm)
		__cam_carry=carry

	def canCarry(self):
		return __cam_carry