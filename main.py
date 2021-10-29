import ezdxf

from table import Table

# Create a new DXF document.
doc = ezdxf.new(dxfversion="R2010")

doc.layers.add("TABLE")

doc.styles.new("custom_style", dxfattribs={"font": "Arial"})

msp = doc.modelspace()

PARAMETRS = {
    "basic_point": {"x": 0, "y": 0},
    "lenght_x": 27.63,
    "lenght_y": 89.75,
    "num_x": 17,
    "num_y": 11,
    "layer": "TABLE",
}

text_base_point = (
    PARAMETRS["lenght_x"] - 5,
    PARAMETRS["lenght_y"] * (PARAMETRS["num_y"] - 1) + 5,
)

msp.add_text(
    "0000000",
    dxfattribs={"height": 20, "rotation": 90, "style": "custom_style"},
).set_pos(text_base_point, align="LEFT")


t = Table(**PARAMETRS)
t.create_grid(msp)


doc.saveas("test3.dxf")
