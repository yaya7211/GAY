# GAY crypto

GAY is a collection of cryptography tools that includes symetrical cyphering and decyphering and hashing based on an algorythm using primary numbers.

## Getting Started

This file (GAY.py) is a library that contains all GAY's functionalities. 

### Prerequisites

Should be used on a Python 3 environement. With "collections" module installed.

### Installing

Install collections with pip

On Windows : 
```
py -m pip install collections
```

On Linux : 
```
pip3 install collections
```
Then install GAY modulo from this Github : 

If you use git : 
```
git clone https://github.com/yaya7211/GAY
```
Or manually if you don't use git.

Then export the main file into your Python packages path.
On Windows (default) : 
```
C:\Users\Random\AppData\Local\Programs\Python\Python37\Lib
``` 

## Running the tests

Check that the file is succefully exported in your packages path by trying on your Python interpretor :
```
>>>import GAY
```
If you get a "ModuleNotFoundError", that means that you should try the installation steps again.

### Explaining algorythms 

Let's see how does that works.

# The cyphering

First of all, the cyphering-decyphering system, it works with a symetrical key that contains all caracters that can be used and a list of primary number. Let's creat it : 
For exemple the key that contains "abc" and [2, 3, 5] :
	- a -> 2
	- b -> 3
	- c -> 5
As you see, we connect all caracters with a primary number. Like in a dictionary or an array.
We want to cypher the word "bac" with our key.
 b a c => 3 x 2 x 5 = 30. 
 **30** Perfect, we've got our first part of our cyphered word. Let's make the second part.
 We have to make a list that contains the indexs of bac (our word) in the order of abc (our key).
 	- b : 1
 	- a : 0
 	- c : 2
Nice, we have finished cyphering the word : *30/1.0.2*

We've receved the cyphered word. Let's make it decyphered.
If you remember, the algorythm is symetrical, so to decypher, we've got the same key that we used to cypher.
We take the first part of the cyphered word : 30, we have to factorize it : 
30 = 2 x 3 x 5
We use the key to change numbers into letters : 
	- 2 : a
	- 3 : b
	- 5 : c
We index our caracters and put them in the order of the second part of the cyphered word (1.0.2)
	- a : 0
	- b : 1
	- c : 2
	========
	- b : 1
	- a : 0
	- c : 2
And finally we've got the decyphered word : bac.

# The hashing

Now we will see how does works the hashing algorythm.
First of all, we creat a key and cypher a word like we did before.
For the same key and the same word, we have got 30/1.0.2.
We call x "30"'s lenght x = lenght("30") = 2, and y [1.0.2]'s lenght y = lenght([1.0.2]) = 3
We find the greatest commom divisor of x and y, that is 1.
The hash is the sucession of 1 caracter from the first part of the cyphred word and 1 from the second, until we use all caracters of the smallest part : 
	- 3 : 1st caracter from 30
	- 1 : 1st caracter from [1.0.2]
	- 0 : 2nd caracter from 30
	- 0 : 2nd caracter from [1.0.2]
We stopped before using the last element of [1.0.2] because we took all elements from 30.
The first caracter is always the first caracter from the first part of the cyphered word.
If the greatest common divisor equal 1, the first part become the first half of the word ( ex : 3040 become 30).

That's all for the algorythm, let's use it in the module.

### Using the module

```py
ìmport GAY

g = GAY.GAY()
g.key = GAY.key_gen("abc", 2)
print(g.cypher("bac"))
print(g.hash("bac"))
``` 
We've started by importing the module.
We created g that contains the class GAY() that contains all main functions.
key is an attribut of the class GAY() that contains the key.
key_gen() is a method from GAY() that generate a key, the first argument is the caracters that we will use, the second is the first primary number that we will use, the script automaticly generate the primary numbers needed that comes after the one gived as argument.
cypher() is the method that cypher a word with the key in GAY().key .
hash() is the method that hash a word with the key in GAY().key .

That ouptuts : 
```
30/1.0.2
3100
```
To decypher, we use the method decypher() from GAY()
```py
print(g.decypher("30/1.0.2"))
```
That output : 
```
bac
```
# Play with keys
To save key you can use the function : 
```py
GAY.save_key(path)
```
that automaticly save in the path specified.

To use a key saved in a file you can use the function : 
```py
g.key = GAY.use_key(path)
```
that automaticly use the key specified in path.

### HELP I'VE GOT ERRORS
The only error you can have is : UnfoundElementError, that means that the key you are using is wrong.

### HAVE FUN !!!
