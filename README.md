# Fake News Detection
our project aims to detect Fake News based on a user query and display the results on a webpage using Flask. It is Static file types


## Dataset overview

 - `politifact_fake.csv` -  Samples related to fake news collected from PolitiFact
 - `politifact_real.csv` -  Samples related to real news collected  from PolitiFact
 - `gossipcop_fake.csv` - Samples related to fake news collected from GossipCop
 - `gossipcop_real.csv` - Samples related to real news collected from GossipCop


###  Requirements:
Data download scripts are writtern in python and requires `python 3.8+` to run.

Install all the libraries in `requirements.txt` using the following command:
````
pip install -r requirements.txt
````


## Running Code

### Virtual Environment setup:
Create the virtual environment:
````
> py -3 -m venv venv
````

Activate the corresponding environment:
````
> venv\Scripts\activate
````

### Flask setup:
Configure flask environment:
````
> $env:FLASK_ENV = "development"
> $env:FLASK_APP = "get_results.py"
````

After the setup, run the following command to launch the flask app on your localhost:
````
> flask run
````


## References
If you use this dataset, please cite the following papers:
~~~~
@article{shu2018fakenewsnet,
  title={FakeNewsNet: A Data Repository with News Content,
         Social Context and Dynamic Information for Studying Fake News on Social Media},
  author={Shu, Kai and  Mahudeswaran, Deepak and Wang, Suhang and Lee, Dongwon and Liu, Huan},
  journal={arXiv preprint arXiv:1809.01286},
  year={2018}
}
~~~