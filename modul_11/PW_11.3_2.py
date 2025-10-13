class Family:
    surname = 'common_family'
    saving = 1000000
    have_hose = False

    def family_info(self):
        print('Family surname: {}\nTotal money: {}\nHave a house: {}\n'.
              format(self.surname, self.saving, self.have_hose))

    def month_saving(self, money):
        self.saving += money
        print('This month saving: {}'.format(money))
        self.family_info()

    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.saving > house_price:
            self.saving -= house_price
            self.have_hose = True
            print('{}\'s family can buy house!\nHouse prise {}'.format(self.surname, house_price))
        else:
            print('Not enough money to buy house')
        self.family_info()

my_family = Family()
my_family.surname = 'Nazarov'
my_family.family_info()
my_family.month_saving(500000)
my_family.buy_house(2000000)
my_family.month_saving(400000)
my_family.buy_house(2000000, 10)
