# waopp to display sal, id, name of emp and display taxes according to sal

class emp:
	def __init__(self, id, name, sal):
		self.id = id
		self.name = name
		self.sal = sal
	def show(self):
		print("id =", self.id)
		print("name =", self.name)
		print("sal =", self.sal)
	def taxes(self):
		if self.sal > 10000:
			tax = self.sal * 0.20
		else:
			tax = self.sal * 0.10
		print("tax = ", tax)
id = int(input("enter id "))
name = input("enter name ")
sal = float(input("enter sal "))

e1 = emp(id, name, sal)
e1.show()
e1.taxes()