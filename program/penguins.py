def find_unavailable_city_for_gas_container(cities, gas_containers, active_connections):
    for each in gas_containers:
        cities.append(each)

    graph = {city: [] for city in cities}
    unavailable_gas_container = []

    for connection in active_connections:
        city_from, city_to = connection
        graph[city_from].append(city_to)

    for gas_container in gas_containers:
        visited = set()
        unavailable_cities = []

        if gas_container not in graph:
            unavailable_gas_container.append([gas_container, cities])
            continue

        queue = [gas_container]
        visited.add(gas_container)

        while queue:

            for neighbor in graph[queue.pop(0)]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        for city in cities:
            if city not in visited and all(city not in container for container in gas_containers):
                unavailable_cities.append(city)

        if unavailable_cities:
            unavailable_gas_container.append([gas_container, unavailable_cities])

    return unavailable_gas_container
