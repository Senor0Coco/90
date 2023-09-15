is_single = True
print(type(is_single))
is_single

budged_janary = input("¿cual es tu presupuesto para enero?")
budged_february = input("¿cual es tu presupuesto para febrero?")
budged_march = input("¿cual es tu presupuesto para marzo?")

budged_janary = int (budged_janary)
budged_february = int (budged_february)
budged_march = int (budged_march)

budget_total = (budged_janary) + (budged_february) + (budged_march)
print ("la suma de los presupuestos es: ", budget_total)
avg_budget = budget_total / 3
print("el promedio es: ", avg_budget)
