import xlrd    
 
s= input("Please enter the signal name for abbreviation\n")

a= s.split();

myPath= r'C:\Users\user\Desktop\Abbrevations.xlsx'
#Place your file which contains the abbreviations in desktop and rename accordingly
 

for temp in a: 
        for sh in xlrd.open_workbook(myPath).sheets():  
            for row in range(sh.nrows):
                for col in range(sh.ncols):
                    myCell = sh.cell(row, col)
                    y = myCell.value
                    if(type(y) != float):
                            y = y.lower()
                            temp = temp.lower()
                            if (myCell.value == temp or y.find(temp) >= 0)  :
                                myCell2 = sh.cell(row, col+1)
                                print(myCell2.value, end ="/")
                            elif (row == (sh.nrows-1)):
                                print(end = "_")
                                break;
                    
