from flask import Flask, request

from onboard_computer_api.validation import validate_compute_odds

app = Flask(__name__)


def test_invalid_types_are_rejected(create_valid_compute_odds_request):
   json_input = {
  "countdown": 10,
  "bounty_hunters": [
    {"planet": "Hoth", "day": 6 },
    {"planet": "Hoth", "day": 'zz' },
    {"planet": "Hoth", "day": 7}
  ]
}
   with app.test_request_context('/', json=json_input):
       errors = validate_compute_odds(request)
       assert errors is not None


def test_missing_required_params_is_rejected(create_valid_compute_odds_request):
   json_input = {
  "countdown": 10,
  "bounty_hunters": [
    {"planet": "Hoth", "day": 6 },
    {"planet": "Hoth", "day": 7 },
    {"planet": "Hoth"}
  ]
}

   with app.test_request_context('/', json=json_input):
       errors = validate_compute_odds(request)
       assert errors is not None


def test_valid_is_accepted(create_valid_compute_odds_request):
   json_input = {
  "countdown": 10,
  "bounty_hunters": [
    {"planet": "Hoth", "day": 6 },
    {"planet": "Hoth", "day": 7 },
    {"planet": "Hoth", "day": 8 }
  ]
}
   with app.test_request_context('/', json=json_input):
       errors = validate_compute_odds(request)
       assert errors is None