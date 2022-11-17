auto = [1, 2, 3, 4]
parkingLot = [1, 0, 4, 1]


def parkCart(cars, parkPlaces):

    if len(cars) != len(parkPlaces):
        return "number of cars and places not same"
    auto.sort()
    parkPlaces.sort()
    maxDifference = 0
    for i in range(len(cars)):
        if maxDifference < abs(cars[i]-parkPlaces[i]):
            maxDifference = abs(cars[i]-parkPlaces[i])
    return maxDifference


min_time = parkCart(auto, parkingLot)
print(min_time)
