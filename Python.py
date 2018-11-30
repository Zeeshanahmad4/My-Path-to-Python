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

#calling function
append_data("data.csv", a,)
