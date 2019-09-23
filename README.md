# GAY
Ciphering-Deciphering

 Create Key : python3 KeyGen.py aze 2 cip => [key's charset] [1st prim num] [cip for cyphering key]
 Cypher : python3 Cipher.py aze => [word to cypher]
 Create decypherring Key : python3 KeyGen.py aze 2 decip => [key's charset] [1st prim num] [decip for decyphering key]
 Decypher : python3 Decipher.py 120 1.2.3 [the word to decypher] [it's order] 


Python modulo :
How to use :
 1) Create 2 keys, one for cyphering, and another one for decyphering with the function KeyGen(charset, 1stPrimNum)
 2) Create an object that containsthe class GAY that contains all mains mathods >>>f = GAY()
 3) Set the class's key >>>f.key = KeyGen("abc", 3)
 4) Set the class's word to cypher, or a list that contains the word and the order to decypher >>>f.word = "bac" or f.word=[105,"1.0.2"]
 5) Cypher or decypher >>>f.cypher() or f.decypher()
