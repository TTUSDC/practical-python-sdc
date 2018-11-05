## [Week 4] TTU ACM Weekly Software Development Club Short Course - Practical Python

This week, we'll be learning about how to store data for our web application using MongoDB. A practical application of this is for secure user registration and login.

(Read these steps on GitHub as the rendered Markdown is a lot easier to read!)

1. Sign up for MongoDB Atlas here: https://www.mongodb.com/cloud/atlas

2. After registering and logged in, create a new cluster by clicking "Build a Cluster". 
    - It can be hosted on of the cloud providers (Amazon Web Services, Google Cloud Platform or Microsoft Azure), but it's best to go with the free options (several selections) and in a region that is closest to you. 
    - Free selections are denoted by a blue "FREE TIER AVAILABLE" label. 
    - Make no changes to the "Cluster Tier" or "Additional Settings". 
    - Name the cluster whatever you would like; "Cluster0" is the default.
    - Click the green "Create Cluster" button at the bottom of the page. Verify that you are not a robot.
    - After a few minutes, the cluster will be previsioned and ready for use. By default, no databases are available on the cluster but will be automatically created when you make a request to add data to one. 

3. Once the cluster is ready, click on "Security" next to the "Overview" tab.

4. Next, located on the far right, click on the green "+ ADD NEW USER" button. To interact with your cloud instance, you'll need to create a [SCRAM](https://docs.mongodb.com/manual/core/security-scram/) account. Type any username and password combination you would like. Remember it because you'll need to use it in your Python code.

5. Make no changes to the "User Privileges" section and click the green "Add User" button.

6. After you've created an account, in the same "Security" section, click on "IP Whitelist" located right next to "MongoDB Users" on the same page.

7. Again, in the far right, click on the green "+ ADD IP ADDRESS" button. 

8. In the "Whitelist Entry:" field type "0.0.0.0/0". This will allow you to access the database from anywhere. When working on security-centric projects, this is a bad idea because it means anyone, from any computer, on any network can connect to your database, if they know your credentials or are a member of your project context. For learning purposes, this is fine!

9. Next, we'll need to install a dependencies that allows Python to interact with the Atlas MongoDB instance. Thes are pymongo and dnspython. 
  - To install, while in the root directory of the folder that will house your project run `pipenv install pymongo[tls] dnspython`. 
  - This will install the pymongo library with the TLS (Transport Layer Security) extension and dnspython. The tls extension and dnspython are only necessary because our database is hosted on Atlas. The TLS extenstion ensures that our requests and responses are security while dnspython ensures that the URI (Universal Resource Identifier) is reached correctly.

10. Now, we'll need to get the URI to our database. Go back to the "Overview" tab and click "Connect" in the "SANDBOX" container. Under step 3, click "Connect Your Application".

11. The menu will change and 3 new steps will appear. Under the first step click "SRV connection string (3.6+ driver)." Because pymongo uses the 3.6+ driver and our database uses version 4.0.0+, we'll need to use this connection URI. Click "Copy".

12. Create a new file in the same directory and call it `db.py`. Refer to the `db.py` provided in the same folder as this README.md!

13. Here's a quick rundown of what the provided class does.
    1. Import `MongoClient` from the `pymongo` file by typing `from pymongo import MongoClient` (notice the captial M and C in `MongoClient`).
        - `MongoClient` is a class located in the `pymongo` module which will provide us a connection to our database and all of its collections.
        - Think of a database as a closet full of boxes and each of those boxes is full of smaller boxes. The boxes are `collections` which contain interesting data. The boxes inside of those boxes are `documents` (the actual data). 
        - If you are familiar with some flavor of SQL database, a collection is a table, and a document is a row. Data within each document does not need to be uniform. With MongoDB 1 row (document) can contain 5 columns (fields), whereas another row (document) can contain any number of completly unrelated columns (fields).
    2. Create a class called MongoConnector.
    3. In the `__init__` method of the class, create a variable called `uri` and assign it the value of the string you copied from Atlas. Replace the password with your password, to the left of the colon, by using an f-string. Your username should already be filled in.
        - To create an f-string simply type an f at the beginning of the string and pass any variables you would like inside of curly brackets: f"{variable_name}"
    
14. Create a class attribute called db and assign it to an instance of MongoClient. Initialize MongoClient with the uri: `self.db = MongoClient(uri)`. Because this this a class attribute (begins with self), it can be accessed from any method inside of the class.

15. Lastly, copy lines 13 - 32 in the provided `db.py` and change the dictionary defined on line 25 to whatever data you would like. Run the script with `pipenv run python db.py`.
    - Your console should show a weird alphanumeric combination and a dictionary.
    - The first alphanumeric combination is the ObjectId of the document you inserted into the database. This is automatically generated for MongoDB.
    - The dictionary printed is the same document retrived from the database. 

16. Go back to your MongoDB Atlas cluster.
    - Click "collections" and expand "app". "app" is the name of the database. 
    - Click "users". "users" is the name of the collection.
    - You should see 1 document containing the very same data that was printed to the console!

Message me on Slack if you had any issues/have questions!