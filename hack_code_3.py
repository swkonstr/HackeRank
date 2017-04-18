# https://www.hackerrank.com/challenges/30-operators

MealCost = float(input())
TipPercent = int(input())
TaxPercent = int(input())

Tip = MealCost * (TipPercent/100)
Tax = MealCost * (TaxPercent/100)
TotalCost = round(MealCost+Tip+Tax, 0)

print ("The total meal cost is", int(TotalCost), "dollars.")