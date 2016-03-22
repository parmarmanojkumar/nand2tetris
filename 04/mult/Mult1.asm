// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@ 3
D = A	
@ R0	
M = D
@ 512
D = A
@ R1
M = D
	
	// Initialize product as zero
	@ R2
	M = 0 
	// Check if either of input is zero and terminate multiplication
	@ R1
	D = M
	@ END1
	D; JEQ
	@ R0
	D = M
	@ END1
	D; JEQ
	// Check for smaller value between 2 variables
	@ R1
	D = D-M
	@ LOOP
	D; JGE
	// Swap smaller values in R1 which is looping variables to reduce number of loop
	@ R0
	D = M
	@ R1
	MD = D + M
	@ R0
	MD = D - M
	@ R1
	MD = M - D
	// Repetative addition to perform multiplication
(LOOP)	
	@ R0
	D = M
	@ R2
	MD = D + M
	@ R1
	MD = M -1
	@ LOOP
	D; JGT
//(END1)
//	@ END1
//	0; JMP
