import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET
import os


root = ET.Element("data")

x = np.linspace(-10,10, 500)
A = 0
y = 0.5+((np.sin(x**2-A**2))**2-0.5)/(1+0.001*(x**2+A**2))

plt.axis([-10,10,0,2])
plt.plot(x,y)

if 'results' not in os.listdir():
    os.makedirs(os.path.join(os.getcwd(), 'results'))

for x, y in dict(zip(x, y)).items():
    doc = ET.SubElement(root, "row")
    ET.SubElement(doc, "x").text = str(x)
    ET.SubElement(doc, "y").text = str(y)
tree = ET.ElementTree(root)
tree.write("results/results.xml", encoding='UTF-8', xml_declaration=True)

plt.show()