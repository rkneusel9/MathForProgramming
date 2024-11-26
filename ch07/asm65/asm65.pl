#!/usr/bin/perl -w
#
# Asm65 - simple 65c02 assembler, RTK, 13-Mar-00
#
# Last update:  22-Jun-00
#
# Assembles Merlin-style (simplified) source to binary
# for Apple II computers (or others).  See asm65.txt
# for more info.  Really meant to assemble the output
# from the SPL compiler.  Use at own risk.  It is
# _very_ unforgiving!
#
##################################################################

use strict;

#############################################
#
#            Data Structures
#
#############################################

my %ops = (
#           imp   imm   zpg   zpx   zpy   zpi   inx   iny   abs   abx   aby   ind   idx
  'ADC' => [0x00, 0x69, 0x65, 0x75, 0x00, 0x72, 0x61, 0x71, 0x6D, 0x7D, 0x79, 0x00, 0x00],
  'AND' => [0x00, 0x29, 0x25, 0x35, 0x00, 0x32, 0x21, 0x31, 0x2D, 0x3D, 0x39, 0x00, 0x00],
  'ASL' => [0x0A, 0x00, 0x06, 0x16, 0x00, 0x00, 0x00, 0x00, 0x0E, 0x1E, 0x00, 0x00, 0x00],
  'BCC' => [0x00, 0x90, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'BCS' => [0x00, 0xB0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'BEQ' => [0x00, 0xF0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'BIT' => [0x00, 0x89, 0x24, 0x34, 0x00, 0x00, 0x00, 0x00, 0x2C, 0x3c, 0x00, 0x00, 0x00],
  'BMI' => [0x00, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'BNE' => [0x00, 0xD0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'BPL' => [0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'BRA' => [0x00, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'BRK' => [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'BVC' => [0x00, 0x50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'BVS' => [0x00, 0x70, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'CLC' => [0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'CLD' => [0xD8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'CLI' => [0x58, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'CLV' => [0xB8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'CMP' => [0x00, 0xC9, 0xC5, 0xD5, 0x00, 0xD2, 0xC1, 0xD1, 0xCD, 0xDD, 0xD9, 0x00, 0x00],
  'CPX' => [0x00, 0xE0, 0xE4, 0x00, 0x00, 0x00, 0x00, 0x00, 0xEC, 0x00, 0x00, 0x00, 0x00],
  'CPY' => [0x00, 0xC0, 0xC4, 0x00, 0x00, 0x00, 0x00, 0x00, 0xCC, 0x00, 0x00, 0x00, 0x00],
  'DEA' => [0x3A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'DEC' => [0x00, 0x00, 0xC6, 0xD6, 0x00, 0x00, 0x00, 0x00, 0xCE, 0xDE, 0x00, 0x00, 0x00],
  'DEX' => [0xCA, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'DEY' => [0x88, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'EOR' => [0x00, 0x49, 0x45, 0x55, 0x00, 0x52, 0x41, 0x51, 0x4D, 0x5D, 0x59, 0x00, 0x00],
  'INC' => [0x00, 0x00, 0xE6, 0xF6, 0x00, 0x00, 0x00, 0x00, 0xEE, 0xFE, 0x00, 0x00, 0x00],
  'INA' => [0x1A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'INX' => [0xE8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'INY' => [0xC8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'JMP' => [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x4C, 0x00, 0x00, 0x6C, 0x7C],
  'JSR' => [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00],
  'LDA' => [0x00, 0xA9, 0xA5, 0xB5, 0x00, 0xB2, 0xA1, 0xB1, 0xAD, 0xBD, 0xB9, 0x00, 0x00],
  'LDX' => [0x00, 0xA2, 0xA6, 0x00, 0xB6, 0x00, 0x00, 0x00, 0xAE, 0x00, 0xBE, 0x00, 0x00],
  'LDY' => [0x00, 0xA0, 0xA4, 0xB4, 0x00, 0x00, 0x00, 0x00, 0xAC, 0xBC, 0x00, 0x00, 0x00],
  'LSR' => [0x4A, 0x00, 0x46, 0x56, 0x00, 0x00, 0x00, 0x00, 0x4E, 0x5E, 0x00, 0x00, 0x00],
  'NOP' => [0xEA, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'ORA' => [0x00, 0x09, 0x05, 0x15, 0x00, 0x12, 0x01, 0x11, 0x0D, 0x1D, 0x19, 0x00, 0x00],
  'PHA' => [0x48, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'PHP' => [0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'PHX' => [0xDA, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'PHY' => [0x5A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'PLA' => [0x68, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'PLP' => [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'PLX' => [0xFA, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'PLY' => [0x7A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'ROL' => [0x2A, 0x00, 0x26, 0x36, 0x00, 0x00, 0x00, 0x00, 0x2E, 0x3E, 0x00, 0x00, 0x00],
  'ROR' => [0x6A, 0x00, 0x66, 0x76, 0x00, 0x00, 0x00, 0x00, 0x6E, 0x7E, 0x00, 0x00, 0x00],
  'RTI' => [0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'RTS' => [0x60, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'SBC' => [0x00, 0xE9, 0xE5, 0xF5, 0x00, 0xF2, 0xE1, 0xF1, 0xED, 0xFD, 0xF9, 0x00, 0x00],
  'SEC' => [0x38, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'SED' => [0xF8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'SEI' => [0x78, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'STA' => [0x00, 0x00, 0x85, 0x95, 0x00, 0x92, 0x81, 0x91, 0x8D, 0x9D, 0x99, 0x00, 0x00],
  'STX' => [0x00, 0x00, 0x86, 0x00, 0x96, 0x00, 0x00, 0x00, 0x8E, 0x00, 0x00, 0x00, 0x00],
  'STY' => [0x00, 0x00, 0x84, 0x94, 0x00, 0x00, 0x00, 0x00, 0x8C, 0x00, 0x00, 0x00, 0x00],
  'TAX' => [0xAA, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'TAY' => [0xA8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'TSX' => [0xBA, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'TXA' => [0x8A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'TXS' => [0x9A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'TYA' => [0x98, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
  'STZ' => [0x00, 0x00, 0x64, 0x74, 0x00, 0x00, 0x00, 0x00, 0x9C, 0x9E, 0x00, 0x00, 0x00],
  'TRB' => [0x00, 0x00, 0x14, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1C, 0x00, 0x00, 0x00, 0x00],
  'TSB' => [0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x00, 0x00, 0x00, 0x00]
);

# pseudo ops:

my %pseudo = ( 'EQU' => 0, 'ORG' => 1, 'ASC' => 2, 'HEX' => 3, 'DS' => 4 );

# Memory:

my @mem;  # 64k RAM max.

# Labels:

my %lbls;

# Default switch values, global:

my $txt_file = 0;
my $sym_list = 0;
my @in_name  = ("input.s");  # input files
my $out_name = "asm.out";


#############################################
#
#              Functions
#
#############################################

sub help {  # output help screen
  print "\nAsm65 :: a simple 65C02 assembler.  RTK, April 2000\n",
        "=====================================================\n\n",
        "Use: asm65 [-ts] [ -o <output>] source1 source2 ..\n\n",
        "Switches:\n\n",
        "   s  -- symbol table listing to <output>.sym\n",
        "   t  -- text output for Apple II\n",
        "   o  -- output to file name, else 'asm.out'\n",
        "\n";
}


sub do_switches {  # setup switches
  my $i;
  for($i=1; $i < length($_[0]); $i++) {
    my $c = substr($_[0],$i,1);
    if ($c eq "t") { $txt_file = 1; }
    if ($c eq "s") { $sym_list = 1; }
  }
}


sub process_cmd_line {  # get command line info
  my $q = shift @ARGV;
  if ((substr($q,0,1) eq "-") && ($q ne "-o")) { 
    &do_switches($q); 
    $q = shift @ARGV;
  }
  if ($q eq "-o") { $out_name = shift @ARGV; }
  else { unshift @ARGV,$q; }
  @in_name = @ARGV;
}


sub parse {  # parse an input line into fields
  my $label = ""; 
  my $inst  = "";
  my $oper  = "";
  my $cmt   = "";
  my $line = shift;
  my $token;

  $line =~ s/^\s+//;  # purge leading whitespace 
  $line =~ s/\s+$//;  # purge trailing whitespace
  
  # change spaces between "quotes" to \001 chars:

  my $n = "";  my $f=0;
  for(my $i=0; $i<length($line); $i++) {
    if (substr($line,$i,1) eq '"') {
      $f = ($f==0) ? 1 : 0;
    }
    if ((substr($line,$i,1) eq ' ')&&($f)) {
      $n .= "\001";
    } else {
      $n .= substr($line,$i,1);
    }
  }
  $line = $n;

  my @line = split(/\s+/,$line);  # get line as an array of tokens

  # check for a comment line:

  if ((substr($line,0,1) eq '*') || (substr($line,0,1) eq ';')) {
    $cmt = $line;
    return ($label, $inst, $oper, $cmt);  # comment line
  }

  # parse line:

  while (@line) {
    $token = shift @line;
    if ((exists $ops{uc($token)})||(exists $pseudo{uc($token)})) {
      $inst = uc($token);
    } elsif (($label eq "")&&($inst eq "")) {
      $label = uc($token);
    } elsif (($oper eq "")&&($inst ne "")) {
      $oper = &restore($token);
      $oper = uc($oper) unless ($inst eq 'ASC');
    } elsif ($token eq ';') {
      $cmt = &restore(join(' ',@line));
      @line = ();
    }
  }
  return ($label, $inst, $oper, $cmt);
}

sub restore {  # return a string with \001 chars replaced by spaces
  my $s = shift;
  $s =~ s/\001/\ /g;
  return $s;
}

sub bomb { # error out
  my ($err, $msg) = @_;
  if ($err == 1) {
    print "**** Error, undefined label: $msg\n";
  }
  exit(1);
}


#############################################
#
#                Main
#
#############################################

# handle command line args:

if ($#ARGV==-1) {
  &help;               # help screen
  exit(0);
} else {
  &process_cmd_line;   # process command line args
}

# diagnostics:

#print "Switches: $sym_file \n";
#print "Output  : $out_name\n";
#print "Input   : ", join(" ",@in_name), "\n";

# input all source code:

my @src = ();

for my $f (@in_name) {
  open(FILE,$f);
  my @text = <FILE>;
  close(FILE);
  push @src, @text;
} 

################################
#
# Pass 0.. get starting address
#
################################

my $start = 0x800;  # a good place for the Apple II

for my $line (@src) {
  my ($label, $inst, $oper, $cmt) = &parse($line);
  # print "<$label> <$inst> <$oper> <$cmt> :: $line";
  if ( uc($inst) eq 'ORG' ) {
    $oper  = substr($oper, 1);  # remove '$'
    $start = hex($oper);        # eval operand field to get ORG
  }
}

# debug:
# printf "\nStarting address: \$%X (%d decimal)\n\n", $start, $start;


#####################################################
#
# Pass 1.. get references and their actual addresses
#
#####################################################

my $pc = $start;   # program counter
my $ptr = 0;       # pointer into memory
my $i;

for my $line (@src) {
  my ($label, $inst, $oper, $cmt) = &parse($line);
  
  if (($inst eq 'EQU') || ($inst eq 'ORG')) {
    $i = 0;
  } elsif ($inst eq 'ASC') {
      $i = length($oper)-2;                           # ASC
  } elsif ($inst eq 'HEX') {
      $i = length($oper)/2;                           # HEX
  } elsif ($inst eq 'DS') {
      $i = hex(substr($oper,1));                      # DS
  } elsif (defined $ops{$inst}) {
    if ($oper eq '')          { $i = 1; }             # implied 
    elsif ($oper =~ /^\#\$\w\w$/) { $i = 2; }         # #$00
    elsif ($oper =~ /^\$\w\w$/) { $i = 2; }           # $00
    elsif ($oper =~ /^\$\w\w,X$/) { $i = 2; }         # $00,X
    elsif ($oper =~ /^\$\w\w,Y$/) { $i = 2; }         # $00,Y
    elsif ($oper =~ /^\(\$\w\w\)$/) { $i = 2; }       # ($00)
    elsif ($oper =~ /^\(\$\w\w,X\)$/) { $i = 2; }     # ($00,X)
    elsif ($oper =~ /^\(\$\w\w\),Y$/) { $i = 2; }     # ($00),Y
    elsif ($oper =~ /^\$\w\w\w\w$/)    { $i = 3; }    # $0000
    elsif ($oper =~ /^\$\w\w\w\w,X$/)   { $i = 3; }   # $0000,X
    elsif ($oper =~ /^\$\w\w\w\w,Y$/)   { $i = 3; }   # $0000,Y
    elsif ($oper =~ /^\(\$\w\w\w\w\)$/) { $i = 3; }   # ($0000)
    elsif ($oper =~ /^\(\$\w\w\w\w,X\)$/) { $i = 3; } # ($0000,X)
    elsif ($oper =~ /^\#\<\$\w\w\w\w$/) { $i = 2; }   # #<$0000
    elsif ($oper =~ /^\#\>\$\w\w\w\w$/) { $i = 2; }   # #>$0000
    elsif ($oper =~ /^\#\<\w+$/) { $i = 2; }          # #<label
    elsif ($oper =~ /^\#\>\w+$/) { $i = 2; }          # #>label
    elsif ($oper =~ /^\w+,X$/) { $i = 3; }            # label,X
    elsif ($oper =~ /^\w+,Y$/) { $i = 3; }            # label,Y
    elsif ($oper =~ /^\(\w+\)$/) { $i = 3; }          # (label)
    elsif ($oper =~ /^\(\w+,X\)$/) { $i = 3; }        # (label,X)
    elsif ($oper =~ /^\(\w+\),Y$/) { $i = 2; }        # (label),Y
    elsif ($oper =~ /^\w+$/) { $i = 3; }              # label
    if (($inst eq 'BCC')||($inst eq 'BCS')||($inst eq 'BEQ')||
        ($inst eq 'BMI')||($inst eq 'BNE')||($inst eq 'BPL')||
        ($inst eq 'BRA')||($inst eq 'BVC')||($inst eq 'BVS')) { $i = 2; }
  } else { $i = 0; }
  
  if (($label ne '') && ($inst ne 'EQU') && ($inst ne 'ORG')) {
    $lbls{$label} = $pc;
  }
  
  if (($label ne '') && ($inst eq 'EQU')) {
    $lbls{$label} = hex(substr($oper,1));
  }
  
  # debug
  # print "<$label> <$inst> <$oper> <$cmt> , size = $i\n";
  
  $pc += $i;
} 


#######################
#
# Pass 2.. output code
#
#######################

$pc = $start;   # program counter
$ptr = 0;       # pointer into memory

for my $line (@src) {
  my ($label, $inst, $oper, $cmt) = &parse($line);
  
  if (($inst eq 'EQU') || ($inst eq 'ORG')) {
    $i = 0;
  } elsif ($inst eq 'ASC') {
      $i = length($oper)-2;                           # ASC
      $oper =~ s/^\"//;   # purge quotes
      $oper =~ s/\"$//;
      for(my $k=0;$k<length($oper);$k++) {
        $mem[$ptr+$k] = 0x80 + ord(substr($oper,$k,1));
      }
  } elsif ($inst eq 'HEX') {
      $i = length($oper)/2;                           # HEX
      for(my $k=0;$k<length($oper);$k+=2) {
        $mem[$ptr+$k/2] = hex(substr($oper,$k,2));
      }
  } elsif ($inst eq 'DS') {
      $i = hex(substr($oper,1));                      # DS
      for(my $k=0;$k<$i;$k++) { $mem[$ptr+$k]=0; }
  } elsif (defined $ops{$inst}) {
    if ($oper eq '')          { 
      $i = 1;                                         # implied
      $mem[$ptr] = ${$ops{$inst}}[0];
    } elsif ($oper =~ /^\#\$\w\w$/) { 
      $i = 2;                                         # #$00
      $mem[$ptr]   = ${$ops{$inst}}[1];
      $mem[$ptr+1] = hex(substr($oper,2,2));
    } elsif ($oper =~ /^\$\w\w$/) { 
      $i = 2;                                         # $00
      $mem[$ptr]   = ${$ops{$inst}}[2];
      $mem[$ptr+1] = hex(substr($oper,1,2));
    } elsif ($oper =~ /^\$\w\w,X$/) { 
      $i = 2;                                         # $00,X
      $mem[$ptr]   = ${$ops{$inst}}[3];
      $mem[$ptr+1] = hex(substr($oper,1,2));
    } elsif ($oper =~ /^\$\w\w,Y$/) { 
      $i = 2;                                         # $00,Y
      $mem[$ptr]   = ${$ops{$inst}}[4];
      $mem[$ptr+1] = hex(substr($oper,1,2));
    } elsif ($oper =~ /^\(\$\w\w\)$/) { 
      $i = 2;                                         # ($00)
      $mem[$ptr]   = ${$ops{$inst}}[5];
      $mem[$ptr+1] = hex(substr($oper,2,2));
    } elsif ($oper =~ /^\(\$\w\w,X\)$/) { 
      $i = 2;                                         # ($00,X)
      $mem[$ptr]   = ${$ops{$inst}}[6];
      $mem[$ptr+1] = hex(substr($oper,2,2));
    } elsif ($oper =~ /^\(\$\w\w\),Y$/) { 
      $i = 2;                                         # ($00),Y
      $mem[$ptr]   = ${$ops{$inst}}[7];
      $mem[$ptr+1] = hex(substr($oper,2,2));
    } elsif ($oper =~ /^\$\w\w\w\w$/) { 
      $i = 3;                                         # $0000
      $mem[$ptr]   = ${$ops{$inst}}[8];
      $mem[$ptr+1] = hex(substr($oper,3,2));
      $mem[$ptr+2] = hex(substr($oper,1,2));
      if (($inst eq 'BCC')||($inst eq 'BCS')||($inst eq 'BEQ')||
          ($inst eq 'BMI')||($inst eq 'BNE')||($inst eq 'BPL')||
          ($inst eq 'BRA')||($inst eq 'BVC')||($inst eq 'BVS')) { 
        $i = 2; 
        $mem[$ptr]   = ${$ops{$inst}}[1];  # really two bytes
        if ($pc > hex(substr($oper,1,4))) {
          $mem[$ptr+1] = (255-($pc-hex(substr($oper,1,4))+1)) & 0xFF;
        } else {
          $mem[$ptr+1] = (hex(substr($oper,1,4))-$pc-2) & 0xFF;
        }
      }
    } elsif ($oper =~ /^\$\w\w\w\w,X$/) { 
      $i = 3;                                         # $0000,X
      $mem[$ptr]   = ${$ops{$inst}}[9];
      $mem[$ptr+1] = hex(substr($oper,3,2));
      $mem[$ptr+2] = hex(substr($oper,1,2));
    } elsif ($oper =~ /^\$\w\w\w\w,Y$/) { 
      $i = 3;                                         # $0000,Y
      $mem[$ptr]   = ${$ops{$inst}}[10];
      $mem[$ptr+1] = hex(substr($oper,3,2));
      $mem[$ptr+2] = hex(substr($oper,1,2));
    } elsif ($oper =~ /^\(\$\w\w\w\w\)$/) { 
      $i = 3;                                         # ($0000)
      $mem[$ptr]   = ${$ops{$inst}}[11];
      $mem[$ptr+1] = hex(substr($oper,4,2));
      $mem[$ptr+2] = hex(substr($oper,2,2));
    } elsif ($oper =~ /^\(\$\w\w\w\w,X\)$/) { 
      $i = 3;                                         # ($0000,X)
      $mem[$ptr]   = ${$ops{$inst}}[12];
      $mem[$ptr+1] = hex(substr($oper,4,2));
      $mem[$ptr+2] = hex(substr($oper,2,2));
    } elsif ($oper =~ /^\#\<\$\w\w\w\w$/) { 
      $i = 2;                                         # #<$0000
      $mem[$ptr]   = ${$ops{$inst}}[1];
      $mem[$ptr+1] = hex(substr($oper,5,2));
    } elsif ($oper =~ /^\#\>\$\w\w\w\w$/) { 
      $i = 2;                                         # #>$0000
      $mem[$ptr]   = ${$ops{$inst}}[1];
      $mem[$ptr+1] = hex(substr($oper,3,2));
    } elsif ($oper =~ /^\#\<(\w+)$/) { 
      $i = 2;                                         # #<label
      $mem[$ptr]   = ${$ops{$inst}}[1];
      $mem[$ptr+1] = $lbls{$1}%256 if defined $lbls{$1};
      if (!defined $lbls{$1}) { &bomb(1,$1); }
    } elsif ($oper =~ /^\#\>(\w+)$/) { 
      $i = 2;                                         # #>label
      $mem[$ptr]   = ${$ops{$inst}}[1];
      $mem[$ptr+1] = $lbls{$1}/256 if defined $lbls{$1};
      if (!defined $lbls{$1}) { &bomb(1,$1); }
    } elsif ($oper =~ /^(\w+),X$/) { 
      $i = 3;                                         # label,X
      $mem[$ptr]   = ${$ops{$inst}}[9];
      $mem[$ptr+1] = $lbls{$1}%256 if defined $lbls{$1};
      $mem[$ptr+2] = $lbls{$1}/256 if defined $lbls{$1};
      if (!defined $lbls{$1}) { &bomb(1,$1); }
    } elsif ($oper =~ /^(\w+),Y$/) { 
      $i = 3;                                         # label,Y
      $mem[$ptr]   = ${$ops{$inst}}[10];
      $mem[$ptr+1] = $lbls{$1}%256 if defined $lbls{$1};
      $mem[$ptr+2] = $lbls{$1}/256 if defined $lbls{$1};
      if (!defined $lbls{$1}) { &bomb(1,$1); }
    } elsif ($oper =~ /^\((\w+)\)$/) { 
      $i = 3;                                         # (label)
      $mem[$ptr]   = ${$ops{$inst}}[11];
      $mem[$ptr+1] = $lbls{$1}%256 if defined $lbls{$1};
      $mem[$ptr+2] = $lbls{$1}/256 if defined $lbls{$1};
      if (!defined $lbls{$1}) { &bomb(1,$1); }
    } elsif ($oper =~ /^\((\w+),X\)$/) { 
      $i = 3;                                         # (label,X)
      $mem[$ptr]   = ${$ops{$inst}}[12];
      $mem[$ptr+1] = $lbls{$1}%256 if defined $lbls{$1};
      $mem[$ptr+2] = $lbls{$1}/256 if defined $lbls{$1};
      if (!defined $lbls{$1}) { &bomb(1,$1); }
    } elsif ($oper =~ /^\((\w+)\),Y$/) { 
      $i = 2;                                         # (label),Y
      $mem[$ptr]   = ${$ops{$inst}}[7];
      $mem[$ptr+1] = $lbls{$1}%256 if defined $lbls{$1};
      if (!defined $lbls{$1}) { &bomb(1,$1); }
    } elsif ($oper =~ /^(\w+)$/) { 
      $i = 3;                                         # label
      $mem[$ptr]   = ${$ops{$inst}}[8];
      $mem[$ptr+1] = $lbls{$1}%256 if defined $lbls{$1};
      $mem[$ptr+2] = $lbls{$1}/256 if defined $lbls{$1};
      if (!defined $lbls{$1}) { &bomb(1,$1); }
      if ((($inst eq 'BCC')||($inst eq 'BCS')||($inst eq 'BEQ')||
          ($inst eq 'BMI')||($inst eq 'BNE')||($inst eq 'BPL')||
          ($inst eq 'BRA')||($inst eq 'BVC')||($inst eq 'BVS'))&&(defined $lbls{$1})) { 
        $i = 2; 
        $mem[$ptr]   = ${$ops{$inst}}[1];  # really two bytes
        if ($pc > $lbls{$1}) {
          $mem[$ptr+1] = (255-($pc-$lbls{$1}+1)) & 0xFF;
        } else {
          $mem[$ptr+1] = ($lbls{$1}-$pc-2) & 0xFF;
        }
      }
    }
  } else { 
    $i = 0;   # a blank line
  }
    
  $pc += $i;    # position in real memory
  $ptr += $i;   # position within buffer
} 

# debug
#  my $c=1;
#  for my $k (@mem) {
#    printf("[%02X:%02X] ", $c, $k) if defined $k;
#    printf("[%02X:00] ", $c, $k) unless defined $k;
#    if (($c % 15) == 0) { print "\n"; }
#    $c++;
#  }

#############################################################
#
# Finish up.. write code to disk + symbol table if asked for
#
#############################################################

if ($txt_file==1) {   # output text for Apple II
  open(FILE, '>' . $out_name);
  print FILE "CALL-151\n";
  my $finis = $#mem;
  push @mem, (0, 0, 0, 0, 0, 0, 0, 0);
  for(my $k=0; $k<=$finis;$k+=8) {
    printf FILE "%04X : %02X %02X %02X %02X %02X %02X %02X %02X \n", ($start+$k), 
      $mem[$k], $mem[$k+1], $mem[$k+2], $mem[$k+3], $mem[$k+4], 
      $mem[$k+5], $mem[$k+6], $mem[$k+7];
  }
  print FILE "BSAVE ",uc($out_name),",A",$start,",L",$#mem,"\n";  
} else {              # output binary data
  open(FILE, '>' . $out_name);
  for my $k (@mem) {
    print FILE chr($k);
  }
  close(FILE);
}

if ($sym_list==1) {
  open(FILE, '>' . $out_name . '.sym');
  for my $k (sort(keys %lbls)) {
    printf FILE "[%04X] %s\n", $lbls{$k}, $k;
  }  
  close(FILE);
}
