-module(try_erlang).
%% -export([start/0,while/1,while/2]).
-compile(export_all).
-include_lib("./try_erlang.hrl").

echo()->
    io:fwrite("aa").

start()->
    Pid = spawn(fun echo/0),
    Pid ! {"aaa"}.

-spec try_spec(Input::integer()) ->atom().

try_spec(_)->
    ok.

try_tryCatch(Input)->
    try Input() of
        aa -> aa
    catch
        Aa -> Aa
    end.