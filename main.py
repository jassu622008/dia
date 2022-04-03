import pandas as pd

from sklearn.tree import DecisionTreeClassifier

import streamlit as st

def main():
	df = pd.read_csv("diabetes.csv")

      X = df[["Glucose", "Insulin", "Age"]]

      Y = df[["Outcome"]]

      model = DecisionTreeClassifier()

      model.fit(X, Y)

      glucose = st.text_input("Enter Glucose Level: ")

      Insulin = st.text_input("Enter Insulin Level: ")

      Age = st.text_input("Enter Your Age: ")

      pre = model.predict([[int(glucose), int(Insulin), int(Age)]])

      if pre == 1:
      	st.write("You have diabetes")

	else:
      	st.write("You Does'n have diabetes")


st.write(main())