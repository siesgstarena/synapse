# Arena 2.0 Recommendation-system
A Recommendation Service developed in python by CodeChef Arena Members, for the Arena Platform, this service will currently recommend users with new competitive programming question based on their skill level, from all the questions available on the arena.
This sevice can be easily expanded to also recommend other things such as blogs, we can easily do that by adding a single folder in the `routes` folder (The structure of the routes folder is explained below)
- How it works

```
The recommendation will be independent of the type of problem, it will be completely dependent on the language in which the user has 
solved the previous problem.
The recommendation system (success score) is based on formula:- 1/(1+TS-PS);
where TS=successful submissions/total submissions,
      PS=successful submissions for a particular language/total submissions for particular language
The dataset received in json form is converted into csv format first. The only columns useful here are the column of problem_id and 
the submission language. Then the formula decided is applied over the data, then the data needs to be standardized, a new csv of 
success score is generated.
For training the model ,KNN algorithm is used.
Based on the calculated success score for a particular problem, the user will be recommended a problem having a similar success score. 
So the user will be recommended with problems having a similar success score to that of the previous problem solved based on language 
used, irrespective of type of problem.
```
- Project structure
```
The current recommendation is only considering the language of solution which user has submitted.
The project is divided in following structure:

.github : This module ensures that the syntax is followed and it builds docker image.

config : This module handles the keys,urls, mail operations

db : This module has the information related to database, database used here is mongodb.

helper: The current recommendation service is for recommending new problems to arena user, the problem 
module has files related to problem recommendation only. In future a new module can be added to the 
helper. e.g. Blog recommendation service.

    1. raw: This module converts json data into csv
    2. preprocess: This module performs the basic operations on the data. e.g. Applies the recommendaton formula over the 
       data.
    3. trainer: This module trains the model using KNN algorithm
    4. similarities: This module finds problems having similarity between them and stores in database.
    5. recommend: This module uses fireball database to recommend a problem to arena user.

middleware : This module ensures authorize access to recommendation service.

ml : This module includes all the pre-processing and machine learning files

model : This module consists of database schema.

routes : This module authorizes login and logout credentials.

services : This module loads or save ml model to database.

storage : This module consists of firebase configuration

test : This module includes of unit and integrated testing files.

utils : This module consists of mail, load or save model files.

```
- Get Started

```
virtualenv env
.\env\Scripts\activate.ps1
pip install -r requirements.txt
```

- Hook install
```
pre-commit install
```

- Hook run command
```
pre-commit run --all-files
```

- Lint

```
pylint $(git ls-files '*.py')
flake8 $(git ls-files '*.py')
```

- Format
```
black .
```

- Spin Docker container for development
```
 docker compose -f .\docker-compose-dev.yml up
```

- Remove chache and build
```
docker compose -f .\docker-compose-dev.yml up --build --remove-orphans --force-recreate
```
