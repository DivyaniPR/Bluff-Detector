# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 11:53:02 2018

@author: dparsara
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values

#Fitting linear regression to the dataset
from sklearn.linear_model import LinearRegression
linear_regressor1 = LinearRegression()
linear_regressor1.fit(X, Y)

#Fitting polynomial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
polynomial_regressor = PolynomialFeatures(degree = 4)
X_poly = polynomial_regressor.fit_transform(X)
linear_regressor2 = LinearRegression()
linear_regressor2.fit(X_poly, Y)

#Visualizing linear regression results
plt.scatter(X, Y, color = 'red')
plt.plot(X, linear_regressor1.predict(X), color = 'blue')
plt.show()

#Visualizing polynomial regression results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, Y, color = 'red')
plt.plot(X_grid, linear_regressor2.predict(polynomial_regressor.fit_transform(X_grid)), color = 'blue')
plt.show()  

#Predict new result with linear regression
linear_regressor1.predict(6.5)

#Predict new result with polynomianlregression
linear_regressor2.predict(polynomial_regressor.fit_transform(6.5))