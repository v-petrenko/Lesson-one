print('МЕДЕЦИНСКАЯ АНКЕТА')
petreson_name = (input('Введите свое имя: '))
family = (input('Введите свою фамилию: '))
age = int(input('Ваш возраст: '))
weight = int(input('Сколько Вы весите: '))
if age <= 30 and 50 <= weight <= 120 :
    print(petreson_name, family, ',', age, 'год', ',', 'вес', weight, '- молодец, так держать!')
elif age <= 30 and weight >= 120 :
    print(petreson_name, family, ',', age, 'год', ',', 'вес', weight, '- необходимо обратиться к врачу!')
elif 30 <= age <= 39 and 50 <= weight <= 120 :
    print(petreson_name, family, ',', age, 'год', ',', 'вес', weight, '- молодец, так держать!')
elif 30 <= age <= 39 and weight <= 50 :
    print(petreson_name, family, ',', age, 'год', ',', 'вес', weight, '- следует заняться йогой.')
elif 30 <= age <= 39 and weight >= 120 :
    print(petreson_name, family, ',', age, 'год', ',', 'вес', weight, '- следует заняться йогой.')
elif age >= 40 and 50 <= weight <= 120 :
    print(petreson_name, family, ',', age, 'год', ',', 'вес', weight, '- молодец, так держать!')
elif age >= 40 and weight <= 50 :
    print(petreson_name, family, ',', age, 'год', ',', 'вес', weight, '- необходимо обратиться к врачу!')
elif age >= 40 and weight >= 120 :
    print(petreson_name, family, ',', age, 'год', ',', 'вес', weight, '- необходимо обратиться к врачу!')
else :
    print('с вводными что-то не так')
