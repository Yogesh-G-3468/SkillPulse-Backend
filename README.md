# Skillpulse.app

## Overview
Skillpulse is an application that allows students to assess their employment readiness and academic statistics by taking tests in subjects they have studied. This readme provides instructions on how to set up and use the Skillpulse application on your local system.


![image](https://github.com/DeexithParand2k2/Skillpulse.app/assets/82024077/5ba6b435-7fcf-4617-ac8e-0cdc3d78a3e8)



## Getting Started

### Cloning the Repository
1. Clone the Git repositories for both the frontend and backend of the Skillpulse application.

### Backend Setup
2. Open a terminal in the backend directory of the cloned repository.
3. Install all the required Python packages by running the following command:
   ```shell
   pip install -r requirements.txt
   ```

4. Start the Django server with the following command:
   ```shell
   python manage.py runserver
   ```

### Frontend Setup
5. Ensure you have Node.js installed on your system.
6. Open a terminal in the frontend directory of the cloned repository.
7. Install all the required Node.js packages and dependencies by running:
   ```shell
   npm install
   ```

8. Start the application with:
   ```shell
   npm start
   ```

### Using the Application
9. After starting the application, you will be directed to the landing page.
10. Click on the "Login" button in the top right corner to access the Log in/Sign up page.
11. Sign up with your details (Username, Email, and Password), then log in using your credentials to access the dashboard.

    
![image](https://github.com/DeexithParand2k2/Skillpulse.app/assets/82024077/ead3cf6d-e53a-44d4-88b7-457b505ac18c)



## Application Features

### Dashboard
- The dashboard has two segments: analytical display and rating display.
- Both segments initially display empty data.
- You can select "Test Type" and "Module" from dropdown menus.

  
![image](https://github.com/DeexithParand2k2/Skillpulse.app/assets/82024077/7672888b-bbc6-4336-a5bd-a4bebec236df)


- To take a test, click the "Take Test" button at the bottom of the page.
- Choose a module (M1 or M2) to view available subjects.
- Select a subject and choose between "Entry Test" and "Exit Test" (Note: You must complete Entry Test to access Exit Test).
- After selecting Entry Test, click the "Take Test" button to attempt the test.

  
![image](https://github.com/DeexithParand2k2/Skillpulse.app/assets/82024077/4da362c7-8559-4817-afd7-b7cc23e64352)


- Complete the Multiple Choice Questions (MCQs) and click "SUBMIT."

  
![image](https://github.com/DeexithParand2k2/Skillpulse.app/assets/82024077/e7eae48a-83d3-438b-a6a8-8df9ed3aa6aa)


- The analytical display will show a bar chart for the attempted test, and the ratings display will show ratings for subtopics.
- Repeat the process for all subjects in both modules and for Exit tests.

  
![image](https://github.com/DeexithParand2k2/Skillpulse.app/assets/82024077/e7ad21e5-dab2-4032-ab8c-907a4a43d473)

![image](https://github.com/DeexithParand2k2/Skillpulse.app/assets/82024077/d9c46d13-910f-4630-9b6e-2c51a33ab9f5)

![image](https://github.com/DeexithParand2k2/Skillpulse.app/assets/82024077/b2e9012e-4619-4560-97cf-84b6a4f8afd8)

### Tests Taken
- This page displays your test history in a tabular format, showing MODULE, SUBJECT, TEST TYPE, DATE, and TIME for each test.
![image](https://github.com/DeexithParand2k2/Skillpulse.app/assets/82024077/22585b33-5d05-4ad1-aff9-81d97369e42b)

### Employment DB
- This page contains data of seniors who got placed in previous years, filterable by CTC (Cost to Company).
- Data is displayed in a tabular format with columns for Profile, Name, Company, CTC (LPA), and EIS Score.

  
![image](https://github.com/DeexithParand2k2/Skillpulse.app/assets/82024077/d80a68fa-a6f5-4e76-ba0f-c0f6c2474767)


### Leaderboard
- The leaderboard ranks students based on their performance and scores.
- You can view your overall rank and compare scores with other students for all subjects in both modules and tests.

  
![image](https://github.com/DeexithParand2k2/Skillpulse.app/assets/82024077/d4c52876-46b6-4971-ac09-502aebebdbd2)


### Resources
- The Resources page allows you to select a subject to access links, information, or materials related to that subject.

![image](https://github.com/DeexithParand2k2/Skillpulse.app/assets/82024077/2ef25fba-04cc-4429-b9f7-788a8b600d29)

## Conclusion
Skillpulse is a comprehensive application for assessing employment readiness and academic performance. Use the provided instructions to set up and explore its features.









