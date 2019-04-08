

import sys
from pikepdf import Pdf

###Requires Pikepdf lib
# a simple python program that simplifies the convination of multiple pdf files into one
# for use run: Python read.py file1.pdf file2.pdf file3.pdf.....fileN.pdf



#this code reads pdf files and breaks them into different files by pages



#this funtion takes a list of pdf files and combines them into a single pdf file.
def mege_pdf(files_m):
  pdf_out= Pdf.new()
  out_p_name = files_m[0].replace(".pdf","Combined.pdf")
  for name in files_m:
    src = Pdf.open(name)
    pdf_out.pages.extend(src.pages)
  pdf_out.save(out_p_name) 
  print("Combined pdfs saved to : "+out_p_name )   




#print( 'Number of arguments:', len(sys.argv), 'arguments.')

files = []
for node in (sys.argv):
  if ".pdf" in node:
    
    files.append(node)
  else:
    print(node, ' is not a valid pdf ') 

print('Combining : ',files) 
mege_pdf(files)   


  
   


fname = "tkt.pdf"

#new_pdf = Pdf.new()
#sample_pdf = Pdf.open(fname)
#num_pages = len(sample_pdf.pages)
#print (num_pages)
#dst = Pdf.new()



def extract_pages(from_s, to_s):
  out_pdf = Pdf.new()    

  for s in range (from_s, to_s): 
    print( s)
 #   out_pdf.pages.append( sample_pdf.pages[s])

  out_pdf.save("Extracted_PAGES.pdf")  




#extract_pages(1,3)   


def Combine_Pages(file1,file2):
 
 first_file = Pdf.open(file1)  
 first_file2 = Pdf.open(file2)
 second_l= len(first_file2.pages)
 for a in range (0, second_l):
   first_file.pages.append(first_file2.pages[a])
 first_file.save(file1+"Full")  






 
