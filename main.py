import random

print('Добро пожаловать в "Сборник цитат"!')

while True:
    print('''\nМЕНЮ
1 - Все цитаты
2 - Случайная цитата
3 - Все авторы
4 - Все цитаты указанного автора
5 - Выход''')

    print('\nСделайте выбор')

    while True:
        menu_item = input('(введите число от 1 до 5): ').strip()
        if menu_item.isdigit() and 1 <= int(menu_item) <= 5:
            menu_item = int(menu_item)
            break
        print('Вы ввели некорректное значение! Повторите ввод...')

    if menu_item == 5:
        print('Программа завершена, до новых встреч!')
        break

    all_quotes = []
    
    with open('quotes.txt', 'r', encoding='utf-8') as f:
        for line in f:
            all_quotes.append(line.strip().split('|'))

    if menu_item == 1:
        if all_quotes:
            print('\nВсе имеющиеся у нас цитаты:\n')
            for quote, author in all_quotes:
                print(f'{quote}\nАвтор: {author}\n')
        else:
            print('Нет ни одной цитаты!')
    elif menu_item == 2:
        if all_quotes:
            print('\nСлучайная цитата:\n')
            rand_quote, rand_author = random.choice(all_quotes)
            print(f'{rand_quote}\nАвтор: {rand_author}\n')
        else:
            print('Нет ни одной цитаты!')
    elif menu_item == 3:
        all_authors = []
        for _, author in all_quotes:
            if author not in all_authors:
                all_authors.append(author)
        if all_authors:
            print('\nСписок всех авторов:')
            for author in all_authors:
                print(author)
        else:
            print('Нет ни одного автора!')
        print()
    elif menu_item == 4:
        target_author = input(
            '\nВведите имя автора для поиска цитат: '
            ).strip().lower()
        if all_quotes:
            found_quotes = []
            orig_author_name = None
            for quote, author in all_quotes:
                if author.lower() == target_author:
                    found_quotes.append(quote)
                    orig_author_name = author
            if found_quotes:
                print(f'\n{orig_author_name} - все цитаты автора: ')
                for item in found_quotes:
                    print(item)
                print()
            else:
                print(
                    f'У нас нет ни одной цитаты автора с указанным именем'
                )
        else:
            print('Нет ни одной цитаты!')
            

        

    
    print('Выбранная операция завершена')
    input('Нажмите Enter, чтобы вернуться в Меню...')
