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
    "lenght_y": 95,
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


t = Table(**TABLE_PARAMETRS)
t.create_grid(msp)

ta = TextArray(**TEXT_PARAMETRS)

ta.insert_text(msp, t.gird[0][0], "112421")

doc.saveas("test.dxf")
