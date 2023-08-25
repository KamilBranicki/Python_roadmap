#FileNotFound

# try:
#     file = open('a_file.txt')
#     a_dic = {'key': 'value'}
#     print(a_dic["key"])
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write("Something")
# except KeyError as error_mssage:
#     print(f"That key {error_mssage} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     #raise TypeError("This is an error that i made up.")
#     file.close()
#     print("File was closed")    

height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('Human height should not be over 3 meters')
bmi = weight / height ** 2
print(bmi)