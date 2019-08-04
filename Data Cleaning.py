
#cleaning double values in csv
import csv
with open('finalcleaning.csv','r') as in_file, open('after cleaning.csv','w') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    for line in in_file:
        if line in seen: continue # skip duplicate

        seen.add(line)
        out_file.write(line)



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


##converting txt files into csv
#read all txt file lines at once
#write in csv
#remove empty spaces.



# This Python file uses the following encoding: utf-8
import csv
import re
def data(file_path, name):
    fieldnames = ['Grade']

    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({
            "Grade": name,

})

z = 0
z1 = 1
list1 = []
for i in range (0,115):
    z += z1 
    fname = "/home/pythonist/Projects/Cleaning Data/邮件/{}.txt".format(z)
    file1 = open(fname,"r")
    z2 = file1.readlines()
    for j in z2:
        list2 = re.split('; |,',j)
        for l in list2:
            list1.append(l)
    print (len(list1))
    file1.close()
print(type(list1[5]))
with open('/home/pythonist/Projects/Cleaning Data/邮件/csvfile.csv','wb') as file:
    for line in list1:
        file.write(line)
        file.write('\n')



with open("/home/pythonist/Projects/Cleaning Data/邮件/csvfile.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print (row)
        
        try:
            city1 = row[0]
            if city1 == "":
                pass
            else:
                city2 = city1.strip()
                data("/home/pythonist/Projects/Cleaning Data/邮件/inputfinal.csv",city2)
        except:
            pass
            

##Removing Duplicates from scv 


# This Python file uses the following encoding: utf-8
with open('/home/pythonist/Projects/Cleaning Data/邮件/inputfinal.csv','r') as in_file, open('/home/pythonist/Projects/Cleaning Data/邮件/outputfinal.csv','w') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    for line in in_file:
        if line in seen: continue # skip duplicate

        seen.add(line)
        out_file.write(line)
        
        
        
        
        
 ##Removing empty rows in csv
        
        
        # This Python file uses the following encoding: utf-8
import csv
def data(file_path, name):
    fieldnames = ['Grade']

    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({
            "Grade": name,

})

with open("/home/pythonist/Projects/Cleaning Data/邮件/outputfinal2.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print (row)
        try:
            city1 = row[0]
            if city1 == "":
                pass
            else:
                city2 = city1
                data("/home/pythonist/Projects/Cleaning Data/邮件/outputfinal3.csv",city2)
        except:
            pass

        
       #spliting rows by dalimater
    
    # This Python file uses the following encoding: utf-8
import csv


def data(file_path, name):
    fieldnames = ['Grade']

    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({
            "Grade": name,

})



list1 = []
with open("/home/pythonist/Projects/Cleaning Data/邮件/outputfinal.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print (row)
        list2 = row[0].split(';')
        for l in list2:
            list1.append(l)



for j in list1:
    data("/home/pythonist/Projects/Cleaning Data/邮件/outputfinal2.csv",j)


