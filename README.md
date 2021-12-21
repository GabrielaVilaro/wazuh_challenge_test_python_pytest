Task 3

Define a class called Agent, whose attributes are given by the data file data.json that contains a
list of 5 agents (attached to this document).

It is requested to create the following modules:

agent.py

● Define the Agent class.

● Define the constructor and attributes of the class Agent (according to the data.json items).

● Create a method to show all the attributes of the agent on the screen.

script.py

● Import the Agent class from the agent.py module previously defined.

● Create a method to load the agents data from the data.json file.

● Create a method to write the agents data to an external json file.

● Create a method to print all the agents information.

● Create a main function to do the following:

- Read all agent information from data.json

- Add a new agent to the list (you can choose the attribute values you want).

- Print all agents information (6 items).

- Export the agents information (6 items) to an external json file called output.json (it
must have the same format as data.json)

Task 4: Pytest framework questions

Pytest is the testing framework we use most often. It is very important to know the basic notions
for the subsequent design and implementation.

Tasks

● How would you parameterize tests?

● What are fixtures used for? What is the importance of their scopes?

● Write an example test showing the use of parameterization and a fixture.

Task 5: Pytest tests

One of the most frequent tasks of a QA is the design, implementation and maintenance of tests.

Tasks

Attached to this document you can find the files and database mentioned in the following
exercises:

- 1 Create test(s) to verify that the content of the input files has the expected value.
{'1.txt': 'a', '2.txt': 'b', '3.txt': 'c', '4.txt':’d’, '5.txt': 'e'}
- 2 Read the clients.db database file and create test(s) that check the following:
- Its field structure is as follows: [‘id’, ‘name’, ‘country’, ‘age’].
- The age field of each record is greater than 5.
- There is no null value in a record.
