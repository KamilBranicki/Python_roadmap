##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
current_day = now.day
current_month = now.month

if current_day in data.values[data.month == current_month]:
    email = str(data.email[data.month == current_month].values)
    name = str(data.name[data.month == current_month].values)
    name = name.replace("['","")
    name = name.replace("']","")
    email = email.replace("['","")
    email = email.replace("']","")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        text = file.readlines()
        text[0] = text[0].replace("[NAME]", str(name))
        email_text = ""
        for row in text:
            if row != "\n":
                email_text += f"{row}\n"
# 4. Send the letter generated in step 3 to that person's email address.
    my_email = "testkamil16@gmail.com"
    password = "bihyhtsbzqosjhfr"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=email, msg=f"Subject:Twoje urodziny!\n\n{email_text}")




