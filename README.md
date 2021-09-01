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

To deploy in AWS we need to follow the below steps:
1. Create the Flask Code - app.py
2. Create AWS Account
3. Create EC2 Instance: Here we have chosen a free-tier Ubuntu instance & created a new Key-pair, which we download as a .pem file
4. Download & Install: Putty & WinSCP
5. Generate private key (.ppk) using PuttyGen and the .pem file created while building the EC2 instance
	a. Choose Puttygen 
	b. Choose 'Load'
	c. Choose the '.pem' file generated earlier
	d. Choose 'Save private key'
6. Open WinSCP & connect to the AWS EC2 Instance (available when we click 'Connect' on the EC2 Instance we created earlier). In this case the 'User Name' is "Ubuntu" and the password is the .ppk file generated in the previous step (Advanced-SSH-Authentication-Private Key File).
7. Copy the below files into the EC2 instance (/home/ubuntu) using WinSCP:
	a. model.pkl
	b. requirements.txt
	c. app.py
	d. templates (for the HTML files)
8. Next we connect to the EC2 instance using Putty to install the required libraries
	a. Provide Host Name as the host-name copied earlier from EC2
	b. SSH-Auth-Browse-choose the private key created in step 5
	c. Save-Open
	d. install libraries using the below commands:
		i. 	sudo apt-get update && sudo apt-get install python3-pip (installs python3-pip)
		ii. pip3 install -r requirements.txt (this installs all libraries from requirements.txt)
9. We then need to create an open security group, so that our app is accessible from the outside world. For this we create a new 'Security Group' under 'Network and Security' and choose 'Create Security Group'. Provide basic details like Security Group name and choose the below parameters for a new 'Inbound Rule':
	a. Type: All traffic
	b. Source: Anywhere
10. This security group needs to be assigned to the earlier EC2 instance using 'Network Interfaces'. We need to choose the correct 'Network Interface ID' and choose 'Change Security Groups' from 'Actions'. Choose the earlier created open Security Group and 'Save'
11. Under 'Instance' and for our EC2 instance, the 'Security Group name' should show this newly attached Security Group.
12. Go back to Putty & run: python3 app.py
13. Go to the instance public dns, copy the same & attach :8080 (as we defined this port in app.py run() ) at the end while pasting in browser to access the model instance.

The web-app is hosted at:
ec2-13-52-250-202.us-west-1.compute.amazonaws.com:8080

