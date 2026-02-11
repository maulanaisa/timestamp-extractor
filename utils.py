import os
import shutil
import math
import csv

def delete_directory(folder_path):
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)
            print(f"Directory '{folder_path}' and its contents deleted successfully.")
        except OSError as e:
            print(f"Error: {folder_path} : {e.strerror}")
    else:
        print(f"Directory '{folder_path}' does not exist.")

def create_directory(folder_path):
    try:
        os.mkdir(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_path}' already exists.")

def haversine_distance(coordinate_1, coordinate_2):
    R = 6371.0  # Earth radius in kilometers

    lat1, lon1 = map(math.radians, tuple(float(x) for x in coordinate_1))
    lat2, lon2 = map(math.radians, tuple(float(x) for x in coordinate_2))

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

def detect_closest_coordinate(coor_dict:dict, target: tuple):

    closest_key = None
    min_distance = float("inf")

    for key, coor in coor_dict.items():
        distance = haversine_distance(coor, target)
        if distance < min_distance:
            min_distance = distance
            closest_key = key

    return closest_key

def coor_csv_to_dict(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        output = {}
        for csv_row in reader:
            location = csv_row[0]
            coordinate = (csv_row[1], csv_row[2])
            output[location] = coordinate
    
    return output