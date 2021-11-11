import ezdxf

from classes.table import Table
from classes.text_array import TextArray


def dxf_generator(start_number, file_name, tbl_params, txt_params):
    # Create a new DXF document.
    doc = ezdxf.new(dxfversion="R2010")
    doc.layers.add(tbl_params["layer"])
    doc.styles.new("font-Arial", dxfattribs={"font": "Arial"})
    msp = doc.modelspace()

    table = Table(**tbl_params)
    table.create_border(msp)

    zeros = starting_zeros(start_number)

    try:
        start_number = int(start_number)
    except:
        return False

    text = TextArray(**txt_params, start_number=start_number, zeros=zeros)
    text.generate_text(msp, table.grid)

    result = save_file(doc, file_name)

    return result


def save_file(doc, file_name):
    try:
        doc.saveas(f"{file_name}.dxf")
    except Exception:
        return False
    else:
        return True


def starting_zeros(input_text):
    zeros = ""
    for c in input_text:
        if c == "0":
            zeros += c
        else:
            break
    return zeros
