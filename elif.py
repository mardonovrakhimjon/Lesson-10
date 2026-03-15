vazn = float(input('Vazn: '))
buy = float(input('bo\'y: '))

bmi = vazn / pow(buy, 2)

if bmi < 18.5:
    print('Siz ozg\'insiz')
elif bmi >= 18.5 and bmi < 25:
    print('Siz normal vaznda')
elif bmi >= 25 and bmi < 30:
    print('Siz ortiqcha vaznda')
elif bmi >= 30:
    print('Siz semizsiz')