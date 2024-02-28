def worldChampionship( pilotList, k):
 for id in k:
    pilot_points = {}
        
    num_position = id[0]
    points = id[1:]

    for value in pilotList:
        for i, pilot in enumerate(value):
            if i < num_position:
                if pilot not in pilot_points:
                    pilot_points[pilot] = 0 
                pilot_points[pilot] += points[i]  

    max_points = max(pilot_points.values())
    
    champions = [pilot for pilot, points in pilot_points.items() if points == max_points]

    print(" ".join(map(str, sorted(champions))))
    

g = 1
p = 3
pilot_list = [[3, 2, 1]]
s = 3
k = [
[3, 5, 3, 2],
[3, 5, 3, 1],
[3, 1, 1, 1]
]

# g = 3
# p = 10
# pilot_list = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#    [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
# ]
# s = 2
# k = [
# [5, 5, 4, 3, 2, 1],
# [3, 10, 5, 1]
# ]

# g = 2
# p = 4
# pilot_list = [
#     [1, 3, 4, 2],
#     [4, 1, 3, 2]
# ]
# s = 2
# k = [
# [3, 3, 2, 1],
# [3, 5, 4, 2]
# ]


worldChampionship( pilot_list, k)


