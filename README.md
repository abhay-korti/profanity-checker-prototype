# Profanity Checker Prototype

A simple Python Script based Profanity checker that flags Profane words used and increases the counter for further analysis. The tool accepts tweets and wrties back the tweets with appropriate count


# Process
This Script follows a few steps -
1. Imports the files needed - A blacklist file - For all the words that are blacklisted, Tweets file - A stream of tweets made by users that has to be checked for profanity
2. Cleaning of blacklisted words - Assuming new lines are created for each word, removing the escape sequence "\n" stored as string from reading the file is necessary
3. Spliting the tweets down - Next step breaks the tweet done into words and then to characters to cleanse the words from specialcharacters
4. Then, the blacklisted words are looped through to check if they are present in to cleaned words suing Regex. It's not the other way around to avoid misflagging in words. For example, If 'example' was a flagged word, 'ample' should not be flagged.
5. The script creates a new file and writes down the original sentence along with the Profanity Score of it. 

# Index
blacklisted-words.txt - File that contains blacklisted words, new line separated.<br>
tweets.txt - File that contains the tweets that need to be checked.<br>
newTweets.text - File returned by the script that contains the original tweets and the profanity score. 
