from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import csv
import nltk
nltk.download('stopwords')
nltk.download('wordnet')


##EXTRACT ALL WORDS
all_words = []
list_of_docs = "all_docs.txt"
tokenizer = RegexpTokenizer(r'\w+')


with open(list_of_docs, 'r') as f:
	docs = f.readlines()

for doc in docs:
	doc_entry = doc.strip()
	f = open(doc_entry,'r')
	doc_text = f.read()
	raw = doc_text.lower()
	tokens = tokenizer.tokenize(raw)
	for token in tokens:
		all_words.append(token)

stopwords = set(stopwords.words('english'))
punctuation = set(string.punctuation)



##REMOVE STOPWORDS/PUNCTUATION
dictionary_all = []
for i in all_words:
	if i not in punctuation and i not in stopwords:
		dictionary_all.append(i)


##LEMMATIZE TO REDUCE RELATED FORMS OF A WORD TO A COMMON BASE AND DEDUPE
lemmatize = WordNetLemmatizer()
dictionary_clean = []
for i in dictionary_all:
	lemmatized_word = lemmatize.lemmatize(i.decode('utf8','ignore'))
	if lemmatized_word not in dictionary_clean:
		dictionary_clean.append(lemmatized_word.encode('utf8'))


##READ TO CSV
csvfile = "dictionary_clean.csv"
with open(csvfile, 'w') as output:
	writer = csv.writer(output, lineterminator='\n')
	for val in dictionary_clean:
		writer.writerow([val])





