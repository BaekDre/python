import pandas as pd

lynx = pd.read_csv("lynx.csv")
lynx["time"] = round(lynx.time/10)*10
print(lynx["time"])

print(lynx.sort_values("time"))