import cv2
import numpy as np
import math
# import webcam 
import multiobjectdetandtrack
from multiobjectdetandtrack import object_coords


def mappingpart():
    # Set up the map
    room_map = {}
    coordinatesXY=[]
    # Add nodes for each object
    for label, coord in object_coords.items():
        tempCoor=[]
        room_map[label] = {"coords": coord}
        print(f"Added node for {label} at {coord}")
        tempCoor.extend([label,coord])
        coordinatesXY.append(tempCoor)


    print(room_map)

    mapping=[]
    edges1 = {}

    # Connect nodes with edges based on their spatial relationships
    for label1, node1 in room_map.items():
        
        # print(object_coords['person']['coords'][0])
        # print(object_coords['person']['coords'][1])
        # print(object_coords['chair']['coords'][0])
        # print(object_coords['chair']['coords'][1])
        # mapping=[]
        # edges1 = {}
        
        for label2, node2 in room_map.items():
            if label1 == label2:
                continue
            # dist = np.linalg.norm(np.array(node1["coords"]) - np.array(node2["coords"]))
            # node1_key = tuple(node1["coords"])
            # node2_key = tuple(node2["coords"])

            # print(node1_key)
            # print(label1)
            # print(object_coords['person']["coords"])
            # dist = np.linalg.norm(np.array(node1_key) - np.array(node2_key))
            # calculate the distance between the two points
            
            x1 = object_coords[label1]['coords'][0]
            y1 = object_coords[label1]['coords'][1]
            x2 = object_coords[label2]['coords'][0]
            y2 = object_coords[label2]['coords'][1]
            

            dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            # dist = object_coords[label1]['coords'][0] - object_coords[label2]['coords'][0]
            # print(dist)

            # print(room_map[node1_key]["coords"])

            # dist = np.linalg.norm(np.array(room_map[node1_key]["coords"]) - np.array(room_map[node2_key]["coords"]))

            # dist = np.linalg.norm(np.array(room_map[node1]["coords"]) - np.array(room_map[node2]["coords"]))

            if dist < 1000:
                edges1[label2] = dist
                tempNeigh=[]
                tempNeigh.extend([label1,label2,dist])
                mapping.append(tempNeigh)
                print(f"Added edge from {label1} to {label2} with weight {dist}")
                # print('distancexxxxxxxxxxxxxxxxxxxxx')
                # print(dist)
        room_map[label1]["edges"] = edges1

    # print("mapping")
    # print(mapping)
    # print("edges1")
    # print(edges1)

    # edges1=mapping

    # print("after mapping")
    # print(mapping)
    # print("after edges1")
    # print(edges1)


    # Find the shortest path between two objects

    # start = "person"
    # end = "cell phone"
    # path = [start]
    # while path[-1] != end:
    #     neighbors = room_map[path[-1]]["edges"]
    #     next_node = min(neighbors, key=neighbors.get)
    #     path.append(next_node)

    # print(f"Shortest path from {start} to {end}: {' -> '.join(path)}")


    print('*******************************************')
    # print(mapping[2])
    return mapping,coordinatesXY
    # return mapping,coordinatesXY,dist