# Docker compose

# Prepare
* prepare .env file (examples in .env_sample)

# Start service
* docker-compose build
* docker-compose up

# Work with API (habits)
* http://127.0.0.1:8000/api/v1/habits/ - show all habits that user has access
* http://127.0.0.1:8000/api/v1/habit/int:pk/ - show user's habit detail information
* http://127.0.0.1:8000/api/v1/habit/create/ - create habit
* http://127.0.0.1:8000/api/v1/habit/update/int:pk/ - update habit
* http://127.0.0.1:8000/api/v1/habit/delete/int:pk/ - delete habit
* http://127.0.0.1:8000/api/v1/share_habits/ - show all public habits
# Work with API (users)
* http://127.0.0.1:8000/api/v1/users/show/ - show all users
* http://127.0.0.1:8000/api/v1/users/show/int:pk/ - show user's detail information
* http://127.0.0.1:8000/api/v1/users/update/int:pk/ - update user information
* http://127.0.0.1:8000/api/v1/users/delete/int:pk/ - delete user information
* http://127.0.0.1:8000/api/v1/users/registration/ - register user
* http://127.0.0.1:8000/api/v1/users/token/ - get token for user
* http://127.0.0.1:8000/api/v1/users/token/refresh/ - refresh user token
# API Documentation
* http://127.0.0.1:8000/redoc/