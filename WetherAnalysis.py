import pandas as pd

data=pd.read_csv(r"C:\Users\91935\Downloads\Data Science training\Udemy - DS Pro\Real World Hands on projects\Project+1+-+Weather+Dataset.csv")
print(data)
print(data.head())  #this functon will shows the N number of data(by default N=5)
print(data.shape) #this will show the number of rows and columns
print(data.index)   #this will show the index like start,stop and step
print(data.columns) #this will show the name of all the columns in data
print(data.dtypes) #this will show the data type of each column in data
print(data['Weather'].unique()) #this functon will show the unique values/names of a specific column from data
print(data.nunique()) #this functon will show the total number of unique values in each column
print(data.count()) #this functon will show the total number of non-null values in each column
print(data['Weather'].value_counts()) #this functon will show the vales with there count of specific column
print(data.info()) #this functon will show the all details of our data

'''1)Find the unique 'Wind Speed' values in data'''
print(data['Wind Speed_km/h'].unique())     #unique 'Wind Speed 'values
print(data['Wind Speed_km/h'].nunique())    #total number of unique values in Wind Speed's column

'''2)Find the number of times when 'Weather is exactly clear'''
# #Using Value Count
print(data['Weather'].value_counts()) #this will show the total number of count of each value
# #Using Filtering
print(data[data.Weather=='Clear']) #This will show only details of the clear weather
# #Using groupby
print(data.groupby('Weather').get_group('Clear'))

'''3)Find the number of times when the Wind Speed was exactly 4km/h'''
print(data.groupby('Wind Speed_km/h').get_group(4))
# #or
print(data[data['Wind Speed_km/h']==4])

'''4)Find out all the NULL values in dataset'''
print(data.isnull().sum())

'''5)Find out all the NOT-NULL values in dataset'''
print(data.notnull().sum())

'''6)Rename the column name 'Weather' of Dataframe to 'Weather-Condition'''
print(data.rename(columns={'Weather':'Weather-Condition'}))

'''7)What us the mean 'Visibility'''
print(data.Visibility_km.mean())

'''8)What is Standard deviation of Pressure in data'''
print(data.Press_kPa.std())
#or
print(data['Press_kPa'].std())


''' 9)What is the Variance of Relative Humidity in data'''
print(data['Rel Hum_%'].var())  #Note if there is any space between the column name then we will use square brace[] instead of dot .

''' 10)Find all instance when snow was recorded'''
# #Using value_count
print(data['Weather'].value_counts())
# #Using Filtering
print(data[data['Weather']=='Snow'])
#Using str.contains
print(data[data['Weather'].str.contains('Snow')])  #this will show even there is partial match like 'Snow Shower'

''' 11)Find the instance when Wind speed is above 24 and visibility is 25'''
print(data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)])

''' 12)What is the mean value of each column aganist each Weather'''
print("Mean")
print(data.groupby('Weather').mean())

''' 13)What is the min and max value of each column aganist each Weather'''
print("Minimum")
print(data.groupby('Weather').min())
print("Maximum")
print(data.groupby('Weather').max())

'''14)Show all the condition where weather is FOG'''
print(data[data['Weather']=='Fog'])

''' 15)Find the instance when weather is clear or visibility is above 40'''
print(data[(data['Weather']=='Clear') | (data['Visibility_km']>40)])

''' 16)Find all the instance when '''
#A) weather is clear and Relative Humidity is greater than 50
#or
#B)Visibility is above 40
print(data[((data['Weather']=='Clear') & (data['Rel Hum_%']>50)) | (data['Visibility_km']>40)])