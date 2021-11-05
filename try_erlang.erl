-module(try_erlang).
-export([start/0,while/1,while/2]).


start() ->
    Arr = [1,3,5,7,9],
    % while(Arr).
    Element = Arr/0,
    io:fwrite(Element).

while(Arr) -> while(Arr,0).
while([],Index) -> Index;
while([Element|Arr],Index) -> 
    io:fwrite("~w\t~w\n",[Index,Element]),
    while(Arr,Index+1).
    