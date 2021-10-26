# agtuary-python

API wrapper interface for agricultural analytics 

### Usage

Create a client:

```python

user = "test@agtuary.com"
psk = "supersecrete123"

at_client = Agtuary(email=user, password=psk)

print(at_client.periods)
print(at_client.subtypes)
```

#### Rainfall

```python
data = at_client.rainfall((-33.33, 149.58))
data = at_client.rainfall("Edgells Ln, Kelso NSW 2795")
data = at_client.rainfall((-33.33, 149.58), subtypes = ["volume"], periods = ["annual"])

```


## Project Road Map

- [x] rainfall
- [ ] soil *(50% complete)*
- [ ] ndvi/productivity
- [ ] temperature

 #### Notes:

- pass in location data and get LGA (region) data = WORKING
- pass in location data and it calculated and returns for a point = Not working yet
- getting all theLGA scores = WORKING

