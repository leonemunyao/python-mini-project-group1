### Weather Trends Analysis

#### Data Structures

Input Data (`historical_weather.csv`)

`date,temperature,rainfall,humidity,season,month,year`
`2020-01-01,23.5,0.0,65,Summer,1,2020`

Output Data (`analysis_results.csv`)

`analysis_date,metric,analysis_type,category,value
2024-04-24,temperature,Yearly Trends,2020,23.13`

#### Dependancies

* `pandas`
* `numpy`
* `python-tk`
* `matplotlib`

#### Running the Program

`cd python-mini-project-group1`
`python src/main.py`

#### Testing independent files.

`python src/analysis.py`
`python src/data_loader.py`
`python src/utils.py`
`python src/visualization.py`

