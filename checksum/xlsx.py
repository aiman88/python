import xlsxwriter


# my_list is a 2d list
def worksheet_generator(my_list):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Checksum_report_2.xlsx')
    worksheet = workbook.add_worksheet()

    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0

    # Iterate over the data and write it out row by row.
    for file_name, file_md5_value in (my_list):
        worksheet.write(row, col, file_name)
        worksheet.write(row, col + 1, file_md5_value)
        row += 1

    workbook.close()
