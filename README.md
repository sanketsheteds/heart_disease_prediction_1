# Heart Disease Prediction

Heart Disease Prediction is a Flask web application that predicts the presence of heart disease based on user input. The application utilizes a trained Logistic Regression model to make accurate predictions.

## Features

**Age**: Enter your age in years.

**Gender**: Select your gender from the options (Female or Male).

**Chest Pain**: Rate your chest pain level based on the provided options (No Chest Pain, Low Chest Pain, Moderate Chest Pain, High Chest Pain).

**Resting Blood Pressure**: Enter your resting blood pressure in mmHg (millimeters of mercury).

**Cholestoral**: Enter your serum cholestoral level in mg/dl (milligrams per deciliter).

**Fasting Blood Sugar**: Select whether your fasting blood sugar level is greater than 120 mg/dl (False or True).

**Resting Electrocardiographic Results**: Select the resting electrocardiographic results from the provided options (0, 1, 2).

**Maximum Heart Rate Achieved**: Enter the maximum heart rate achieved during exercise.

**Exercise Induced Angina**: Select whether you experience exercise-induced angina (No or Yes).

**ST Depression**: Enter the ST depression induced by exercise relative to rest.

**Slope**: Select the slope of the peak exercise ST segment from the provided options (0, 1,2).

**Number of Major Vessels**: Select the number of major vessels colored by fluoroscopy from the provided options (0, 1, 2, 3, 4).

**Thal**: Select the type of thalassemia from the provided options (0, Normal Defect, Fixed Defect, Reversible Defect).

## Prerequisites(reqirements.txt)

Flask==2.3.2
scikit-learn==1.2.2
pandas==2.0.0
numpy==1.24.2


## Connect to the EC2 instance

1. Open Git Bash (or your preferred SSH client).

2. Use the cd command to navigate to the directory where the private key file is located.
3. chmod 400 private-key.pem
4. Connect to the EC2 instance using SSH with the following command:

   1. ssh -i private-key.pem ec2-user@<public-ip-address>
   2. Clone the application repository and navigate to the project directory

5. Once connected to the EC2 instance, clone your application repository by running:

   1. git clone <repository-url>
   2. Navigate to the project directory using the cd command:
   3. pip3 install -r requirements.txt
   4. Start the Flask application by executing : python3 app.py

## Conclusion

The Heart Disease Prediction application is tool for predicting the presence of heart disease based on a trained Logistic Regression model. By providing relevant input features such as age, gender, chest pain level, and other vital indicators, users can obtain accurate predictions regarding their heart health.
