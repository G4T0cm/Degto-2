import os
import subprocess 
import sys
import time
from tqdm import tqdm
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
prGreen("""\
 _____             _         ___    ___  
 |  __ \           | |       / _ \  |__ \ 
 | |  | | ___  __ _| |_ ___ | (_) |    ) |
 | |  | |/ _ \/ _` | __/ _ \ \___/    / / 
 | |__| |  __/ (_| | || (_) |_____|  / /_ 
 |_____/ \___|\__, |\__\___/        |____|
               __/ |                      
              |___/                       
                    """)
prGreen("Degtoº2 2.0 VERSION ")
print (" ")
print (cyan+b+"              [[ IMAGE GPS EXTRACTOR & GEO LOCATOR ]]"+b+gren)
print (" ")
prYellow("--Created by G4T0--")
print (" ")
prRed("Path example: /home/kali/Desktop/image.jpg")




import os
import subprocess
import json
import importlib


# Check if the requirements file exists
if os.path.exists("requirements.txt"):
    # Check if the user previously said they don't want to install the requirements
    if os.path.exists("install_requirements.json"):
        with open("install_requirements.json", "r") as f:
            install_requirements = json.load(f)
            if not install_requirements['install']:
                install = False
            else:
                install = True
    else:
        install = None

    # Ask the user if they want to install the requirements
    if install is None:
        print (" ")
        print (" ")
        install = input("Install the requierements? REMEMBER TO START PROGRAM AGAIN AFTER INSTALLATION (y/n) ") == "y"
        with open("install_requirements.json", "w") as f:
            json.dump({'install': install}, f)

    # Install the requirements
    if install:
        try:
            import geopy
        except ImportError:
            subprocess.run(["pip", "install", "-r", "requirements.txt"])
            importlib.reload(geopy)
            print("Please execute the program again")
        else:
            prGreen("geopy is already installed.")
            prGreen("piexif is already installed.")
            prGreen("tqdm is already installed.")

import re
from geopy.geocoders import Nominatim
import piexif

def get_location(image_path):
    exif_dict = piexif.load(image_path)
    gps_info = exif_dict.get("GPS", None)
    if gps_info:
        lat_ref = gps_info.get(piexif.GPSIFD.GPSLatitudeRef, None)
        lat = gps_info.get(piexif.GPSIFD.GPSLatitude, None)
        lon_ref = gps_info.get(piexif.GPSIFD.GPSLongitudeRef, None)
        lon = gps_info.get(piexif.GPSIFD.GPSLongitude, None)

        if lat and lon:
            lat = [x[0] / x[1] for x in lat]
            lat = lat[0] + lat[1] / 60 + lat[2] / 3600
            if lat_ref == 1:
                lat = -lat

            lon = [x[0] / x[1] for x in lon]
            lon = lon[0] + lon[1] / 60 + lon[2] / 3600
            if lon_ref == 1:
                lon = -lon

            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.reverse(f"{lat}, {lon}", exactly_one=True)
            address = location.raw["address"]
            country = address.get("country", "")
            city = address.get("city", "")
            street = address.get("road", "")
            
            prPurple(f"Country: {country}")
            prYellow(f"City: {city}")
            prCyan(f"Street: {street}")
        else:
            print("There is no GPS metadates in the image")
    else:
        print("There is no GPS metadates in the image")

if __name__ == "__main__":
    image_path = input("Enter image path: ")
    get_location(image_path)




