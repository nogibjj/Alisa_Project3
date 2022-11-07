import csv
import sqlite3
from sqlite3 import Error
import pandas as pd


connects = sqlite3.connect('Analysis.db')
cursor = connects.cursor()


# upload dataset
df=pd.read_csv("aac_shelter_cat_outcome_eng.csv")


#create the table and then execute
table = 'CREATE TABLE Analysis9 (animal_id	integer PRIMARY KEY,age_upon_outcome text,animal_type text,breed text,color text,date_of_birth text,datetime text,monthyear text,name text,outcome_subtype text,outcome_type text,sex_upon_outcome text,count integer,sex text,Periods integer,Period Range integer,outcome_age_days integer,outcome_age_years integer,sex_age_outcome text,age_group text,dob_year integer,dob_month integer,dob_monthyear text,outcome_month integer,outcome_year integer,outcome_weekday text,outcome_hour integer,breed1 text,breed2 text,cfa_breed text,domestic_breed text,coat_pattern text,color1 text,color2 text,coat text)'

cursor.execute(table)
