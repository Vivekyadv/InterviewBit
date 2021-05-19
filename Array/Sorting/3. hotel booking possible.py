# Given arrival and depart of customers, and total no of rooms in hotel
# you have to check if there are enough rooms to satisfy demands in hotel

# Algorithm:
# step 1: create time = arrival and depart
# step 2: sort time
# step 3: for every t in time, 
#           count += 1 if t is arrival
#           count -= 1 if t is depart
#           *at any instant if count > no_of_rooms then return False

# def hotelBooking(arival,depart,no_of_rooms):
#     time = arival + depart
#     time.sort()
#     count = 0
#     for t in time:
#         if t in arival:
#             count += 1
#         if t in depart:
#             count -= 1
#         if count > no_of_rooms:
#             return False
#     return True


def hotelBooking(arival, depart, rooms):
    time = [(t,1) for t in arival] + [(t,0) for t in depart]
    time.sort()
    count = 0
    for t in time:
        if t[1] == 1:
            count += 1
        else:
            count -= 1
        if count > rooms:
            return False
    return True

arrival = [1,2,3]
departed = [2,3,4]
rooms = 1
print(hotelBooking(arrival,departed, rooms))

