
#knowing current dictonary
pwd

#deling files and folders 
https://askubuntu.com/questions/217893/how-to-delete-a-non-empty-directory-in-terminal
  

#Zip and Unzip

zip -r compressed_filename.zip foldername

unzip file.zip -d destination_folder


csv viewer
cat filename.csv


















#Handling AWS with cmd

#connecting with aws
ssh -i key.pem ubuntu@ec2-18-220-130-227.us-east-2.compute.amazonaws.com


#sending files
scp -i key.pem file_name ubuntu@ec2-18-220-130-227.us-east-2.compute.amazonaws.com:zee

  #note ec2 DNS number may be change every time 
