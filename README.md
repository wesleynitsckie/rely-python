# Rely Compliance

A Simple Workflow to test a user's compliance

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Usage

```python
python manage.py runserver
```
Once the server is running open your browser and go to:
[http://127.0.0.1:8000](http://127.0.0.1:8000/)

>Sanctioned List 
```Jacob Zuma 2019-12-25```

>PEP List
```Jacob Zuma 2019-12-25```
```Julius Malema 2019-12-25```

## API 
**Create a Transaction**
```python
http://127.0.0.1:8000/api/transaction_list
POST
{
    "first_name": "Wesley",
    "last_name": "Nitsckie",
    "dob": "2003-12-12",
    "income": 26000.34
}
```
> Sample Response
```json
{
    "id": "c5719c24-45c5-4f4a-8e2b-25ba7cc55c7a",
    "status": "SC",
    "transaction_blob": "{\"first_name\": \"Wesley\", \"last_name\": \"Nitsckie\", \"income\": 26000.34, \"dob\": \"2003-12-12\"}"
}
```

**Check Status**
```python
http://127.0.0.1:8000/api/status
POST
{
    "id":"c5719c24-45c5-4f4a-8e2b-25ba7cc55c7a"
}
> Sample Response
```json
{
    "id": "c5719c24-45c5-4f4a-8e2b-25ba7cc55c7a",
    "status": "DENIED",
    "transaction_blob": "{\"first_name\": \"Wesley\", \"last_name\": \"Nitsckie\", \"income\": 26000.34, \"dob\": \"2003-12-12\"}"
}
```

**Confirm Sanction**
```python
http://127.0.0.1:8000/api/confirm_sanction
POST
{
    "id":"c5719c24-45c5-4f4a-8e2b-25ba7cc55c7a",
    "confirm" : false
}
> Sample Response
```json
{
    "id": "c5719c24-45c5-4f4a-8e2b-25ba7cc55c7a",
    "status": "PC",
    "transaction_blob": "{\"first_name\": \"Wesley\", \"last_name\": \"Nitsckie\", \"income\": 26000.34, \"dob\": \"2003-12-12\"}"
}
```


**Confirm PEP**
```python
http://127.0.0.1:8000/api/confirm_pep
POST
{
    "id":"c5719c24-45c5-4f4a-8e2b-25ba7cc55c7a",
    "confirm" : true
}
> Sample Response
```json
{
    "id": "c5719c24-45c5-4f4a-8e2b-25ba7cc55c7a",
    "status": "AS",
    "transaction_blob": "{\"first_name\": \"Wesley\", \"last_name\": \"Nitsckie\", \"income\": 26000.34, \"dob\": \"2003-12-12\"}"
}
```

## Status Codes
```
INIT - 'Initialized'
SC - 'Sanction Check')
SCC - 'Sanction Check Completed'
PC - 'PEP Check'
PCC - 'PEP Check Completed'
AS - 'Assessment'
ACCEPTED - 'Accepted'
DENIED - 'Denied'
```

## API Workflow
- Create a new Transaction
- Get the new Transaction Id
- Check the status of the Transaction 
- If the status is *SCC* (Sanction Check Completed) then a *Sanction Confirm* is required
- If the status is *PCC* (PEP Check Completed) then a *PEP Confirm* is required

## License
[MIT](https://choosealicense.com/licenses/mit/)
