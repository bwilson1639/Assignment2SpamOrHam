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
    spamFileCount = 0
    hamDic = {}
    hamCount = 0
    hamFileCount = 0
    fileDir = 'train_Lemmatized'
    fileNameList = os.listdir(fileDir)
    isSpam = False


#   for each fileName in test_Lemmantized
    for file in fileNameList:

#       if name starts with spm
        if 'spm' in file:
            isSpam = True
            spamFileCount += 1
        else:
            hamFileCount += 1

        fileName = fileDir + '\\' + file

#       open file
        inFile = open(fileName,'r')

#       read file
        readFile = inFile.read()
        inFile.close()
        readFile = readFile.strip()
        readFile = readFile.replace('\n', ' ')
        readFile = readFile.strip()
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


    spamPValueFile = open('probability_spam_words.txt', 'w')
    spamPValueFile.write(format(spamCount))
    spamPValueFile.write("\n")
    spamValue = spamFileCount / (spamFileCount + hamFileCount)
    spamPValueFile.write(format(spamValue))
    spamPValueFile.write("\n")

#   for file format, convert into Json for best results
#   for each instance of spam
    for spamWord in spamDic.items():
        wordCount = spamWord[1]
#       calculate P
        pValue = wordCount / spamCount
#       save to file
        tempString = format(spamWord[0]) + " " + format(pValue)
        spamPValueFile.write(tempString + "\n")
    spamPValueFile.close()

    hamPValueFile = open('probability_ham_words.txt', 'w')
    hamPValueFile.write(format(hamCount))
    hamPValueFile.write("\n")
    hamValue = hamFileCount / (hamFileCount + spamFileCount)
    hamPValueFile.write(format(hamValue))
    hamPValueFile.write("\n")

#   for each instance of ham
    print(hamDic.items())
    errorBuffer = 6
    for hamWord in hamDic.items():
        if errorBuffer > 0:
            errorBuffer -= 1
            continue
        wordCount = hamWord[1]
#       calculate P
        pValue = wordCount / hamCount
#       save to file
        tempString = format(hamWord[0]) + " " + format(pValue)
        hamPValueFile.write(tempString + "\n")
    hamPValueFile.close()
#   for each word in dictionary
#       save to .txt file

#note: main should not run training data function, that should have ran earlier and just use the .txt files created

#run test
train()