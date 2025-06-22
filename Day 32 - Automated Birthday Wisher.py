import pandas, random, glob, smtplib
import datetime as dt
##################### Extra Hard Starting Project ######################
MY_EMAIL = "gordon.freeman.MIT1999@gmail.com"
MY_PASSWORD = "Password123"
# 1. Update the birthdays.csv
birthdaysCSV = pandas.read_csv("birthdays.csv")
# 2. Check if today matches a birthday in the birthdays.csv
current = dt.datetime.now()
currentMonth = current.month
currentDay = current.day
counter = 0
while counter < len(list(birthdaysCSV.name)):
        if birthdaysCSV.iloc[counter].month == currentMonth:
            if birthdaysCSV.iloc[counter].day == currentDay:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
                birthdayBoyOrGirl = list(birthdaysCSV.name)[counter]
                emailAddrToSend = birthdaysCSV.iloc[counter].email
# 4. Send the letter generated in step 3 to that person's email address.
                templates = glob.glob("./letter_templates/*.txt")
                rngLetter = random.randint(0, len(templates) - 1)
                with open(templates[rngLetter],mode="r") as docs1:
                    contents = docs1.read()
                    newContent = contents.replace("[NAME]", f"{birthdayBoyOrGirl}")
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                    connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs=emailAddrToSend,
                                        msg=f"Subject:Happy Birthday!!!\n\n{newContent}")
                    connection.close()
                counter += 1
            else:
                counter += 1
        else:
            counter += 1
