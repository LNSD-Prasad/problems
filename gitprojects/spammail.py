import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
df=pd.read_csv(r'E:\problems\gitprojects\spham.csv',sep='|',encoding='latin-1')
print(df.columns)
df.columns=df.columns.str.strip()
df=df[['Label','Message']]
df['Label']=df['Label'].str.strip()
df['Label']=df['Label'].map({'ham':0,'spam':1})
df['Label']=df['Label'].fillna(0)
df['Label']=df['Label'].astype(int)
print(df)
vectorizer=CountVectorizer()
x=vectorizer.fit_transform(df['Message'])
y=df['Label']
model=MultinomialNB()
model.fit(x,y)
def predict_spam(message):
    message_vec=vectorizer.transform([message])
    result=model.predict(message_vec[0])
    return 'spam' if result==1 else 'ham' 
msg=input('Enter a message:')
print(predict_spam(msg))


