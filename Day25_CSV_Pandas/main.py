import pandas

data = pandas.read_csv("C:\Python\Projects\Day25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["gray", "red", "black"],
    "count": [gray_count, red_count, black_count]
}

my_data = pandas.DataFrame(data_dict)
my_data.to_csv("C:\Python\Projects\Day25\my_data.csv")

