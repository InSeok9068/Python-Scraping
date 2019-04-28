from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retsts = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retsts, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retsts.getvalue()
    retsts.close()

    return content

pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
#로컬파일
#pdfFile = open("../pages/warandpeace/chapter1.pdf",'rb')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()
