input = open(
    '/Users/krishjain/Desktop/AdventOfCode/Day 6/input.txt', "r").read()
input = input.split("\n\n")

countForEachGroup = []
for i in input:
    listOfAnswersToWhichAnsweredYes = []

    x = i.split("\n")

    if "" in x:
        x.remove("")

    numberOfRepeatingChars = len(set.intersection(*[set(e) for e in x])) 
    countForEachGroup.append(numberOfRepeatingChars)


sumOfCounts = sum(countForEachGroup)
print("Answer is: " + str(sumOfCounts))
