#calculate training data for test
#   for each fileName in test_Lemmantized
#       save name to testList
#   for each name in testList
#       if name starts with spm
#           isSpam = true
#       open file
#       read file
#           for each instance of word
#               if isSpam
#                   save word to spamDictionary
#               else
#                   save word to hamDictionary
#       close file
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