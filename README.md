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
