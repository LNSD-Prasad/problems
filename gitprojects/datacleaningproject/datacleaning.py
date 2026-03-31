import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
df=pd.read_csv('messy_linear_regression_data.csv')

df['Age']=df['Age'].fillna(df['Age'].median())

df['Salary']=pd.to_numeric(df['Salary'].str.replace('USD','').str.strip(),errors='coerce')

df['Salary']=df['Salary'].fillna(df['Salary'].median())

df['Dept']=df['Dept'].astype('category')
df['Dept']=df['Dept'].cat.codes
df['Years_Experience']=df['Years_Experience'].fillna(df['Years_Experience'].median())
df['Height_cm']=pd.to_numeric(df['Height_cm'].str.replace('m','').str.strip(),errors='coerce')
df['Target_Sales']=df['Target_Sales'].fillna(df['Target_Sales'].median())
print(df.shape)
print(df)
x=df[['Age','Dept','Years_Experience','Target_Sales']]
y=df['Salary']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_train)
cousto_pred=model.predict([[55,3,11,250]])
print('predicted salary of employee:',cousto_pred,'USD')
score=r2_score(y_train,y_pred)
print('r square score:',score)
plt.scatter(y_train,y_pred)
plt.xlabel('trained data')
plt.ylabel('predicted data')
plt.show()
