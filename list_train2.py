# Training List 
# Sort smallest value
"""
def minimum (distances_A):
    mini :float = distances_A[0]
    for i  in range(len(distances_A)):
        if distances_A[i] <= mini:
            mini = distances_A[i]
            position = i
    return(mini,position)


chauffeurs = ["Pierre" , "Paul", "Marie", "Patrick" , "Alex" , "Laura" , "Julie"]
distances = [1.5 , 2.2, 0.4 , 0.9 , 7.1 , 1.1 , 0.6]
plus_proche = minimum(distances)
print (f"le chauffeur le plus proche est {chauffeurs[plus_proche[1]]}  et sa distance est {plus_proche[0]} km")
"""

def plus_Proche (voitures_F):
    mini = voitures_F [0][1]
    for i in range(len(voitures_F)):
        if voitures_F[i][1] <= mini:
            mini = voitures_F [i][1]
            position = i
    return (position)


voitures = [
    ["Pierre",1.5] ,
    ["Paul",2.2]  , 
    ["Marie",0.4]  , 
    ["Patrick",0.9] , 
    ["Alex",7.1] , 
    ["Laura",1.1] , 
    ["Julie",0.6]
]
proche = plus_Proche (voitures)
print (f"le chauffeur le plus proche est {voitures[proche][0]}  et sa distance est {voitures[proche][1]}  km")