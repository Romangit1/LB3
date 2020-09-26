kubik = [1,2,3,4,5,6]
import random
random.shuffle(kubik)
print('Покидаєм кубик?')
count = 0

while True:
    choice = input('Будете кидати куб? y/n\n')
    if choice == 'y':
        current = kubik.pop()
        print('Вам инала цифра під номером %d' %current)
        count += current
        if count > 24:
            print('Вибачте , ви програли')
            break
        elif count == 24:
            print('Поздравляю, вы виграли!')
            break
        else:
            print('У вас %d балів.' %count)
    elif choice == 'n':
        print('У вас %d балів і ви закінчили гру.' %count)
        break

print('Гра закінчена!')


