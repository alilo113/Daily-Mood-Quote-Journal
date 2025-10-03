import datetime

mood = input("How do you feel today? ")
today = datetime.date.today()

moodDB = []

moodDB.append({
    "mood": mood,
    "time": today
})

print(moodDB)