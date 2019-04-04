#!/usr/bin/env python2

import sys
import struct
import datetime
import binascii
import time

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

#Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

WORD = 4
DWORD = 8

stypes = ["ASCII", "UTF8", "WORDS", "DWORDS", "DOUBLES", "COORD", "REFERENCE", "PNG", "GIF87", "GIF89"]


if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8

def analyze(counter, sect_count):
	stype, slen = struct.unpack("<LL", data[counter : counter + DWORD])
	counter += DWORD
	
	if (slen <= 0):
		bork("DOesn't work")
			
	print("Section Type: SECTION_{0}\nSection Length: {1}").format(stypes[int(stype) - 1], slen)	
		
	if (0x1 <= stype <= 0x2):
		text = None
	
		try:
			if (stype == 0x1):
				text = data[counter:counter + slen].decode('ascii')
			else:
				text = data[counter:counter + slen].decode('utf-8')
		except UnicodeDecodeError:
			bork("ASCII")
		else:
			if (stype == 0x1):
				print("\n{0}\n").format(text)
			else:
				print("\n{0}\n").format(text)
				
			counter += slen
	elif (0x3 <= stype <= 0x5):
		flag = arr = None
	
		if (stype == 0x3):
			flag = "<" + ("L" * (slen / WORD))
		else:
			flag = "<" + ("L" * (slen / DWORD))
			
		arr = struct.unpack(flag, data[counter:counter + slen])
		counter += slen
		print("\n{0}\n").format(arr)
		
	elif (stype == 0x6):
		if (slen != 16):
			bork("coord")
		
		lat, longi = struct.unpack("<dd", data[counter:counter + slen])
		print("\n({0}, {1})\n").format(lat, longi)
		
		counter += slen	
	elif (stype == 0x7):
		if (slen != 4):
			bork("Ref")
		
		ref = int(struct.unpack("<L", data[counter:counter + WORD])[0])
		if (0 <= ref <= sect_count):
			print("\n({0}\n").format(ref)
			counter += WORD
		else:
			bork("ref")
			
	elif (stype == 0x8):
		if (data[counter + 4 : counter + 8] != "IHDR"):
			bork("png")
		
		file = open("image.png", "wb")
		file.write("\211PNG\r\n\032\n" + data[counter : counter + slen])
		file.close()
		
		print("\nPNG File written to image.png\n")
		counter += slen
	elif (0x9 <= stype <= 0xA):
		sig = data[counter + 0 : counter + 4]
		file = open("image.gif", "wb")
		
		if (stype == 0x9 and sig == "#87a"):
			file.write("GIF87a " + data[counter : counter + slen])
			print("\nGIF87 File written to image.gif\n")
		elif(stype == 0xA and sig == "#89a"):
			file.write("GIF89a " + data[counter : counter + slen])
			print("\nGIF89 File written to image.gif\n")
		else:
			bork("gif")
			
		counter += slen
	
	return counter


def header(counter):
	magic, version = struct.unpack("<LL", data[0:counter])

	if magic != MAGIC:
		bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

	if version != VERSION:
		bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))
	
	timestamp = float(struct.unpack("<L", data[counter:counter + WORD])[0])
	counter += WORD
	if (timestamp <= 0 or timestamp > time.time()):
		bork("Time")
		
	name = None
	try:
		name = data[counter:counter+DWORD].decode('ascii')
	except UnicodeDecodeError:
		bork("Name")
	else:
		counter += DWORD

	count = struct.unpack("<i", data[counter:counter + WORD])[0]
	counter += WORD

	if (count <= 0):
		bork("Count is wrong")	
		
		
	print("------- HEADER -------")
	print("MAGIC: %s" % hex(magic))
	print("VERSION: %d" % int(version))
	print("Date: {0}").format(datetime.datetime.fromtimestamp(timestamp))
	print("Name: {0}").format(name)
	print("Count: {0}").format(count)
	
	return (counter, count)

	
tuple = header(DWORD)
counter = tuple[0]
print("-------  BODY  -------")
for i in range(0, tuple[1]):
	counter = analyze(counter, tuple[1])
