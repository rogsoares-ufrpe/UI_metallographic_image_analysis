# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:20:33 2023

@author: Rogério Soares da Silva
"""

import xlsxwriter

def export_to_excel(filename, data):
    """Creates a .xlxs file for data
    """
    
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(filename + '.xlsx')
    worksheet = workbook.add_worksheet()
    
    # Some data we want to write to the worksheet.
    # expenses = (
    #     ['Rent', 1000],
    #     ['Gas',   100],
    #     ['Food',  300],
    #     ['Gym',    50],
    # )
    
    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0
    
    # First, print headers
    header = data[0]
    worksheet.write(row, col, header[0])
    worksheet.write(row, col+1, header[1])
    
    # Iterate over the data and write it out row by row.
    row = 1
    for r in data[1]:
        worksheet.write(row, col,     r[0])
        worksheet.write(row, col + 1, r[1])
        row += 1
    
    workbook.close()
    
    
# headers = ["Item", "Results"]
# rows = [['Average Grain size ', 33],
#         ['Average Diameter size', 98]
#         ]
# raw_table = [ headers, rows ]

# # table = PrettyTable()
# # table.title = "Titulo"
# # table.field_names = raw_table[0]
# # table.add_rows(raw_table[1])
# # table.align = "l"

# # for row in raw_table[1]:
# #     print(row)


# export_to_excel('Analysis', raw_table)
    
    
    
    