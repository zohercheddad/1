Python 3.6.0rc2 (v3.6.0rc2:800a67f7806d, Dec 16 2016, 23:22:07) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 11/6
1.8333333333333333
>>> type(zozo)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    type(zozo)
NameError: name 'zozo' is not defined
>>> type (3.2)
<class 'float'>
>>> type (true)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type (true)
NameError: name 'true' is not defined
>>> type (0)
<class 'int'>
>>> a =4
>>> message =
SyntaxError: invalid syntax
>>> print(a)
4
>>> zozo = 0.0
>>> print(zozo) =
SyntaxError: invalid syntax
>>>  print(zozo)
 
SyntaxError: unexpected indent
>>> print (a , zozo)
4 0.0
>>> message = '2 * 2'
>>> print (a,message)
4 2 * 2
>>> message = '2*2='
>>> print (a,message)
4 2*2=
>>> x =5
>>> y =10
>>> z =x
>>>  x = 4*5
 
SyntaxError: unexpected indent
>>> x = 4*x
>>> y = 4*y
>>> z = x * y
>>> print(x,y,z)
20 40 800
>>> type(x)
<class 'int'>
>>> 15%3
0
>>> 16%3
1
>>> 7%2
1
>>> 7**7
823543
>>> 7**2
49
>>> 6//2
3
>>> 7//2
3
>>> 5//5
1
>>> 6//5
1
>>> 5*(3+2)
25
>>> 5*3+2
17
>>> 5.0/2
2.5
>>> 5.0//2
2.0
>>> x =5
>>> 10+x
15
>>> x =(x -3.0)**4
>>> x
16.0
>>> message = 'hello' +'world'
>>> print(message)
helloworld
>>> 'zo'*2
'zozo'
>>> x =( x-3)**4
>>> x
28561.0
>>> x =5
>>> x =( x-3)**4
>>> x
16
>>>  message = 'hello' +' world'
 
SyntaxError: unexpected indent
>>> message = 'hello' +''+'world'
>>> message
'helloworld'
>>> print(message)
helloworld
>>> message = 'hello' +' '+'world' +'!'
>>> message
'hello world!'
>>> print('hello' *6)
hellohellohellohellohellohello
>>> print (2**2,2**3)
4 8
>>> print ('bonj \t bonj')
bonj 	 bonj
>>> print ( 'zo \n zo')
zo 
 zo
>>> print( '//' ,' \'')
//  '
>>> nom = input ("entrez votre nom:")
entrez votre nom:zoher
>>> print(nom)
zoher
>>> type(nom)
<class 'str'>
>>> prenom = input ("vous prenomer comment?")
vous prenomer comment?zot
>>> prenom = input ("vous prenomer comment?")#lolo
vous prenomer comment?zo
>>> v =6 #c'est la vitesse en km/h
>>> """blabla blabla
blabla
blabla"""
'blabla blabla\nblabla\nblabla'
>>> '''
blabla blabla
blabla blabla
blabla blabla
'''
'\nblabla blabla\nblabla blabla\nblabla blabla\n'
>>> import math
>>> rayon = input ("rentre le rayon")
rentre le rayon4
>>> rayon = float (rayon)
>>> aire = math.pi*(rayon ** 2 )
>>> print ("air" + str (aire) + " cm carres ")
air50.26548245743669 cm carres 
>>> aire
50.26548245743669
>>> air
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    air
NameError: name 'air' is not defined
>>> aire
50.26548245743669
>>> 
