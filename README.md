# Alisa_Project3: Analysis of animal shelter database

The data for this project is from Austin Animal Center, which only includes the record of cats. As one of ther largest no-kill animal shelter in US, The Austin Animal Center offers care and shelter to over 18000 animals every year.  I analyzed the dataset of the Austin Animal Center Shelter and hope to help these organization make better use of the limited resources. I generated a scriipt that query the database from Kaggle with Sqlite. 

Link to the dataset: https://www.kaggle.com/datasets/aaronschlegel/austin-animal-center-shelter-outcomes-and.

# Question to answer: 

### Question1: Which type of breed has the highest waiting days in the shelter?
'domestic longhair/domestic longhair' breed has average waiting days of 5475. 'domestic mediumhair/maine coon' breed has second average waiting days of 4745, followed by 'scottish fold' breed (4015 days) and 'domestic mediumhair/manx' breed 2920 (days). 


### Question2: Which type of breed has the highest waiting days in the shelter?
The 'birman' breed has the shortest waiting days of 30 in the shelter when compared to other breeds. The 'american wirehair','domestic shorthair/domestic mediumhair' as well as 'domestic shorthair/maine coon' breed have the same waiting period of 60. 

### Question3: What is the most common age of cats in Austin Animal Center?
It is a heart-broken fact that cats are abandoned at such a young age: 2 months.

### Question4: On what day of the week is the cat most likely to be adopted?
Cats are most likely to be adopted on Saturday. 


### Question5: On what day of the week is the cat least likely to be adopted?
Thursday! People get busy during the week and have little time visit the Austin Animal Center. 

# Created and connect the database, Inseted Data to the table in SQL
1.  Use kaggle API to turn this dataset to csv file
mkdir /home/codespace/.kaggle
cp kaggle.json /home/codespace/.kaggle
chmod 600 ~/.kaggle/kaggle.json
cd /home/codespace/.kaggle







