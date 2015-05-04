// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.
// 24576
// 8192

(START)
	@ SCREEN
	D = A
	@ screenfill
	M = D
	
	@ 8191
	D = A
	@ fillcount
	M = D
	
	@ fillval
	M = 0
	
	@ KBD
	D = M
	@ keystrike
	M = D
	
	@ FILL
	D; JEQ
	
	@ fillval
	M = -1
		
(FILL)
	@ fillval
	D = M
	@ screenfill
	A = M
	M = D
	@screenfill
	M = M + 1
	@ fillcount
	MD = M-1
	@ FILL
	D; JGE
	
	@ START
	0; JMP
	
