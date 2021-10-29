import ezdxf

from table import Table

# Create a new DXF document.
doc = ezdxf.new(dxfversion="R2010")

doc.layers.add("TABLE")

msp = doc.modelspace()


PARAMETRS = {
    "basic_point": {"x": 0, "y": 0},
    "lenght_x": 27.63,
    "lenght_y": 89.75,
    "num_x": 17,
    "num_y": 11,
    "layer": "TABLE",
}

t = Table(**PARAMETRS)
t.create_grid(msp)
# create_grid(**PARAMETRS)

doc.saveas("test.dxf")
