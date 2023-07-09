# pickling the model
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)

def welcome():
	return 'welcome all'


def prediction(no_of_adults, no_of_children, no_of_weekend_nights, 
				no_of_week_nights, type_of_meal_plan, required_car_parking_space, 
				room_type_reserved, lead_time, arrival_year, arrival_month, arrival_date, 
				market_segment_type, repeated_guest, no_of_previous_cancellations, no_of_previous_bookings_not_canceled, 
				avg_price_per_room, no_of_special_requests):

	prediction = model.predict(
		[[no_of_adults, no_of_children, no_of_weekend_nights, 
				no_of_week_nights, type_of_meal_plan, required_car_parking_space, 
				room_type_reserved, lead_time, arrival_year, arrival_month, arrival_date, 
				market_segment_type, repeated_guest, no_of_previous_cancellations, no_of_previous_bookings_not_canceled, 
				avg_price_per_room, no_of_special_requests]])
	print(prediction)
	return prediction


def main():

	st.title("Hotel Reservation Prediction")
	html_temp = """
	<div style ="background-color:gry;padding:13px">
	<h1 style ="color:blue;text-align:center;">Streamlit Hotel Reservation Prediction ML App </h1>
	</div>
	"""
	st.markdown(html_temp, unsafe_allow_html = True)
	result =""


	no_of_adults = st.slider('No of Adults', 0, 4, 0)
	st.write("You Selected", no_of_adults, 'Adults')

	no_of_children = st.slider('no_of_children', 0, 10, 0)
	st.write("You Selected", no_of_children, 'No of Children')
	
	no_of_weekend_nights = st.slider('no_of_weekend_nights', 0, 7, 0)
	st.write("You Selected", no_of_weekend_nights, 'No of Weekend Nights')

	no_of_week_nights = st.slider('no_of_week_nights', 0, 17, 0)
	st.write("You Selected", no_of_week_nights, 'No of Week Nights')

	type_of_meal_plan = st.slider('type_of_meal_plan', 0, 3, 0)
	st.write("You Selected", type_of_meal_plan, 'Type of Meal Plan')


	required_car_parking_space = st.selectbox('Car Parking Space',('Yes', 'No'))
	if required_car_parking_space == 'Yes':
		parking = 1
	elif required_car_parking_space == 'No':
		parking = 0
	else:
		None
	st.write("You Selected", required_car_parking_space, 'Required Car Parking Space')


	room_type_reserved = st.slider('room_type_reserved', 0, 6, 0)
	st.write("You Selected", room_type_reserved, 'Room Type Reserved')
	
	lead_time = st.slider('lead_time', 0, 450, 0)
	st.write("You Selected", lead_time, 'Lead Time')

	arrival_year = st.selectbox('Arival Year',
    ('2017', '2018'))
	st.write("You Selected", arrival_year, 'Arrival Year')


	arrival_month = st.slider('arrival_month', 1, 12, 0)
	st.write("You Selected", arrival_month, 'Arrival Month')

	arrival_date = st.slider('arrival_date', 1, 31, 0)
	st.write("You Selected", arrival_date, 'Arrival Date')

	market_segment_type = st.slider('market_segment_type', 0, 4, 0)
	st.write("You Selected", market_segment_type, 'Market Segment Type')

	repeated_guest = st.selectbox('Repeated Guest',('Include', 'Not include'))
	if repeated_guest == 'Yes':
		rep_guest = 1
	elif repeated_guest == 'No':
		rep_guest = 0
	else:
		None
	st.write("You Selected", repeated_guest, 'Required Car Parking Space')

	no_of_previous_cancellations = st.slider('no_of_previous_cancellations', 0, 13, 0)
	st.write("You Selected", no_of_previous_cancellations, 'No of Previous Cancellations')

	no_of_previous_bookings_not_canceled = st.slider('no_of_previous_bookings_not_canceled', 0, 60, 0)
	st.write("You Selected", no_of_previous_bookings_not_canceled, 'No of Previous Bookings Not Canceled')

	avg_price_per_room = st.slider('avg_price_per_room', 0, 540, 0)
	st.write("You Selected", avg_price_per_room, 'Avg Price Per Room')

	no_of_special_requests = st.slider('no_of_special_requests', 0, 5, 0)
	st.write("You Selected", no_of_special_requests, 'No of Special Requests')
	if st.button("Predict"):
		result = prediction(no_of_adults, no_of_children, no_of_weekend_nights, 
				no_of_week_nights, type_of_meal_plan, required_car_parking_space, 
				room_type_reserved, lead_time, arrival_year, arrival_month, arrival_date, 
				market_segment_type, repeated_guest, no_of_previous_cancellations, no_of_previous_bookings_not_canceled, 
				avg_price_per_room, no_of_special_requests)
	st.success('The output is {}'.format(result))
	
if __name__=='__main__':
	main()