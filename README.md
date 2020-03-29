#BestNeighbor
### Inspiration
 
The COVID_19 pandemic has severely impacted the most vulnerable members of our community, and it has strained those working on the frontlines of the response. Our team wanted to provide our community with a tool where people in need can ask for help in getting grocery items, and volunteers can log in and provide the help. 

A user in need could range from a person whose health makes them vulnerable enough to leave the house, a healthcare worker who’s too busy in the frontlines to get groceries for their family, or a single parent who can’t leave their kids alone.

### What it does

Through BestNeighbor, a person in need of help can provide a wishlist of items they need from a local store along with their zip-code. Volunteers can then log in and see wishlists available within a selected zip-code. These two users will be able to contact each other and coordinate payment and delivery.

### How we built it

In 48-hours, our team brainstormed the project idea, built, integrated and tested the webapp using the following software stack:
Backend: Postgresql, Flask, SqlAlchemy
Frontend: HTML, CSS, Bootstrap

## Installation

### Prerequisites
- Python3
- PostgreSQL
- Flask
- SQLAlchemy

### Run BestNeighbor on your local computer:

Clone repository:

```
$ git clone https://github.com/Hackbright-Covid-19-Hackathon/hack-covid-19.git
```
Create and activate a virtual environment inside your local directory:
```
$ virtualenv env --always-copy  
$ source env/bin/activate
```

Install dependencies:
```
$ pip install -r requirements.txt
```
Create a database called volunteerdb:
```
$ createdb volunteerdb
```
Import the data:
```
python3 -i seed.py
```
Run the app from the command line:
```
$ python3 server.py
```
## Features

### Homepage

[insert homepage image]

### Volunteer page

[insert volunteer page image]

### Asker page

[insert asker page image]


## What’s next
The following features are planned for implementation:
- Secure messaging within webapp to keep user’s personal phone number and email private
- Ratings system for volunteers
- User verification


## About the Developers:
