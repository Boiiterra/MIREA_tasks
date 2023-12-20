def To2(a, size):
	s = ""
	while(a>0):
		s = str(a%2) + s
		a //= 2
	if(len(s) < size):
		s = "0" * (size - len(s)) + s
	return s
input_value = input("Введите значения для ячеек:")
data = {}
LEN = -1
for i in range(0,5):
	if(2**i == len(input_value)):
		LEN = i
		break
assert LEN!=-1, "Неправильная размерность"
print("Количество переменных =", LEN)

all_x = []
first = []
second = []

#print("[x1,x2][x3,x4]")
if(LEN!=1):
	print(end="[")
	for i in range(LEN//2):
		print("x" + str(i), end="," if i+1!=LEN//2 else "")
		all_x.append("x" + str(i))
		first.append("x" + str(i))
	print(end="]")
print(end="[")
for i in range(LEN//2, LEN):
	print("x" + str(i), end="," if i+1!=LEN else "")
	all_x.append("x" + str(i))
	second.append("x" + str(i))
print("]")

if(first):
	value = 0
	for x in range(len(first) * 2):
		if(x==2):
			x=3
		elif(x==3):
			x=2
		for y in range(len(second) * 2):
			if(y==2):
				y=3
			elif(y==3):
				y=2
			data["["+To2(x, len(first))+"]["+To2(y, len(second))+"]"] = int(input_value[value])
			value += 1
else:
	for y in range(len(second) * 2):
		data["["+To2(y, len(second))+"]"] = int(input_value[y])
print("-" * 20 + "\nВывод:")
#output
start_x=""
if(first):
	start_x = "["
	for x in range(len(first)):
		start_x += first[x] + ("," if x!=len(first)-1 else "")
	start_x += "]"

start_y = "["
for y in range(len(second)):
	start_y += second[y] + ("," if y!=len(second)-1 else "")
start_y += "]"
print(end=start_x + start_y)
for y in range(len(second) * 2):
	if(y==2):
		y=3
	elif(y==3):
		y=2
	print(To2(y, len(second)), end=" ")
print()
start = len(start_x) + len(start_y)
if(first):
	for x in range(len(first) * 2):
		if(x==2):
			x=3
		elif(x==3):
			x=2
		print(To2(x, len(first)), end=" " * (len(start_x) - len(first) - 1) + "|" + " " * len(start_y))
		for y in range(len(second) * 2):
			if(y==2):
				y=3
			elif(y==3):
				y=2
			print(data["["+To2(x, len(first))+"]["+To2(y, len(second))+"]"], end=" " * (len(second)))
		print()
else:
	print(end=" " * len(start_y))
	for y in range(len(second) * 2):
		print(data["["+To2(y, len(second))+"]"], end=" " * (len(second)))
	print()
zeros = []
points = []
for X in range(len(first) * 2, 0, -1):
	for Y in range(len(second) * 2, 0, -1):
		flag = False
		for i in range(1, 5):
			if(2**i == X*Y):
				flag = True
		if(not flag):
			continue
		for x in range(len(first) * 2 - X + 1):
			for y in range(len(second) * 2 - Y + 1):
				#Check if one of zeros or points
				ix, iy = x, y
				if(ix==2):
					ix=3
				elif(ix==3):
					ix=2
				if(iy==2):
					iy=3
				elif(iy==3):
					iy=2
				value = data["["+To2(ix, len(first))+"]["+To2(iy, len(second))+"]"]
				flag = True
				pos = []
				for ix in range(x, x + X):
					if(ix==2):
						ix=3
					elif(ix==3):
						ix=2
					for iy in range(y, y + Y):
						if(iy==2):
							iy=3
						elif(iy==3):
							iy=2
						pos.append("["+To2(ix, len(first))+"]["+To2(iy, len(second))+"]")
						if(data["["+To2(ix, len(first))+"]["+To2(iy, len(second))+"]"] != value):
							flag = False
							break
					if(not flag):
						break
				if(flag):
					if(value):points.append(pos)
					else:zeros.append(pos)

delta_x = 1
delta_y = 1
if(len(first) > 1):
	delta_x = 2
if(len(second) > 1):
	delta_y = 2

positions = ["["+To2(0, len(first))+"]["+To2(0, len(second))+"]",
	"["+To2(len(first)*2 - delta_x, len(first))+"]["+To2(0, len(second))+"]",
	"["+To2(0, len(first))+"]["+To2(len(second)*2 - delta_y, len(second))+"]",
	"["+To2(len(first)*2 - delta_x, len(first))+"]["+To2(len(second)*2 - delta_y, len(second))+"]",]

def check_round(x0, x1, x2, x3):
	global points, zeros
	pos = [positions[x0]]
	value = data[positions[x0]]
	flag = 0
	if(data[positions[x1]] == value):
		pos.append(positions[x1])
		flag += 1
	if(data[positions[x2]] == value):
		pos.append(positions[x2])
		flag += 1
	if((flag == 2) and (data[positions[x3]] == value)):
		pos.append(positions[x3])
	if(len(pos) != 1):
		if(len(pos) == 3):
			if(value):
				points.append([pos[0], pos[1]])
				points.append([pos[0], pos[2]])
			else:
				zeros.append([pos[0], pos[1]])
				zeros.append([pos[0], pos[2]])
		else:
			if(value):
				points.append(pos)
			else:
				zeros.append(pos)
if(first):
	check_round(0, 1, 2, 3)
	check_round(1, 3, 0, 2)
	check_round(3, 2, 1, 0)
	check_round(2, 0, 3, 1)
	#Up and down
	for x in range(len(first) * 2 - 1):
		if(x == 2):
			x = 3
		value = data["["+To2(x, len(first))+"]["+To2(0, len(second))+"]"]
		if(value == data["["+To2(x, len(first))+"]["+To2(len(second)*2 - delta_y, len(second))+"]"]):
			X = x + 1
			if((X < len(first) * 2) and (value == data["["+To2(X, len(first))+"]["+To2(0, len(second))+"]"]) and (value == data["["+To2(X, len(first))+"]["+To2(len(second)*2 - delta_y, len(second))+"]"])):
				if(value):
					points.append(["["+To2(x, len(first))+"]["+To2(0, len(second))+"]",
						"["+To2(x, len(first))+"]["+To2(len(second)*2 - delta_y, len(second))+"]",
						"["+To2(X, len(first))+"]["+To2(0, len(second))+"]",
						"["+To2(X, len(first))+"]["+To2(len(second)*2 - delta_y, len(second))+"]",])
				else:
					zeros.append(["["+To2(x, len(first))+"]["+To2(0, len(second))+"]",
						"["+To2(x, len(first))+"]["+To2(len(second)*2 - delta_y, len(second))+"]",
						"["+To2(X, len(first))+"]["+To2(0, len(second))+"]",
						"["+To2(X, len(first))+"]["+To2(len(second)*2 - delta_y, len(second))+"]",])
			else:
				if(value):
					points.append(["["+To2(x, len(first))+"]["+To2(0, len(second))+"]",
						"["+To2(x, len(first))+"]["+To2(len(second)*2 - delta_y, len(second))+"]",])
				else:
					zeros.append(["["+To2(x, len(first))+"]["+To2(0, len(second))+"]",
						"["+To2(x, len(first))+"]["+To2(len(second)*2 - delta_y, len(second))+"]",])
	#Left and right
	for y in range(len(second) * 2 - 1):
		if(y == 2):
			y = 3
		value = data["["+To2(0, len(first))+"]["+To2(y, len(second))+"]"]
		if(value == data["["+To2(len(first)*2 - delta_x, len(first))+"]["+To2(y, len(second))+"]"]):
			Y = y + 1
			if((Y < len(second) * 2) and (value == data["["+To2(0, len(first))+"]["+To2(Y, len(second))+"]"]) and (value == data["["+To2(len(first)*2 - delta_x, len(first))+"]["+To2(Y, len(second))+"]"])):
				if(value):
					points.append(["["+To2(0, len(first))+"]["+To2(y, len(second))+"]",
						"["+To2(len(first)*2 - delta_x, len(first))+"]["+To2(y, len(second))+"]",
						"["+To2(0, len(first))+"]["+To2(Y, len(second))+"]",
						"["+To2(len(first)*2 - delta_x, len(first))+"]["+To2(Y, len(second))+"]",])
				else:
					zeros.append(["["+To2(0, len(first))+"]["+To2(y, len(second))+"]",
						"["+To2(len(first)*2 - delta_x, len(first))+"]["+To2(y, len(second))+"]",
						"["+To2(0, len(first))+"]["+To2(Y, len(second))+"]",
						"["+To2(len(first)*2 - delta_x, len(first))+"]["+To2(Y, len(second))+"]",])
			else:
				if(value):
					points.append(["["+To2(0, len(first))+"]["+To2(y, len(second))+"]",
						"["+To2(len(first)*2 - delta_x, len(first))+"]["+To2(y, len(second))+"]",])
				else:
					zeros.append(["["+To2(0, len(first))+"]["+To2(y, len(second))+"]",
						"["+To2(len(first)*2 - delta_x, len(first))+"]["+To2(y, len(second))+"]",])

def check_in(mass):
	i = 0
	while(i<len(mass)):
		g = 0
		while(g<len(mass)):
			if(i==g):
				g+=1
				continue
			kol = [0, 0]
			if(i>=len(mass)):break
			for key in mass[i]:
				if(key in mass[g]):
					kol[0] += 1
			for key in mass[g]:
				if(key in mass[i]):
					kol[1] += 1
			if(kol[0] == len(mass[i])):
				mass = mass[:i] + mass[i + 1:]
			elif(kol[1] == len(mass[g])):
				mass = mass[:g] + mass[g + 1:]
				g -= 1
			g += 1
		i += 1
	return mass
if(first):
	points = check_in(points)
	zeros = check_in(zeros)

	isolated = [[], []]

	for x in range(len(first) * 2):
		if(x==2):
			x=3
		elif(x==3):
			x=2
		for y in range(len(second) * 2):
			if(y==2):
				y=3
			elif(y==3):
				y=2
			pos = "["+To2(x, len(first))+"]["+To2(y, len(second))+"]"
			flag = True
			if(data[pos]):
				for i in range(len(points)):
					if(pos in points[i]):
						flag = False
						break
				if(flag):
					out = ""
					text = pos[1:-1]
					text = text[:text.find("]")] + text[text.find("[") + 1:]
					for key in range(len(text)):
						if(key!=0):
							out += "*"
						if(int(text[key])):
							out += all_x[key]
						else:
							out += "-" + all_x[key]
					isolated[0].append(out)
			else:
				for i in range(len(zeros)):
					if(pos in zeros[i]):
						flag = False
						break
				if(flag):
					out = ""
					text = pos[1:-1]
					text = text[:text.find("]")] + text[text.find("[") + 1:]
					for key in range(len(text)):
						if(key!=0):
							out += "+"
						if(not int(text[key])):
							out += all_x[key]
						else:
							out += "-" + all_x[key]
					isolated[1].append(out)

	output = ""
	for i in range(len(points)):
		out = {}
		for g in range(len(points[i])):
			text = points[i][g][1:-1]
			text = text[:text.find("]")] + text[text.find("[") + 1:]
			for key in range(len(text)):
				if(key in out.keys()):
					if(int(text[key]) != out[key]):
						out[key] = -1
				else:
					out[key] = int(text[key])
		group = ""
		for key in out:
			if(out[key] != -1):
				if(group):
					group += "*"
				if(not out[key]):
					group += "-"
				group += all_x[key]
		if(group):
			if(output):
				output += "+"
			output += group

	if(isolated[0] and output):
		output += "+"
	for i in range(len(isolated[0])):
		if(i != 0):
			output += "+"
		output += isolated[0][i]
	print("МДНФ:", output)
	output = ""
	for i in range(len(zeros)):
		out = {}
		for g in range(len(zeros[i])):
			text = zeros[i][g][1:-1]
			text = text[:text.find("]")] + text[text.find("[") + 1:]
			for key in range(len(text)):
				if(key in out.keys()):
					if(int(text[key]) != out[key]):
						out[key] = -1
				else:
					out[key] = int(text[key])
		group = ""
		for key in out:
			if(out[key] != -1):
				if(group):
					group += "+"
				if(out[key]):
					group += "-"
				group += all_x[key]
		if(group):
			if(output):
				output += "*"
			output += "("+group+")"

	if(isolated[1] and output):
		output += "*"
	for i in range(len(isolated[1])):
		if(i != 0):
			output += "*"
		output += "(" + isolated[1][i] + ")"

	print("МКНФ:", output)
else:
	if((data["[0]"] == 1) and (data["[1]"] == 1)):
		output = "1"
	elif(data["[0]"] == 1):
		output = "-x0"
	elif(data["[1]"] == 1):
		output = "x0"
	else:
		output = "0"
	print("МДНФ:", output)
	if((data["[0]"] == 0) and (data["[1]"] == 0)):
		output = "0"
	elif(data["[0]"] == 0):
		output = "x0"
	elif(data["[1]"] == 0):
		output = "-x0"
	else:
		output = "1"
	print("МКНФ:", output)
input()#Для консоли