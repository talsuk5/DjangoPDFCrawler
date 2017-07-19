from PyPDF2 import PdfFileReader
import io


class PdfParser:

    def __init__(self, stream):
        reader = PdfFileReader(io.BytesIO(stream))

        self.contents = []
        for i in range(0, reader.getNumPages()):
            page_obj = reader.getPage(i)
            self.contents += page_obj.extractText().split()

    def getParesdWordList(self):
        return self.contents
