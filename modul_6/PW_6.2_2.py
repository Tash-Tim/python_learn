incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
tot_income = sum(incomes.values())
min_incom = min(incomes.keys(), key = incomes.get)

print(f'Общий доход за год составил {tot_income} рублей')
print(f'Самый маленький доход у {min_incom}. Он составляет {incomes[min_incom]} рублей')

incomes.pop(min_incom)
print(f'Итоговый словарь: {incomes}')
