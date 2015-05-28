// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/mult/Mult.tst

load Computer.hdl,
ROM32K load myMult.hack,
output-file myMult.out,
compare-to myMult.cmp,
output-list time%S1.4.1 reset%B2.1.2 RAM16K[0]%D1.7.1 RAM16K[1]%D1.7.1 RAM16K[2]%D1.7.1;

set reset 1,
output;
repeat 2 {
  tick, tock;
}
set reset 0,
set RAM16K[0] 0,   // Set test arguments
set RAM16K[1] 0,
set RAM16K[2] -1;  // Test that progRAM16K initialized product to 0
output;
repeat 20 {
  tick, tock;
}
set RAM16K[0] 0,   // Restore arguments in case progRAM16K used them as loop counter
set RAM16K[1] 0,
output;

set reset 1,
output;
repeat 2 {
  tick, tock;
}
set reset 0,
set RAM16K[0] 1,   // Set test arguments
set RAM16K[1] 0,
set RAM16K[2] -1;  // Ensure that progRAM16K initialized product to 0
output;
repeat 50 {
  tick, tock;
}
set RAM16K[0] 1,   // Restore arguments in case progRAM16K used them as loop counter
set RAM16K[1] 0,
output;

set reset 1,
repeat 2 {
  tick, tock;
}
set reset 0,
set RAM16K[0] 0,   // Set test arguments
set RAM16K[1] 2,
set RAM16K[2] -1;  // Ensure that progRAM16K initialized product to 0
repeat 80 {
  tick, tock;
}
set RAM16K[0] 0,   // Restore arguments in case progRAM16K used them as loop counter
set RAM16K[1] 2,
output;

set reset 1,
repeat 2 {
  tick, tock;
}
set reset 0,
set RAM16K[0] 3,   // Set test arguments
set RAM16K[1] 1,
set RAM16K[2] -1;  // Ensure that progRAM16K initialized product to 0
repeat 120 {
  tick, tock;
}
set RAM16K[0] 3,   // Restore arguments in case progRAM16K used them as loop counter
set RAM16K[1] 1,
output;

set reset 1,
repeat 2 {
  tick, tock;
}
set reset 0,
set RAM16K[0] 2,   // Set test arguments
set RAM16K[1] 4,
set RAM16K[2] -1;  // Ensure that progRAM16K initialized product to 0
repeat 150 {
  tick, tock;
}
set RAM16K[0] 2,   // Restore arguments in case progRAM16K used them as loop counter
set RAM16K[1] 4,
output;

set reset 1,
repeat 2 {
  tick, tock;
}
set reset 0,
set RAM16K[0] 6,   // Set test arguments
set RAM16K[1] 7,
set RAM16K[2] -1;  // Ensure that progRAM16K initialized product to 0
repeat 210 {
  tick, tock;
}
set RAM16K[0] 6,   // Restore arguments in case progRAM16K used them as loop counter
set RAM16K[1] 7,
output;
