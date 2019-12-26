import os

#wrong way
#db_user='testuser@gmail.com'
#db_user='testing@123'


#right way
#go to the home directory and open .bash_profile using your favorite texteditor and type the following 
#export DB_USER='testuser@gmail.com'
#export DB_PASS='testing@123'
db_user=os.environ.get('DB_USER')
db_password=os.environ.get('DB_PASS')


print(db_user)
print(db_password)
