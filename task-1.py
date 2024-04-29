


our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes.intersection(competitor_routes)
print("common destinations:", common_destinations)


unique_to_our_airline = our_routes.difference(competitor_routes)
print("destinations unique to our airline:", unique_to_our_airline)


unique_destinations = our_routes.symmetric_difference(competitor_routes)
if not common_destinations:
    print("No common destinations.")
else:
    print("unique destinations between both airlines:", unique_destinations)
