Transistor AND, OR, and NOT gate videos
---------------------------------------

Each video shows a breadboard implementation of the corresponding logic
gate.  The gates implement the circuits in Chapter 3 of Math for Programming.

The resistors are

R1 = 5 k ohm (I used 5.1 k in the videos)
R2 = 10 k ohm

R1 is there to drop the voltage on the common when the transistor is on.
R2 limits the current through the transistor when there's an input on the base.

The transistors themselves are NPN.  I used decades old 2N3904, which are
still available from Jameco for about $0.25 each.  I suspect any small
signal transistor will work, but make sure it's NPN.  The circuit for a
PNP transistor is different.

I connected push button switches from the 5V source to the transistor bases to act
as inputs.  Switch closed is 1, open is 0.

I ran the outputs through a 1 k ohm resistor followed by an LED to ground.  When
the LED is on, the output is 1, otherwise the output is 0.

For the videos, I used the 5V output on my benchtop power supply.  If you want to
use a battery, I recommend a 9V battery running through a 5V voltage regulator.

Jameco electronics has everything necessary for about $20, see the parts list
in jameco1.png, jameco2.png, and jameco3.png.

