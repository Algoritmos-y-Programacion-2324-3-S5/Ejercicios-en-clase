score = float(input("Enter employee score: "))
amount = 0
score_description= ""
isValid = True

if score == 0.0:
    score_description = "Inaceptable"
elif score == 0.4:
    amount = 2400 * 0.4
    score_description = "Aceptable"
elif score > 0.4:
    amount = 2400 * 0.6
    score_description = "Meritorio"
else:
    isValid = False
    print("Invalid score")

if isValid:
    print(f"Your score is {score_description} and you will earn {amount} euros")
