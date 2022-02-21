# Backend
## Installation

```python
# run flask server
cd backend
pip install -r .\requirements.txt
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
- db accessed with a controller (ORM not used)
## Setup
- env file for multi environnement support
- no deployment context
- dependencies in the requirement.txt, setup.py not used as there are no abstract or custom libs needed
## Testing
- API, validations and logic are unit and integration tested
- Missing db and facory tests (lack of time)
## Security
- DOS handled at a lower level (web server).
- SQL injections can't happen in the current.
app
- Insecure deserialization not happening with a json tested content.
- No uncontrolled data exposure

## Todo(missing)
- DB and starting parameters not validated
- Enhanced tests with variable parameters for cases
- loging system but here, I couldn't have logged much, ex: IP of the people accessing my public API, and I assume this it automatically done on the web server level.

# FrontEnd
## Installation

```python
# run flask server
cd frontend
npm install
npm run serve  

# run tests
pytest -v
```
## Structure
- App structured using vue single page components, and vue components
- Components are not lazy loaded/ condition loaded client side, because of the application scale, but I am sensitive to its usefullness in larger applications.
- Api requests are abstracted using controllers
- User input is content checked client-side

- API in routes.py
- algorithme in odds_computer.py
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
cd frontend
```

# Algorithme
## BFS
I am using a BFS(Breadth First Search) Solution 
# Pros:
- quick to imagine and setup.
- good maintenability and readability.
# Cons:
- will likely use more memory depending on the data.
- similar performances to DFS in most cases.

## DFS (Depth First Search) 
# Pros:
- if there is an optimal route in its first iteration the DFS can be more efficient as it would stop iterating when found.
- likely uses less memory depending on the data.

# Cons:
- worse readability and maintainability 
- similar performances to BFS in most
cases.
- doesn't scale well in certain languages
(over flow risk)
