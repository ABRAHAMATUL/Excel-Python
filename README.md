# Excel-Python
Contains useful code for automating tedious tasks in handling large Excel documents
Fetching_Abbreviations is quite useful in tasks when you have a list of keywords that should be abbreviated and combine them into a single signal seperated by underscores.
Suppose if you have some keywords

Pencil Pen Stencil Erasor
and the expected output is Pcil_Pn_Stnl_Ersr

The code does that by referring the Excel file which contains the keywords and the respective abbreviations by the side 
The excel file should be of the format

SlNo  Keyword   Abrreviation
1     Pencil    Pncl
2     Pen       Pn
3     Stencil   Stnl
4     Erasor    Ersr

Note:
The code was developed for a huge excel file with Abbreviations of atleast 10000 words
So if there were instances when Drive can be matched with Driven,in case there was no drive
So the program may return two or more abbreviations seperated by /
The user should edit the final signal name to select the right keyword in these cases.
