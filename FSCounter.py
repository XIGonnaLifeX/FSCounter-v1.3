from colorama import Fore
print(Fore.RED + ' _____________')
print(Fore.RED + '|###  ###  ###|')
print(Fore.RED + '|#   #    #   |')
print(Fore.RED + '|##   ##  #   |')
print(Fore.RED + '|#      # #   |')
print(Fore.RED + '|#   ###   ###|')
print(Fore.RED + '~~~~~~~~~~~~~~~')
print('Привет эта программа поможет посчитать необходимое кол-во слитков на изготовление какого-либо предмета в FS...')
print('Что изготавливаем?')
print('1.Двигатели;')
print('2.Манипуляторы;')
print('3.Турбины;')
print('4.Эл.компоненты;')
print('5.Микросхемы;')
print('6.Процессоры;')
print('7.Нагрев.элементы;')
print('8.Сплавы...')
choise = int(input('~$ '))
if choise != 8 :
    Kolvo = int(input('Количество: '))
    a = 0
if choise == 1 :
    if int(Kolvo) % 2 !=0 :
        a = a+1
    print('В металлоформовщик (Подшипники): ' + str(Kolvo*3) + ' слитков;')
    print('В металлоформовщик (Стержни): ' + str(int((Kolvo + a) / 2)) + ' слитков;')
    print('В металлоформовщик (Шестерни): '+ str(Kolvo * 2) + ' слитков;')
    print('В сборщик механизмов (Роторы): '+ str(Kolvo) + ' слитков;')
    print('В сборщик механизмов (Статоры): '+ str(Kolvo) +' слитков;')
    print('В формовщик проводов: ', str(Kolvo * 2), ' слитков;')
    print('Итого: '+ str(Kolvo * 2) +' слитков на провода,'+ str(int((Kolvo*7) + ((Kolvo + a) / 2))) + ' слитков на остальные части.')
if choise == 2 :
    d = Kolvo * 5 / 2
    if Kolvo % 2 != 0 :
        d = ((Kolvo * 5 + 1) / 2)
    print('В сборщик механизмов (Манипуляторы): ', str(Kolvo*3), ' слитков')
    print('В металлофорщик (Стержни): ', str(int(d)) , ' слитков')
    print('В металлофорщик (Подшипники): ', str(Kolvo * 3), ' слитков')
    print('В формовщик проводов->сборщик эл.компонентов: ', str(Kolvo*4), ' слитков')
    print('В формовщик проводов->сборщик эл.компонентов->сборщик микросхем: ', str(Kolvo*4), ' слитков и ', str(Kolvo), ' слитков на пластины')
    print('Итого: ', str(Kolvo * 4 * 2), ' слитков на провода,', str(int(Kolvo*3 + d + Kolvo*3)), ' слитков на остальные части и ', Kolvo, ' слитков на пластины')
if choise == 3 :
    print(str(Kolvo*6), ' слитков на пластины')
    print(str(Kolvo), ' слитков в металлоформовщик (стержни)')
    print(str(Kolvo*2), ' слитков в металлоформовщик (подшипники)')
    print('Итого: ', str((Kolvo*6)+(Kolvo*2)+Kolvo), ' слитков.')
if choise == 4 :
    print('В формовщик проводов->сборщик электрокомпонентов ', str(Kolvo*2), ' слитков.')
    print('Итого: ', str(Kolvo*2), ' слитков.')
if choise == 5 :
    print('В формовщик проводов->сборщик эл.компонентов->сборщик эл.схем ', str(Kolvo*4), ' слитков.')
    print('Итого: ', str(Kolvo*4), ' слитков на провода и ', str(Kolvo), ' слитков на пластины.')
if choise == 6 :
    Yadra = input('Кол-во ядер: ')
    print('В формовщик проводов->сборщик эл.компонентов->сборщик эл.схем ', str(int(Kolvo) * 4 * int(Yadra)), ' слитков и ', str(Yadra), ' пластин из вольф.стали');
    print('В формовщик проводов->сборщик эл.компонентов(Охл.элементы) ', str(Kolvo * Yadra), ' слитков платины.');
    print('В формовщик продов->сборщик эл.комп.->сборщик эл.схем->сборщик эл.комп.(Охл.элемнты) ', str(int(Kolvo) * 4 * int(Yadra)), ' слитков платины и ', str(Yadra), ' пластин из вольф.стали');
    print('В гидр.прес->сборщик эл.комп.(охл.эл) ', str(Yadra), ' слитков золота');
    print('Итого: ', str(int(Kolvo) * 4 * int(Yadra)), ' слитков на эл.схемы, ', str((int(Kolvo) * 4 * int(Yadra)) + (int(Kolvo) * int(Yadra))), ' слитков платины на охл.элементы и ', str(int(Yadra) * 2), ' слитков вольф.стали на пластины');
if choise == 7 :
    print(str(Kolvo), ' слитков олова в формовщик проводов->сборщик эл.комп.(Нагрев.элементы)')
    print(str(Kolvo), ' слитков железа в гидр.прес->сборщик эл.комп.(Нагрев.элементы)')
    print(str(Kolvo * 4), ' слитков олова и ', str(Kolvo), ' в формовщик проводов->сборщик эл.комп.->сборщик эл.схем->сборщик эл.комп.(Нагрев.элементы)')
if choise == 8 :
    print('1.Бронза;')
    print('2.Сталь;')
    print('3.Нерж.сталь;')
    print('4.Электрум;')
    print('5.Вольф.сталь;')
    print('6.Платинин;')
    print('7.Титан-вольфрам;')
    print('8.Тантал-титан;')
    print('9.Осмиридиум;')
    print('10.Неоридиум.')
    choiseB = int(input('~$ '))
    Kolvo = int(input('Количество: '))
    if choiseB == 1 :
        while Kolvo % 4 != 0 :
            Kolvo += 1
        b = Kolvo // 4
        SlitokA = b * 3
        SlitokB = b * 1
        print(str(SlitokA) + ' слитков меди и ' + str(SlitokB) + ' слитков олова')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков бронзы')
    if choiseB == 2 :
        while Kolvo % 4 != 0 :
            Kolvo += 1
        b = Kolvo // 4
        SlitokA = b * 3
        SlitokB = b * 1
        print(str(SlitokA) + ' слитков железа и ' + str(SlitokB) + ' угля')
    if choiseB == 3 :
        while Kolvo % 4 != 0 :
            Kolvo += 1
        b = Kolvo // 4
        SlitokA = b * 3
        SlitokB = b * 1
        print(str(SlitokA) + ' слитков стали и ' + str(SlitokB) + ' слитков хрома')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков нерж.стали')
        print('Вы можете посчитать кол-во компонентов для стали в этой программе, перезапустив её.')
    if choiseB == 4 :
        while Kolvo % 8 != 0 :
                Kolvo += 1
        b = Kolvo // 8
        SlitokA = b * 5
        SlitokB = b * 3
        print(str(SlitokA) + ' слитков серебра и ' + str(SlitokB) + ' слитков золота')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков электрума')
    if choiseB == 5 :
        while Kolvo % 5 != 0 :
                Kolvo += 1
        b = Kolvo // 5
        SlitokA = b * 3
        SlitokB = b * 2
        print(str(SlitokA) + ' слитков стали и ' + str(SlitokB) + ' слитков вольфрама')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков вольф.стали')
        print('Вы можете посчитать кол-во компонентов для стали в этой программе, перезапустив её')
    if choiseB == 6 :
        while Kolvo % 3 != 0 :
                Kolvo += 1
        b = Kolvo // 3
        SlitokA = b * 2
        SlitokB = b * 1
        print(str(SlitokA) + ' слитков платины и ' + str(SlitokB) + ' слитков серебра')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков платинина')
    if choiseB == 7 :
        while Kolvo % 4 != 0 :
                Kolvo += 1
        b = Kolvo // 4
        SlitokA = b * 3
        SlitokB = b * 1
        print(str(SlitokA) + ' слитков титана и ' + str(SlitokB) + ' слитков вольфрама')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков вольфрам-титана')
    if choiseB == 8 :
        while Kolvo % 8 != 0 :
                Kolvo += 1
        b = Kolvo // 8
        SlitokA = b * 5
        SlitokB = b * 3
        print(str(SlitokA) + ' слитков тантала и ' + str(SlitokB) + ' слитков титана')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков тантал-титана')
    if choiseB == 9 :
        while Kolvo % 2 != 0 :
                Kolvo += 1
        b = Kolvo // 2
        SlitokA = b * 1
        SlitokB = b * 1
        print(str(SlitokA) + ' слитков иридия и ' + str(SlitokB) + ' слитков осмия')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков осмиридия')
    if choiseB == 10 :
        while Kolvo % 3 != 0 :
                Kolvo += 1
        b = Kolvo // 3
        SlitokA = b * 2
        SlitokB = b * 1
        print(str(SlitokA) + ' слитков неодима и ' + str(SlitokB) + ' слитков иридия')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков неоридиума')
input()