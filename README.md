## How to run the application

(0) If not yet installed, install PostgreSQL on your device

instructions: https://github.com/hy-tsoha/local-pg

1. Clone the application repository to your device


```bash
git clone https://github.com/hakkajoe/Restaurant-Central---Database-application
```

2. Open psql and create a new database, and then copy the contents of the schema.sql -file to that database

```bash
CREATE DATABASE <name of the database that you can choose>
```
```bash
psql -d <database name that you chose> < schema.sql
```

3. Create .env file to the cloned folder with the following content:


DATABASE_URL=postgresql+psycopg2:///(name of the database that you chose in phase 2)

SECRET_KEY= (secret key of your choosing)


4. Create virtual environment in the cloned folder and activate it

```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

5. Install dependent libraries

```bash
pip install -r requirements.txt
```
