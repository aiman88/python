import openpyxl as xl

from openpyxl import Workbook
import time

book = Workbook()

#sheet = book.active

#sheet['A1'] = 1500
#sheet['B1'] = 2500

#now = time.strftime("%x")

#sheet['C1']=now

book.save("demo2.xlsx")
