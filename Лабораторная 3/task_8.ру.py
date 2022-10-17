money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
all_money = money_capital + salary
cash = spend * increase
month = 0  # количество месяцев, которое можно прожить
while all_money > 0:
    all_money = all_money - (spend + cash)
    month += 1
print(month)
