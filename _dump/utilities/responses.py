# File Name: responses.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[*] Link Excel Spreadsheet correctly
#[] Finish all Normal User Requests
#[] Finish all Project Mode User Requests

#* Libraries *#

from openpyxl import * #load workbook in Excel

#* Custom Libraries *#



#^ Variables ^#



#& Functions &#

def excel():
    wb = load_workbook("./data/other/Jarvis-Responses.xlsx") #Opens the excel document for data
    wu = wb.get_sheet_by_name('User') #sets the sheet in Excel for user prompts
    wr = wb.get_sheet_by_name('Replies') #sets the sheet in Excel for replies


    urow1 = wu['1'] #hello
    urow2 = wu['2'] #how are you
    urow3 = wu['3']
    urow4 = wu['4']
    urow5 = wu['5']
    hello_list = [urow1[x].value for x in range(len(urow1))]
    how_are_you = [urow2[x].value for x in range(len(urow2))]
    time_list = [urow3[x].value for x in range(len(urow3))]
    day_list = [urow4[x].value for x in range(len(urow4))]
    printing_list = [urow5[x].value for x in range(len(urow5))]

    rrow1 = wr['1'] #how are you
    rrow2 = wr['2'] #how are you
    reply_hello_list = [rrow1[x].value for x in range(len(rrow1))]
    reply_how_are_you = [rrow2[x].value for x in range(len(rrow2))]
    return hello_list, reply_hello_list, reply_how_are_you, how_are_you, time_list, day_list, printing_list

def projectMode():
  wb = load_workbook("./data/other/Jarvis-Responses.xlsx")
  pm = wb.get_sheet_by_name('ProjectMode') #sets the sheet in Excel for user prompts
  urow1 = pm['1']
  urow2 = pm['2']
  urow3 = pm['3']
  urow4 = pm['4']
  urow5 = pm['5']
  urow6 = pm['6']
  urow7 = pm['7']
  
  search_list = [urow1[x].value for x in range(len(urow1))]
  toPrinter_list = [urow2[x].value for x in range(len(urow2))]
  downloadFiles_list = [urow3[x].value for x in range(len(urow3))]
  exitProjectMode_list = [urow4[x].value for x in range(len(urow4))]
  printOne_list = [urow5[x].value for x in range(len(urow5))]
  printTwo_list = [urow6[x].value for x in range(len(urow6))]
  printThree_list = [urow7[x].value for x in range(len(urow7))]
  
  return search_list, toPrinter_list, downloadFiles_list, exitProjectMode_list, printOne_list, printTwo_list, printThree_list

#= Classes =#

#~ define and build classes here

#! Main Program !#

#~ the main program goes here



#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#