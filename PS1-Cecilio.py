#--------------------------------
#Name:          Eduardo  Cecilio
#Username:      n/a
#Problem Set:   PS1
#Due Date:      January 29, 2019
#---------------------------------

text = open('titanicdata.csv')

line = text.readline()

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

firstClass1 = []
firstClass0 = []
sur1 = []
sur0 = []
i = 0

for x in firstClass:
    if x is "1":
        firstClass1.append(x)
        sur1.append(survived[i])
    else:
        firstClass0.append(x)
        sur0.append(survived[i])
    i = i + 1


countSur = 0
countDead = 0

for x in sur1:
    if x is "1":
        countSur = countSur + 1
    else:
        countDead = countDead + 1

if countSur > countDead:
    argMax = countSur
else: 
    argMax = countDead

majority1 = argMax

print "First Class\t %d" % len(firstClass)
print "\tPassangers that were First Class \t %d" % len(sur1)
print "\t\tNumber that Survived:\t %d" % countSur
print "\t\tNumber that Died:\t %d" % countDead
print "\t\tmajority1: %d" % argMax 


countSur = 0
countDead = 0

for x in sur0:
    if x is "1":
        countSur = countSur + 1
    else:
        countDead = countDead + 1

if countSur > countDead:
    argMax = countSur
else: 
    argMax = countDead

majority0 = argMax
accuracy = (majority0 + majority1)/ float(len(firstClass))
err = 1 - accuracy


print "\tPassangers were NOT First Class\t %d" % len(sur0)
print "\t\tNumber that Survived:\t %d" % countSur
print "\t\tNumber that Died:\t%d" % countDead
print "\t\tmajority0: %d" % argMax

print "Accuracy: %r" % accuracy 
print "Error: %r" % err 