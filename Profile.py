print('МЕДЕЦИНСКАЯ АНКЕТА')
petreson_name = (input('Введите свое имя: '))
family = (input('Введите свою фамилию: '))
age = int(input('Ваш возраст: '))
weight = int(input('Сколько Вы весите: '))
if age <= 30 and weight >= 120 and weight <= 50 :
    print(petreson_name, family, ',', age, 'год', ',', 'вес', weight, '- следует заняться йогой.')
elif age >= 40 and weight >= 120 and weight <= 50 :
    print(petreson_name, family, ',', age, 'год', ',', 'вес', weight, '- необходимо обратиться к врачу!')
elif age <= 30 and weight >= 50 and weight <= 120 :
    print(petreson_name, family, ',', age, 'год', ',', 'вес', weight, '- молодец, так держать!')
else:
    print('с вводными что-то не так')