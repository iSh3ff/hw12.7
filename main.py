per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

print("Доступные вклады в банках", per_cent)
money = input("Dведите сумму вклада")
m = float(money)

b1 = per_cent.get('ТКБ')
b2 = per_cent.get('СКБ')
b3 = per_cent.get('ВТБ')
b4 = per_cent.get('СБЕР')

d1 = (b1 * m) / 100
d2 = (b2 * m) / 100
d3 = (b3 * m) / 100
d4 = (b4 * m) / 100

print("deposit", d1,d2,d3,d4)
deposit1 = [ d1,d2,d3,d4 ]
deposit2 = max(deposit1)
print("Максимальная сумма, которую вы можете заработать",deposit2)




