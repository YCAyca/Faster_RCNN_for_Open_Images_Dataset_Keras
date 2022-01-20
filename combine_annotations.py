
import os 
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


def without_tag(element):
    element = element.split(">")[1]
    element = element.split("<")[0]
    return element
    

filepath = "dataset_roadsign\\test\\voc\\"
combined_file = open("test_annotations.txt", "w")

for filename in os.listdir(filepath):
   with open(filepath+filename, "r+") as f:
       data = f.read()
       
   data = BeautifulSoup(data, "xml")
   
   try:
       image_name = str(data.find('filename'))
       image_name = without_tag(image_name)
       objects = data.find_all('object')
       xmins = data.find_all('xmin')
       ymins = data.find_all('ymin')  
       xmaxs = data.find_all('xmax') 
       ymaxs = data.find_all('ymax')  
       class_names = data.find_all('name')  
       object_count = len(objects)
       for i in range(object_count):
           combined_file.write(filepath+image_name)
           combined_file.write(", ")
           xmin = without_tag(str(xmins[i]))
           combined_file.write(xmin)
           combined_file.write(", ")
           
           ymin = without_tag(str(ymins[i]))
           combined_file.write(ymin)
           combined_file.write(", ")
           
           xmax = without_tag(str(xmaxs[i]))
           combined_file.write(xmax)
           combined_file.write(", ")
           
           ymax = without_tag(str(ymaxs[i]))
           combined_file.write(ymax)
           combined_file.write(", ")
           
           class_name = without_tag(str(class_names[i]))
           combined_file.write(class_name)
           combined_file.write("\n")
            
           
   except:
       print("no objects")

combined_file.close()       