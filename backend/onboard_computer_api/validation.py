from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

compute_odds_schema = {
    'type': 'object',
    'properties': {
        'countdown': {'type': 'number'},
        'bounty_hunters': {"type": "array",
                           "items": {
                               "type": "object", 'properties': {
                                   'planet': {'type': 'string'},
                                   'day': {'type': 'integer'}
                               }, 'required': ['planet', 'day']
                           }}
    },
    'required': ['countdown', 'bounty_hunters'],
}
class ValidateComputeOddsInputs(Inputs):
    json = [JsonSchema(schema=compute_odds_schema)]

def validate_compute_odds(request):
    inputs = ValidateComputeOddsInputs(request)
    if inputs.validate():
        return None
    else:
        return inputs.errors