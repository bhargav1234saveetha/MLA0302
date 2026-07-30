routes = {
    "Route A": 100,
    "Route B": 20,
    "Route C": 60
}

for route, passengers in routes.items():
    print(route, "Passengers:", passengers)

busy_route = max(routes, key=routes.get)
print("Send Extra Bus To:", busy_route)
