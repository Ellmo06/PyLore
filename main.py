from entities import *



def __main__():
	c = entity("test")
	d = entity("test2")
	f = item("door",True)


	entities = []


	entities.append(c)
	entities.append(d)
	entities.append(f)

	for i in entities:
		i.update()

__main__()
