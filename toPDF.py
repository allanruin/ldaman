# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from os import *
from PIL import Image


print "hello"

imgdir = "img"

title = "LDAman.pdf"
(w,h) = portrait(A4)

print w,h

c = canvas.Canvas(title, pagesize = portrait(A4))

files = [f for f in listdir(imgdir)]
files.sort()
# for f in files:
# 	print f

for filename in files:
	filename = imgdir+"/"+filename
	im = Image.open(filename)
	width, height = im.size
	# c.drawImage(filename, 0,0,w, w/width*h, preserveAspectRatio=True )
	c.drawImage(filename, 0,0,w, h, preserveAspectRatio=True )
	c.showPage()
	print "add image " + filename

c.save()
print "all done\n"
