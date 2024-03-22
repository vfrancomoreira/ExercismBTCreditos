# Este arquivo é uma calculadora que opera com números inteiros
# algumas operações básicas, com manipulação de pilha
# e realiza definições e testes de erros.

# Esta parte do código define uma classe 'StackUnderflowError' 
# que herda da classe 'Exception' 
class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message

# Esta função recebe uma lista de strings como entrada
def evaluate(input_data):
    result = []
    custom = {}


    if len(input_data) == 1:
        # Avaliação de expressões individuais
        # para operações aritméticas e operações de pilha básicas
        if input_data[0].split()[0] == ':':
            if input_data[0].split()[1].isalpha() == False:
                raise ValueError("illegal operation")

        # Assim como nesta função acima o uso de funções
            # integradas como a split e isalpha

            # slipt = é usado em strings para dividir a string em uma 
            # lista de substrings com base em um separador especificado.

            # isalpha = é útil para validar se uma entrada de uúario
            # contém apenas letras antes de realizar operações 
            # especificas, como manipulação de string ou cálculos
            # que não devem incluir números ou caracteres especiais.  
        for elem in input_data[0].split():
            if elem == '+':
                # len = usado para obter o comprimento de um objeto.
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                sum = 0
                for elem2 in result:
                    sum += elem2
                result = [sum]
            elif elem == '-':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result = [result[0]-result[1]]
            elif elem == '*':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result = [result[0]*result[1]]
            elif elem == '/':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                if result[1] == 0:
                    raise ZeroDivisionError("divide by zero")
                result = [result[0]//result[1]]
                # lower = converte para letras minúsculas
            elif elem.lower() == 'dup':
                if len(result) < 1:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result.append(result[-1])
            elif elem.lower() == 'drop':
                if len(result) < 1:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result.pop(-1)
            elif elem.lower() == 'swap':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                temp = result[-1]
                result[-1] = result[-2]
                result[-2] = temp
            elif elem.lower() == 'over':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result.append(result[-2])
            else:
                # Exceções de tratativas de erros.
                try:
                    result.append(int(elem))
                except:
                    raise ValueError("undefined operation")
                
    # Se houver duas ou mais linhas de entrada, a função
    # interpreta a primeira parte como definições personalizadas
    # de operações.
    elif len(input_data) >= 2:
        # Processamento de definições personalizadas
        for strings in input_data:
            if strings.split()[0] == ':':
                defined = strings.lower().split()[1:-1]
                variable = defined[0]
                other = defined[1:]
                # custom.keys() obtém as chaves do dicionário
                if len(other) == 1 and other[0] in custom.keys():
                    custom[variable] = custom[other[0]]
                elif other[0] in custom.keys():
                    custom[variable].extend(other[1:])
                else:
                    custom[variable] = other

            
        analyze = []

        for elem in input_data[-1].lower().split():
            if elem in custom.keys():
                analyze.extend(custom[elem])
            else:
                analyze.append(elem)

        for elem in analyze:
        # Código para execução das operações após análise das definições personalizadas
            if elem == '+':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                sum = 0
                for elem2 in result:
                    sum += elem2
                result = [sum]
            elif elem == '-':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result = [result[0]-result[1]]
            elif elem == '*':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result = [result[0]*result[1]]
            elif elem == '/':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                if result[1] == 0:
                    raise ZeroDivisionError("divide by zero")
                result = [result[0]//result[1]]
            elif elem == 'dup':
                if len(result) < 1:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result.append(result[-1])
            elif elem == 'drop':
                if len(result) < 1:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result.pop(-1)
            elif elem == 'swap':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                temp = result[-1]
                result[-1] = result[-2]
                result[-2] = temp
            elif elem == 'over':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result.append(result[-2])
            else:
                result.append(int(elem))

    # No final da função, o resultado final das operações 
    # sobre a pilha é retornado como uma lista
    return result


# Minha análise sobre o sistema é a forma correta
# que eu vejo de desenvolver usando python
# Usando suas principais funções,
# POO e ferramentas que ajudam na matemática
# tornando o código mais objetivo e bonito.
