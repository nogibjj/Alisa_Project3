import csv
import sqlite3
from sqlite3 import Error
import pandas as pandas


connects = sqlite3.connect('Analysis.db')
cursor = connects.cursor()

#create the table
table = 'CREATE TABLE ANALYSIS ()'