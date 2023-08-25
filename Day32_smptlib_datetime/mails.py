import smtplib

my_email = "testkamil16@gmail.com"
password = "bihyhtsbzqosjhfr"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="madafakaa115@gmail.com", msg="Subject:Hello\n\nThis is the body")
