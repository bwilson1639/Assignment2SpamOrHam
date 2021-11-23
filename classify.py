#classify
import sys
import math

def classify(importFileString, exportFileString):

    wordDic = {}
#get data from text file
    hamProbabilityFile = open('probability_ham_words.txt')
    hamProbabilityFile.readline()
    hamTotalWords = hamProbabilityFile.readline()
    hamTrainingP = hamProbabilityFile.readline()
    hamProbabilityString = hamProbabilityFile.read()
    hamProbabilityFile.close()

    spamProbabilityFile = open('probability_spam_words.txt')
    spamProbabilityFile.readline()
    spamTotalWords = spamProbabilityFile.readline()
    spamTrainingP = spamProbabilityFile.readline()
    spamProbabilityString = spamProbabilityFile.read()
    spamProbabilityFile.close()

#save data into testing dictionary
    hamProbabilityDic = {}
    spamProbabilityDic = {}

    hamProbabilityString = hamProbabilityString.split("\n")
    print(hamProbabilityString)
    for word in hamProbabilityString:
        tempWord = word.split()
        print(tempWord)
        if len(tempWord) <= 1:
            continue
        hamProbabilityDic[tempWord[0]] = tempWord[1]

    spamProbabilityString = spamProbabilityString.split("\n")
    for word in spamProbabilityString:
        tempWord = word.split()

        if len(tempWord) <= 1:
            continue
        spamProbabilityDic[tempWord[0]] = tempWord[1]



#open inputted test file
    testFile = open(importFileString, 'r')
    readFile = testFile.read()
    testFile.close()
    readFile = readFile.strip()
    readFile = readFile.replace('\n', ' ')
    readFile = readFile.strip()
    readFileList = readFile.split(' ')

#   store each word in dictionary
    for word in readFileList:
        if not (word in wordDic):
            wordDic[word] = 1

        else:
            wordDic[word] += 1
    spamPTotal = 0
    hamPTotal = 0

    for index in wordDic.items():

#   check to see if word is in spam testing dictionary
        if index[0] in spamProbabilityDic:
            spamPTotal += math.log10(index[1])
        else:
            spamPTotal += math.log10(1/ int(spamTotalWords))
#       if it is then add it's probability to the total spam probablility

#   check to see if word is in ham testing dictionary
        if index[0] in hamProbabilityDic:
            hamPTotal += math.log10(index[1])
        else:
            hamPTotal += math.log10(1/ int(hamTotalWords))
#       if it is then add it's probability to hte total ham probabability

#   if the total spam probability is greater than total ham probability
    if spamPTotal > hamPTotal:
#       the file is spam
        print("is Spam")

importFile = sys.argv[1]
exportFile = sys.argv[2]

classify(importFile, exportFile)

