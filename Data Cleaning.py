#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning 

# In[ ]:


#checking for missing data
Data.isnull()
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[ ]:


#inspect the data for trend and try to drop the colunm whihc has more missing data and fill the data in the column which has few values
#for average the column

def impute_age(cols):#function is taking a variable
    Age = cols[0]#putting columns is equal to variable age column
    Pclass = cols[1]#putting respected coulmn in row is equal to varibale 
    
    if pd.isnull(Age):#checking if entry is missing

        if Pclass == 1:#putting the reerance value in the missing
            return 37

        elif Pclass == 2:
            return 29

        else:
            return 24

    else:
        return Age


# In[ ]:


#droping non_usable columns
train.drop("Cabin",axis = 1 ,inplace = True)
train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)#droping muliple columns


# In[ ]:


## Converting Categorical Features into numerical for machine learning 
sex = pd.get_dummies(train["Sex"],drop_first = True) #making dummy data of a male and female only 
#one column will be output with two catagorical values





