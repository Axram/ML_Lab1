import monkdata as m
import dtree as dt
import drawtree as dw

def print_average_gains(av_gain, av_gain_name = "", print_range = 6):
        print(av_gain_name, end = "\t")
        for i in range(print_range):
                print(round(av_gain[i], 4), end = "\t")
        print("")

def draw_tree(dataset):
        t = dt.buildTree(dataset, m.attributes)
        dw.drawTree(t)
        return t

        
# Assignment 1 calculate entropy

print("")
m1e = dt.entropy(m.monk1)
m2e = dt.entropy(m.monk2)
m3e = dt.entropy(m.monk3)

print("Monk1 entropy: ", m1e) 
print("Monk2 entropy: ", m2e)
print("Monk3 entropy: ", m3e) 
print("")

# Assignment 2: Calculate average gains of all attributes in all data sets

M1 = []
M2 = []
M3 = []

for i in range(6):
	M1.append(dt.averageGain(m.monk1, m.attributes[i]))
	M2.append(dt.averageGain(m.monk2, m.attributes[i]))
	M3.append(dt.averageGain(m.monk3, m.attributes[i]))

print("\ta1: \ta2: \ta3: \ta4: \ta5: \ta6:")
print_average_gains(M1, "M1")
print_average_gains(M2, "M2")
print_average_gains(M3, "M3")	

# Assignment 3: Build decision trees of all data sets
draw_tree(m.monk1)
#draw_tree(m.monk2)
#draw_tree(m.monk3)





        


