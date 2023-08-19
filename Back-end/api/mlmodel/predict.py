import pickle
from api.models import NewRideDetail
# Load the pickle file
with open('sharing', 'rb') as shar:
    model1 = pickle.load(shar)

with open('rentention', 'rb') as ren:
    model2 = pickle.load(ren)

with open('fare_amount', 'rb') as fare:
    model3 = pickle.load(fare)



def predict_carpool_percentage(ride):
    # Prepare the input features for prediction
    features1 = [ride.PULocationID, ride.DOLocationID, ride.trip_miles, ride.trip_time,
                ride.wav_request_flag, ride.request_datetime,]

    # Perform any necessary preprocessing or feature engineering on the features

    # Make the prediction using the loaded model
    carpool_percentage = model1.predict([features1])[0]

    return carpool_percentage

# Assuming you have a ride instance
ride = NewRideDetail.objects.get(ride_id=1234)

# Call the predict_carpool_percentage function
carpool_percentage = predict_carpool_percentage(ride)

# Assign the predicted carpool percentage to the ride instance
ride.carpoolPercent = carpool_percentage
ride.save()




def predict_fare_amount(ride):
    features2 = [ride.passenger_count,ride.trip_distance,ride.pickup_longitude,ride.pickup_latitude,
                 ride.pickup_latitude,ride.dropoff_longitude,ride.dropoff_latitude,ride.tolls_amount]

    fare_amount = model2.predict([features2])[0]

    return fare_amount