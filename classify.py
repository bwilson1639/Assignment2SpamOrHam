#classify
import sys
import math

def classify(importFileString, exportFileString):

    wordDic = {}
#get data from text file
    hamProbabilityFile = open('probability_ham_words.txt')
    hamProbabilityFile.readline()

    hamTotalWords = hamProbabilityFile.readline()
    hamTotalWords = hamTotalWords.strip()
    hamTotalWords = float(hamTotalWords)

    hamTrainingP = hamProbabilityFile.readline()
    hamTrainingP = hamTrainingP.strip()
    hamTrainingP = float(hamTrainingP)
    hamProbabilityString = hamProbabilityFile.read()
    hamProbabilityFile.close()

    spamProbabilityFile = open('probability_spam_words.txt')
    spamProbabilityFile.readline()

    spamTotalWords = spamProbabilityFile.readline()
    spamTotalWords = spamTotalWords.strip()
    spamTotalWords = float(spamTotalWords)

    spamTrainingP = spamProbabilityFile.readline()
    spamTrainingP = spamTrainingP.strip()
    spamTrainingP = float(spamTrainingP)

    spamProbabilityString = spamProbabilityFile.read()
    spamProbabilityFile.close()

#save data into testing dictionary
    hamProbabilityDic = {}
    spamProbabilityDic = {}

    hamProbabilityString = hamProbabilityString.split("\n")

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
    spamPTotal = spamTrainingP
    hamPTotal = hamTrainingP

    outputFile = open(exportFileString, 'w')

# ==================================================================================
    outputFile.write("(1) P(Spam, all words)\n")
    tempString = "    P(Spam)=" + format(spamTrainingP) +"\n"
    outputFile.write(tempString)

    for index in wordDic.items():

        tempString = "    P('" + format(index[0]) + "'|Spam)="
        outputFile.write(tempString)
#   check to see if word is in spam testing dictionary
        if index[0] in spamProbabilityDic:
            spamPTotal += math.log10(float(spamProbabilityDic[index[0]]))
            tempString = format(spamProbabilityDic[index[0]]) + "\n"
            outputFile.write(tempString)
        else:
            baseP = 1 / spamTotalWords
            spamPTotal += math.log10(baseP)
            tempString = format(baseP) + "\n"
            outputFile.write(tempString)
#       if it is then add it's probability to the total spam probablility

    tempString = "    LogP(Spam, all words) =" + format(spamPTotal) +"\n"
    outputFile.write(tempString)
#==================================================================================
    outputFile.write("(2) P(Ham, all words)\n")
    tempString = "    P(Ham)=" + format(hamTrainingP) + "\n"
    outputFile.write(tempString)

    for index in wordDic.items():

        tempString = "    P('" + format(index[0]) + "'|Ham)="
        outputFile.write(tempString)

#   check to see if word is in ham testing dictionary
        if index[0] in hamProbabilityDic:
            hamPTotal += math.log10(float(hamProbabilityDic[index[0]]))
            tempString = format(hamProbabilityDic[index[0]]) + "\n"
            outputFile.write(tempString)
        else:
            baseP = 1 / hamTotalWords
            hamPTotal += math.log10(baseP)
            tempString = format(baseP) + "\n"
            outputFile.write(tempString)
#       if it is then add it's probability to hte total ham probability
    tempString = "    LogP(Ham, all words) =" + format(hamPTotal) + "\n"
    outputFile.write(tempString)
# ==================================================================================

    outputFile.write("\n")
#   if the total spam probability is greater than total ham probability
    if spamPTotal > hamPTotal:
#       the file is spam
        outputFile.write("Conclusion: the message is Spam")
    else:

        outputFile.write("Conclusion: the message is not Spam")
    outputFile.close()
#==================================================================================
importFile = sys.argv[1]
exportFile = sys.argv[2]

classify(importFile, exportFile)

