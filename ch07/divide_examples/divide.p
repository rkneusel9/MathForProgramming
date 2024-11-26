program Divide(input, output, stderr);

var
    a,b,q,r : integer;

begin
    a:=33; b:=7; q:=a div b; r:=a mod b;
    writeLn(a:4, b:4, q:4, r:4);
    a:=-33; b:=7; q:=a div b; r:=a mod b;
    writeLn(a:4, b:4, q:4, r:4);
    a:=33; b:=-7; q:=a div b; r:=a mod b;
    writeLn(a:4, b:4, q:4, r:4);
    a:=-33; b:=-7; q:=a div b; r:=a mod b;
    writeLn(a:4, b:4, q:4, r:4);
end.

