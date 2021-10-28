# agtuary-python

API wrapper interface for agricultural analytics 

***WARNING: very early stages of development. Breaking changes may occur***

## Setup

## Install

Install the `agtuary` package:

```
pip install agtuary
```

### Create a client


```python
from agtuary import Agtuary

user = "test@agtuary.com"
psk = "supersecret123"

at_client = Agtuary(email=user, password=psk)
```

## API layout

The API wrapper functions for getting data rely upon a region ID. This region ID is a unique code, that is generated on-demand for a GeoJSON-based region, and pre-determined for government-defined regions (postcodes, suburbs, LGA/shires, broadacre zones, states). 

For these government defined regions, the analytics are pre-calculated so it is available instantly through the API wrapper. For your own GeoJSON-based region, like a particular property or farm, the analytics are calculated on-demand. These are accessible based on your pricing plan.

There are helper functions that return all of the region ID's for a particular point or address (street or town name).


## Products and Subtypes

The data types and analytics are split up by products and subtypes. A product is a specific internal dataset that we create analytics from, and a subtype is a set of values created by an algorithm or method on that dataset. A product most commonly has multiple subtypes.

Available products:

- Rainfall
- Productivity
- Soil
- Temperature

### Rainfall


|Subtype|Description|How it's calculated|
|---|---|---|
|volume|Rainfall volumes of each season for each year|For each month, average the rainfall over that area, add to the sum for that season|
|duration|The number of months with significant rainfall during a season for each year|For each season, sum the number of months in that season that have rainfall of `> 30mm`|
consistency|For a period of 12 months, output the average for each month with corresponding 75% percentiles to show consistency|For each month, calculate the average historical rainfall and it's corresponding 75 percentile error intervals|
|reliability|Histograms of each season indicating the reliability of typical rainfall for this region|For each season create  histogram with `50 mm` bins using average rainfall for each year|

#### Usage

Get all the data using a point:

```python
data = at_client.rainfall((-33.33, 149.58))
```

Get all the data using an address:

```python
data = at_client.rainfall("Edgells Ln, Kelso NSW 2795")
```

Get some of the data based on the `subtypes`. First, get a list of the `subtypes` by calling:

```python
print(at.rainfall_subtypes)
```

Then pass the desired `subtypes` into the `rainfall()` method:

```python
data = at_client.rainfall((-33.33, 149.58), subtypes=["volume"])
```

This should return:

`print(data.values)`

```json
[
    ["1995-01-01T00:00:00",
     {"summer": 46.53524684906006,
      "autumn": 114.27728319168091,
      "winter": 156.54125213623047,
      "spring": 83.89842867851257}],
    ["1996-01-01T00:00:00", {
        ...
    }],
    ...
]
```

### Productivity

|Subtype|Description|How it's calculated|
|---|---|---|
|landuse|Land use classification per year of the major types|For each year, a classification model is ran to infer the best-matched land use type, creating a mask over the region. The total area of each land use type in hectares is then calculated |
|ndvi_aoc|Total area under the NDVI growth curve|For each year, sum the area under the NDVI growth curve over the region. From this, calculate the average for each land use type|
|ndvi_max|Maximum NDVI throughout the year|For each year, calculate the maximum NDVI value over the region. From this, calculate the average for each land use type| 
|plant_harvest|Estimated planting and harvesting dates|For each year, for winter and summer areas from the land use mask, fit each to a curve equation and estimate the planting and harvest dates| 

#### Usage

```python
data = at_client.productivity((-33.33, 149.58), subtypes=["landuse"])
```

This should return:

`print(data.values)`

```json
[
    ["2003-01-01T00:00:00",
     {"pasture": 73.2,
      "winter": 1420.2,
      "summer": 0.0,
      "nature": 21.6,
      "other": 326.9}],
    ["2004-01-01T00:00:00", {
        ...
    }],
    ...
]
```

## API Road Map

- [x] rainfall
    - [x] volume
    - [x] consistency
    - [x] reliability
    - [x] duration
- [ ] ndvi/productivity *(10% complete)*
    - [ ] Land use classification
    - [ ] Area under NDVI growth curve
    - [ ] Maximum NDVI ndvi_max
    - [ ] rainfall vs productivity
- [ ] soil *(50% complete)*
    - [x] pH
    - [ ] soil texture (sand, silt, clay content)
    - [x] available water capacity (AWC)
- [ ] temperature
    - [ ] frost risk
    - [ ] heat risk
    - [ ] temperature trend over time
