
from reportlab.pdfgen import canvas

c = canvas.Canvas('cram.pdf')
c.drawString(100, 750, 'Hello World')
c.save()
