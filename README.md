<!-- @format -->

### Put the appropiate info into .env file

```bash
DB_NAME=xyz
DB_USER=xyz
DB_PASS=xyz
DB_PORT=5432
DB_HOST=localhost

```

### Create virtual environment(venv)

```bash
$ pip install virtualenv
$ virtualenv -p python3 venv
$ source ./venv/Scripts/activate (windows)
$ source venv/bin/activate (linux)
```

### Install dependences

```bash
$ pip install -r requirements.txt
```

### Usages

**Insert data from all detected indices (depending on folder name)**

```
python main.py ./path
```

**Insert data of selected indices but with all UUIDs**

```
python main.py ./path -i index,index,....
```

**Insert data of all indices but selected UUIDs**

```
python main.py ./path -u uuid,uuid,.....
```

**Insert data of selected indices and selected UUIDs**

```
python main.py ./path -i index,index,... -u uuid,uuid,...
```

**_There is another option(-o/--option) that will detect the operation_**

`-o insert(default option)`: Insert all data into database

Example:

`python main.py ./path --option insert`, `python main.py ./path -i index,index -u uuid,uuid -o insert` etc

`-o update`: Update only existing data

Example:

`python main.py ./path -i index,index --option update`, `python main.py ./path -u uuid,uuid -o update` etc

`-o reset`: Remove existing data and insert all data from location

Example:

`python main.py ./path -i index,index -o reset`, `python main.py ./path -u uuid,uuid --option reset` etc
