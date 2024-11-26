The file DX.LISP contains 1980s era Lisp code that implements
symbolic differentiation.  It originally ran on a Data General MV/8000
mainframe using a Lisp interpreter written in FORTRAN.

The main function is at the bottom, DX.  It expects a list representing
the function to differentiate using standard Lisp prefix notation:

cos(3*x-4)

becomes:

(COS (- (* 3 X) 4))

which, for the old Lisp interpreter becomes:

(COS (DIFFERENCE (TIMES 3 X) 4))

The output of DX is the derivative of the argument
to DERIV given in the above format after passing the derivative
to SIMPLIFY to handle easy transformations and then INFIX
to convert the prefix format answer to a fully-parenthesized
infix expression.

I'm putting the code here for two purposes.  First, as an example
of how compact symbolic manipulation can be and second, as a challenge
exercise for you to transform the 40 year old code into a modern
language like Python or Scheme.

If you do, and you get it working, let me know: rkneuselbooks@gmail.com

