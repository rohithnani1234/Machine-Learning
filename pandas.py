#Pandas is generally used for Data Analyst
#It allows importing data from various file formats ex:JSON,csv,Excel.Sql,ect.
#Features: Data Manipulation,Reading and Writing Data,Reshaping of Data,Data Filteration,Data cleaning
import pandas as pd

dict_1={"car":["city","ignis","800","verna","Venue","punto"],"brand":["Honda","Maruti","maruti","Hyundai","Hyundai","Fiat"],
        "cost":[900000,600000,1000000,800000,950000,750000],"year":[5,7,10,4,2,6]}

auto=pd.DataFrame(dict_1)

auto

#now using a real time dataset that is Titanic dataset
import pandas as pd
#and then i have downloaded titanic.csv file from the browser and dragged it into this platform

data=pd.read_csv("titanic.csv")

data.head(10) #head - means it will print first 10 values of the data from the dataset
#if we didn't mention any value then by default it will take first five values
#is very useful for the visualing the dataset

data.info() #if we want to datatype of the each column and how many null values in each column
#whatever textual data and catogerical we have that will as object data

data.shape #shape method allows you return number of rows and number of columns
#it is an attribute

data.columns #is used to see the name of all the columns and it is an attribute

data['Embarked'].value_counts() #value_counts is used to count the each distinct value  in a coulmn in a dataset

data['Sex'].unique()# is used to find unique values in a dataframe and it wont return as the count
#it will just return as the what distinct values are there

#Accessing Columns
data['Name'] # it will return only the name column

data[['Name','Sex','Pclass']] #it will return both name and sex column and we will provide a nested list

#ACCESSING ROWS
data.iloc[0,:].values #iloc or loc parametrs are index of row and index of column

data.iloc[0:5,4].values

data.loc[1:5,['Name','Sex']] # it returns only the first 1 to 5 data and columns are which are name and sex

#iloc is only used for indexes not strings ex:data.iloc[1:5,['name']]--it will give you an Index error
#loc is used for the strings ex:data.loc[1:7,['name']] it will prints 1 to 6 name of column :name

#FILTERING OF DATA
new_data=data['Sex']=="male"
new_data #it will filter the data from column sex and which are in male category
#if it male it returns true and if not it returns false
#it willcompare every row in tha dataset and returns true which is matched

#SORTING OF DATA
auto.sort_values("cost") #here it sorts the data with respect to the cost

#GROUPING AND AGGREGATION
groups=data.groupby(['Sex']) #is used to grouping the data
groups #it returns <pandas.core.groupby.generic.DataFrameGroupBy object at 0x79e23092d450>

groups.mean()
#it returns the mean of all columns with respect to Sex column

groups.size() #here we can see the how many number of data it consists of each catogery

groups.count() #it counts occurence of each and every data in all columns according to the Sex column