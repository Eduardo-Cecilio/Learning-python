#--------------------------------
#Name:          Eduardo  Cecilio
#Username:      n/a
#Problem Set:   PS1
#Due Date:      January 29, 2019
#---------------------------------

#1 if the passenger was in rst class, 0 if not
firstClass = []
#0 for male, 1 for female
gender = []
#0 for ages less than 25, 1 for ages greater than or equal to 25
age = []
# 0 if not siblings or spouse present, 1 if true
siblings_or_spouse = []
# 0 if no parents or children were present, 1 if true
parent_or_children = []
# 1 if passenger left from Southampton, 0 if not.
embarked = []
# 0 if passenger did not survive, 1 if true
survived = []  
#used to make   
sur1 = []
sur0 = []

#Read he data and divide it into lists for each col. 
def readData():
    text = open('titanicdata.csv')
    line = text.readline()
    while line != "":
        line = text.readline()
        result = [x.strip() for x in line.split(',')]   
        if line != "":
            firstClass.append(result[0]) 
            gender.append(result[1]) 
            age.append(result[2]) 
            siblings_or_spouse.append(result[3]) 
            parent_or_children.append(result[4]) 
            embarked.append(result[5])  
            survived.append(result[6]) 
    text.close()

#sorts the 1 and 0. -> issue the 1 is a string and not a number. 
def sort_Dead_Survived(list_arg):
    i = 0
    for x in list_arg:
        if x is "1":
            #firstClass1.append(x)
            sur1.append(survived[i])
        else:
            #firstClass0.append(x)
            sur0.append(survived[i])
        i = i + 1

#count used to count the ones that survived(1) and the ones that died(0)
def countofAlive(list_arg):
    countSurvived = 0
    for x in list_arg:
        if x is "1":
            countSurvived = countSurvived + 1
    return countSurvived

def countofDead(list_arg):
    countDead = 0
    for x in list_arg: 
        if x is "0":
            countDead = countDead + 1
    return countDead

def find_ArgMax(arg_alive, arg_dead):
    if arg_alive > arg_dead:
        argMax = arg_alive
    else: 
        argMax = arg_dead
    return argMax

def calc_Majority(arg_sur):
    return find_ArgMax(countofAlive(arg_sur), countofDead(arg_sur))

def print_info(list_arg):
    surv = countofAlive(list_arg)
    dead = countofDead(list_arg)
    maxN = find_ArgMax(surv, dead)
    print "\t\tNumber that Survived:\t %r" % surv
    print "\t\tNumber that Died:\t %d" % dead
    print "\t\tmajority1: %d" % maxN

def calc_accuracy(maj0_arg, maj1_arg, arg_list):
    return (maj0_arg + maj1_arg)/ float(len(arg_list))

def calc_error(accuracy_arg):
    return 1 - accuracy_arg

def clear_sur(sur1_arg, sur0_arg):
    del sur1_arg[:]
    del sur0_arg[:]

#reads the data
readData()

#calculatoins for First Class (not cleaned up code)
sort_Dead_Survived(firstClass)
countSurvived = countofAlive(sur1)
countDead = countofDead(sur1)
argMax = find_ArgMax(countSurvived, countDead)
majority1 = argMax
print "First Class\t %d" % len(firstClass)
print "\tPassangers that were First Class \t %d" % len(sur1)
print_info(sur1)
countSurvived = countofAlive(sur0)
countDead = countofDead(sur0)
argMax = find_ArgMax(countSurvived, countDead)
majority0 = argMax
accuracy = calc_accuracy(majority0, majority1, firstClass)
err = calc_error(accuracy)
print "\tPassangers were NOT First Class\t %d" % len(sur0)
print_info(sur0)
print "Accuracy: %r" % accuracy 
print "Error: %r" % err 

#clear sur1 and sur0 due to appending in def 
clear_sur(sur1, sur0)
sur1 = []
sur0= []

print "----------------------------------------------------"

#Calculate for gender
sort_Dead_Survived(gender)

majority1 = calc_Majority(sur1)
print "Gender\t %d" % len(gender)
print "\tPassangers that were Male \t %d" % len(sur1)
print_info(sur1)

majority0 = calc_Majority(sur0)
print "\tPassangers were Female\t %d" % len(sur0)
print_info(sur0)

accuracy = calc_accuracy(majority0, majority1, gender)
err = calc_error(accuracy)
print "Accuracy: %r" % accuracy 
print "Error: %r" % err 

#clear sur1 and sur0 due to appending in def 
clear_sur(sur1, sur0)
sur1 = []
sur0= []

print "----------------------------------------------------"
#Calculate for Age
sort_Dead_Survived(age)

majority1 = calc_Majority(sur1)
print "Age\t %d" % len(age)
print "\tPassangers that were 25 or older \t %d" % len(sur1)
print_info(sur1)

majority0 = calc_Majority(sur0)
print "\tPassangers were younger than 25\t %d" % len(sur0)
print_info(sur0)

accuracy = calc_accuracy(majority0, majority1, age)
err = calc_error(accuracy)
print "Accuracy: %r" % accuracy 
print "Error: %r" % err 

#clear sur1 and sur0 due to appending in def 
clear_sur(sur1, sur0)
sur1 = []
sur0= []

print "----------------------------------------------------"
#Calculate for Age
sort_Dead_Survived(age)

majority1 = calc_Majority(sur1)
print "Age\t %d" % len(age)
print "\tPassangers that were 25 or older \t %d" % len(sur1)
print_info(sur1)

majority0 = calc_Majority(sur0)
print "\tPassangers were younger than 25\t %d" % len(sur0)
print_info(sur0)

accuracy = calc_accuracy(majority0, majority1, age)
err = calc_error(accuracy)
print "Accuracy: %r" % accuracy 
print "Error: %r" % err 

