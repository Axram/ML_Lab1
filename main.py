import monkdata as m
import dtree as dt
import drawtree as dw
import random

def print_average_gains(av_gain, av_gain_name = "", print_range = 6):
        #Prints with nice format
        print(av_gain_name, end = "\t")
        for i in range(print_range):
                print(round(av_gain[i], 4), end = "\t")
        print("")

def draw_tree(dataset):
        #Draws a decision tree from dataset
        t = dt.buildTree(dataset, m.attributes)
        dw.drawTree(t)
        return t

def check_tree_performance(tree, testset):
        '''
        Builds a dec tree from dataset and 
        checks the performance on test set
        '''
        performance_test = dt.check(tree, testset)
        return performance_test

def partition(data, fraction):
        ldata = list(data)
        random.shuffle(ldata)
        breakPoint = int(len(ldata)*fraction)
        return ldata[:breakPoint], ldata[breakPoint:]

def print_table(row_names, col_names, data):
        #Print a table with arbitrary number of columns and one row
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

def make_pruned(dataset, testset, ratio = 0.5):
        '''
        Takes data- and testset and partitions data. 
        Then makes pruned tree and checks performance
        '''
        test, val = partition(dataset, ratio)
        tree = dt.buildTree(test, m.attributes)
        per_ref = check_tree_performance(tree, testset)
        best = prune(tree, val, per_ref)
        per_pruned = check_tree_performance(best, testset)
        return best, per_ref, per_pruned

def prune(tree, testdata, performance_ref):
        #Prunes tree from given test data
        alternatives = dt.allPruned(tree)
        best_per = 0
        best_tree = None
        for subtree in alternatives:
                performance = dt.check(subtree, testdata)
                if performance > best_per:
                        best_per = performance
                        best_tree = subtree
        if best_per >= performance_ref:
                return prune(best_tree, testdata, performance_ref)
        else:
                return tree
        
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

# Build all trees and check performance
monk1_tree = dt.buildTree(m.monk1, m.attributes)
monk1_performance = check_tree_performance(monk1_tree, m.monk1test)
monk1_train_per = check_tree_performance(monk1_tree, m.monk1)
monk2_tree = dt.buildTree(m.monk2, m.attributes)
monk2_performance = check_tree_performance(monk2_tree, m.monk2test)
monk2_train_per = check_tree_performance(monk2_tree, m.monk2)
monk3_tree = dt.buildTree(m.monk3, m.attributes)
monk3_performance = check_tree_performance(monk3_tree, m.monk3test)
monk3_train_per = check_tree_performance(monk3_tree, m.monk3)
print_table(["Performance Train", "Performance Test"],
            ["MONK1", "MONK2", "MONK3"],
            [[monk1_train_per, monk2_train_per, monk3_train_per],
            [monk1_performance, monk2_performance, monk3_performance]])
# Draw trees
#draw_tree(m.monk1)
#draw_tree(m.monk2)
#draw_tree(m.monk3)

## Assignment 4: Prune tree and plot class error as function of partition size

lbest = []
lper_ref = []
lper_pruned = []

# Loop gets pruned trees for all 3 data sets
for i in [(m.monk1, m.monk1test), (m.monk2, m.monk2test), (m.monk3, m.monk3test) ]:
        best, per_ref, per_pruned = make_pruned(i[0], i[1], 0.5)
        lbest.append(best)
        lper_ref.append(per_ref)
        lper_pruned.append(per_pruned)
print(lper_ref+lper_pruned)

print_table(["Unpruned decision tree", "Pruned decision tree"],
            ["MONK1", "MONK2", "MONK3"],
            [lper_ref, lper_pruned])

        


