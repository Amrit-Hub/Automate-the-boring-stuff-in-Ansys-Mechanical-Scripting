from __future__ import print_function
import clr
# https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word
clr.AddReference("Microsoft.Office.Interop.Word")

# import Application
import Microsoft.Office.Interop.Word as Word

# Create excel object
word = Word.ApplicationClass()

# Make the excel application visible
word.Visible = True

# add document
# doc = word.Documents.Add()

# Read the workbook
doc = word.Documents.Open(r"D:\AnsysScripting\004 Word from IronPython\word.docx")

# Store doc used rows
# wordCount = doc.Words.Count
# wordCount = doc.Paragraphs.Count
print(doc.Content.Text)

# print doc lines
# for row in range(1, wordCount+1):
#     print(doc.Words[row].Text)


# save doc
# doc.Save()

# close and exit word
doc.Close()
word.Quit()

