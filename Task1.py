def open_file(file_name, mode):
    try:
        file = open(file_name, mode)  # Відкриття файлу з заданим режимом
    except IOError:
        print(f"Помилка: не вдалося відкрити файл '{file_name}'!")  # Обробка помилки відкриття файлу
        return None
    else:
        print(f"Файл '{file_name}' відкрито успішно!")  # Виведення повідомлення про успішне відкриття файлу
        return file


def create_file_with_lines(file_name):
    try:
        with open(file_name, 'w') as file:  # Відкриття файлу для запису. Додав нижній прочерк для коректного сприйняття у файлі та консолі
            lines = [
                "Lorem_ipsum_dolor_sit_amet,_consectetur_adipiscing_elit.",  # Список рядків для запису
                "Sed_do_eiusmod_tempor_incididunt_ut_labore_et_dolore_magna_aliqua.",
                "Ut_enim_ad_minim_veniam,_quis_nostrud_exercitation_ullamco_laboris_nisi_ut_aliquip_ex_ea_commodo_consequat."
            ]
            for line in lines:
                file.write(line + '\n')  # Запис кожного рядка в файл
        print(f"Файл '{file_name}' успішно створено.")
    except IOError:
        print(f"Помилка: не вдалося створити файл '{file_name}'.")  # Обробка помилки при створенні файлу


def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                line = line.strip()  # Видалення зайвих пробілів з початку та кінця рядка
                length = len(line)
                i = 0
                while i < length:
                    for j in range(1, 11):  # Починаємо з 1, так як перший рядок буде містити 1 символ
                        if i < length:
                            outfile.write(line[i:i+j] + '\n')  # Записуємо відрізок символів довжиною j у новий рядок
                            i += j
                        else:
                            break
        print(f"Вміст файла '{input_file}' оброблено і записано у файл '{output_file}'.")
    except IOError:
        print(f"Помилка: не вдалося відкрити/записати у файл(и) '{input_file}', '{output_file}'.")


def print_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(f"Вміст файла '{file_name}':")
            for line in file:  # Зчитування кожного рядка з файлу
                print(line.strip())  # Виведення рядка без зайвих символів
    except IOError:
        print(f"Помилка: не вдалося відкрити файл '{file_name}'.")  # Обробка помилки відкриття файлу


if __name__ == "__main__":
    input_file = "TF12_1.txt"
    output_file = "TF12_2.txt"

    # а) Створення текстового файлу
    create_file_with_lines(input_file)

    # б) Обробка та запис у файл з вказаною структурою
    process_file(input_file, output_file)

    # в) Виведення вмісту обробленого файлу
    print_file(output_file)
