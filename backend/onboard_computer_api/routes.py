import flask
from flask import Blueprint, current_app, jsonify

from onboard_computer_api.controller import get_universe_routes
from onboard_computer_api.invalid_usage import InvalidUsage
from onboard_computer_api.odds_computer import OddsComputer
from onboard_computer_api.validation import validate_compute_odds

api = Blueprint('api', __name__)

@api.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
   response = jsonify(error.to_dict())
   response.status_code = error.status_code
   return response

@api.route('/compute_odds', methods=["POST"])
def compute_odds():
    errors = validate_compute_odds(flask.request)
    if errors is not None:
        print(errors)
        raise InvalidUsage(errors)

    start_parameters = current_app.config['START_PARAMETERS']
    empire_parameters = flask.request.get_json()
    calculator = OddsComputer(start_parameters, empire_parameters, get_universe_routes())
    answer = str(calculator.get_success_rate())
    return answer
