import smtplib, random
import datetime as dt

myEmail = "gordon.freeman.MIT1999@gmail.com"
with open("quotes.txt", mode="r") as docs1:
    quotes = docs1.read().splitlines()
    rngQuote = random.choice(quotes)

currentDay = dt.datetime.now().weekday()
if currentDay == 5:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=myEmail,password="Password123")
        connection.sendmail(from_addr=myEmail,
                            to_addrs="JohnSmith@cia.gov",
                            msg=f"Subject:Hang in there!\n\n{rngQuote}")
        connection.close()