from onboard_computer_api.odds_computer import OddsComputer

db_extract = [{'link': ['Tatooine', 'Dagobah'], 'travelTime': 6}, {'link': ['Dagobah', 'Endor'], 'travelTime': 4}, {'link': ['Dagobah', 'Hoth'], 'travelTime': 1}, {'link': ['Hoth', 'Endor'], 'travelTime': 1}, {'link': ['Tatooine', 'Hoth'], 'travelTime': 6}]
starting_parameters = {'autonomy': 6, 'departure': 'Tatooine', 'arrival': 'Endor', 'routes_db': 'universe.db'}
empire_parameters = {'countdown': 9, 'bounty_hunters': [{'planet': 'Hoth', 'day': 6}, {'planet': 'Hoth', 'day': 7}, {'planet': 'Hoth', 'day': 8}]}





def test_compute_odds_route_chances(client):
    assert OddsComputer(starting_parameters, empire_parameters, db_extract).get_route_chances(0) == 100
    assert OddsComputer(starting_parameters, empire_parameters, db_extract).get_route_chances(4) == 65.61
    assert OddsComputer(starting_parameters, empire_parameters, db_extract).get_route_chances(None) == 0

def test_compute_odds_get_next_route_points(client):
    assert OddsComputer(starting_parameters, empire_parameters, db_extract).get_next_routes_points(
        {'current_planet': 'Tatooine',
         'next_move_time': 4,
         'nb_bounty_hunters_met': 2,
         'current_autonomy': 6}) == [{'current_planet': 'Tatooine', 'next_move_time': 5, 'nb_bounty_hunters_met': 2, 'current_autonomy': 6}]

    assert OddsComputer(starting_parameters, empire_parameters, db_extract).get_next_routes_points(
        {'current_planet': 'Tatooine',
         'next_move_time': 0,
         'nb_bounty_hunters_met': 0,
         'current_autonomy': 6}) == [{'current_planet': 'Dagobah', 'next_move_time': 6, 'nb_bounty_hunters_met': 0, 'current_autonomy': 0}, {'current_planet': 'Hoth', 'next_move_time': 6, 'nb_bounty_hunters_met': 1, 'current_autonomy': 0}, {'current_planet': 'Tatooine', 'next_move_time': 1, 'nb_bounty_hunters_met': 0, 'current_autonomy': 6}]

def test_compute_odds_integration(client):
    assert OddsComputer(starting_parameters, empire_parameters, db_extract).get_success_rate() == 90

db_extract2 = db_extract.copy()
starting_parameters2 = starting_parameters.copy()
empire_parameters2 = empire_parameters.copy()
empire_parameters2['countdown'] = 0

def test_compute_odds_integration_with_limit_data(client):
    assert OddsComputer(starting_parameters2, empire_parameters2, db_extract2).get_success_rate() == 0
    empire_parameters2['countdown'] = 10
    assert OddsComputer(starting_parameters2, empire_parameters2, db_extract2).get_success_rate() == 0

