import datetime as dt
import smtplib
import random    

time = dt.datetime.now()
day = time.weekday()
if day == 6:
    with open("C:\Python\Projects\Day32\quotes.txt", mode="r") as data:
        data_list = data.readlines()
    quote = random.choice(data_list)

    my_email = "testkamil16@gmail.com"
    password = "bihyhtsbzqosjhfr"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="madafakaa115@gmail.com", msg=f"Subject:Motivational Quote\n\n{quote}")
