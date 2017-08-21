#!/usr/local/bin/python

# script to dynamically create a PDF document inserting Images
# Template will have Image and its details along with datetime and page numbers as below
#
#                      [Document Name]                          Date Created: {}
# [Image details]
#                                   Image
#                                                               Page [i of n]

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle, TA_LEFT
import datetime
import save_image


style1 = ParagraphStyle(
    name='Normal',
    fontName='Helvetica',
    fontSize=11,
    alignment=TA_LEFT,
    textColor=colors.blueviolet
)
style2 = ParagraphStyle(
    name='Normal',
    fontName='Helvetica',
    fontSize=11,
    alignment=TA_LEFT,
    textColor=colors.lightcoral
)

class TemplateCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_canvas(page_count)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_canvas(self, page_count):
        self.setStrokeColorRGB(0.2, 0.5, 0.3)
        self.setLineWidth(1.0)
        self.line(47, 7.3*inch, A4[0]+200, 7.3*inch)
        self.line(47, 88, A4[0]+200, 88)
        self.setFillColor(colors.olivedrab)
        self.setFont('Helvetica-Bold', 14.5)
        self.drawString(2*inch, 7.5*inch, "Traveler's Check Images for {name}".format(name=save_image.tc_name))
        self.setFillColor(colors.black)
        self.setFont('Times-Roman', 13)
        self.drawRightString(280*mm, 7.5*inch, "Date Created: {date}".format(date=datetime.date.today().strftime("%m/%d/%Y")))
        self.drawRightString(265*mm, 14*mm + (0.2*inch), "Page %d of %d" % (self._pageNumber, page_count))
        self.saveState()
        self.restoreState()

def create_doc(elements):
    """
    Method will create a PDF documents with Images and paragraphs
    :param elements: List of Paragraph objects and Image objects (PIL images)
    :return: Creates a PDF document and returns None
    """
    doc = SimpleDocTemplate("{name}.pdf".format(name=save_image.tc_name), pagesize=A4)
    doc.pagesize = landscape(A4)
    doc.build(elements, canvasmaker=TemplateCanvas)

