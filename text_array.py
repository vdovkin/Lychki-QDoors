class TextArray:
    def __init__(self, font_height, font_rotation, margin, style):
        self.font_height = font_height
        self.font_rotation = font_rotation
        self.margin = margin
        self.style = style

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
