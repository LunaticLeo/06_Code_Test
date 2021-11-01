-module(ex1).
-compile(export_all).

start(N)-> 
    C = spawn(?MODULE, counter_servre, [0]),
    [spawn(?MODULE,turnstile,[C,50])||_ <-lists:seq(1,N)],
    C.