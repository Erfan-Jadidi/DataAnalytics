import numpy as np
from hazm import *
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

text = r"آخرین خبر/نشست خبری نصیرزاده رییس فدراسیون پرورش اندام: برای گرفتن میزبانی مسابقات قهرمانی جهان کیش ۲۵۰ هزار یورور پول پرداخت کردیم؛ پیش بینی می‌کنیم ۵۰۰ ورزشکار در مسابقات شرکت کنند که هر نفر باید ۵۵۰ یورو پرداخت کنند."


normalizer = Normalizer()
norm_text = normalizer.normalize(text)
# print(norm_text)

sentences = sent_tokenize(norm_text)
words = word_tokenize(norm_text)

cleaned_word = [word  for word in words if word not in stopwords_list()]
# print(words)
# print(cleaned_word)

# stemmer = Stemmer()
# for word in cleaned_word:
    # print(word, stemmer.stem(word))

# lemmatizer = Lemmatizer()
# for word in cleaned_word:
#     print(word, lemmatizer.lemmatize(word))


tagger = POSTagger(model='pos_tagger.model')

# for sentence in sentences:
#     print(tagger.tag(word_tokenize(sentence)))



# count_vectorizer = CountVectorizer()
# count_vector = count_vectorizer.fit_transform(cleaned_word)
# print(count_vector)
#
# tfidf_vectorizer = TfidfVectorizer()
# tfidf_vector = tfidf_vectorizer.fit_transform(cleaned_word)
# print(tfidf_vector)
# print(tfidf_vectorizer.inverse_transform([[1]]))


text = "man ali man reza shoma"

words=np.array(text.split(" ")).reshape(-1,1)

# encoder = LabelEncoder()
# print(encoder.fit_transform(words))


one_hot_encoder = OneHotEncoder()
print(one_hot_encoder.fit_transform(words))