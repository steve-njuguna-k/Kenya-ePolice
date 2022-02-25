# Kenya ePolice
A Police Station Management System built on Django that allows users to book criminals, cases, court details &amp; cell occupancy. User must be logged in to access the application.

![](https://github.com/steve-njuguna-k/Kenya-ePolice/blob/master/Screenshots/Screenshot-1.PNG)

![](https://github.com/steve-njuguna-k/Kenya-ePolice/blob/master/Screenshots/Screenshot-2.PNG)

## Requirements
The user can perform the following functions:

- A user can add arrested persons
- A user can add case details 
- A user can add court details
- A user can add cell details
- A user must be signed in to access the application
- A user can can search for arrested persons

## Installation / Setup instruction
The application requires the following installations to operate:
- pip
- gunicorn
- django
- postgresql

## Technologies Used
- python 4.0.1

## Project Setup Instructions
1) git clone the repository 
```
https://github.com/steve-njuguna-k/Kenya-ePolice.git
```
2. cd into Kenya-ePolice
```
cd Kenya-ePolice
```
3. create a virtual env
```
py -m venv env
```
4. activate env
```
env\scripts\activate
```
5. Open CMD & Install Dependancies
```
pip install -r requirements.txt
```
6. Make Migrations
```
py manage.py makemigrations
```
7. Migrate DB
```
py manage.py migrate
```
8. Run Application
```
py manage.py runserver
```

## Known Bugs
- There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information
If you have any question or contributions, please find me on [LinkedIn](https://www.linkedin.com/in/steve-njuguna-aa426096/)

© 2022 Steve Njuguna

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
