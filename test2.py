# Este arquivo é um interpretador 
# de linguagem de programação simplificado, semelhante
# a uma máquina virtual, que opera
# em uma pilha assim como
# o primeiro teste com
# uso de números inteiros.

# Importações necessárias
# Cada import, dentro dele, ele busca uma função
# para que o sistema funcione de acordo com as 
# necessidades que o desenvolvedor busca
import re
from types import FunctionType
from typing import Any, Dict, List


# Definição da exceção para subfluxo da pilha
# chamada de 'StackUnderflowError' herdando da classe 'Exception'
class StackUnderflowError(Exception):
    pass

# Definição das funções de operação para a pilha
def plus(stack: List[int]):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
    stack.append(stack.pop() + stack.pop())

# Definição das outras funções de operação
# Cada função realiza operações aritméticas
def minus(stack: List[int]):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
    n2 = stack.pop()
    n1 = stack.pop()
    stack.append(n1 - n2)

def multiply(stack: List[int]):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
    stack.append(stack.pop() * stack.pop())

def divide(stack: List[int]):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
    n2 = stack.pop()
    n1 = stack.pop()
    if n2 == 0:
        raise ZeroDivisionError("divide by zero")
    stack.append(n1 // n2)

# Essas funções realizam operações duplicação
# remoção, troca e acessos de elementos.
    # dup(), drop(), swap() e over()
def dup(stack: List[int]):
    if len(stack) < 1:
        raise StackUnderflowError("Insufficient number of items in stack")
    stack.append(stack[-1])

def drop(stack: List[int]):
    if len(stack) < 1:
        raise StackUnderflowError("Insufficient number of items in stack")
    stack.pop()

def swap(stack: List[int]):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
    a = stack.pop()
    b = stack.pop()
    stack.append(a)
    stack.append(b)

def over(stack: List[int]):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
    stack.append(stack[-2])



# Esta função itera uma lista que chamamos de Comprehension
    # e executa ações com base no conteúdo de casa string
def _evaluate(input: List[str], words: Dict[str, Any], stack: List[int]):
    for word in input:
        match word:
            case int(i):
                stack.append(i)
            case FunctionType():
                word(stack)
            case list(l):
                _evaluate(l, words, stack)

# Esta função recebe uma string word e
# retorna a própria string em letra minúscula
# ou o número convertido para inteiro.
def _normalize_word(word: str) -> str|int:
    if re.match(r"\-?\d+", word):
        return int(word)
    return word.lower()

# Função para compilar as sentenças do programa
def _compile(sentence: List[str], words: Dict[str, List]) -> List:
    compiled_sentence = []
    for word in sentence:
        word = _normalize_word(word)
        print("WORD", word)
        match word:
            case int(i):
                compiled_sentence.append(i)
            case str(s):
                if word not in words:
                    raise ValueError("undefined operation")
                compiled_sentence.append(words[word])
    return compiled_sentence


# Função principal para avaliar o programa
def evaluate(program: List[str]) -> List[int]:
    # Dicionário que mapeia operações e variáveis 
    # para suas definições ou funções correspondentes.
    # Somando, subtraindo, multiplicando, etc...
    words: Dict[str, Any] = {
        '+': plus,
        '-': minus,
        '*': multiply,
        '/': divide,
        'dup': dup,
        'drop': drop,
        'swap': swap,
        'over': over
    }

    # List comprehension vazia chamada de stack que
    # só pode manter numeros inteiros.
    stack: List[int] = []

    # Itera sobre as linhas do programa
    # Cada linha do for de acordo com a lógica estabelecida: 
    # definir novas funções (palavras) ou executar as operações existentes, 
    # compilando e avaliando as instruções conforme necessário.
    for line in program:
        sentence = line.split()
        if len(sentence) > 3 and sentence[0] == ":" and sentence[-1] == ";":
            word = _normalize_word(sentence[1])
            # Se a palavra normalizada não for uma string
            if not isinstance(word, str):
                raise ValueError("illegal operation")
            words[word] = _compile(sentence[2:-1], words)
        # Compile a linha, imprime a lista compilada
            # e avalie a lista.
        else:
            compiled_sentence = _compile(sentence, words)
            print("COMPILED", compiled_sentence)
            _evaluate(compiled_sentence, words, stack)

    # Retorna a pilha resultante.
    return stack

# Este código também usa POO e consiste em usar
# ferramentas que ajudam no desenvolvimento.
# Comprehension uma delas.
# Assim como importação de outras funções
# que ajudam a chegar no objetivo do sistema.
