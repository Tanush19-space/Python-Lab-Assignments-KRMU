
print('Welcome to Daily Calorie Tracker :) !!')

print('This tool helps you to keep track of your daily total calories and compares it with your calorie limit..')


n=int(input('Enter the amount of meals:'))
limit=float(input('Enter the calorie limit:'))
meal=[]
calorie=[]
for i in range(1,n+1):
    mn=input('Enter the meal name:')
    ca=float(input('Enter the calorie amount:'))
    meal.append(mn)
    calorie.append(ca)
    total_cal_in=sum(calorie)
    average_cal_per=sum(calorie)/n
    if total_cal_in>=limit:
        result='!! Calorie intake greater than daily limit !!'
    else:
        result='Congrats!! Calorie within daily limit..!'

# -------------------------------
print("\n----------- DAILY SUMMARY REPORT -----------\n")
print("Meal Name            Calories")
print("--------------------------------------------")

for i in range(len(meal)):
    print(f"{meal[i]}              {calorie[i]}")

print("--------------------------------------------")
print(f"Total:               {total_cal_in}")
print(f"Average:             {average_cal_per}")
print(f"Status:              {result}")
print("--------------------------------------------")