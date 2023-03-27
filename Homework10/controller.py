import phone_book
import view

pb = phone_book.PhoneBook('Homework10\phone_db.txt')

while True:
    print(pb.main_menu())
    choice = int(input('Выберите пункт меню: '))
    match choice:
        case 1:
            view.print_pb(pb)

        case 2:
            name = input('Введите имя: ')
            phone = input('Введите телефон: ')
            comment = input('Введите комментарий: ')
            pb.new_contact(name, phone, comment)

        case 3:
            word = input('Введите поисковый запрос: ')
            view.print_pb(pb.search(word))

        case 4:
            view.print_pb(pb)
            index = int(
                input('Введите индекс контакта, который будем менять: '))
            name = input(
                'Введите имя (нажмите Enter чтобы оставить без изменения): ')
            phone = input(
                'Введите номер телефона (нажмите Enter чтобы оставить без изменения): ')
            comment = input(
                'Введите комментарий (нажмите Enter чтобы оставить без изменения): ')
            pb.change(index-1, name, phone, comment)

        case 5:
            print(pb)
            index = int(
                input('Введите индекс контакта, который хотите удалить: '))

        case 6:
            pb.save()

        case 7:
            break
