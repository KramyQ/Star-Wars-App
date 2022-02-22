I have let the .env in place on git for quick testing purpose of course.

# Backend
## Installation

```python
# run flask server
cd backend
# on Pycharm let it automatically create your virtual environnement
pip install -r .\requirements.txt # You can use a venv
python .\server_start.py       

# run tests
pytest -v
```

## Deployment
I was asked to make a production ready app not to setup the deployment that should be independant of the app implementation, therefor I do not have an uWsgi or yaml config files.
## Structure
- Using a factory to create the app and a config file with the env variables attributions centralised
- api is modularised using flask blueprints
- apis content validated
- db accessed with a controller and ORM
- API in routes.py
- algorithm in odds_computer.py
## Setup
- env file for multi environnement support
- no deployment context
- dependencies in the requirement.txt, setup.py not used as there are no abstract or custom libs needed
- CORS handling
## Testing
- API, validations and logic are unit and integration tested
- Missing db and factory tests (lack of time)
## Security
- DOS handled at a lower level (web server).
- SQL injections can't happen in the current.
app
- Insecure deserialization not happening with a json tested content.
- No uncontrolled data exposure

## Todo(missing)
- DB and starting parameters not validated, algorithm limit values not controlled (+32bits, negative values), input control only done on the client input (API), not the conf and starting files
- enhanced tests with variable parameters for cases
- loging system but here, I couldn't have logged much, ex: IP of the people accessing my public API, and I assume this is automatically done on the web server level.

# FrontEnd
## Installation

```python
# run flask server
cd frontend
npm install
npm run serve  

# run tests
npm run test:unit
```
## Structure
- App structured using vue single page components, and vue components
- Components are not lazy loaded/ condition loaded client side, because of the application scale, but I am sensitive to its usefullness in larger applications.
- Api requests are abstracted using controllers
- User input is content checked client-side

## Setup
- the app was created using vue-cli
- dev dependencies and production dependencies correctly separated, using ESlint and babel
- using vue env variables for the api server adress (and not a relative path to the server in case we want to separate our front and back to support an independant or multiple api servers)

## Testing

## Security
-	Cross site scripting is irrelevant here as users can't post anything
-	No possibility to use stolen cookies or tokens either (no auth)

## Todo(missing)

- Make the frontend Responsive to resizing and different devices.
- Implement EndToEnd testing.
- Factoring the CSS that can be factored.
- Using placeholders in the front to support language change.
- Enhancing unit tests.
- Using a generic object to handle api calls and responses to the user and add a loading state.
- Implement that generic object in the Vuex store.

# CLI

```python
# run cli
cd CLI\dist
give-me-the-odds absolute/path/to/start-parameters.json  absolute/path/to/empire-parameters.json
```
## Things to know :
1. If you're running an other OS than windows 64bits you have to rebuild the exe 
assuming you have python 3^ and pip installed, install what is in the requirement file and delete the dist folder
then run :
```python
cd CLI
#Build the app in a single file with output
pyinstaller --onefile give-me-the-odds.py
```
Don't forget to put your universe.db of choice in the root folder of the exe.

# Algorithme
The thoroughly commented version of the algo is in the backend server
the algorithme uses an object of this sort :
```python
{'current_planet': string,
'next_move_time': number,
'nb_bounty_hunters_met': number,
'current_autonomy': number}
```
We manage collections of this object, and we iterate on every day until we find an optimal path, or the current day of iteration goes beyond the countdown where the planet would be destroyed, and all hopes are doomed.
We don't record the path history and only interest ourselves at snapshots of where the ship could be at a certain time, because it's the only information we need along the number of bounty hunters the ship has met.
# BFS
I am using a BFS(Breadth First Search) Solution 
## Pros:
- quick to imagine and setup.
- good maintenability and readability.
## Cons:
- will likely use more memory depending on the data.
- similar performances to DFS in most cases.

# DFS (Depth First Search) 
## Pros:
- if there is an optimal route in its first iteration the DFS can be more efficient as it would stop iterating when found.
- likely uses less memory depending on the data.

## Cons:
- worse readability and maintainability 
- similar performances to BFS in most
cases.
- doesn't scale well in certain languages
(overflow risk)
