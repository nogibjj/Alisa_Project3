import csv
import sqlite3
import requests


connects = sqlite3.connect('Analysis.db')
cursor = connects.cursor()

df=requests.get("https://www.kaggle.com/datasets/aaronschlegel/austin-animal-center-shelter-outcomes-and/download?datasetVersionNumber=1.csv")
print(type(df))