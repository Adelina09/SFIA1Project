# Holiday Destination Ideas

Projet aiming to suggest a holiday destination idea based on user input of activities they have planned. 
## Index

1. [Brief](#brief)
2. [Trello Board](#trello)
3. [Risk Assessment](#riskassessment)

4. [Architecture](#architecture)
   + [Entity Relationship Diagrams(ERDs)](#ERD)
   + [Architecture Diagram](#architecturediagram)
   
5. [Testing](#testing)

6. [Deployment](#deployment)

7. [Front End Design](#design)

8. [Future Improvements](#improvements)


<a name="brief"></a>
## 1. The Brief 
   The project intends to fulfill the brief provided in week one of the training.
   The requirements include: 
+ Delivering a CRUD application by making use of the tools, methodologies and technologies that encapsulate all core modules covered during training;
+ Having a minimum of 2 tables within the database;
+ Having a functioning front-end website and integrated APIs using Flask.

This specific application lets the user input a number of preferred holiday activities, based on which they will be provided with a list of suggested holiday destinations. It is a customisable environment, and lets the user have full control over the activities chosen. 

<a name="trello"></a> 
## 2. Trello Board

As shown in  the figure below, Trello has been used to keep track of the progress across its duration.

The project started by defining the user stories, which have been added as a reminder of the project scope and its deliverables, hence serving the role of product backlog as well. 

The project  itself has been split in 4 major sprints(lasting a week each). In order to make tracking of progress easier and to monitor the time left until the deadline, the sprints have been assigned different colours starting with green, which represents the first sprint and ending with red, which represents the last sprint. The image below represents the Trello board at the beginning of the project, right after the sprints have been divided into individual tasks. 

![alt text][trello1]
 
[trello1]:  https://i.imgur.com/pMVApzY.png " Initial Trello Board"
 
As the weeks went by, the tasks started to shift across into the Progress and eventually Done tab. I have chose to include only the initial and final board as the sprint differentiation has been made clear with the aid of colour coding. 

The project has been considered complete and ready to be delivered when all tasks have moved into the Done tab, leaving no task left unfinished. These tasks tasks themselves have been considered done when they fulfill the user stories. A tab that has appeared throughout the project has been the Bugs tab, where various issues have been added. The image below represents the finished project, just before delivery.
 
 ![alt text][trello2]
 
[trello2]:  https://i.imgur.com/9lD41TG.png " Final Trello Board"
 
 
 <a name="riskassessment"></a>
 ## 3. Risk Assessment
 
| Risk ID       | Risk Description   | Mitigation     | Likelyhood of occurrence |  Possible Impact  | Impact at occurrence| 
|:-------------:|:------------------:|:--------------:|:------------------------:|:-----------------:|:-------------------:|
| 1    | Unstable internet connection | Work on small, individual parts of the project, to avoid being dependent on the internet connection. When unavailable, work on the project management part. | 4 | Not being able to deliver the project in time, pushing back some of the tasks that require internet.| 3|
| 2    | Data compromised on the workstation | Make frequent back ups of the project, set up an account password, and ensure computer is locked when leaving the station.  | 2 | Having to start the project/parts of the project from scratch, missing out on possible crucial information previously included| 4|
| 3    | Security breach of the databases | Ensure a strong password is selected, encrypt the data, and hash the passwords. | 3 | Depending on what stage of the process it occurs at, its impact varies. If it happens in the first half of the project, may consist in small delays, if it's happening in the second half of the project, it might push back the other steps.| 5|
| 4    | Exhausting the free trial offered by GCP | Keep track of all the instances used, making sure to delete/terminate the ones that are not useful for the project, and stopping the instances when not in use. | 1 | Having to start the project/parts of the project from scratch, missing out on possible crucial information previously included| 5 |
| 5    | Difficulty understanding the material  | Pay attention to the material taught in class. Follow up on the supplemental materials provided, and practice when given the opportunity. Always ask for help if needed. | 3 | Delivering a poor project due to the lack of not understanding the brief/ not knowing how to execute the project| 4|
| 6    | Not being able to complete the project in time | Keeping track of the project management timeline using the Trello board, making sure to complete/start at least a task daily.  | 2 | Falling behind with the weekly tasks, randomly working on different other parts of the project, not boxing off particular sections of it | 5|

 
 
 
<a name="architecture"></a>
## 4. Architecture

<a name="ERD"></a>
### Entity Relationship Diagrams (ERDs)
 The project started by considering 3 linked tables, 2 main and one joining, in a MYSQL database. The joining table would consist of the IDs of the other 2 tables in order to describe a many to many relationship between the 2 main tables. The 2 main initial tables are represented in the figure below.  

 ![alt text][ERD]
 
[ERD]:  https://imgur.com/Kzn5qJk.png "ERD Diagram"


 As the project has advanced, it has been observed that the second table needed to comprise of more columns, in order to deliver the desired front end of the application. Hence, three new columns have been inserted: description(containing the description of the location), picture(containing a hyperlink to an image of the location) and finally an activity comlumn(containing possible activities that can be undertaken in the selected location).
 
 This last column has been used as the link between the 2 tables, making the third table impractical, hence reducing the initial relationship from a many-to-many to a one-to-many relationship as observed in the figures below. 

![alt text][ERDNew]

[ERDNew]: https://i.imgur.com/pWTDKxl.png  "New ERD Diagram"



 


<a name="#architecturediagram"></a>
### Architecture Diagram


--Insert Architecture Diagram Here--



<a name="testing"></a>
## 5. Testing

The application has been tested using pytest. The unit testing conducted includes URL as well as database testing. The first image represents the test coverage in just the URL case, where a success of 46% can be observed. A number of 4 functions have been tested, these including checks for existing as well as checks for inexistent pages. 

![alt text][testingURL]
 
[testingURL]:  https://i.imgur.com/hbrzU4E.png "ULR Testing coverage"

The database testing has then been added to the test file, performing the tests on the select, insert and delete functions, adding another 3 test functions to the file. It can be observed that the coverage percentage has now dropped to 38%. This is believed to have happened due to the addition of new libraries that need to be tested, and hence due to a much larger testing environment. 

![alt text][testing]
 
[testing]:  https://i.imgur.com/88Z5Byu.png "Testing coverage after adding the DB testing"


<a name="deployment"></a>
## 6. Deployment

The deployment of this application has been done through the use of Jenkins Pipeline. A GitHub webhook has also been used, to ease the build process when changes are made to the GitHub repository. With the use of the Pipeline, Jenkins is able to install all the necessary packages needed to run the application, wait for the packages to be installed, deploy the application as a service and finally perform the tests mentioned in the section above. The results of these tests are printed in the console output of Jenkis, giving the user the ability to improve the testing stage if results are not satisfactory.



