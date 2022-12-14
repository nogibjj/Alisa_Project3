# Alisa_Project3: Analysis of animal shelter database

The data for this project is from Austin Animal Center, which only includes the record of cats. As one of ther largest no-kill animal shelter in US, the Austin Animal Center offers care and shelter to over 18000 animals every year.  I analyzed the dataset of the Austin Animal Center Shelter and hope to help these organization make better use of the limited resources. I generated a script that query the database from Kaggle with Sqlite. 


<img width="652" alt="Screen Shot 2022-11-08 at 11 01 22 PM" src="https://user-images.githubusercontent.com/89174034/200735416-2ba43a04-f30e-44b3-bd24-26a0eb09a28c.png">


Link to the dataset: https://www.kaggle.com/datasets/aaronschlegel/austin-animal-center-shelter-outcomes-and.

# Question to answer: 

### Question1: Which type of breed has the highest waiting days in the shelter?
'domestic longhair/domestic longhair' breed has average waiting days of 5475. 'domestic mediumhair/maine coon' breed has second average waiting days of 4745, followed by 'scottish fold' breed (4015 days) and 'domestic mediumhair/manx' breed 2920 (days). 


### Question2: Which type of breed has the lowest waiting days in the shelter?
The 'birman' breed has the shortest waiting days of 30 in the shelter when compared to other breeds. The 'american wirehair','domestic shorthair/domestic mediumhair' as well as 'domestic shorthair/maine coon' breed have the same waiting period of 60. 

### Question3: What is the most common age of cats in Austin Animal Center?
It is a heart-broken fact that cats are abandoned at such a young age: 2 months.

### Question4: On what day of the week is the cat most likely to be adopted?
Cats are most likely to be adopted on Saturday. 


### Question5: On what day of the week is the cat least likely to be adopted?
Thursday! People get busy during the week and have little time visit the Austin Animal Center. 

# Created and connect the database, insert data to the table in SQL
1.  Use kaggle API to turn this dataset to csv file

 ````markdown
mkdir /home/codespace/.kaggle
````
````markdown
cp kaggle.json /home/codespace/.kaggle
````
 ````markdown
chmod 600 ~/.kaggle/kaggle.json
````
 ````markdown
cd /home/codespace/.kaggle
````

2. Download the dataset from Kaggle by copying the API command. 


3. Create and connect the database with Sqlite3 in codespace (analysis.py)


4. Analysis the animal shelter dataset (analysis.py)



