from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import getFont, stringWidth


class PDF:
    def __init__(self, name, pagesize=letter):
        self.font = 'Helvetica'
        self.face = getFont(self.font).face
        self.size = 24

        self.canvasWidth, self.canvasHeight = pagesize
        self.spaceWidth = self.getTextWidth(' ')

        self.c = canvas.Canvas(name, pagesize=pagesize)
        self.c.setFont(self.font, self.size)
        self.c.setFillColor(colors.black)

    def drawText(self, text, x, y):
        width, height = self.getTextSize(text)
        self.c.drawString(x, self.canvasHeight - height - y, text)
        return width, height

    def save(self):
        self.c.save()

    def getTextSize(self, text):
        return self.getTextWidth(text), self.getTextHeight(text)

    def getTextWidth(self, text):
        return stringWidth(text, self.font, self.size)

    def getTextHeight(self, text):
        return (self.face.ascent - self.face.descent) / 1000 * self.size


if __name__ == '__main__':
    pdf = PDF('cram.pdf')
    pdf.drawText('Test', 0, 0)
    pdf.drawText('Hello World', 0, 22)
    width, _ = pdf.drawText('Hello', 0, 44)
    pdf.drawText('World', width + pdf.spaceWidth, 44)
    pdf.save()
