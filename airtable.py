# install it
pip uninstall airtable
pip install airtable-python-wrapper
# import it
from airtable import Airtable

#intilize
airtable1 = Airtable(api_key='key7BnLq2O4dACj81',
                     table_name='leading_ads', base_key='appPzGUWNjmOLCJqG')

#for loop on  list
for info in airtable1.get_all():
  print(info['fields'])
  
#update record  
airtable1.update(info['id'], {'Profile_name': 'Ready'})

#replace whole row
fields = {'PassangerName': 'Mike', 'Passport': 'YASD232-23'}
airtable1.replace(record['id'], fields)
 #or send the dic

