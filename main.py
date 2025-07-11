import numpy as np;
import matplotlib.pyplot as plt;
import pandas as pd;
from sklearn.model_selection import train_test_split;
from sklearn.linear_model import LogisticRegression;
from sklearn.preprocessing import LabelEncoder;

# Load the dataset
# dataset = {
# 	'students': ['Ahmed', 'Sayed', 'Ali', 'Mohamed', 'Hassan', 'Omar', 'Yasser', 'Khaled', 'Tamer', 'Sara'],
# 	'grades_math': [85, 90, 78, 88, 92, 95, 80, 75, 89, 82],
# 	'grades_science': [80, 85, 88, 90, 92, 95, 78, 82, 84, 87],
# 	'grades_english': [78, 82, 85, 88, 90, 92, 80, 75, 89, 84],
# 	'behavior': ['good', 'good', 'bad', 'good', 'bad', 'good', 'bad', 'bad', 'good', 'bad'],
# 	'passed': [1, 1, 0, 1, 1, 1, 0, 0, 1, 1],
# 	'issues': [0, 0, 1, 0, 0, 0, 1, 1, 0, 0]
# 	}

# print("Dataset loaded successfully.", dataset)

# # Convert the dataset into a DataFrame
# df = pd.DataFrame(dataset)
# df.to_csv("student_data.csv", index=False)
# print("DataFrame created successfully.")
df = pd.read_csv("student_data.csv")
print(df)
