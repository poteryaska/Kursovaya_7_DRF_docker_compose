Coursework_7_DRF

WORK WITH DJANGO DRF
Allow to create habits scheduler and make notification to user telegram bot
Requirements.
Python
Redis
Postgres
Installation
Download repo
Install requirements (pip3 install -r requirements.txt)
Run service Redis (redis-server)
Prepare
prepare .env file (examples in .env_sample)
create database for postgres
prepare migrations (python3 manage.py makemigrations)
make migrate (python3 manage.py migrate)
prepare test user (optional) (python3 manage.py ccsu)
prepare telegram bot for send information 
run command /start in telegram bot
Start service
run command: celery -A config worker -l INFO
run command: celery -A config beat -l info -S django
python3 manage.py runserver
Work with API (habits)
http://127.0.0.1:8000/api/v1/habits/ - show all habits that user has access
http://127.0.0.1:8000/api/v1/habit/int:pk/ - show user's habit detail information
http://127.0.0.1:8000/api/v1/habit/create/ - create habit
http://127.0.0.1:8000/api/v1/habit/update/int:pk/ - update habit
http://127.0.0.1:8000/api/v1/habit/delete/int:pk/ - delete habit
http://127.0.0.1:8000/api/v1/share_habits/ - show all public habits
Work with API (users)
http://127.0.0.1:8000/api/v1/users/show/ - show all users
http://127.0.0.1:8000/api/v1/users/show/int:pk/ - show user's detail information
http://127.0.0.1:8000/api/v1/users/update/int:pk/ - update user information
http://127.0.0.1:8000/api/v1/users/delete/int:pk/ - delete user information
http://127.0.0.1:8000/api/v1/users/registration/ - register user
http://127.0.0.1:8000/api/v1/users/token/ - get token for user
http://127.0.0.1:8000/api/v1/users/token/refresh/ - refresh user token
API Documentation (v1)
http://127.0.0.1:8000/redoc/