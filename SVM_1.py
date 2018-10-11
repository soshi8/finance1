# coding: utf-8
from sklearn import svm
import pandas as pd
stock_data = pd.read_csv('stockchart_yyyymmdd.csv')
count_s =  len(stock_data)
owarine = stock_data['終値'].values.tolist()


successive_data = []
answers = []
for i in range(4, count_s):
    successive_data.append([owarine[i-4], owarine[i-3], owarine[i-2], owarine[i-1]])
    x1 = (owarine[i] - owarine[i-1]) / 100
    x2 =round(x1)
    answers.append(x2)

clf = svm.LinearSVC()
n = len(successive_data)
m = len(answers)


clf.fit(successive_data, answers)
predicted = clf.predict(successive_data)
