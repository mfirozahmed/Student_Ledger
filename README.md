# Student_Ledger

Ledger is a python and mysql based command-line application.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install mysql-connector-python
```

## Run the project

```bash
python main.py
```

## Usage

First, you have to set the database credentials. Go into 'Database' -> 'database.py', change 'user' and 'password' as your local mysql username and password.

For the first time, as there will be no database or tables for the application, it will create one. Every time after that, it will try to access the created database.

Tasks:

    * A student can be added by giving the necessary info as input.
    * A student can be deleted if s/he is active by giving the class and name.
    * A student info can be updated by giving class and name as input. Teaching days in specific subject of mark can be updated.
    * All the students can be shown in a tabular form given the class. Individual student can also be shown in details by giving his/her name.
    * Overall info can be found, for example
        i.   Total days taught accross all classes,
        ii.  Individual days taught accross each class,
        iii. Total earnings,
        iv.  Individual earnings of each class,
        v.   Individual earnings of each subject,
        vi.  Average marks of all students
