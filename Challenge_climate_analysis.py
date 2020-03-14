# Add dependancies
%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
#Create the connection between sqlite and pandas
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# We can view all of the classes that automap found
Base.classes.keys()
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)
 #Design a query to get June temperature data for all station and allthe years.
#complete the query to extract all desired results and put them in a list.
juneallresults = []
juneallresults = session.query(Measurement.date, Measurement.tobs).filter(func.extract('month', Measurement.date) == 6).all()
june_all_df = pd.DataFrame(juneallresults, columns=['date','temperatures'])
june_all_df.describe()
#june_all_df
 #Design a query to get June temperature data for all station and only for two years.
# Calculate the date one year from the last date in data set.
prev_year = dt.date(2017,8,23)- dt.timedelta(days=365)
#complete the query to extract all desired results and put them in a list.
junetwoyearresults = []
junetwoyearresults = session.query(Measurement.date, Measurement.tobs).filter(func.extract('month', Measurement.date) == 6).filter(Measurement.date >= prev_year).all()
june_twoyear_df = pd.DataFrame(junetwoyearresults, columns=['date','temperatures'])
june_twoyear_df.describe()
#june_twoyear_df
 #Design a query to get December temperature data for all station and all the years.
#complete the query to extract all desired results and put them in a list.
decemberallresults=[]
decemberallresults = session.query(Measurement.date, Measurement.tobs).filter(func.extract('month', Measurement.date) == 12).all()
dec_all_df = pd.DataFrame(decemberallresults, columns=['date','temperatures'])
dec_all_df.describe()
#dec_all_df
#Design a query to get December temperature data for all station and only for two years.
# Calculate the date one year from the last date in data set.
prev_year = dt.date(2017,8,23)- dt.timedelta(days=365)
#complete the query to extract all desired results and put them in a list.
dectwoyearresults=[]
#complete the query to extract all desired results and put them in a list.
dectwoyearresults = session.query(Measurement.date, Measurement.tobs).filter(func.extract('month', Measurement.date) == 12).filter(Measurement.date >= prev_year).all()
dec_twoyr_df = pd.DataFrame(dectwoyearresults, columns=['date','temperatures'])
dec_twoyr_df.describe()
#dec_twoyr_df