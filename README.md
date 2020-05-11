# GAY crypto

GAY is a collection of cryptography tools used for symetrical cyphering and decyphering and hashing based on an primary numbers based on algorythm.

## Getting Started

This file (GAY.py) is a library that contains all GAY's functionalities. 

### Prerequisites

Should be used on a Python 3 environement. With "collections" module installed.

### Installing

Install GAY and collections with pip

On Windows : 
```
py -m pip install collections
py -m pip install GAY
```

On Linux : 
```
pip3 install collections
pip3 install GAY
``` 

## Running the tests

Check that the lib is succefully installed by trying on your Python interpretor :
```
>>>import GAY
```
If you get a "ModuleNotFoundError", that means that you should try the installation steps again.

### Explaining algorythms 

Let's see how does that works.

# The cyphering

First of all, we have to creat a key that will be used to cipher and decipher the messages. The key contains all the caracters that would be used in the clear message. Let's take an exemple, we want to encrypt the word "bac", so our key will at least contain "a", "b" and "c". Every caracter in the key will be assigned to a primary number, no matter it order. Let's take the three firsts primary numbers : 2, 3 and 5. The key structur is a dictionnary like : 
key = { "a" : 2,
	"z": 11,
	"b" : 5,
	"c" : 3,
	"d" : 7}
Ok, the key is ready, let encrypt our word. The encryption is done in two parts : the firts one is the cyphered word, the second is the order of the craacters : 
First part : we take every number assigned to there letter of the word from the key and we multipli them : 
b * a * c = 5 * 2 * 3 = 30
The firts part is done, let's do the scond one : 
We have to index every caracter of the word depends on the alphabetical order defined in the key : 
b -> 2 : because it's the second letter 
a -> 1 : because it's the firts
c -> 3 : bacause it's the third
Everything is done, our encrypted word is `30/2.1.3`

Let's decipher it !
We will use the same key.
We start with factoring the first part of the encrypted word : 
30 = 2 * 3 * 5
Using the key, we can find the letters assigned to the primary numbers found.
2 -> "a"
3 -> "b"
5 -> "c"
Now, we have to index it depends on the second part of the encrypted word : 
a -> 2 : we move the a to the second place
b -> 1 : we move the b to the first place
c -> 3 : we let the c at the third place
And finaly we find "bac".



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
print(g.cipher("bac"))
print(g.hash("bac"))
``` 
We've started by importing the module.
G is a new instance of class GAY that contains all main functions.
key is an attribut of the class GAY() that contains the key.
key_gen() is a method from GAY() that generate a key, the first argument is the caracters that we will use, the second is the first primary number that we will use, the script automaticly generate the primary numbers needed that comes after the one gived as argument.
cipher() is the method that cypher a word with the key in GAY().key .
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
