import json

with open('labels.json') as file:
    sentiment_dict = json.load(file)

print(sentiment_dict)


# def SentimentAnalysisProcess(self,tweet,positivelist,negativelist):
#     ps = PorterStemmer()
#     # PorterStemmer using for look up words have 1 root word
#     # For example : Root Word : Like include Likes Liking Liked Likely

#     tweet = word_tokenize(tweet)
#     tweet_list = []
#     score = 0

#     for word in tweet:
#         word = ps.stem(word)
#         if word in positivelist:
#             score += score

#         elif word in negativelist:
#             score -= score

#         else:
#             pass
#     return score

# def checkRank(self,score,rank):
#     query = "SELECT ranked FROM Comments"
#     rank = Provider.ExecuteQuery(query)
#     if (score > 0):
#         rank = "Good"
#     elif (score == 0):
#         rank = "Neutral"
#     else:
#         rank = "Bad"
#     return rank

