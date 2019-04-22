#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack(): #cracks passwords from servers
	passwords = []
	hashes = {}
	
	with open ('passwords.txt') as file: #reads in the passwords
		passwords = file.readlines()
	passwords = list(map(str.strip, passwords)) #removes whitespace and newline from each input
    
	characters = string.ascii_lowercase #gets all lowercase chars in the english alphabet
	server_ip = "134.209.128.58"
	server_port = 1337

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((server_ip, server_port))
	
	for p in passwords: #iterates through all passwords
		for c in characters: #iterates through all chars
			h = hashlib.sha256(c + p) #gets the SHA256 hash from appending the char to the passoword
			hashes[h.hexdigest()] = c + p #maps the key as the hash and the value as the password
	
	for x in range(3): #iterate three times
		data = s.recv(1024).split("\n")[2] #parses the output and get the hash value
		if (data in hashes): #check if hash is in the dictionary
			print (hashes[data] + "\n") 
			s.send(hashes[data] + "\n") #send it to the server
			
	print s.recv(1024) #gets the flag

if __name__ == "__main__": #main method, calls the server crack method
    server_crack()
