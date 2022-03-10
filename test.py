# -*- coding = utf-8 -*-
# @Time : 2022/3/8 17:34
# @Author : zzw
# @File : test.py
# @Software: PyCharm
import pandas as pd

iris_data=pd.read_csv('iris.data.csv')
iris_data.columns=['sepal_length_cm','sepal_width_cm','petal_length_cm','petal_width_cm','class']
iris_data.head()

















