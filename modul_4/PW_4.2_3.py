def prc_calc(price, tax):
    return round(price + price * tax / 100, 2)


prc_lst = [float(input('Цена на товар: ')) for _ in range(5)]
frst_year = int(input('Повышение на первый год: '))
scnd_year = int(input('Повышение на второй год: '))

prc_frst_yr = [prc_calc(i_price, frst_year) for i_price in prc_lst]
prc_scnd_yr = [prc_calc(k_price, scnd_year) for k_price in prc_frst_yr]

print(f'Сумма цен за каждый год: {sum(prc_lst)}, {sum(prc_frst_yr)}, {sum(prc_scnd_yr)}' )