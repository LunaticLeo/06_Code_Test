-module(try_erlang).
%% -export([start/0,while/1,while/2]).
-compile(export_all).
-include_lib("./try_erlang.hrl").

start()->
    #ship{id=1,name="yufuliao"}.

show(Input)->
    io:fwrite("~w",[Input#ship.id]).

while(Arr) -> while(Arr,0).
while([],Index) -> Index;
while([Element|Arr],Index) -> 
    io:fwrite("~w\t~w\n",[Index,Element]),
    while(Arr,Index+1).

%% eb 7 exercise 5
mult(Num,Num2) ->
    Num*Num2.

double(Num) ->
    Num*2.

distance(Tuple,Tuple2) ->
    {X , Y} = Tuple,
    {X2 , Y2 } = Tuple2,
    DisX = X2 - X,
    DisY = Y2 - Y,
    %math:sqrt(DisX * DisX + DisY*DisY).
    DisX * DisX + DisY*DisY.
    