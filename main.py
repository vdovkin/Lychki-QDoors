import ezdxf

# Create a new DXF document.
doc = ezdxf.new(dxfversion="R2010")

doc.layers.add("TABLE")

msp = doc.modelspace()


def create_x_line(basic_point, lenght, number, layer="TABLE"):
    for i in range(number):
        msp.add_line(
            (basic_point["x"], basic_point["y"]),
            (basic_point["x"] + lenght, basic_point["y"]),
            dxfattribs={"layer": layer},
        )
        basic_point["x"] += lenght


def create_y_line(basic_point, lenght, number, layer="TABLE"):
    for i in range(number):
        msp.add_line(
            (basic_point["x"], basic_point["y"]),
            (basic_point["x"], basic_point["y"] + lenght),
            dxfattribs={"layer": layer},
        )
        basic_point["y"] += lenght


def create_grid(basic_point, lenght_x, lenght_y, num_x, num_y):
    bp = basic_point.copy()
    for i in range(num_y + 1):
        create_x_line(bp, lenght_x, num_x)
        bp["x"] -= lenght_x * num_x
        bp["y"] += lenght_y

    bp = basic_point.copy()
    for i in range(num_x + 1):
        create_y_line(bp, lenght_y, num_y)
        bp["x"] += lenght_x
        bp["y"] -= lenght_y * num_y


PARAMETRS = {
    "basic_point": {"x": 0, "y": 0},
    "lenght_x": 27.63,
    "lenght_y": 89.75,
    "num_x": 17,
    "num_y": 11,
}


create_grid(**PARAMETRS)

doc.saveas("test.dxf")
