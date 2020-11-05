from kanren import *
from pyDatalog.pyDatalog import  assert_fact, retract_fact, load, ask
from pyDatalog import pyDatalog
pyDatalog.create_terms('parent,Rickard,Eddard,Brandon,Benjen,Robb, Rickon,Bran,Jon,Frank,Lyarra,Lyanna, Catelyn,Sansa,Cersei,Daenerys,Stacey, ancestor,descendents,manager, X,Y,Z,N,N1,F,  factorial, first_remainder, odd,even, _split')

i = 0
parent = Relation()
people = Relation()

facts(people, ("Rickard", "Male"),
      ("Eddard", "Male"),
      ("Brandon", "Male"),
      ("Benjen", "Male"),
      ("Robb", "Male"),
      ("Rickon", "Male"),
      ("Bran", "Male"),
      ("Jon", "Male"),
      ("Frank", "Male"),
      ("Justin", "Male"),
      ("Lyarra", "Female"),
      ("Lyanna", "Female"),
      ("Catelyn", "Female"),
      ("Sansa", "Female"),
      ("Cersei", "Female"),
      ("Daenerys", "Female"),
      ("Stacey", "Female"),
      ("Dallis", "Female"),
      ("CeeCee", "Female"))

facts(parent, ("Eddard", "Rickard"),
      ("Brandon", "Rickard"),
      ("Benjen", "Rickard"),
      ("Lyanna", "Rickard"),
      ("Eddard", "Lyarra"),
      ("Brandon", "Lyarra"),
      ("Benjen", "Lyarra"),
      ("Lyanna", "Lyarra"),
      ("Robb", "Eddard"),
      ("Sansa", "Eddard"),
      ("Arya", "Eddard"),
      ("Bran", "Eddard"),
      ("Rickon", "Eddard"),
      ("Jon", "Eddard"),
      ("Robb", "Catelyn"),
      ("Sansa", "Catelyn"),
      ("Arya", "Catelyn"),
      ("Bran", "Catelyn"),
      ("Rickon", "Catelyn"),
      ("Jon", "Catelyn"),
      ("Cersei", "Jon"),
      ("Cersei", "Daenerys"),
      ("Frank", "Rickon"),
      ("Stacey", "Frank"),
      ("Lyarra", "Justin"),
      ("Lyarra", "Dallis"),
      ("CeeCee", "Jon"),
      ("CeeCee", "Daenerys"))


# need to figure out how to get it from printing own name as sibling
#function to print all siblings
def sibling_of(x, s):
    p = var()
    return conde((parent(x, p), parent(s, p)))


what = var()
name1 = "Jon"
output1 = run(0, what, sibling_of(name1, what))
siblings = [x for x in output1 if x != name1]
print("Siblings of", name1, "are: ")
for who in siblings:
    print(who)
print('*' * 50)

#function to print brother
def brother_of(x, m):
    return conde((sibling_of(x, m), people(m, "Male")))


name2 = "Brandon"
output2 = run(0, what, brother_of(name2, what))
brothers = [x for x in output2 if x != name2]
print("Brothers of", name2, "are: ")
for who in brothers:
    print(who)
print('*' * 50)

#function to print sister
def sister_of(x, m):
    return conde((sibling_of(x, m), people(m, "Female")))


name3 = "Jon"
output3 = run(0, what, sister_of(name3, what))
sisters = [x for x in output3 if x != name3]
print("Sisters of", name3, "are: ")
for who in sisters:
    print(who)
print('*' * 50)

#function to print mother
def mother_of(x, m):
    return conde((parent(x, m), people(m, "Female")))


name4 = "Jon"
print("Mother of", name4, "is: ")
for who in run(0, what, mother_of(name4, what)):
    print(who)
print('*' * 50)

#function to print father
def father_of(x, m):
    return conde((parent(x, m), people(m, "Male")))


name5 = "Eddard"
print("Father of", name5, "is: ")
for who in run(0, what, father_of(name5, what)):
    print(who)
print('*' * 50)

#function to print grandparents
def gp_of(x, gp):
    p = var()
    return conde((parent(x, p), parent(p, gp)))


name6 = "Robb"
print("Grandparents of", name6, "are: ")
gp = run(0, what, gp_of(name6, what))
for who in gp:
    print(who)
print('*' * 50)

#function to print uncles and aunts
def uncle_or_aunt(x, w):
    p = var()
    return conde((parent(x, p), sibling_of(p, w)))


name7 = "Sansa"
father = run(0, what, father_of(name7, what))[0]
mother = run(0, what, mother_of(name7, what))[0]
output4 = run(0, what, uncle_or_aunt(name7, what))
print("Uncle or Aunt of", name7, " are: ")
u_o_a = [x for x in output4 if x != father and x != mother]
for who in u_o_a:
    print(who)
print('*' * 50)

#function to print uncles
def uncle_of(x, w):
    return conde((uncle_or_aunt(x, w), people(w, "Male")))


name8 = "Cersei"
father = run(0, what, father_of(name8, what))[0]
print("Uncle of", name8, "are: ")
output5 = run(0, what, uncle_of(name8, what))
uncle = [x for x in output5 if x != father]
for who in uncle:
    print(who)
print('*' * 50)


#function to print aunts
def aunt_of(x, w):
    return conde((uncle_or_aunt(x, w), people(w, "Female")))


name9 = "Bran"
mother = run(0, what, mother_of(name9, what))[0]
print("Aunt of", name9, "are: ")
output6 = run(0, what, aunt_of(name9, what))
aunt = [x for x in output6 if x != mother]
for who in aunt:
    print(who)
print('*' * 50)


#Function to print cousins
def cousin_of(x,c):
    gp = var()
    return conde((gp_of(x, gp), gp_of(c, gp)))

print("Cousin of Cersei are:")
output7 = run(0, what, cousin_of("Cersei", what))
output8 = run(0, what, sibling_of("Cersei", what))
cousins = [x for x in output7 if x!= "Cersei" and x not in output8]
for who in cousins:
    print(who)
print('*' * 50)
#returns both parents


#function to print Ancestors
print("Ancestors of Cersei are :")
load ( """ 
    + parent('Eddard', 'Rickard')
    + parent('Brandon', 'Rickard')
    + parent('Benjen', 'Rickard')
    + parent('Lyanna', 'Rickard')
    + parent('Eddard', 'Lyarra')
    + parent('Brandon', 'Lyarra')
    + parent('Benjen', 'Lyarra')
    + parent('Lyanna', 'Lyarra')
    + parent('Robb', 'Eddard')
    + parent('Sansa', 'Eddard')
    + parent('Arya', 'Eddard')
    + parent('Bran', 'Eddard')
    + parent('Rickon', 'Eddard')
    + parent('Jon', 'Eddard')
    + parent('Robb', 'Catelyn')
    + parent('Sansa', 'Catelyn')
    + parent('Arya', 'Catelyn')
    + parent('Bran', 'Catelyn')
    + parent('Rickon', 'Catelyn')
    + parent('Jon', 'Catelyn')
    + parent('Cersei', 'Jon')
    + parent('Cersei', 'Daenerys')
    + parent('Frank', 'Rickon')
    + parent('Stacey', 'Frank')
    + parent('Lyarra','Justin')
    + parent('Lyarra','Dallis')



# specify what an ancestor is
ancestor(X,Y) <= parent(X,Y)
ancestor(X,Y) <= parent(X,Z) & ancestor(Z,Y)
    """ ) 
print ( ask ( "ancestor('Cersei',X)" ))
