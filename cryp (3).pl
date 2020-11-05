go:-
  puzzle(Show,[0,1,2,3,4,5,6,7,8,9],_),
  Show,
  fail
; nl.

/*

  S E N D +
  M O R E
---------
M O N E Y

*/

% problem specific code
puzzle(show(T,E,X,A,S,N,V,D,L,K))-->

  add_digits(S,A,A,  0,C1),
  add_digits(A,D,K, C1,C2),
  add_digits(X,A,S, C2,C3),
  add_digits(E,V,A, C3,C4),
  add_digits(T,E,L, C4,C5),
  add_digits(0,N,A, C5, 0),


 {T>0, E>0}.

show(T,E,X,A,S,N,V,D,L,K):-
( write('  '),
  write([T,E,X,A,S]),
  write('+'),nl,
  write('  '),
  write([N,E,V,A,D,A]),
  write('='),nl,
  write([A,L,A,S,K,A]),nl,
  fail
; nl
).



% reusable code

digit(X)-->{integer(X)},!.
digit(X)-->sel(X).

add_digits(D1,D2,Res,C1,C2)-->
   digit(D1),
   digit(D2),
   digit(Res),
   {add_with_carry(D1,D2,C1, Res,C2)}.

add_with_carry(D1,D2,C1, Res,C2):-
    S is (D1+D2)+C1,
    Res is S mod 10,
    C2 is S // 10.

sel(X,[X|Xs],Xs).
sel(X,[Y|Xs],[Y|Ys]):-sel(X,Xs,Ys).

