# AWS EC2-Demo
### This project is forked from https://github.com/krishnaik06/Heroku-Demo.
#### I have added more comments and have updated the below Readme to make the files more readable & the overall process more understandable.

In this demonstration, we show how we can deploy a ML model using Amazon EC2 using a Flask WebAPI.

Our ML model is a simple salary predictor and takes the below 3 i/p as features, along with the salary drawn as the target:
1. experience
2. test_score
3. interview_score

This data is availabe in a csv file called 'hiring.csv'.

We then perform a simple LinearRegression to predict salaries for employees for whom we have only the above features, but not the actual salary. Thus, this is a Supervised Learning problem.

Once the model is trained, we save it as a .pkl file using pickle. This model is then deployed on AWS EC2 using a Flask web-service, and a html page is provided to capture the i/p features and display the predicted salary.

Using Flask, we can also execute the model locally and provide the i/p features either using the webpage hosted on our local m/c or by passing the features via a URL request.

The web-app is hosted at:
https://deb-simplesalarypred-demo.herokuapp.com


#### I had faced issues in direct deployment from krishnaik06/Heroku-Demo due to mismatch in sklearn version provided in requirements.txt and the version used to build the model (and saved as model.pkl). I rebuild the model in my local system and provided my local system sklearn version (sklearn.__version__) in requirements.txt
#### The error was as: ModuleNotFoundError: No module named 'sklearn.linear_model.base'
#### This was available in Heroku CLI & I used the command:$ heroku logs --app deb-simplesalarypred-demo to check the deployment logs. Here deb-simplesalarypred-demo is my Heroku app name ####
