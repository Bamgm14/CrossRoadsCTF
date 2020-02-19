

push ebp
mov ebp, esp

sub esp, 60

mov [esp-16], 3
mov [esp-4], 16

push 10
push 14
call someFuncThatTakesTwoArgs

sub esp, 8

push 100





