import wikipedia
wikipedia.set_lang("ru")

while True:

    try:
        search = input("Что искать?\n")
        if search == 'стоп':
            break

        s = wikipedia.page(search)
        print(s.content)
        print("Ссылка: "+s.url)
    except:
        print("По вашему запросу ничего не найдено!")
        print()
        print("Допустимые варианты:")
        print("====================")
        valid_list = wikipedia.search(search)
        for item in valid_list:
            print(item)
        print("====================")
        print()