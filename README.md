# agtuary-python

API wrapper interface for agricultural analytics 

### Usage

Create a client:

```python

user = "test@agtuary.com"
psk = "supersecrete123"

agtuary = Agtuary(email=user, password=psk)
```

#### Rainfall

```python
data = agtuary.rainfall()
```

Notes:

- pass in location data and get LGA (region) data = WORKING
- pass in location data and it calculated and returns for a point = Not working yet
- getting all theLGA scores = WORKING

