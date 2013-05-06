from PyPDF2 import PdfFileReader, PdfFileWriter
import StringIO
from reportlab.lib.pagesizes import letter, legal
from reportlab.pdfgen import canvas


class PdfEditor(object):
    '''Class for modifying a previously existing PDF's.

    note::
    Currently only works 1 page PDF's.
    Origin is on LOWER left corner.
    '''

    def __init__(self, filename, pageSize):
        '''Args:
            filename (str): Location of the original PDF.
            pageSize (str): Either letter or legal.
        '''
        super(PdfEditor, self).__init__()
        self.pdf = PdfFileReader(filename).getPage(0)
        self.content = StringIO.StringIO()
        self.parser = canvas.Canvas(self.content, pagesize=(letter if pageSize == 'letter' else legal))

    def drawString(self, x, y, content):
        '''Args:
            x (int): X coordinate.
            y (int): Y coordinate.
            content (str): String to be written.
        '''
        self.parser.drawString(x, y, content)

    def setFontSize(self, size):
        '''Args:
            size (int): Select size of the font.
        '''
        self.parser.setFontSize(int(size))

    def save(self, filename):
        '''Args:
            filename (str): Name of the file to be saved.
        '''
        self.parser.save()
        self.content.seek(0)
        text = PdfFileReader(self.content)
        output = PdfFileWriter()
        self.pdf.mergePage(text.getPage(0))
        output.addPage(self.pdf)
        outputStream = open(filename, 'wb')
        output.write(outputStream)
