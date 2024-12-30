# -*- coding: utf-8 -*-
"""(P) Carbon Prediction and Alternative Transportation

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rrgxX3taxR-3hyLwe5EliiNOyO2221wA
"""

# Commented out IPython magic to ensure Python compatibility.
import csv
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tabulate import tabulate
import warnings

# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
sns.set_style('darkgrid')
import warnings
def ignore_warn(*args, **kwargs):
    pass
warnings.warn = ignore_warn #ignore annoying warning (from sklearn and seaborn)

from scipy import stats
from scipy.stats import norm, skew

pd.set_option('display.float_format', lambda x: '{:.3f}'.format(x))

def read_car_data():
    car_data = pd.read_csv('NEW_car_emission_dataset.csv', delimiter=';')
    return car_data

car_data = read_car_data()
car_data.head()

car_data.tail()

car_data.info()

car_data.describe()

car_data.columns

car_data.isna().sum()

sns.pairplot(car_data[['CAR TYPE', 'YEAR', 'VEHICLE CLASS', 'ENGINE SIZE (L)', 'CYLINDERS', 'TRANSMISSION', 'FUEL TYPE', 'FUEL CONSUMPTION CITY'
                , 'FUEL CONSUMPTION HWY', 'COMB (L/100 km)', 'COMB (mpg)', 'CO2 EMISSIONS']], diag_kind='kde')

# Max limit input
max_limit_input = float(input("Set the maximum limit of carbon emissions per day (gram): "))
# Set the user car's detail
mileage = float(input("Enter your car mileage in km: "))
car_type = input("Enter your car type: ")
car_year = int(input("Enter your car year: "))
fuel_type = input("Enter your car fuel type: ")
car_transmission = input("Enter your car transmission: ")

usercar = car_data.loc[(car_data['CAR TYPE'] == car_type) & (car_data['YEAR'] == car_year) & (car_data['FUEL TYPE'] == fuel_type) & (car_data['TRANSMISSION'] == car_transmission)]

lect = LabelEncoder()
car_data['CAR TYPE'] = lect.fit_transform(car_data['CAR TYPE'])
usercar['CAR TYPE'] = lect.transform(usercar['CAR TYPE'])

ley = LabelEncoder()
car_data['YEAR'] = ley.fit_transform(car_data['YEAR'])
usercar['YEAR'] = ley.transform(usercar['YEAR'])

levc = LabelEncoder()
car_data['VEHICLE CLASS'] = levc.fit_transform(car_data['VEHICLE CLASS'])
usercar['VEHICLE CLASS'] = levc.transform(usercar['VEHICLE CLASS'])

lees = LabelEncoder()
car_data['ENGINE SIZE (L)'] = levc.fit_transform(car_data['ENGINE SIZE (L)'])
usercar['ENGINE SIZE (L)'] = levc.transform(usercar['ENGINE SIZE (L)'])

lecs = LabelEncoder()
car_data['CYLINDERS'] = lecs.fit_transform(car_data['CYLINDERS'])
usercar['CYLINDERS'] = lecs.transform(usercar['CYLINDERS'])

letr = LabelEncoder()
car_data['TRANSMISSION'] = letr.fit_transform(car_data['TRANSMISSION'])
usercar['TRANSMISSION'] = letr.transform(usercar['TRANSMISSION'])

left = LabelEncoder()
car_data['FUEL TYPE'] = left.fit_transform(car_data['FUEL TYPE'])
usercar['FUEL TYPE'] = left.transform(usercar['FUEL TYPE'])

labels = np.array(car_data['CO2 EMISSIONS'])
car_data = car_data.drop('CO2 EMISSIONS', axis = 1)
real = np.array(usercar['CO2 EMISSIONS'])
usercar = usercar.drop('CO2 EMISSIONS', axis = 1)
datalist = list(car_data.columns)
car_data = np.array(car_data)

# Select relevant features for training the model
features = ['YEAR', 'CAR TYPE', 'VEHICLE CLASS', 'ENGINE SIZE (L)', 'CYLINDERS', 'TRANSMISSION', 'FUEL TYPE', 'FUEL CONSUMPTION CITY', 'FUEL CONSUMPTION HWY', 'COMB (mpg)', 'COMB (L/100 km)']
target = 'CO2 EMISSIONS'

train_data, test_data, train_target, test_target = train_test_split(
        car_data, labels, test_size=0.2, random_state=42
        )

# Define Neural Network
model = tf.keras.Sequential([
        tf.keras.layers.Dense(512, activation='relu', input_shape=(len(features),)),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

# Optimizer
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

# Compile the model
model.compile(optimizer=optimizer, loss='mean_squared_error')

model.summary()

# Train the model
history = model.fit(train_data, train_target, epochs=100, verbose=1, validation_split=0.2)

def plot_loss(history):
  plt.plot(history.history['loss'], label='loss')
  plt.plot(history.history['val_loss'], label='val_loss')
  plt.xlabel('Epoch')
  plt.ylabel('Error [CO2 EMISSION]')
  plt.legend()
  plt.grid(True)

plot_loss(history)

prediction = model.predict(test_data)
print(prediction)

# Function to read car data from the CSV database
def read_car_data():
    car_data = {}
    with open('NEW_car_emission_dataset.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            car_type = row['CAR TYPE']
            car_year = int(row['YEAR'])
            vehicle_class = row['VEHICLE CLASS']
            engine_size = float(row['ENGINE SIZE (L)'])
            cylinders = int(row['CYLINDERS'])
            transmission = row['TRANSMISSION']
            fuel_type = row['FUEL TYPE']
            fuel_consumption_city = float(row['FUEL CONSUMPTION CITY'])
            fuel_consumption_highway = float(row['FUEL CONSUMPTION HWY'])
            comb1 = float(row['COMB (L/100 km)'])
            comb2 = float(row['COMB (mpg)'])
            co2_emission = float(row['CO2 EMISSIONS'])
            if car_type not in car_data:
                car_data[car_type] = []
            car_data[car_type].append({
                    'car_year': car_year,
                    'vehicle_class': vehicle_class,
                    'engine_size' : engine_size,
                    'cylinders' : cylinders,
                    'transmission': transmission,
                    'fuel_type': fuel_type,
                    'fuel_consumption_city': fuel_consumption_city,
                    'fuel_consumption_highway': fuel_consumption_highway,
                    'comb1' : comb1,
                    'comb2' : comb2,
                    'co2_emission': co2_emission
            })
    return car_data

# Function to calculate carbon emissions
def calculate_carbon_emissions(car_type, car_year, mileage, car_data, emission):
    warnings.simplefilter(action='ignore', category=FutureWarning)

    if car_type in car_data:
        cars = car_data[car_type]
        for car in cars:
            if car['car_year'] == car_year:
                #co2_emission = car['co2_emission']
                #total_emissions = mileage * co2_emission
                total_emissions = mileage * emission
                return total_emissions
    return None

def display_warning(carbon_emission, max_limit):
    if carbon_emission is not None:
        if carbon_emission > max_limit:
            print("Warning: The carbon emissions of your car exceed the maximum limit.")
        else:
            carbon_remainder = max_limit - carbon_emission
            print(f"Your daily carbon emission remaining: {carbon_remainder} gram")

def read_alternative_data(mileage):
  alternative_emission = {}
  with open('Alternatives.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            trans_type = row['Transportation']
            trans_emission = int(row['CO2 Emission (g/km)'])
            alternative_emission[trans_type] = trans_emission * int(mileage)
  return alternative_emission

# Function to recommend alternatives based on their emissions
def recommendation(alternative_emission, max_limit):
    # Sort the alternative emissions dictionary by emission values in ascending order
    sorted_alternatives = sorted(alternative_emission.items(), key=lambda x: x[1])

    # Initialize a list to store recommended alternatives
    recommended_alternatives = []

    # Iterate over the sorted alternatives and check if their emissions are within the maximum limit
    for alternative, emission in sorted_alternatives:
        if emission <= max_limit:
            recommended_alternatives.append(alternative)

    # Display the recommended alternatives
    if recommended_alternatives:
        print("\nYou have exceeded the maximum limit of carbon emissions.")
        print("\nHere are some alternative transportation options with lower CO2 emissions.")
        print("Recommended alternatives:")
        for alternative in recommended_alternatives:
            alternative_emission_str = str(alternative_emission[alternative])
            print("- " + alternative + " with total emission " + alternative_emission_str + " gram")
    else:
        print("No alternatives found within the maximum limit.")

# Use the trained model for prediction
def predict(car_data):
  prediction = model.predict(usercar)
  carbonpred = prediction[0][0]

  print(f"\nPredicted CO2 Emission: {carbonpred} g/km")

  # Calculate carbon emissions
  carbon_emission = calculate_carbon_emissions(car_type, car_year, mileage, car_data, carbonpred)
  if carbon_emission is not None:
      print(f"\nTotal carbon emissions: {carbon_emission} gram.")

  try:
      if carbon_emission is not None:
          max_limit = float(max_limit_input) if max_limit_input else None

          # Display a warning if emissions exceed the maximum limit
          display_warning(carbon_emission, max_limit)

          # Recommend alternatives based on their emissions
          if carbon_emission > max_limit:
              alternative_emission = read_alternative_data(mileage)
              recommendation(alternative_emission, max_limit)
      else:
          print("Error: No emissions data found for the provided vehicle information.")
  except ValueError:
        print("Error: Invalid input. Please enter numeric values for mileage, vehicle year, and maximum limit.")

# Main function
def main():
    # Read vehicle data from the CSV database
    car_data = read_car_data()

    # Run the ML model training and prediction
    predict(car_data)

# Run the main function
main()