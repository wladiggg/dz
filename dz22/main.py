from HomeLibrary import *

books_list = [Book('Кошмары аиста Марабу', 'Ирвин Уэлш'), Book('На игле', 'Ирвин Уэлш'),
              Book('Эйсид Хаус', 'Ирвин Уэлш'), Book('Бойцовский клуб', 'Чак Паланик'), Book('Призраки', 'Чак Паланик'),
              Book('Удушье', 'Чак Паланик')]

while True:
    success = True
    success_counter = 0
    counter = 1
    user_choice = input('Выберите действие:\n(1 - поиск, 2 - добавить книгу,'
                        ' 3 - вывести весь список книг, 0 - выйти)\n>')
    print('')

    if user_choice == '0':
        break

    elif user_choice == '1':
        user_choice2 = input('Выберите действие:\n(1 - поиск по названию, 2 - поиск по автору)\n>')
        print('')

        if user_choice2 == '1':
            search_name = input('Введите название: ')
            print('********************** Список книг **********************')
            for book in books_list:
                if str(book.book[0]).lower() == search_name.lower():
                    print(f'{counter}. ', end='')
                    counter += 1
                    success_counter += 1
                    book.show()
                    if success_counter > 0:
                        success = True
                    else:
                        success = False
                else:
                    if success_counter > 0:
                        success = True
                    else:
                        success = False
            if not success:
                print('Пусто')
            print('*********************************************************\n')

        elif user_choice2 == '2':
            search_name = input('Введите автора: ')
            print('')
            print('********************** Список книг **********************')
            for book in books_list:
                if str(book.book[1]).lower() == search_name.lower():
                    print(f'{counter}. ', end='')
                    counter += 1
                    success_counter += 1
                    book.show()
                    if success_counter > 0:
                        success = True
                    else:
                        success = False
                else:
                    if success_counter > 0:
                        success = True
                    else:
                        success = False
            if not success:
                print('Пусто')

            print('*********************************************************\n')
        else:
            print('Вы ввели что то не то!\n')

    elif user_choice == '2':
        add_book = [input('Введите название книги:\n>'), input('\nВведите автора книги\n>')]
        print(f'Книга: {add_book[0]} {add_book[1]}, успешно добавлена в вашу библиотеку\n')
        books_list.append(Book(add_book[0], add_book[1]))

    elif user_choice == '3':

        print('********************** Список книг **********************')
        for book in books_list:
            print(f'{counter}. ', end='')
            counter += 1
            book.show()
        print('*********************************************************\n')
    else:
        print('Вы ввели что то не то!\n')
