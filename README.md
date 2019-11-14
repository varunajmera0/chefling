# chefling
For Assignment 1 - instructions:
1) download chefling - assignment 1 folder
2) go to chefling - assignment 1 folder and run requirement file using this command on terminal/cmd
   command- python3 install -r requirement.txt
3) after that run python3 manage.py runserver and hit this ip on the chrome - 127.0.0.1:8000


#
1) signup api - http://127.0.0.1:8000/api/v1/signup/ - method - post
    data_fields = {name: 'chefling',
            email: 'chefling@gmail.com,
            password: 'chefling'}
            
2) signin api - http://127.0.0.1:8000/api/v1/signin/ - method - post
    data_fields = {email: 'chefling@gmail.com, password: 'chefling'}
    
3) profile detail - http://127.0.0.1:8000/api/v1/profile/ - method - get
    Token required
    Note - you have to pass auth token in header. you can use postman. In postman go to header section pass key as Authorization and value as Token {auth_token}.
   auth token you can receive from signup api as well as signin api.

4) profile update - http://127.0.0.1:8000/api/v1/profile/update/ - method - put
   Token required
   data_fields = {name: 'chefling', password: 'chefling'}
   Note - you can use postman. In postman go to header section pass key as Authorization and value as Token {auth_token}.
   auth token you can receive from signup api as well as signin api.
