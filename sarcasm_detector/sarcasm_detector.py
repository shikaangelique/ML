import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_json("Sarcasm Detector/sarcasm.json")
data["is_sarcastic"] = data["is_sarcastic"].map({0: "Not Sarcasm", 1: "Sarcasm"})
# print(data.head())

data = data[["headline", "is_sarcastic"]]
x_data = np.array(data["headline"])
y_data = np.array(data["is_sarcastic"])

vectoriser = CountVectorizer()
base_data = vectoriser.fit_transform(x_data)
bd_train, bd_test, y_train, y_test = train_test_split(base_data, y_data, test_size=0.20, random_state=50)

bernoulli = BernoulliNB()
bernoulli.fit(bd_train, y_train)
bernoulli_pred = bernoulli.predict(bd_test)
print('Accuracy of BernoulliBN model on test set: {:.2f}'.format(bernoulli.score(bd_test, y_test)))
bernoulli_conf_matrix = metrics.confusion_matrix(y_test, bernoulli_pred)
print('BernoulliBN model confusion matrix is:', bernoulli_conf_matrix)

X_two_train, X_two_test, y_two_train, y_two_test = train_test_split(base_data, y_data, test_size=0.20, random_state=0)
log_reg = LogisticRegression(solver="lbfgs", max_iter=10000)
log_reg.fit(X_two_train, y_two_train)

log_reg_prediction = log_reg.predict(X_two_test)
print('Accuracy of logistic regression model on test set: {:.2f}'.format(log_reg.score(X_two_test, y_two_test)))

log_reg_conf_matrix = metrics.confusion_matrix(y_two_test, log_reg_prediction)
print('Logistic regression model confusion matrix is:', log_reg_conf_matrix)
# Diagonal values represent accurate predictions, while non-diagonal elements are inaccurate predictions.

# using inputs to predict the output
user_input = input("Enter a Text: ")
user_data = vectoriser.transform([user_input]).toarray()
gen_output = bernoulli.predict(user_data)
gen_output_two = log_reg.predict(user_data)
print('BernoulliBN prediction:', gen_output)
print('Logistic regression prediction:', gen_output_two)
