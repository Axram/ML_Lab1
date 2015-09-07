import monkdata as m
import dtree as dt

#Assignment 1 calculatee enropy

m1e = dt.entropy(m.monk1)
m2e = dt.entropy(m.monk2)
m3e = dt.entropy(m.monk3)

print("Monk1 entropy: ", m1e) 
print("Monk2 entropy: ", m2e)
print("Monk3 entropy: ", m3e) 

M1 = [None]*5
M2 = [None]*5
M3 = [None]*5

for i in range(0, 6):
	M1[i] = dt.averageGain(m.monk1, m.attributes[i])
	M2[i] = dt.averageGain(m.monk2, m.attributes[i])
	M3[i] = dt.averageGain(m.monk3, m.attributes[i])

print("		a1: a2: a3, a4: a5: a6")
#for i in range(0.3):
print(M1[0], M1[1],M1[2], M1[3], M1[4], M1[5])	