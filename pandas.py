

#reading and setting index on column 1
df = pd.read_csv('College_Data',index_col=0)


#Building datafram using variables
df_jobsearch = pd.DataFrame(columns=['location', 'time', 'applicants','jobfunction','industry'])
df_jobsearchappend = pd.DataFrame()

df_jobsearch = pd.DataFrame(dict_jobsearch,columns=['location', 'time','applicants','jobfunction','industry'] ) 
  df_jobsearchappend = df_jobsearchappend.append(df_jobsearch,ignore_index=True)     
  print(df_jobsearchappend)
