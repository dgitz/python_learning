# Mutable vs Immutable
* If an object's value can change, it is `mutable`.<br>
* If an object's value cannot change, it is `immutable`.<br>

Example:<br>
`age = 42`<br>
`id(age)` >>> `9802560`<br>
`age = 43`<br>
`id(age)` >>> `9802592`<br>

Therefore, the type `int` is `immutable`.  `age` is just a name that points to a value.

Other data types that are `immutable`:
* numbers
* boolean
* string
* bytes

# Tuples
* Tuples are `immutable`.
* Tuples are an arbitrary sequence of Python objects separated by commas.

`t = () # Empty tuple`<br>
`type(t)` >>> `<class 'tuple'>`<br>

`one_element_tuple = (42,) # Need a trailing comma!`<br>
`three_element_tuple = (1,2,3) # Parentheses optional.`<br>

* Tuples support one-line swaps:<br>

`a,b = 1, 2`<br>
`a,b` >>> `(1,2)`<br>
`b,a = a,b`<br>
`a,b` >>> `(2,1)`<br>

# Lists
* Lists are `mutable`.
* Lists are similiar to tuples, but don't have restriction on immutability.
* Lists are commonlyused for storing collections of homogeneous objects, but they can be used for heterogeneous objects as well.

`a = [1,2,1,3]`<br>
`a.append(13)`<br>
`a` >>> `[1,2,1,3,13]`<br>
`a.count(1) # How many 1's are there in the list?` >>> `2`

# Dictionaries

* Maps keys to values
* Keys need to be `hashable`.  Values can be of any arbitrary type.
* Dictionaries are `mutable`.

`a = dict(A=1,Z=-1)`<br>
`b = {'A': 1, 'Z':-1}`<br>
`c = dict(zip(['A','Z'],[1,-1]))`<br>
`d = dict([('A',1),('Z',-1)])`<br>
`e = dict({'Z':-1,'A':1})`<br>
`a == b == c == d == e` >>> `True`<br>