My first project in Python

Objective: 
To build a bluff detector using regression models that helps HR team of a company in hiring process - salary negotiation. It helps the HR partner to predict the salary of the potentially new employee based on his designation in previous company and how often he shifts companies. This would let the HR team know if the candidate is being honest about the salary quoted and the negotiations.

Methods used: 
Polynomial Regression, Linear Regression

Project Description: 
Data: We have the list of levels in the previous organization and the salaries for the respective levels. I did not split the data into train and test sets as the data was pretty small. 

The goal is to learn the correlation between levels and the salaries to predict if the employee is bluffing about its salary. I made use of polynomial regression with degrees of freedom = 4.
