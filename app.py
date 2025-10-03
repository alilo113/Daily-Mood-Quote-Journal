import datetime

mood = input("How do you feel today? ")
now = datetime.datetime.now()

moodDB = []

moodDB.append({
    "mood": mood,
    "time": datetime.datetime.now()
})

print(moodDB)