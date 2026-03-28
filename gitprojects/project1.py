import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
df=pd.read_csv("E:\problems\gitprojects\studentstudyhours.csv")
print(df)
x=df[['Hours_Studied']]
y=df['Marks_Scored']
model=LinearRegression()
model.fit(x,y)
hours=float(input("enter hours:"))
predicted_marks=model.predict([[hours]])
y_pred=model.predict(x)
print(f"predicted marks for 6 {hours}:",predicted_marks[0])
plt.scatter(x,y)
plt.plot(x,y_pred)
plt.title("Study Hours vs Marks Scored")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.show()
print("slope (m):",model.coef_)
print("intercept(c):",model.intercept_)
