# extract a source --> the boarding pass who's source does not exists in all destinations
# extract a destination --> the boarding pass who's destination does not exits in all sources
# extract the middle routes

def findPath(routes):
    reverse_routes = {value:key for key, value in routes.items()}

    # find starting point
    start = None
    for source in routes: # check if the source exists in the list to destinations, if not, it is going to be the source
        if source not in reverse_routes:
            start = source

    print('starting point is ', start)

    # now just traverse from SFO to the end of the route
    itinerary = []
    to = routes.get(start)
    while to is not None:
        itinerary.append([start, to])
        start = to
        to = routes.get(to)

    print(itinerary)

if __name__ == "__main__":
    routes = {"NYC":"MCO", "SFO":"AZX", "AZX":"NYC"}
    findPath(routes)
