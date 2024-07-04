# task 1 

#sets with destinations for each airline
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}


# function to determine similar destinations

def similar_dest(our_routes, competitor_routes):
    sim_routes = []
    sim_routes = our_routes.intersection(competitor_routes)
    print(f"Similar destinations:")
    for i, sim in enumerate(sim_routes):
        print(f"{sim}") 

#function for unique destinations in our airline        
def unique_dest(our_routes, competitor_routes):
    unique_routes = our_routes - competitor_routes
    print(f"\nUnique destinations:")
    for unique in unique_routes:
        print(f"{unique}") 


#function for both combined unique destinations 
def neither_share(our_routes, competitor_routes):
    unique_routes_one = our_routes - competitor_routes
    unique_routes_two = competitor_routes - our_routes
    unique_routes_combined = unique_routes_one | unique_routes_two
    print(f"\nUnique destinations both airlines:")
    for unique in unique_routes_combined:
        print(f"{unique}") 

similar_dest(our_routes, competitor_routes)
unique_dest(our_routes, competitor_routes)
neither_share(our_routes, competitor_routes)




