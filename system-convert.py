#Here's the update so far. I found a process in python that allows me to generate a text file from the PDF. I am now working on parsing the PDF files by extracting the name of the asset and the margin price separately (the text extraction is very crude at this point). I need to work on making sure the right numbers are added to the array, and to find a way to exclude the page numbers that come up. Then I will create methods to save numbers and compare them.

import subprocess

def createTextFromPDF(pdfPath):
    retcode = subprocess.call(["/usr/bin/pdftotext", pdfPath])

#if __name__ == "__main__":
 #   createTextFromPDF('/home/dkurk/Documents/dkurk/sample.pdf')

file = open("sample.txt").readlines()
[s.strip() for s in file]

companies = []
margins = [] 
lines = []

for line in file:
    line.rstrip('\n')
    if line !='\n' and "RISK-BASED" not in line and line != "PRODUCT GROUP\n" and line != "OFFSET GROUP\n":
        if  "CLASS GROUP" in line:
            companies.append(line)
        elif "USIDX" in line:
            companies.append(line)
        elif "PRODUCT GROUP" in line:
            companies.append(line)
        elif "GROSS MARGIN" in line:
            companies.append(line)
        elif line[0].isdigit() and '/' not in line and "83824" not in line:
            margins.append(line)
        
#print len(companies)
#print len(margins)

print companies
print margins

#tuples = zip(companies, margins)

#for a in tuples:
#    print a
