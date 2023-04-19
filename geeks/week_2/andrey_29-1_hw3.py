while True:
    print('Для остановки программы введите "exit" или "выход"\n')

    word = input("Введите слово на латинице или кириллице: ")

    if len(word) == 0:
        print("\nВы ничего не ввели. Попробуйте еще раз!\n\n")
        continue

    if word == 'exit' or word == 'выход':
        break

    vowels_letters = "аиеёоуыэюяaeiouy"
    vowels_count = 0
    consonants_count = 0

    for i in word.lower():
        if not i.isalnum() or i.isdigit():
            print("\nОбнаружены недопустимые символы в строке. Попробуйте снова!\n\n")
            break

        if i in vowels_letters:
            vowels_count += 1
        else:
            consonants_count += 1        
    else:
        print(f"\nСлово: {word}")
        print(f"Количество букв: {len(word)}")
        print(f"Согласных букв: {consonants_count}")
        print(f"Гласных букв: {vowels_count}")
        print(f"Гласные/Согласные: {round(vowels_count / len(word) * 100, 2)}% / {round(consonants_count / len(word) * 100, 2)}%\n\n")