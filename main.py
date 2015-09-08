import monkdata as m
import dtree as dt
import drawtree as dw

def print_average_gains(av_gain, av_gain_name = "", print_range = 6):
        " Prints with nice format"
        print(av_gain_name, end = "\t")
        for i in range(print_range):
                print(round(av_gain[i], 4), end = "\t")
        print("")

def draw_tree(dataset):
        "Draws a decision tree from dataset "
        t = dt.buildTree(dataset, m.attributes)
        dw.drawTree(t)
        return t

def build_and_check(dataset, testset):
        "Builds a dec tree from datast and checks the performance on test set"
        t = dt.buildTree(dataset, m.attributes)
        performance_train = dt.check(t, dataset)
        performance_test = dt.check(t, testset)
        return t, [performance_train, performance_test]

def print_table(row_names, col_names, data):
        "Print a table with arbitrary number of columns and one row"
        print("\t\t\t", end = "")
        for i in col_names:
                print(i, end = "\t")
        print("")
        for index, name in enumerate(row_names):
                print(name, end = "\t")
                for i in data[index]:
                        print(round(i, 2), end = "\t")
                print("")
        print("")

## Assignment 1: Calculate entropy

print("\nAssignment 1")
m1e = dt.entropy(m.monk1)
m2e = dt.entropy(m.monk2)
m3e = dt.entropy(m.monk3)

print("Monk1 entropy: ", m1e) 
print("Monk2 entropy: ", m2e)
print("Monk3 entropy: ", m3e) 
print("")

## Assignment 2: Calculate average gains of all attributes in all data sets
print("Assignment 2")
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

## Assignment 3: Build decision trees of all data sets
print("Assignment 3")
monk1_tree, monk1_performance = build_and_check(m.monk1, m.monk1test)
monk2_tree, monk2_performance = build_and_check(m.monk2, m.monk2test)
monk3_tree, monk3_performance = build_and_check(m.monk3, m.monk3test)
print_table(["Performance Train", "Performance Test"],
            ["MONK1", "MONK2", "MONK3"],
            [[monk1_performance[0], monk2_performance[0], monk3_performance[0]],
            [monk1_performance[1], monk2_performance[1], monk3_performance[1]]])

draw_tree(m.monk1)
#draw_tree(m.monk2)
#draw_tree(m.monk3)

# Check performance



        


