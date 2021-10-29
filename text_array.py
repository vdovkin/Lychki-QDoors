class TextArray:
    def __init__(self, font_height, font_rotation, margin, style, start_number):
        self.font_height = font_height
        self.font_rotation = font_rotation
        self.margin = margin
        self.style = style
        self.start_number = start_number

    def insert_text(self, msp, cell, text):
        position = (cell[0] - self.margin[0], cell[1] + self.margin[1])
        msp.add_text(
            text,
            dxfattribs={
                "height": self.font_height,
                "rotation": self.font_rotation,
                "style": self.style,
            },
        ).set_pos(position, align="LEFT")

    def generate_text(self, msp, grid):
        for row in grid:
            for cell in row:
                self.insert_text(msp, cell, str(self.start_number))
