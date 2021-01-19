from sklearn import linear_model
from pandas import DataFrame
import pandas as pd
import pandas
import matplotlib.pyplot as plt

input_data = pandas.read_table("height.csv", sep=",", header=0, names=("weight", "height"))

plt.scatter(input_data["weight"], input_data["height"])
plt.show()

