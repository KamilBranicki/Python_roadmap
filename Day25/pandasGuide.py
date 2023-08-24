# with open("C:\Python\Projects\Day25\weather_data.csv", mode="r") as data:
#     data_list = data.readlines()

# print(data_list) #za duży przerabiania stringów



# import csv #poniższy kod też zajmuje za dużo miejsca, pandas będzie lepsze

# with open("C:\Python\Projects\Day25\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data) #To jest obiekt, ale może być przeloopowany
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1])) #każdy row to lista stringów
# print(temperatures)

import pandas
data_file = pandas.read_csv("C:\Python\Projects\Day25\weather_data.csv")
print(data_file)
print(type(data_file))
print(data_file["temp"])
print(type(data_file["temp"]))

# data_dict = data_file.to_dict()
# print(data_dict)
# temp_list = data_file["temp"].to_list()
# print(temp_list)

# temp_avg = sum(temp_list) / len(temp_list)
# print(temp_avg)

# temp_avg = data_file["temp"].mean()
# print(temp_avg)
# max_temp = data_file["temp"].max()
# print(max_temp)
# print(data_file.condition)

# print(data_file[data_file.day == "Monday"])

# print(data_file[data_file.temp == data_file.temp.max()])

# monday = data_file[data_file.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("C:\Python\Projects\Day25\\new_csv_file.csv")
