import csv
import sqlite3
from sqlite3 import Error
import pandas as pd


connects = sqlite3.connect('Analysis.db')
cursor = connects.cursor()


# upload dataset
Sheltor_outcome=pd.read_csv("aac_shelter_cat_outcome_eng.csv")
#file=open('aac_shelter_cat_outcome_eng.csv')


#create the table and then execute
#table = 'CREATE TABLE Analysis19 (animal_id	integer PRIMARY KEY,age_upon_outcome text,animal_type text,breed text,color text,date_of_birth text,datetime text,monthyear text,name text,outcome_subtype text,outcome_type text,sex_upon_outcome text,count integer,sex text,Periods integer,Period_Range integer,outcome_age_days integer,outcome_age_years integer,sex_age_outcome text,age_group text,dob_year integer,dob_month integer,dob_monthyear text,outcome_month integer,outcome_year integer,outcome_weekday text,outcome_hour integer,breed1 text,breed2 text,cfa_breed text,domestic_breed text,coat_pattern text,color1 text,color2 text,coat text)'

#cursor.execute(table)

#insert query
#insert='INSERT INTO Analysis19 (animal_id,age_upon_outcome,animal_type,breed,color,date_of_birth,datetime,monthyear,name,outcome_subtype,outcome_type,sex_upon_outcome,count,sex,Periods,Period_Range,outcome_age_days,outcome_age_years,sex_age_outcome,age_group,dob_year,dob_month,dob_monthyear,outcome_month,outcome_year,outcome_weekday,outcome_hour,breed1,breed2,cfa_breed,domestic_breed,coat_pattern,color1,color2,coat)'
#query=csv.reader(file)
#cursor.executemany(insert, query)

Sheltor_outcome.to_sql(
    "Sheltor_outcome1", connects, if_exists="replace", index=False)

#overview: first a few rows
select = "SELECT * FROM Sheltor_outcome1 LIMIT 5"
for n in cursor.execute(select):
    print(n)

# Question1: Which type of breed has the highest waiting days in the shelter

select_breed = 'SELECT breed, AVG(outcome_age_days) AS avg_days from Sheltor_outcome1 GROUP BY breed ORDER BY avg_days DESC LIMIT 5'
for i in cursor.execute(select_breed):
    print(i)

#  Question2:  Which type of breed has the highest waiting days in the shelter
select_breed2 = 'SELECT breed, AVG(outcome_age_days) AS avg_days from Sheltor_outcome1 GROUP BY breed ORDER BY avg_days ASC LIMIT 5'
for i in cursor.execute(select_breed2):
    print(i)
