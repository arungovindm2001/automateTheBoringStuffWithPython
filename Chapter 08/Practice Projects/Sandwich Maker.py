import pyinputplus as pyip

sandwichMaker = { 'Wheat':10, 'White':12, 'Sourdough':15, 'Chicken':20, 'Turkey':50, 'Ham':25, 'Tofu':30, 'Cheddar':8, 'Swiss':10, 'Mozzarella':12}

print('Bread Type')
breadType = pyip.inputMenu(['Wheat','White','Sourdough'])

breadTypeCost = sandwichMaker[breadType]

print('Protein Type')
proteinType = pyip.inputMenu(['Chicken','Turkey','Ham','Tofu'])

proteinTypeCost = sandwichMaker[proteinType]

ifCheese = pyip.inputYesNo('Do you want cheese?:')

if ifCheese == 'yes':
    print('Cheese Type')
    cheeseType = pyip.inputMenu(['Cheddar','Swiss','Mozzarella'])
    cheeseTypeCost = sandwichMaker[cheeseType]
else:
    cheeseTypeCost = 0

print('Sauce')    
sauce = pyip.inputYesNo('Do you want Mayo, Mustard, Lettuce or Tomato?:')

sauceCost = 10 if sauce == 'yes' else 0
    
sandwichesNumber = pyip.inputInt('How many sandwiches?',greaterThan = 1)

total = (breadTypeCost + proteinTypeCost + cheeseTypeCost + sauceCost) * sandwichesNumber

print("Total Cost:",total)
