# pvf-language
A self-made programming language. This language was made throughout the 7th semester subject **Programming Logic** given by the teacher MACIEL CALEBE VIDAL.

## Motivation
The main motivation for this project was to understand how languages are made. I learned alot during the implementation of this project and, by the end, I could easly undertand many concepts involving the way many programming languages are made.

## Language characteristics

The implementation of the language was made using an Abstract syntax tree (AST). Every command is a Node with an `evaluate` method. After the AST is made, the `evaluate` method from the last parent is called.

To further see the implementation of this code, visit the source github:
```
https://github.com/fontes99/compiler
```
The has 7 diferent characteristics:
- `if/else` logic
- `while` logic
- function calling/declaring
- variable assignment
- read line
- terminal output

## EBNF


```md
BLOCK = { COMMAND } ; 
COMMAND = ( λ | ASSIGNMENT | PRINT | IF | ELSE | WHILE), ";" ; 
FUNCDEFBLOCK = { IDENTIFIER, TYPE,  "(", { IDENTIFIER, TYPE, "," }, ")", COMMAND }
ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ; 
COMPARISON = EXPRESSION, ("==" | "<" | ">" | "<=" | ">="), EXPRESSION ;
PRINT = "printo", "(", EXPRESSION, ")" ; 
IF = "ifo", "(", COMPARISON, ")", "{", BLOCK, "}", { ESLSE } ;
ELSE = "elso", "{", BLOCK "}" ;
WHILE = "whilo", "(", COMPARISON, ")", "{", BLOCK, "}" ;
EXPRESSION = TERM, { ("+" | "-"), TERM } ; 
TERM = FACTOR, { ("*" | "/"), FACTOR } ; 
FACTOR = (("+" | "-"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ; 
NUMBER = DIGIT, { DIGIT } ; 
LETTER = ( a | ... | z | A | ... | Z ) ; 
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ; 
```

## Sintax Diagram

![alt text](DS.png)

## Tests
On the root of the project, you will find a file caled `test.py`. This file contains various example tests using this language.

To run it, you must have `pytest` and run the following command

```bash
pytest test.py
```

## Using the languages

To run a file from the language, use the following command

```bash
python3 main.py <name-of-file>.pvf
```

There is an Example file in the root of this project. To run it, run the following command

```bash
python3 main.py example.pvf
```