#!/usr/bin/env python3

import hashlib
import string

def crack(): #cracks passwords
	hashes = []
	passwords = []
	with open ('hashes.txt') as file: #reads in the hashes
		hashes = file.readlines()
	hashes = list(map(str.strip, hashes)) #removes whitespace and newline from each input
	
	with open ('passwords.txt') as file: #reads in the passwords
		passwords = file.readlines()
	passwords = list(map(str.strip, passwords)) #removes whitespace and newline from each input
    
	characters = string.ascii_lowercase #gets all lowercase chars in the english alphabet

	for p in passwords: #iterates through all passwords
		for c in characters: #iterates through all chars
			h = hashlib.sha256(c + p) #gets the SHA256 hash from appending the char to the passoword
			if (h.hexdigest() in hashes): #sees if it is in the hash list
				print(c + p + ": " + h.hexdigest()) #prints output
				break #exits inner loop since it was already found

if __name__ == "__main__": #main method, calls the crack method
    crack()
