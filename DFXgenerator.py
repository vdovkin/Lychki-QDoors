import ezdxf

from parametrs import TABLE_PARAMETRS, TEXT_PARAMETRS

from classes.table import Table
from classes.text_array import TextArray


def dfx_generator(
    start_number, file_name, tbl_params=TABLE_PARAMETRS, txt_params=TEXT_PARAMETRS
):
    # Create a new DXF document.
    doc = ezdxf.new(dxfversion="R2010")
    doc.layers.add(tbl_params["layer"])
    doc.styles.new("font-Arial", dxfattribs={"font": "Arial"})
    msp = doc.modelspace()

    table = Table(**tbl_params)
    table.create_grid(msp)

    zeros = ""
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
