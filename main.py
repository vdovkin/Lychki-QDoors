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

start_number = 112421


table = Table(**TABLE_PARAMETRS)
table.create_grid(msp)
text = TextArray(**TEXT_PARAMETRS, start_number=start_number)
text.generate_text(msp, table.grid)

doc.saveas("test.dxf")
