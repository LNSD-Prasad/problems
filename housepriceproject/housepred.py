import pandas as pd
from sklearn.linear_model import LinearRegression
df=pd.read_csv("E:\problems\housepriceproject\pricedata.csv")
print(df)
x=df[['Area','Bedrooms','Age','Distance']]
y=df['Price']
model=LinearRegression()
model.fit(x,y)
area=float(input('Enter area:'))
bedrooms=int(input('Enter number of bedrooms:'))
age=int(input('enter age of house:'))
distance=float(input('Enter distance from city:'))
user_input=[[area,bedrooms,age,distance]]
predicted_price=model.predict(user_input)
print('predicted House price:',predicted_price[0])