import re

blacklist_obj = open(r"blacklisted-words.txt", "r")
tweet_Object = open(r"tweets.txt", "r")
newFile_Object = open(r"newtweets.text", "w")
sentenceList = tweet_Object.readlines()
profaneWords = []
for words in blacklist_obj.readlines():
    if "\n" in words:
        words = words[0 : len(words) - 1]
    profaneWords.append(words)

for lines in sentenceList:
    profanityCounter = 0
    cleanedWords = ""
    splitLine = lines.split()
    for words in splitLine:
        for letters in words:
            if letters.isalnum():
                cleanedWords += letters.lower()
            else:
                continue
            for word in profaneWords:
                searchResult = re.match("^{0}$".format(word.lower()), cleanedWords)
                if searchResult != None:
                    print(cleanedWords)
                    profanityCounter += 1
        cleanedWords = ""
    newFile_Object.write("{0} Profanity Counter:{1} \n".format(lines, profanityCounter))

tweet_Object.close()
newFile_Object.close()
