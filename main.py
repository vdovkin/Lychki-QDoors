import ezdxf

from table import Table
from text_array import TextArray

from parametrs import TABLE_PARAMETRS, TEXT_PARAMETRS, NUMBER_SIZE


def starting_zeros(input_text):
    zeros = ""
    for c in input_text:
        if c == "0":
            zeros += c
        else:
            break
    return zeros


def get_start_number():
    while True:
        input_str = (input("Введите базовый номер: ")).strip()
        if quit_program(input_str):
            quit()
        if len(input_str) != NUMBER_SIZE:
            print(f"Число должно быть из {NUMBER_SIZE} знаков")
            continue
        else:
            zeros = ""
            if input_str[0] == "0":
                zeros = starting_zeros(input_str)
            try:
                number = int(input_str)
            except ValueError:
                print("Вы ввели не число")
                continue
            else:
                return number, zeros


def get_file_name():
    while True:
        input_str = (input("Введите название файла: ")).strip()
        if quit_program(input_str):
            quit()

        if not input_str.strip():
            print(f"Нельзя вводить пустую строку")
            continue
        else:
            return input_str


def save_file(doc, file_name):
    try:
        doc.saveas(f"{file_name}.dxf")
    except Exception:
        print(
            "Не удалось создать файл. Возможно у Вас уже открыт файл с таким же именем"
        )
    else:
        print(f"{file_name} успешно создан")


def quit_program(input_str):
    return input_str.strip().lower() == "q"


def display_start_info():
    print("-----------------------------------------")
    print("Программа для генерации файла с лычками")
    print("-----------------------------------------")

    print('(Что бы выйти из программы - нажмите "q")')


def programm():
    display_start_info()
    while True:
        start_number, zeros = get_start_number()
        file_name = get_file_name()

        # Create a new DXF document.
        doc = ezdxf.new(dxfversion="R2010")
        doc.layers.add(TABLE_PARAMETRS["layer"])
        doc.styles.new("font-Arial", dxfattribs={"font": "Arial"})
        msp = doc.modelspace()

        table = Table(**TABLE_PARAMETRS)
        table.create_grid(msp)

        text = TextArray(**TEXT_PARAMETRS, start_number=start_number, zeros=zeros)
        text.generate_text(msp, table.grid)

        save_file(doc, file_name)

        while True:
            input_str = input(
                "Нажите 'y' если хотите создать еще файл или 'q' что бы выйти из программы: "
            )
            if quit_program(input_str):
                quit()

            if input_str.strip().lower() == "y":
                break


if __name__ == "__main__":
    programm()
