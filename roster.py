# https://goheels.com/sports/mens-basketball/roster
import pandas as pd

player = {"Last Name": ["High", "Cadeau", "Ryan", "Davis", "Bacot", "Trimble", "Wokcik", "Washington", "Lebo", "Landry"],
          "First Name": ["Zayden", "Elliot", "Cormac", "RJ", "Armando", "Seth", "Paxson", "Jalen", "Creighton", "Rob"],
          "height": [81, 73, 77, 72, 83, 75, 77, 82, 73, 76],
          "weight": [225, 180, 195, 180, 240, 195, 195, 230, 180, 190]
          }

data = pd.DataFrame(player)

# bmi = weight in kg/ height in meters squared
data["bmi"] = [(weight / 2.205) / ((height / 39.37) ** 2) 
    for weight, height in zip(data["weight"], data["height"])]
data["bmi"] = [f'{bmi:.2f}' for bmi in data["bmi"]]

print(data)

data.to_csv("bmi.csv")