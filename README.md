# Arena 2.0 Recommendation-system
A recommendation system developed in python for the arena members, that will recommend them new competitive programming question from all the questions available on the arena.
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
    poc: This modules takes up raw data and applies the formula and trains the model,then everything is stored as backup for 
    recommendation in the database
    recommend: This module recommends using the database.
    1. raw: This module converts json data into csv
    2. preprocess: This module performs the basic operations on the data. e.g. Applies the recommendaton formula over the 
       data.
    3. trainer: This module trains the model using KNN algorithm
    4. similarities: This module finds problems having similarity between them and stores in database.
    5. recommend: This module uses fireball database to recommend a problem to arena user.

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
