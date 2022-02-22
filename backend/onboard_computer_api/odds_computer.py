class OddsComputer:
    def __init__(self, millennium_falcon_parameters, empire_parameters, db_routes):
        self.planet_connections = db_routes
        self.arrival = millennium_falcon_parameters['arrival']
        self.autonomy = millennium_falcon_parameters['autonomy']
        self.countdown = empire_parameters['countdown']
        self.bounty_hunters = empire_parameters['bounty_hunters']
        self.departure = millennium_falcon_parameters['departure']

    # Function responsible for creating our first route data point that will start the iteration of the main algorithm
    def initRoute(self):
        bounty_hunters_present = 0
        for planet_hunting_day in self.bounty_hunters:
            if (planet_hunting_day['planet'] == self.departure and planet_hunting_day['day'] == 0):
                bounty_hunters_present = 1
        # Standard format of the manipulated object route point
        return {'current_planet': self.departure,
                'next_move_time': 0,
                'nb_bounty_hunters_met': bounty_hunters_present,
                'current_autonomy': self.autonomy}

    def get_next_routes_points(self, route_point):
        next_route_points = []
        # Adding to the next route points all the route points achievable before the countdown and within the ship autonomy
        for connection in self.planet_connections:
            if (route_point['current_planet'] in connection['link'] and route_point['next_move_time'] + connection[
                'travel_time']
                    <= self.countdown and route_point['current_autonomy'] - connection[
                        'travel_time'] >= 0):
                target_planet = list(filter(lambda x: x != route_point['current_planet'], connection['link']))[0]
                # Checking for bounty_hunters
                bounty_hunters_present = 0
                for planet_hunting_day in self.bounty_hunters:
                    if (planet_hunting_day['planet'] == target_planet and planet_hunting_day['day'] == route_point[
                        'next_move_time'] + connection['travel_time']):
                        bounty_hunters_present = 1
                # creating a new route after meeting all the conditions
                next_route_points.append({
                    'current_planet': target_planet,
                    'next_move_time': route_point['next_move_time'] + connection['travel_time'],
                    'nb_bounty_hunters_met': route_point['nb_bounty_hunters_met'] + bounty_hunters_present,
                    'current_autonomy': route_point['current_autonomy'] - connection['travel_time']
                })
        # Adding the case where the ship doesn't move for 1 day to refuel, must take in account the fact that bounty hunters can arrive the next day and countdown is not done
        if route_point['next_move_time'] + 1 <= self.countdown:
            bounty_hunters_present = 0
            for planet_hunting_day in self.bounty_hunters:
                if ((planet_hunting_day['planet'] == route_point['current_planet'] and planet_hunting_day['day'] ==
                     route_point['next_move_time'] + 1)
                        # It seems that if you were on a planet that had bounty_hunters and you refuel on it, you double your chances of getting caught but if we follow the example it's not the case
                        # or (planet_hunting_day['planet'] ==  route['current_planet'] and planet_hunting_day['day'] == route['next_move_time'])
                ):
                    bounty_hunters_present += 1
            next_route_points.append(
                {
                    'current_planet': route_point['current_planet'],
                    'next_move_time': route_point['next_move_time'] + 1,
                    'nb_bounty_hunters_met': route_point['nb_bounty_hunters_met'] + bounty_hunters_present,
                    'current_autonomy': self.autonomy
                }
            )
        return next_route_points

    def pick_best_route(self, possible_route_points, current_day, nb_bounty_hunters_met_on_success):
        next_route_points = []
        # We keep iterating while we still have time to move
        if current_day <= self.countdown:
            for route_point in possible_route_points:
                # If the route has reached the destination we save it and check if it's a better route than the ones we already had
                if (route_point['current_planet'] == self.arrival):
                    # We stop iterating if the route is optimal
                    if (route_point['nb_bounty_hunters_met'] == 0):
                        return 0
                    # Otherwise we check if it's our current best route
                    elif (nb_bounty_hunters_met_on_success is None):
                        nb_bounty_hunters_met_on_success = route_point['nb_bounty_hunters_met']
                    else:
                        nb_bounty_hunters_met_on_success = min(route_point['nb_bounty_hunters_met'],
                                                               nb_bounty_hunters_met_on_success)
                else:
                    # Else if it's time to move we replace the route by its possible moves
                    if (route_point['next_move_time'] == current_day):
                        next_route_points = next_route_points + self.get_next_routes_points(route_point)
                    # Else the route point stays dormant and we pass it along until the day for it to move comes
                    else:
                        next_route_points.append(route_point)
            # We start the next day and loop again on our new routes and dormant (ship traveling) others
            return self.pick_best_route(next_route_points, current_day + 1,
                                        nb_bounty_hunters_met_on_success)
        # We stop iterating once we are past the countdown
        else:
            return nb_bounty_hunters_met_on_success

    def get_route_chances(self, nb_bounty_hunters_met):
        if (nb_bounty_hunters_met is None):
            return 0
        if (nb_bounty_hunters_met == 0):
            return 100
        payload = 0
        for i in range(nb_bounty_hunters_met):
            payload += (9 ** i) / (10 ** (i + 1))
        return 100 - payload * 100

    def get_success_rate(self):
        return self.get_route_chances(self.pick_best_route([self.initRoute()], 0, None))
