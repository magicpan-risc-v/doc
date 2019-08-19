.globl _start;
_start:
  lui a5, 0x800;
  addi a5, a5, -8;
  lbu a0, 0(a5);
cyc:
  sb a0, 0(a5);
  j cyc;
