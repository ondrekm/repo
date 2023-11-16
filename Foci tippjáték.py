import tkinter as tk
import random

def check_result():
    user_score = 0

    for i in range(10):
        result = results[i]
        user_guess = guess_entries[i].get()

        # Az eredmény kiírása
        result_label = tk.Label(window, text="Eredmény #" + str(i+1) + ": " + result)
        result_label.pack()

        # A tipp ellenőrzése és a pontszám frissítése
        if user_guess == result:
            user_score += 1

    score_label.config(text="Pontszám: " + str(user_score))

window = tk.Tk()
window.title("Foci Tippjáték")

rules_label = tk.Label(window, text="Tippeld meg az eredményeket a formátummal (pl.: 1-0)!")
rules_label.pack()

guess_entries = []
results = []

teams = [
    "Manchester City",
    "Milan",
    "Napoli",
    "Real Madrid",
    "Inter",
    "Benfica",
    "Bayern München",
    "Chelsea",
    "Liverpool",
    "PSG",
    "Tottenham",
    "Lipcse",
    "Porto",
    "Brugge",
    "Dortmund",
    "Eintracht Frankfurt",
    "Juventus",
    "Sevilla",
    "Marseille",
    "Celtic"
]

used_teams = set()

for i in range(10):
    guess_label = tk.Label(window, text="Mérkőzés #" + str(i+1) + ": ")
    guess_label.pack()

    home_team = random.choice(teams)
    used_teams.add(home_team)

    away_team = random.choice(teams)
    while away_team in used_teams:
        away_team = random.choice(teams)
    used_teams.add(away_team)

    match_label = tk.Label(window, text=home_team + " vs. " + away_team + ": ")
    match_label.pack()

    guess_entry = tk.Entry(window)
    guess_entry.pack()
    guess_entries.append(guess_entry)

    result = str(random.randint(0, 5)) + "-" + str(random.randint(0, 5))
    result = home_team + " " + result + " " + away_team
    results.append(result)

submit_button = tk.Button(window, text="Tipp elküldése", command=check_result)
submit_button.pack()

score_label = tk.Label(window, text="Pontszám: 0")
score_label.pack()

window.mainloop()
