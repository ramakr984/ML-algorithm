import pandas as pd

a=pd.read_csv("Walmart.csv")


a['Date'] = pd.to_datetime(a['Date'], format='mixed')

a['Date_Ordinal'] = a['Date'].apply(lambda x: x.toordinal())


x=a[['Store','Date_Ordinal','Holiday_Flag','Temperature','Fuel_Price','CPI','Unemployment']]

y=a[['Weekly_Sales']]

print(x)

print(y)


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x_train,y_train)

model.predict(x_test)