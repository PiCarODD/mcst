def search(ver):
	print ver
	T = ""
	old.append(ver)
	for i in range (inp):
		for j in range(len(weight[i])):
			if weight[i][j] not in old:
				T += ver + "," + weight[i][j]
				search(weight[i][j])
				print weight[i][j]
			else:
				search(ver)
				print "else"
	print T

inp = input("Enter number of vertes : ")
vertes = [str(i+1) for i in range(inp)]
weight = [0 for i in range(inp)]
old = []
for i in range(inp):
	weight[i] = raw_input("Enter Weight : ").split(",")

search(vertes[0])
print old