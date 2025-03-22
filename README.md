# COMP 636: Python Assessment

Due: **5pm Friday 28 March 2025**

Worth 40% of COMP636 grade

Submit via Akoraka | Learn

## Introduction

Selwyn Event Ticketing (SET) is a New Zealand based company that sells tickets for Events.
SET would like to develop a system to keep a record of Events, Customers and tickets sold.
Information is stored about each Customer, and they are assigned a unique ID number.
Events have a unique name, a date (NZ format), a capacity limit (how many tickets can be sold), an age restriction.
For each Event, the system records how many tickets have been sold in total, along with a record of how many tickets each Customer purchased.

You have been asked to help develop this system for SET by undertaking the tasks described below.

## Task

Add the following features to the system:

1.  **Menu enhancement:** Modify the code so that the user can enter an upper- or lower-case X (i.e., X or x) to exit the program.

2.  **List Customers and their Events:** List all the Customers (ordered by family name, then first name) and their details along with the Events they have bought tickets for. Display Customer information, including ID number, name, birth date and email address. Birth date should be presented in an appropriate human readable NZ date format. For each Customer, underneath their details, display the Events they have purchased tickets for. The Events for each Customer must be ordered by Event name.

3.  **List Event details:** List all Events in alphabetical order by name, showing all of the Event details, except for the list of Customers.

4.  **Buy Tickets1:** The user specifies an existing Customer and then the Event that that Customer is buying tickets for and the number of tickets. Customers can purchase tickets only if they are old enough to attend that Event and there are sufficient tickets available. Customers can purchase tickets only for future Events.

5.  **Add new Customer:** Ask the user to enter details of a new Customer, which must be saved in the _customer_ list:

    - a. The new Customer ID must be unique (using provided unique_id() function)
    - b. Birth date should be entered in an appropriate NZ date format and no later than the current date, no earlier than 110 years before today.
    - c. A Customer has a first name and a family name, both MUST be entered.
    - d. The system will keep asking the user to add new Customers until the user enters an option to return to the main menu.

6.  **List Future Events with unsold tickets:**

    - a. List all future Events, which still have tickets available (where the tickets have not all been sold).
    - b. Events should be listed in date order, with the earliest Event first.
    - c. Details of the Events including the number of available tickets should be shown.
    - d. Do not list Customers who have bought tickets for each Event – just the details of the Event overall.

### Notes:

- The provided _events_your_name.py_ Python file contains a menu structure and partially completed functions. These functions must not be deleted or renamed, but you may add arguments/parameters to these functions. You may also add additional functions of your own. Remember to rename the file to include your name.

_\* For the purposes of this assignment, it is assumed the purchaser of tickets is responsible for ensuring their group all meet the age restriction._

---

### Reference

- [Setting multiple accounts on git and vscode](https://stackoverflow.com/questions/70755815/setting-multiple-accounts-on-git-and-vscode)

_You can specify a user.name and a user.email for each repo. Run below command in the git repo where you need to specify the user/email_

```
git config user.name <user-name>
git config user.email <user-email>
```

_Personnaly, i have a global configuration (i.e. git config --global user.name ) for my work (because i have a looooot of projects to deal with), and for my personnal projects (just a few) I do the local configuration like above._
