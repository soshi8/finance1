# coding: utf-8
from sklearn.linear_model import LinearRegression
import pandas as pd

stock_data = pd.read_csv('stockchart_20180908.csv')
count_s =  len(stock_data)
owarine = stock_data['終値'].values.tolist()
successive_data = []
answers = []

for i in range(4, count_s):
    successive_data.append([owarine[i-4], owarine[i-3], owarine[i-2], owarine[i-1]])
    answers.append(owarine[i] )

reg = LinearRegression().fit(successive_data, answers)
n = len(successive_data)
m = len(answers)
predicted = reg.predict(successive_data)
pd.Series(answers)
c = pd.Series(answers)
d = pd.Series(predicted)
e = pd.concat([c,d],axis=1)
e.to_csv('result.csv')

