# MRRS

A Medical Registration Recommendaion System

---

## Description

Now I only implement the front-end. If you type something in the search box,
the web will return a table with results. A naive project:)

## Installation

### 1. Django

```sh
sudo pip install django
```

### 2. PostgreSQL

#### 2.1 [Install PostgreSQL](https://bibaijin.github.io/homepage/technology/postgresql.md)

#### 2.2 Python's interface library with PostgreSQL

```sh
sudo pacman -S python-psycopg2
```

### 3. other python library

```sh
cd MRRS/front-end
sudo pip install pip.txt
```

## Run

```sh
cd MRRS/front-end
python manage.py migrate    # create new table
python manage.py runserver
```

## Visit the website

Open `http://127.0.0.1:8000/search_engine` in a browser.
