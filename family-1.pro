c:-['family.pro'].

% facts

male('Rickard').
male('Eddard').
male('Brandon').
male('Benjen').
male('Robb').
male('Rickon').
male('Bran').
male('Jon').

female('Lyarra').
female('Lyanna').
female('Catelyn').
female('Sansa').
female('Arya').
female('Cersei').
female('Daenerys').

parent_of('Eddard', 'Rickard').
parent_of('Brandon', 'Rickard').
parent_of('Benjen', 'Rickard').
parent_of('Lyanna', 'Rickard').
parent_of('Eddard', 'Lyarra').
parent_of('Brandon', 'Lyarra').
parent_of('Benjen', 'Lyarra').
parent_of('Lyanna', 'Lyarra').
parent_of('Robb', 'Eddard').
parent_of('Sansa', 'Eddard').
parent_of('Arya', 'Eddard').
parent_of('Bran', 'Eddard').
parent_of('Rickon', 'Eddard').
parent_of('Jon', 'Eddard').
parent_of('Robb', 'Catelyn').
parent_of('Sansa', 'Catelyn').
parent_of('Arya', 'Catelyn').
parent_of('Bran', 'Catelyn').
parent_of('Rickon', 'Catelyn').
parent_of('Jon', 'Catelyn').
parent_of('Cersei', 'Jon').
parent_of('Cersei', 'Daenerys').



% rules
sibling_of(X,S):-parent_of(X,P),parent_of(S,P),X\==S.

brother_of(X,B):-sibling_of(X,B),male(B).

sister_of(X,S):-sibling_of(X,S),female(S).

mother_of(X,M):-parent_of(X,M),female(M).

father_of(X,M):-parent_of(X,M),male(M).

gp_of(X,GP):-parent_of(X,P),parent_of(P,GP).

cousin_of(X,C):-
  gp_of(X,GP),
  gp_of(C,GP),
  X\==C,
  not(sibling_of(X,C)).
  
uncle_or_aunt_of(X,Who):-
  parent_of(X,P),
  sibling_of(P,Who).
  
uncle_of(X,Who):-uncle_or_aunt_of(X,Who),male(Who).

aunt_of(X,Who):-uncle_or_aunt_of(X,Who),female(Who).

ancestor_of(Person, Ancestor) :- parent_of(Person, Ancestor).

ancestor_of(Person, Ancestor) :-
	parent_of(Person, X),
	ancestor_of(X, Ancestor).