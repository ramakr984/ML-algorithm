import fastapi
from fastapi import FastAPI
import joblib

app = FastAPI()

@app.post("/predict")
def predict(Store,Date_Ordinal,Holiday_Flag,Temperature,Fuel_Price,CPI,Unemployment):
    df1 = pd.DataFrame({'Store':[11], 'Date':['05-02-2050'],  'Holiday_Flag':[1], 'Temperature':[34],'Fuel_Price':[67], 'CPI':[89], 'Unemployment':[90], 'Date_Ordinal':[90]})
    model =joblib.load(r"C:\Users\HP\Desktop\python projects\healthcareproject\walmart.joblib")
    response = model.predict(df1)
    return response