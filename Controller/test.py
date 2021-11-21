from nltk.tokenize import word_tokenize
import nltk
# Create a reference variable for Class word_tokenize
# tk = SyllableTokenizer()
	
# # Create a string input
# gfg = "hey bro what up are"
	
# # Use tokenize method
# geek = tk.tokenize(gfg)
	
# print(geek)

# s = "Hey Brown"
# word_tokenize(s)
sentence = "At eight o'clock on Thursday morning, Arthur didn't feel very good."

nltk_words = word_tokenize(sentence)
print(nltk_words)



