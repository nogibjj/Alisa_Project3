import csv
import sqlite3
from sqlite3 import Error
import pandas as pd


connects = sqlite3.connect('Analysis.db')
cursor = connects.cursor()


# upload dataset
df=pd.read_csv("aac_shelter_outcomes.csv")


#create the table
table = 'CREATE TABLE ANALYSIS ()'