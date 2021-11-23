#classify
import sys

def classify(importFileString, exportFileString):

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
    for word in hamProbabilityString:
        tempWord = word.split()
        hamProbabilityDic[tempWord[0]] = tempWord[1]

    spamProbabilityString = spamProbabilityString.split("\n")
    for word in spamProbabilityString:
        tempWord = word.split()
        spamProbabilityDic[tempWord[0]] = tempWord[1]



#open inputted test file
#   store each word in dictionary
#   check to see if word is in spam testing dictionary
#       if it is then add it's probability to the total spam probablility
#   check to see if word is in ham testing dictionary
#       if it is then add it's probability to hte total ham proabability
#   if the total spam probability is greater than total ham probability
#       the file is spam

#importFile = sys.argv[1]
#exportFile = sys.argv[2]

classify()

