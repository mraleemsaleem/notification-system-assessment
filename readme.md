# Introduction
Notification system that has the ability to send a message depending on the category and subscribers, notify to users in their channels they are registered..

## Installation Front-End
open frontend  : cd my-app

install node module : npm install

run server : npm start

## Installation Backend

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install these packages.

```bash
pip install django
pip install djangorestframework

```

## Usage
There are 3 message categories:

▪ Sports
▪ Finance
▪ Movies


And there are 3 types of notifications channel, each type have its own class to manage the logic of sending the message independently in the user channels.


▪ SMS
▪ E-Mail
▪ Push Notification


Anonymous users are not allowed to receive notification or the need to communicate with any external APIs, only registered users the sent notification in an archive of Logs or in a database.


In the log, information of notification are save that has sent correctly to the respective subscriber, such as the type of message, type of notification, user data, time, etc.
Information about users:

• ID

• Name

• Email

• Phone number

• Subscribed [ ] All the categories where the user is subscribed 

• Channels [ ] A list of the notification's channels (SMS | E-Mail | Push Notification)


As user interface there are 2 main elements.
1. Submission form. A simple form to send the message, which  have 2 fields:

• Category. List of available categories.
• Message. Text area, only validate that the message is not empty.

2. Log history. A list of all records in the log, sorted from newest to oldest.