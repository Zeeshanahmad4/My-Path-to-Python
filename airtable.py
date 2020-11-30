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


  
  #saving screen shots
  dbx = dropbox.Dropbox('key')   

 
  def saveScreenshot():
    filename=str(random.random())[2:]+'.png'
    driver.save_screenshot(f'Screenshots/{filename}')
    with open(f'Screenshots/{filename}','rb') as file:
        ss=file.read()

    ss=dbx.files_upload(ss,f'/{filename}',autorename=True)


    ss_link=dbx.sharing_create_shared_link(f'/{filename}')

    ss_link=ss_link.url.replace('?dl=0','').replace('www','dl')

    attachment=[
          {
            "url": ss_link
          }
        ]
    airtable.update(row_id,fields={'Screenshot':attachment})
