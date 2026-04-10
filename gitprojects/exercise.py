import spacy
nlp = spacy.blank("en")
nlp.add_pipe("sentencizer")
text='''
Look for data to help you address the question. Governments are good sources because data from public research is often freely available. Good places to start include http://www.data.gov/, and http://www.science.gov/, and in the United Kingdom, http://data.gov.uk/.
Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, and the European Social Survey at http://www.europeansocialsurvey.org/.
'''
doc=nlp(text)
for sentence in doc.sents:
    urls=[]
    for token in sentence:
        if token.like_url:
            urls.append(token.text)
print(urls)
