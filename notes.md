
## How to run
First run the setup script, which will allow you to download the required packages from NLTK
```
python3 setup.py
```
To run the grader make sure to be in the main directory and run the following, if you don't have the nltk package downloaded feel free to use the setup script I made, or just run the application and it should autodownload the dependancy.
```
python3 grade.py policies/PBS_Kids.txt    
python3 grade.py policies/rvappstudios.txt
python3 grade.py policies/gamebra.txt 
```
The final line will display the total score that the policy has created. 
I would like to include more specific rules for identifying the total sentiment of each chekclist item, but started with a grading system in which the bag of words used in the policy was added to the synonyms list and compared to each policy. 
