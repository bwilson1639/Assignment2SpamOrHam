import os
#calculate training data for test



    # def __init__(self):
    #     spamDic = {}
    #     hamDic = {}
    #     fileNameList = []
    #     fileDir = "C:\Users\Benjamin\PycharmProjects\Assignment2SpamOrHam\train_Lemmatized"

def train():

    spamDic = {}
    spamCount = 0
    hamDic = {}
    hamCount = 0
    fileDir = 'train_Lemmatized'
    fileNameList = os.listdir(fileDir)
    isSpam = False


#   for each fileName in test_Lemmantized
    for file in fileNameList:

#       if name starts with spm
        if 'spm' in file:
            isSpam = True

        fileName = fileDir + '\\' + file

#       open file
        inFile = open(fileName,'r')

#       read file
        readFile = inFile.read()
        inFile.close()

        readFileList = readFile.split(' ')
#           for each instance of word
        for word in readFileList:
            if isSpam is True:

                spamCount += 1

                if not (word in spamDic):
                    spamDic[word] = 1
                else:
                    spamDic[word] += 1

            else:

                hamCount += 1
                if not (word in hamDic):
                    hamDic[word] = 1

                else:
                    hamDic[word] += 1
    print(spamCount)
    print(hamCount)
    print(spamDic["summer"])

#   for each instance of spam
#       calculate P
#       save to dictionary
#   for each instance of ham
#       calculate P
#       save to dictionary
#   create 'probability_spam_words.txt'
#   crate 'probability_ham_words.txt'
#   for each word in dictionary
#       save to .txt file

#note: main should not run training data function, that should have ran earlier and just use the .txt files created

#run test
train()