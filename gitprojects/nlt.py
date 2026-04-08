import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
nltk.download("punkt")
nltk.download("punkt_tab")
text = "Dr. Strange lives in the U.S.A. He works at 5 p.m. everyday."
sentences = sent_tokenize(text)
sentences2=word_tokenize(text)
for sentence in sentences:
    print(sentence)
for word in sentences2:
    print(word)