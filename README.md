<!-- @format -->
### Python command line script for PostgreSQL bulk insert, update, update-on-conflict
---
Nowadays data is one of the important things in the digital world. So most of the time we need to insert a list of data into the database. To insert a list of data into the database normally we do these things:
1) Traverse all list and insert one item at a time
2) Traverse all list and generate a query and insert all data at a time
3) Without traversing we can insert data at a time from the list **(bulk insert)**

#1 and #2 both process seems costly and complicated for me, so here we going to **learn** how can we implement #3 in **Postgre database using python script**. 

Besides that, we learn some more things like:
- Bulk update
- Bulk update on conflict
- How to write Python command-line script
- Optional and mandatory command-line argument

#### Tools & Technology :
---
* [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
* [psycopg2](https://www.psycopg.org/docs/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

#### Configuration (put the appropiate info into .env file) :

```bash
DB_NAME=xyz
DB_USER=xyz
DB_PASS=xyz
DB_PORT=5432
DB_HOST=localhost

```
#### Installation :
Create databse named **BulkDB** and table named **bulktable**. You can create it manually or execute script **sql.sql** found in project root directory.

Create virtual environment(venv)

```bash
$ pip install virtualenv
$ virtualenv -p python3 venv
$ source ./venv/Scripts/activate (windows)
$ source venv/bin/activate (linux)
```

Install dependences

```bash
$ pip install -r requirements.txt
```

#### Usages: 

Bulk insert:

```
python main.py ./data/data.json -o insert
```

Bulk update:

```
python main.py ./data/data.json -o update
```

Bulk update on conflict:

```
python main.py ./data/data.json -o update-on-conflict
```
