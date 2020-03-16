# Holiday Destination Ideas

Projet aiming to suggest a holiday destination idea based on user input of activities they have planned. 
## Index

1. [Brief](#brief)
2. [Trello Board](#trello)
3. [Risk Assessment](#riskassessment)

4. [Architecture](#architecture)
   + [Entity Relationship Diagrams(ERDs)](#ERD)
   + [Architecture Diagram](#architecturediagram)
5. [Design Considerations](#design)

6. [Testing](#testing)

7. [Implementations](#implementations)


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

The Project Backlog contais the user and developer stories, as it can be observed in the figure below. Moving on from these, the project has been split in 4 sprints(lasting a week each) represented by various colours; green being the first sprint and red being the last sprint. 

Each sprint has been split into a number of tasks, which have moved across the board from the tasks tab, to in progress and eventually to done. The tasks are considered done when they satisfy the user stories. the image below represents the project status in its fourth week. As it can be observed, most tasks are resting in the done category, with little tasks still left in progress and in the tasks tab. These will get done over the course of the last week of the project. 

The bugs tab at the far right of the project represents the issues encountered throughout the project. They have either been overcome, or the project scope has been changed to fit the minimum viable product. 
   
 
 ![alt text][trello]
 
[trello]:  https://i.imgur.com/ASrA8oe.png "Trello Board"
 
 
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



