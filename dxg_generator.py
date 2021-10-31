import ezdxf

from parametrs import TABLE_PARAMETRS, TEXT_PARAMETRS

from classes.table import Table
from classes.text_array import TextArray


def dfx_generator(
    start_number, file_name, tbl_params=TABLE_PARAMETRS, txt_params=TABLE_PARAMETRS
):
    # Create a new DXF document.
    doc = ezdxf.new(dxfversion="R2010")
    doc.layers.add(tbl_params["layer"])
    doc.styles.new("font-Arial", dxfattribs={"font": "Arial"})
    msp = doc.modelspace()

    table = Table(**tbl_params)
    table.create_grid(msp)

    text = TextArray(**txt_params, start_number=start_number, zeros=zeros)
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
