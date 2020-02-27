def hotel_cost(night):
    return 140*(night)

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    cost = 40*(days)
    if days > 7:
        cost = cost-50
    elif 3 < days < 7:
        cost = cost-20
    return cost

def trip_cost(city, days):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)

print(trip_cost("Tampa",5))

def trip_cost2(city, days, spendin_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spendin_money

print(trip_cost2("Tampa",5,130))
