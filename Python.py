import csv
#exception handling in python
try:
    a = 10
    b = 20
    c = 0

    d = (a + b) / c
    print(d)
except:
    print("In the except block")
else:
    print("Because there was no exception, else is executed")
finally:
    print("Finally, always executed")
    
    
    
    #iterating-through-directories-with-python
https://stackoverflow.com/questions/19587118/iterating-through-directories-with-python
   #creating-file-and-folder-loop
https://stackoverflow.com/questions/23678576/creating-file-and-folder-loop
   #how-to-save-an-image-locally-using-python-whose-url-address-i-already-know
    https://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know
    #download-file-with-urlretrieve-to-subfolder
   https://stackoverflow.com/questions/46413651/download-file-with-urlretrieve-to-subfolder
    



#handling files

"""
File I/O
'w' -> Write-Only Mode
'r' -> Read-only Mode
'r+' -> Read And Write Mode
'a' -> Append Mode
"""

my_list = [1, 2, 3]

my_file = open("firstfile.txt", "w")

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()

#handling file with as with 
with open("withas.txt", "w") as with_as_write:
    with_as_write.write("This is an example of with as write/read")


#creating csv
def append_data(file_path, name,):
    fieldnames = ['paragraph']

    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({
            "paragraph": name,

        })
        
   #muliple fields csv
def book_info(file_path, name, edition,subheading,isbn,isbn13,authors):
    fieldnames = ['Name', 'Edition', 'Subheading', 'Isbn', 'Isbn13', 'Authors']

    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({
            "Name": name,
            "Edition": edition,
            "Subheading": subheading,
            "Isbn":isbn,
            "Isbn13":isbn13,
            "Authors":authors
})


#calling function
append_data("data.csv", a,)
book_info("/media/work_aholic/289AAAF29AAABC26/chegg/Soultion_html/"+str(z)+"/Book_info.csv", "Precalculus",
                      "7th edition", "Mathematics for Calculus", "1305071751", "9781305071759", "James Stewart Lothar Redlin Saleem Watson")




#reading from csv
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row
        url = row[0]
        driver.get(url)
        sleep(5)
        


