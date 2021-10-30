import ezdxf

from table import Table
from text_array import TextArray

# Create a new DXF document.
doc = ezdxf.new(dxfversion="R2010")

doc.layers.add("TABLE")

doc.styles.new("font-Arial", dxfattribs={"font": "Arial"})

msp = doc.modelspace()

TABLE_PARAMETRS = {
    "basic_point": {"x": 0, "y": 0},
    "lenght_x": 30,
    "lenght_y": 96,
    "num_x": 17,
    "num_y": 11,
    "layer": "TABLE",
}

TEXT_PARAMETRS = {
    "font_height": 20,
    "font_rotation": 90,
    "margin": (5, 1),
    "style": "font-Arial",
}


NUMBER_SIZE = 6


def get_start_number():
    while True:
        input_str = (input("Введите базовый номер: ")).strip()
        if quit_program(input_str):
            quit()
        if len(input_str) != NUMBER_SIZE:
            print(f"Число должно быть из {NUMBER_SIZE} знаков")
            continue
        else:
            try:
                number = int(input_str)
            except ValueError:
                print("Вы ввели не число")
                continue
            else:
                return number


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
    if input_str.lower() == "q":
        return True
    else:
        return False


def programm():
    print("-----------------------------------------")
    print("Программа для генерации файла с лычками")
    print("-----------------------------------------")

    print('(Что бы выйти из программы - нажмите "q")')

    while True:
        start_number = get_start_number()
        file_name = get_file_name()

        table = Table(**TABLE_PARAMETRS)
        table.create_grid(msp)
        text = TextArray(**TEXT_PARAMETRS, start_number=start_number)
        text.generate_text(msp, table.grid)

        save_file(doc, file_name)

        while True:
            input_str = input(
                "Нажите 'y' если хотите создать еще файл или 'q' что бы выйти из программы: "
            )
            if quit_program(input_str):
                quit()

            if input_str.lower() == "y":
                break


if __name__ == "__main__":
    programm()
