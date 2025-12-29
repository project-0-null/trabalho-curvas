def ln(x,iteracoes):
    iteracoes = 100

    if x<=0:
        return "Erro: ln(x) indefinido para x <= 0"
    if x==1:
        return 0

    fator=0
    y=x

    while y>2:
        y /= 2.718281828459045
        fator += 1
    
    while y < 0.5:
        y *= 2.718281828459045
        fator -= 1
    
    z=y-1
    resultado = 0.0 

    for n in range(1, iteracoes):
        termo = ((-1) ** (n+1)) * (z ** n) / n
        resultado += termo

    # Adiciona os fatores acumulados: ln(x) = ln(y) + fator
    #ln(a) -ln(e) +ln(e) = ln(a)
    #       |
    #       V
    #-> ln(a) = ln(a/e) + 1
    #           ||
    #-> ln(a) = ln(a*e) - 1
    #return resultado + fator
    # essa funçao vai ser irrlevante aparentemente
import os
import platform
from Problemacorrente import resolvedor_do_problema_1
from Problemacorrente import configurar_graficos 

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def main():
    
    print("\n" + "="*60)
    print("TESTE COMPUTACIONAL - AJUSTE DE CURVAS")
    print("Turma 25/2")
    print("="*60)
    print("Integrantes do grupo:")
    print("1. [SEU NOME]")
    print("2. [NOME COLEGA 1]")
    print("3. [NOME COLEGA 2]")
    print("="*60)
    
    input("\nPressione Enter para continuar...")
    
    while True:
        print("\n" + "="*60)
        print("MENU PRINCIPAL")
        print("="*60)
        print("1. Problema 1 - Circuito RC (ajuste exponencial)")
        print("2. Problema 2 - Volume de Árvore (ajuste potência)")
        print("3. Sair do programa")
        print("="*60)
        
        opcao = input("\nDigite o número da opção desejada: ").strip()
        
        if opcao == "1":
            plt_obj, modo_interativo = configurar_graficos()
            resolvedor_do_problema_1(plt_obj, modo_interativo) #chamar isso aqui dps, foi chamado
            input("\nPressione Enter para voltar ao menu...")
            
        elif opcao == "2":
            print("\nfazendo ainda calam filho")
            input("Pressione Enter para voltar ao menu...")
            
        elif opcao == "3":
            print("\nEncerrando programa...")
            print("Obrigado por me usar!")
            break
            
        else:
            print("\nOpção inválida! Digite 1, 2 ou 3.")
            input("Pressione Enter para tentar novamente...")
main()