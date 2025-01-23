import pandas as pd
import os
import kagglehub
path = kagglehub.dataset_download("idowuadamo/students-performance-in-2024-jamb")
print("Path to dataset files:", path)
df = pd.read_csv(os.path.join(path,'jamb_exam_results.csv')) 
os.listdir(path)
# read data from path using pandas
df = pd.read_csv(os.path.join(path, 'jamb_exam_results.csv'))
 # group the parental education by jamb score average
data_pel = df.groupby('Parent_Education_Level')['JAMB_Score'].mean()

grouped_data = df.groupby('Study_Hours_Per_Week')['JAMB_Score'].mean().reset_index()
