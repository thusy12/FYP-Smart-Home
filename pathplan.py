import networkx as nx
import matplotlib.pyplot as plt
import voice_assistant
import speech_recognition as sr
# import socket
import pyttsx3
import math
import room
from multiobjectdetandtrack import object_coords


word=voice_assistant.recog()

# Define the room layout
room_graph = nx.Graph()
roomedges=room.mappingpart()[0]
coordinatesxy=room.mappingpart()[1]
# weight=room.mappingpart()[2]

# print('weighttttttttttttttt')
# print(weight) 

for i in roomedges:
    room_graph.add_edge(i[0], i[1], weight=i[2])

# print(room_graph.add_edge(i[0], i[1], weight=i[2]))
print('cccccccccccccccccccc')
print(coordinatesxy)
# print(coordinatesxy[start_location])
print(room_graph)
print(roomedges)
print('cccccccccccccccccccc')


# room_graph.add_edge('table', 'kitchen', weight=4)
# room_graph.add_edge('table', 'washroom', weight=2)
# room_graph.add_edge('kitchen', 'washroom', weight=1)
# room_graph.add_edge('kitchen', 'nowords', weight=1)
# room_graph.add_edge('kitchen', 'bat', weight=3)
# room_graph.add_edge('washroom', 'bat', weight=4)
# room_graph.add_edge('nowords', 'bat', weight=1)

print('bbbbbbbbbbbbbb')
print(roomedges[0])
print(roomedges[0][2])
print('bbbbbbbbbbbbbbbbbbb')

room_positions={}
# room_positions = {'table': tuple([0, 0]), 'kitchen': tuple([2, 2]), 'washroom': tuple([2, 0]), 
#                 'nowords': tuple([4, 0]), 'bat': tuple([4, 2]), }
for i in coordinatesxy:
    key=i[0]
    # print(i)
    x=i[1]['coords'][0]
    y=i[1]['coords'][1]
    room_positions.update({key: tuple([x,y])})

# print('aaaaaaaaaaaaaaaaaaaaaaaaaa')
# print(room_positions)
# print('aaaaaaaaaaaaaaaaaaaaaaaaaa')


# room_positions = {'table': tuple([0, 0]), 'kitchen': tuple([2, 2]), 'washroom': tuple([2, 0]), 
#                 'nowords': tuple([4, 0]), 'bat': tuple([4, 2]), }

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()
#room_positions = {'a': [0, 0], 'b': [2, 2], 'c': [2, -2], 'd': [4, 0]}
directions = []
# print(weight)
# Define the function to determine the shortest path
def determine_path(start_location, end_location):

    
    #shortest_path = nx.shortest_path(room_graph, source=start_location, target=end_location, weight='weight')
    shortest_path = nx.shortest_path(room_graph, source=start_location, target=end_location, weight=dist)

    #directions = []
    for i in range(len(shortest_path)-1):
        curr_node = shortest_path[i]
        next_node = shortest_path[i+1]
        curr_pos = room_positions[curr_node]
        next_pos = room_positions[next_node]
        delta_x = next_pos[0] - curr_pos[0]
        delta_y = next_pos[1] - curr_pos[1]
        angle = math.degrees(math.atan2(delta_y, delta_x))
        # rounded_angle = ((round(angle / 45) * 45) % 360 + 360) % 360
        actual_angle = (angle % 360 + 360) % 360
        rounded_angle = round(actual_angle, 2)
        print("rounded_angle")
        print(rounded_angle)

        # rounded_angle = round(angle / 45) * 45
        direction = ''
        if rounded_angle >= 0 and rounded_angle < 15:
            direction = 'East'

        elif rounded_angle >= 15 and rounded_angle < 30:
            direction = 'middle between North East and East'
        elif rounded_angle >= 30 and rounded_angle < 60:
            direction = 'North East'
        elif rounded_angle >= 60 and rounded_angle < 75:
            direction = 'middle between North East and North'
        elif rounded_angle >= 75 and rounded_angle < 105:
            direction = 'North'
        elif rounded_angle >= 105 and rounded_angle < 120:
            direction = 'middle between North and North West'
        elif rounded_angle >= 120 and rounded_angle < 150:
            direction = 'North West'
        elif rounded_angle >= 150 and rounded_angle < 165:
            direction = 'middle between North West and West'
        elif rounded_angle >= 165 and rounded_angle < 195:
            direction = 'West'

        elif rounded_angle >= 195 and rounded_angle < 210:
            direction = 'middle between West and South West'
        elif rounded_angle >= 210 and rounded_angle < 240:
            direction = 'South West'
        elif rounded_angle >= 240 and rounded_angle < 255:
            direction = 'middle between South West and South'
        elif rounded_angle >= 255 and rounded_angle < 285:
            direction = 'South'
        elif rounded_angle >= 285 and rounded_angle < 300:
            direction = 'middle between South and South East'
        elif rounded_angle >= 300 and rounded_angle < 330:
            direction = 'South East'
        elif rounded_angle >= 330 and rounded_angle < 345:
            direction = 'middle between South East and East'
        elif rounded_angle >= 345 and rounded_angle <= 360:
            direction = 'Eastt'

        directions.append(direction)
    return shortest_path, directions

# Example usage
start_location = 'person'
end_location = word

print('ssssssssssssssssssssssssssssssssss')
# print(coordinatesxy[start_location])
x1 = object_coords[start_location]['coords'][0]
y1 = object_coords[start_location]['coords'][1]
x2 = object_coords[end_location]['coords'][0]
y2 = object_coords[end_location]['coords'][1]

dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(dist)
print('wwwwwwwwwwwwwwwwwwwwwwwwwwwww')
# print(object_coords[start_location]['coords'][0])

shortest_path, directions = determine_path(start_location, end_location)
nx.draw_networkx_nodes(room_graph, room_positions, nodelist=shortest_path, node_color='r')
#shortest_path = determine_path(start_location, end_location)
print(f"The shortest path from {start_location} to {end_location} is: {shortest_path} with {dist} cm")
print('Directions: ',directions)

# Visualize the room layout and the shortest path
nx.draw(room_graph, room_positions, with_labels=True)
plt.title(f"Shortest path from {start_location} to {end_location}")
#nx.draw_networkx_nodes(room_graph, room_positions, nodelist=shortest_path, node_color='r')
nx.draw_networkx_edges(room_graph, room_positions, edgelist=[(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)], edge_color='r', width=2)
plt.show()

speak("Here the path for your destination")


t=0
rounded_distance = round(dist, 2)
distance=str(rounded_distance)
for i in directions:
    a="you are the "+shortest_path[t]+ ", go "+distance+" cm in the " +i +" direction to " +shortest_path[t+1]
    print(a)
    speak(a)
    t=t+1




