# Eco-Route
Eco-Route is a mobile application that offers users a tool to calculate their personal transportation carbon emissions, monitor their progress over time, and discover ways to decrease their emissions.

## User Carbon Emissions Prediction and Alternative Transportation Recommendation
This project uses a machine learning model to predict carbon emissions from vehicles based on various features like car type, year, fuel type, and others. When the emissions exceed a specified daily limit, it recommends alternative transportation options with lower carbon emissions to help reduce environmental impact.

The model is built using a Neural Network (implemented with TensorFlow) to predict the CO2 emissions of a car based on its features. It uses historical data to train the model and predict the emissions of the user’s car.

## Why Use a Neural Network?
- Handles Complex Relationships: The model learns complex relationships between features (like car type, engine size, and fuel consumption, etc.) and carbon emissions.
- Predicts Accurate Emissions: The neural network is trained to predict carbon emissions, which is a key factor in managing environmental impact.
- Flexible & Scalable: This model can be adapted to other datasets or extended for different prediction tasks.

## Features
- Predicts the CO2 emissions of a car using machine learning (TensorFlow).
- Compares the predicted emissions with a user-defined daily limit.
- Recommends alternative transportation options based on emissions data if the car's emissions exceed the limit.
- Provides a warning if the car's emissions exceed the set limit.

## Machine Learning Tools and Resources for Developing Eco-Route
1. Code platform: Jupyter Notebook and Google Colaboratory
2. Programming language: Python
3. Library:
   - Python: For implementing the code and machine learning model.
   - TensorFlow: For building and training the neural network model.
   - Scikit-learn: For data preprocessing and model evaluation.
   - Pandas: For handling datasets.
   - Seaborn/Matplotlib: For visualizing data.

## Workflow
1. Data Loading:
   - Load vehicle emission data from the NEW_car_emission_dataset.csv file.
2. Data Preprocessing:
   - Clean and preprocess the data by encoding categorical features using LabelEncoder.
   - Split the data into training and testing sets using train_test_split.
3. Model Development:
   - Build a multi-layer Neural Network using TensorFlow.
   - Train the model with input features such as car type, year, fuel consumption, and engine size.
4. Prediction:
   - The model predicts the CO2 emissions for the given car.
   - Calculate total carbon emissions based on mileage.
5. Emission Evaluation:
   - Compare the predicted emissions with a user-defined limit.
   - Provide recommendations for alternative transportation options if emissions exceed the limit.
6. Model Evaluation:
   - Display training and validation loss.
   - Provide a prediction of total emissions and offer alternative transportation options.

## Example Output
- Input:

  Set the maximum limit of carbon emissions per day (gram): 2000

  Enter your car mileage in km: 15

  Enter your car type: ACURA INTEGRA

  Enter your car year: 1995

  Enter your car fuel type: X

  Enter your car transmission: A4
  
- Output:

  Predicted CO2 Emission: 228.9041290283203 g/km


  Total carbon emissions: 3433.5619354248047 gram.

  Warning: The carbon emissions of your car exceed the maximum limit.
  You have exceeded the maximum limit of carbon emissions.


  Here are some alternative transportation options with lower CO2 emissions.

  Recommended alternatives:

  - Train with total emission 615 gram
  - Electric vehicle with total emission 795 gram
  - Motor cycle with total emission 1545 gram
  - Bus with total emission 1575 gram
 
## File Structure
- NEW_car_emission_dataset.csv: Dataset containing vehicle information, CO2 emissions, fuel consumption, etc.
- Alternatives.csv: Dataset with alternative transportation options and their CO2 emissions.
- (p)_carbon_prediction_and_alternative_transportation.py: Main Python script for training the model, making predictions, and recommending alternatives.

## Metrics Used
- Mean Squared Error (MSE): Measures the average squared difference between predicted and actual emissions.
- Loss Function: The model uses mean squared error for training the neural network.
