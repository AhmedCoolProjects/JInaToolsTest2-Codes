# fct => table de verite
f = list(map(str,input('enter your fct plz :').split()))
table = [[0,0,0],[0,1,0],[1,0,0],[1,1,0]]  

for i in f:
	if i == '+':
		f.remove(i)
# print('this is output',f)

#  f= ["A_B_", "A_"]  a = 0 , b = 0 b =1
l = [1,1]
for i in f:
	if len(i) > 1:
		for j in range(0,len(i)) :
			if i[j] == '_':
				if i[j-1] == 'A':  #[0,1]   A_B  l [0,1] 
					l[0] = 0
					if len(i) <= 2:
						for k in table:
							if [0,0]== k[:2]:
								k[-1] = 1
							if [0,1]== k[:2]:
								k[-1] = 1
				if i[j - 1] == 'B':
					l[1] = 0
					if len(i) <= 2:
						for k in table:
							if [0,0]== k[:2]:
								k[-1] = 1    #'A' 'B' 
							if [1,0]== k[:2]:
								k[-1] = 1

		
		for k in table:
			if l == k[:2]:
				k[-1] = 1
	if len(i) == 1:

		if i == 'A':
			for k in table:
				if [1,0]== k[:2]:
					k[-1] = 1
				if [1,1]== k[:2]:
					k[-1] = 1
		else:
			for k in table:
				if [0,1]== k[:2]:
					k[-1] = 1
				if [1,1]== k[:2]:
					k[-1] = 1

print(table)


#A_B + B







