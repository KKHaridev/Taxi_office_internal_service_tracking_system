import pickle
from api.models import NewRideDetail
from api.models import yellow_tripdata_2016_03
import pandas as pd
import random
import numpy as np
from sklearn.preprocessing import StandardScaler

# # Query the data
# trip_data = yellow_tripdata_2016_03.objects.all()

# # Convert the query result to a DataFrame
# data = pd.DataFrame(list(trip_data.values('pickup_longitude', 'pickup_latitude')))
# import os
# print(os.getcwd())

# script_dir = os.path.dirname(__file__)  # Get the directory of the script
# pickle_path = os.path.join(script_dir, 'sharing_of_cab.pickle')
# print(pickle_path)


#Load the pickle file
with open('sharing_of_cab.pickle', 'rb') as shar:
    model1 = pickle.load(shar)

# shar = open('sharing_of_cab', 'ab')
# model1 = pickle.load(shar)
# with open('rentention', 'rb') as ren:
#     model2 = pickle.load(ren)

with open('fare_amount_final.pickle', 'rb') as fare:
    model3 = pickle.load(fare)



def predict_carpool_percentage(ride):

    if(ride.start_from=="central park"):
        PULocationID = 43;
    if(ride.start_from=="jfk airport"):
        PULocationID = 132;
    if(ride.start_from=="LGA"):
        PULocationID = 230;
    if(ride.start_from=="lowermanhattan"):
        PULocationID = 138;
    if(ride.start_from=="timesq"):
        PULocationID = 211;
    
    if(ride.destination=="central park"):
        DOLocationID = 43;
    if(ride.destination=="jfk airport"):
        DOLocationID = 132;
    if(ride.destination=="LGA"):
        DOLocationID = 230;
    if(ride.destination=="lowermanhattan"):
        DOLocationID = 138;
    if(ride.destination=="timesq"):
        DOLocationID = 211;


    if(ride.start_from=="central park" and ride.destination=="jfk airport"):
        tripdistance = 18.5
    if(ride.start_from=="central park" and ride.destination=="LGA"):
        tripdistance = 8.5
    if(ride.start_from=="central park" and ride.destination=="lowermanhattan"):
        tripdistance = 3.2
    if(ride.start_from=="central park" and ride.destination=="timesq"):
        tripdistance = 2.3


    if(ride.start_from=="jfk airport" and ride.destination=="central park"):
        tripdistance = 17.5
    if(ride.start_from=="jfk airport" and ride.destination=="LGA"):
        tripdistance = 9.5
    if(ride.start_from=="jfk airport" and ride.destination=="lowermanhattan"):
        tripdistance = 18.2
    if(ride.start_from=="jfk airport" and ride.destination=="timesq"):
        tripdistance = 16.3

    if(ride.start_from=="LGA" and ride.destination=="central park"):
        tripdistance = 7.4
    if(ride.start_from=="LGA" and ride.destination=="jfk airport"):
        tripdistance = 9.5
    if(ride.start_from=="LGA" and ride.destination=="lowermanhattan"):
        tripdistance = 9.4
    if(ride.start_from=="LGA" and ride.destination=="timesq"):
        tripdistance = 8.6

    if(ride.start_from=="lowermanhattan" and ride.destination=="central park"):
        tripdistance = 4.5
    if(ride.start_from=="lowermanhattan" and ride.destination=="jfk airport"):
        tripdistance = 16.5
    if(ride.start_from=="lowermanhattan" and ride.destination=="LGA"):
        tripdistance = 9.4
    if(ride.start_from=="lowermanhattan" and ride.destination=="timesq"):
        tripdistance = 3.0
    
    if(ride.start_from=="timesq" and ride.destination=="central park"):
        tripdistance = 2.1
    if(ride.start_from=="timesq" and ride.destination=="jfk airport"):
        tripdistance = 16.2
    if(ride.start_from=="timesq" and ride.destination=="LGA"):
        tripdistance = 9.4
    if(ride.start_from=="timesq" and ride.destination=="lowermanhattan"):
        tripdistance = 2.9
            
   
    shared_request_flag  = random.randint(0, 1)
    shared_match_flag =  random.randint(0, 1)
    wav_request_flag = random.randint(0, 1)

    requestdateime = np.int64(ride.request_datetime) // (10 ** 9)

    trip_time = 954

    sc = StandardScaler()

    features1 = sc.fit_transform([[
        PULocationID,
        DOLocationID, 
        tripdistance, 
        trip_time,
        wav_request_flag, 
        requestdateime,
        shared_request_flag,
        shared_match_flag],
        [PULocationID,
        DOLocationID, 
        tripdistance, 
        trip_time,
        wav_request_flag, 
        requestdateime,
        shared_request_flag,
        shared_match_flag]])
    # Prepare the input features for prediction
    
    


    # Perform any necessary preprocessing or feature engineering on the features

    # Make the prediction using the loaded model
    carpool_percentage = model1.predict_proba(features1)[0]

    return carpool_percentage *1000

# Assuming you have a ride instance
#ride = NewRideDetail.objects.get(ride_id=1234)

# Call the predict_carpool_percentage function
#carpool_percentage = predict_carpool_percentage(ride)

# Assign the predicted carpool percentage to the ride instance
#ride.carpoolPercent = carpool_percentage
#ride.save()






def predict_fare_amount(ride):
    central_park = 40.7800783589499,-73.9606739744674
    jfk_airport = 40.6462557859199,-73.7848832063897    
    LGA = 40.7701691816197,-73.8722559067017   
    lowermanhattan = 40.7257674140677,-73.996344250052   
    timesq = 40.7555076813623,-73.9824387182809 


    if(ride.start_from=="central park"):
        pickup_latitude=40.7800783589499
        pickup_longitude=-73.9606739744674
    if(ride.start_from=="jfk_airport"):
        pickup_latitude=40.6462557859199
        pickup_longitude=-73.7848832063897
    if(ride.start_from=="LGA"):
        pickup_latitude=40.7701691816197
        pickup_longitude=-73.8722559067017
    if(ride.start_from=="lowermanhattan"):
        pickup_latitude=40.7257674140677
        pickup_longitude=-73.996344250052
    if(ride.start_from=="timesq"):
        pickup_latitude=40.7555076813623
        pickup_longitude=-73.9824387182809

    if(ride.destination=="central park"):
        dropoff_latitude=40.7800783589499
        dropoff_longitude=-73.9606739744674
    if(ride.destination=="jfk_airport"):
        dropoff_latitude=40.6462557859199
        dropoff_longitude=-73.7848832063897
    if(ride.destination=="LGA"):
        dropoff_latitude=40.7701691816197
        dropoff_longitude=-73.8722559067017
    if(ride.destination=="lowermanhattan"):
        dropoff_latitude=40.7257674140677
        dropoff_longitude=-73.996344250052
    if(ride.destination=="timesq"):
        dropoff_latitude=40.7555076813623
        dropoff_longitude=-73.9824387182809

       

    if(ride.start_from=="central park" and ride.destination=="jfk airport"):
        tripdistance = 18.5
    if(ride.start_from=="central park" and ride.destination=="LGA"):
        tripdistance = 8.5
    if(ride.start_from=="central park" and ride.destination=="lowermanhattan"):
        tripdistance = 3.2
    if(ride.start_from=="central park" and ride.destination=="timesq"):
        tripdistance = 2.3


    if(ride.start_from=="jfk airport" and ride.destination=="central park"):
        tripdistance = 17.5
    if(ride.start_from=="jfk airport" and ride.destination=="LGA"):
        tripdistance = 9.5
    if(ride.start_from=="jfk airport" and ride.destination=="lowermanhattan"):
        tripdistance = 18.2
    if(ride.start_from=="jfk airport" and ride.destination=="timesq"):
        tripdistance = 16.3

    if(ride.start_from=="LGA" and ride.destination=="central park"):
        tripdistance = 7.4
    if(ride.start_from=="LGA" and ride.destination=="jfk airport"):
        tripdistance = 9.5
    if(ride.start_from=="LGA" and ride.destination=="lowermanhattan"):
        tripdistance = 9.4
    if(ride.start_from=="LGA" and ride.destination=="timesq"):
        tripdistance = 8.6

    if(ride.start_from=="lowermanhattan" and ride.destination=="central park"):
        tripdistance = 4.5
    if(ride.start_from=="lowermanhattan" and ride.destination=="jfk airport"):
        tripdistance = 16.5
    if(ride.start_from=="lowermanhattan" and ride.destination=="LGA"):
        tripdistance = 9.4
    if(ride.start_from=="lowermanhattan" and ride.destination=="timesq"):
        tripdistance = 3.0
    
    if(ride.start_from=="timesq" and ride.destination=="central park"):
        tripdistance = 2.1
    if(ride.start_from=="timesq" and ride.destination=="jfk airport"):
        tripdistance = 16.2
    if(ride.start_from=="timesq" and ride.destination=="LGA"):
        tripdistance = 9.4
    if(ride.start_from=="timesq" and ride.destination=="lowermanhattan"):
        tripdistance = 2.9
            


    sc = StandardScaler()
    features2 = sc.fit_transform([[ride.passenger_count,
                 tripdistance,
                 pickup_longitude,
                 pickup_latitude,
                 dropoff_longitude,
                 dropoff_latitude],[ride.passenger_count,
                 tripdistance,
                 pickup_longitude,
                 pickup_latitude,
                 dropoff_longitude,
                 dropoff_latitude]])

    fare_amount = model3.predict(features2)[0]


    return fare_amount