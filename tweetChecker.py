import re
import os

# Assumed environement keys are - BLACKLISTWORDS, OLDTWEETS, NEWTWEETS

testvar = [1, 2, 3, 4]
testdict = {}
testdict = {"someKey": testvar}
print(testdict)


def getFileLocations():
    BLACKLIST_WORDS = os.environ.get("BLACKLISTWORDS")
    OLD_TWEETS = os.environ.get("BLACKLISTWORDS")
    NEW_TWEETS = os.environ.get("BLACKLISTWORDS")
    profaneWords = []
    blacklist_obj = open(BLACKLIST_WORDS, "r")
    tweet_Object = open(OLD_TWEETS, "r")
    newFile_Object = open(NEW_TWEETS, "w")

    sentenceList = tweet_Object.readlines()
    for words in blacklist_obj.readlines():
        if "\n" in words:
            words = words[0 : len(words) - 1]
        profaneWords.append(words)

    object_values = {}
    object_values = {
        "blacklist_obj": blacklist_obj,
        "tweet_Object": tweet_Object,
        "sentenceList": sentenceList,
        "profaneWords": profaneWords,
        "newFile_Object": newFile_Object,
    }
    return object_values


def cleanWords(obj):
    for lines in obj.sentenceList:
        profanityCounter = 0
        cleanedWords = ""
        splitLine = lines.split()
        for words in splitLine:
            for letters in words:
                if letters.isalnum():
                    cleanedWords += letters.lower()
                else:
                    continue
                for word in obj.profaneWords:
                    searchResult = re.match("^{0}$".format(word.lower()), cleanedWords)
                    if searchResult != None:
                        print(cleanedWords)
                        profanityCounter += 1
            cleanedWords = ""
        obj.newFile_Object.write(
            "{0} Profanity Counter:{1} \n".format(lines, profanityCounter)
        )
    obj.tweet_Object.close()
    obj.newFile_Object.close()
    obj.blacklist_obj.close()


def main():
    mainObj = getFileLocations()
    cleanWords(mainObj)


if __name__ == "__main__":
    main()
