def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def par_ou_impar(n):
    if n % 2 == 0:
        return "par"
    else:
        return "impar"


def main():
    print("=== Calculadora no Terminal ===")
    print("Operações disponíveis: + (soma), - (subtração), * (multiplicação), / (divisão), primo (par ou impar).")
    
    while True:
        op = input("Digite a operação (+, -, *, /, primo) ou 'sair' para encerrar: ")
        
        if op == "sair":
            print("Encerrando a calculadora. Tchau!")
            break
        
        if op not in ["+", "-", "*", "/", "primo"]:
            print("Operação inválida! Tente novamente.")
            continue

        if op in ["+", "-", "*", "/"]:
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
                continue
        elif op == "primo":
            try:
                n = int(input("Digite um número inteiro: "))
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")
                continue
        

        if op == "+":
            resultado = soma(a, b)
        elif op == "-":
            resultado = subtracao(a, b)
        elif op == "*":
            resultado = multiplicacao(a, b)
        elif op == "/":
            resultado = divisao(a, b)
        elif op == "primo":
            resultado = par_ou_impar(n)

        print(f"Resultado: {resultado}\n")


if __name__ == "__main__":
    main()
