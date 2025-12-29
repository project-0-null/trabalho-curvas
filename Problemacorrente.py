#-----------------------------------------------------------------------
#configuração do matplotlib
#-----------------------------------------------------------------------
import sys
import math

def configurar_graficos():
    """
    Configura matplotlib para funcionar no Ubuntu
    """
    print("\n" + "="*60)
    print("INICIANDO SISTEMA DE GRÁFICOS")
    print("="*60)
    
    # Lista de backends para tentar (em ordem de preferência)
    backends = [
        'TkAgg',      # Requer python3-tk (sudo apt-get install python3-tk)
        'Qt5Agg',     # Requer PyQt5 (pip install PyQt5)
        'GTK3Agg',    # Requer PyGObject
        'WXAgg',      # Requer wxPython
    ]
    
    print("\nTentando configurar gráficos interativos...")
    
    for backend in backends:
        try:
            import matplotlib
            matplotlib.use(backend)
            import matplotlib.pyplot as plt
            
            # Testa se o backend realmente funciona
            plt.figure()
            plt.close()
            
            print(f"✓ Backend '{backend}' configurado com sucesso!")
            print(f"  Gráficos serão mostrados em janelas interativas.")
            return plt, True
            
        except Exception as e:
            print(f"✗ Backend '{backend}' falhou: {str(e)[:50]}...")
            continue
    
    # Se nenhum backend interativo funcionou
    print("\nNenhum backend interativo funcionou.")
    print("  Instale um deles:")
    print("  1. sudo apt-get install python3-tk  (para TkAgg)")
    print("  2. pip install PyQt5                (para Qt5Agg)")
    print("\n  Usando modo de salvamento automático por enquanto...")
    
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    return plt, False

#-----------------------------------------------------------------------
#funçoes do trabalho
#-----------------------------------------------------------------------


def exibe_sistema_formatado(A, b, label=""): #exibe com  formatação
    print(f"\n{label}")
    for i in range(len(A)):
        row = ' '.join(f"{A[i][j]:>10.4f}" for j in range(len(A)))
        print(f"[{row}] | {b[i]:>10.4f}")
    print()

def Eliminação_de_Gauss_com_pivoteamento(n, A, b):
    #exibe_sistema_formatado(A,b,"Sistema inicial")
    for k in range(0,n-1):  # k-esima etapa da Eliminação
        # fazendo o pivoteamento
        Amax = abs(A[k][k])
        lin_indice_max = k
        for i in range(k,n): #percorre as linhas abaixo da diagonal
          if abs( A[i][k] )  > Amax:
           Amax = abs(A[i][k])
           lin_indice_max = i

        if abs(A[lin_indice_max][k]) < 1e-15:
            raise ValueError(f"Pivo nulo (ou próximo de zero) na etapa {k}.")

        if lin_indice_max != k: #fazer a troca de linhas
            A[k], A[lin_indice_max] = A[lin_indice_max], A[k]
            b[k], b[lin_indice_max] = b[lin_indice_max], b[k]

        for i in range(k + 1, n):  # i se refere a linha
            m = A[i][k] / A[k][k]
            A[i][k] = 0.0
            for j in range(k+1, n):  # j se refere a coluna
                A[i][j] =  A[i][j]  - m * A[k][j]
            b[i] = b[i] - m * b[k]
        #exibe_sistema_formatado(A, b, f"Após a {k+1}a Etapa ")
    exibe_sistema_formatado(A, b, f"Sistema triangularizado ")
    # Retrosubstituição
    # criando a lista com elementos nulos
    x = [0.0 for i in range(n)]

    x[n-1]= b[n-1]/A[n-1][n-1]
    passo = -1
    for i in range((n-2),(-1), passo):
        soma = 0
        for j in range(i + 1, n):
           soma = soma + A[i][j] * x[j]
        x[i] = (b[i] - soma) / A[i][i]
    return x


# lineariza par o caso modelo exponencial: y = a * exp(b * x)
def  transforma_dados_caso_exponencial(y):
   n = len(y)
   # inicializa o vetor colocando zeros em todas as posicões
   z = [0 for i in range(n)]
   #aplica a linearização
   for i in range(0,len(y)):
     z[i] = math.log(y[i])
   return z

# Função para exibir alguns elementos da lista
def exibe_alguns_elementos(lista,inic, fim):
    print(lista[inic:fim])

def plotar_grafico(x,y,titulo,plt_obj, modo_interativo):
    #plota o grafco com dados fornecidos
    plt_obj.figure(figsize=(10,6))#cria a figura
    plt_obj.scatter(x,y,color='red', s=100, label='DATA', edgecolor='black', linewidth=1, alpha=0.8)
    plt_obj.axhline(0,color='gray', linestyle='--',alpha=0.5)
    plt_obj.axvline(0,color='gray', linestyle='--',alpha=0.5)

    plt_obj.title(titulo, fontsize=16, fontweight='bold')
    plt_obj.xlabel('x', fontsize=12)
    plt_obj.ylabel('y', fontsize=12)
    plt_obj.legend(fontsize=11)
    plt_obj.grid(True, alpha=0.3)

    if modo_interativo:
        plt_obj.show()
        print(f"Gráfico '{titulo}'")
    else:
        # Modo não-interativo - salva arquivo
        nome_arquivo = titulo.replace(' ', '_').replace('(', '').replace(')', '') + '.png'
        plt_obj.savefig(nome_arquivo, dpi=150, bbox_inches='tight')
        print(f"✓ Gráfico salvo como: {nome_arquivo}")
        plt_obj.close()

#-----------------------------------------------------------------------
#PROBLEMA 1
#-----------------------------------------------------------------------
def resolvedor_do_problema_1(plt_obj, modo_interativo):
    print("\n"+"="*60)
    print("PROBLEMA 1 - CIRCUITO RC (AJUSTE EXPONENCIAL)")
    print("="*60)

    #os dados que eu vou colocar aqui pode vir um for com um input pra serem variaveis depois mais ai tem que mudar a parre da matriz tb
    tempos = [0.2, 1.0, 2.0, 5.0, 10.0, 20.0, 30.0, 50]
    correntes = [12.9, 11.7, 10.0, 7.0, 3.5, 0.9, 0.2, 0.017]

    print(f"\nDados experimentais (n = {len(tempos)}):")
    print(f"Tempos (s):    {tempos}")
    print(f"Correntes (A): {correntes}")

    plotar_grafico(tempos, correntes, "experimental data - RC Circuit ", plt_obj, modo_interativo)

    z= transforma_dados_caso_exponencial(correntes)
    print(f"\nDados linearizados (z = ln(corrente)):")
    exibe_alguns_elementos(z,0,len(z))

    # 3. Plota dados linearizados
    plotar_grafico(tempos, z, "linearized data - RC Circuit", 
                   plt_obj, modo_interativo)

    # 4. Monta sistema normal para ajuste linear z = β₀ + β₁*t
    n = len(tempos)
    smt_t = sum(tempos)
    smt_t2 = sum(t * t for t in tempos)
    smt_z = sum(z)
    smt_tz = sum(tempos[i] * z[i] for i in range(n))
    #smt=somatorio

    print(f"\nSomatórias para sistema normal:")
    print(f"  n = {n}")
    print(f"  Σt = {smt_t:.4f}")
    print(f"  Σt² = {smt_t2:.4f}")
    print(f"  Σz = {smt_z:.4f}")
    print(f"  Σtz = {smt_tz:.4f}")

    # Sistema normal: [[n, Σt], [Σt, Σt²]] * [β₀, β₁] = [Σz, Σtz]
    A_sistema = [[n, smt_t], [smt_t, smt_t2]]
    b_sistema = [smt_z, smt_tz]

    print(f"\nSistema normal a ser resolvido:")
    exibe_sistema_formatado(A_sistema, b_sistema, "Sistema Normal")

    try:
        solucao = Eliminação_de_Gauss_com_pivoteamento(2, A_sistema, b_sistema)
        beta0, beta1 = solucao[0], solucao[1]
        
        print(f"\nSolução do sistema normal:")
        print(f"  β₀ = {beta0:.6f}  (intercepto)")
        print(f"  β₁ = {beta1:.6f}  (inclinação)")
        
        # 6. Converte para parâmetros originais
        a = math.exp(beta0)
        b = beta1
        
        print(f"\nParâmetros do modelo exponencial:")
        print(f"  a = exp(β₀) = {a:.6f}")
        print(f"  b = β₁ = {b:.6f}")
        print(f"\nModelo ajustado: i(t) = {a:.4f} * e^({b:.4f} * t)")
        
        # 7. Calcula corrente para t = 40s
        t_predicao = 40.0
        i_predito = a * math.exp(b * t_predicao)
        print(f"\nPrevisão para t = {t_predicao}s:")
        print(f"  i({t_predicao}) = {i_predito:.6f} A")
        
        # 8. Calcula soma dos quadrados dos resíduos
        residuos = []
        soma_quadrados = 0

        for i in range(n):
            i_ajustado = a * math.exp(b * tempos[i])
            residuo = i_ajustado - correntes[i]
            residuos.append(residuo)
            soma_quadrados += residuo ** 2
        
        print(f"\nAnálise de resíduos:")
        print(f"  Resíduos: {[f'{r:.4f}' for r in residuos]}")
        print(f"  Soma dos quadrados dos resíduos: Σr² = {soma_quadrados:.6f}")
        
        # 9. Plota curva ajustada
        # Para plotar a curva suave, precisamos de mais pontos
        import numpy as np
        t_suave = np.linspace(min(tempos), max(tempos) * 1.1, 100)
        i_suave = a * np.exp(b * t_suave)
        
        # Cria gráfico com pontos e curva
        plt_obj.figure(figsize=(10, 6))
        plt_obj.scatter(tempos, correntes, color='blue', s=100, 
                       label='Dados experimentais', edgecolor='black', linewidth=1)
        plt_obj.plot(t_suave, i_suave, 'r-', linewidth=2, 
                    label=f'$i(t) = {a:.3f}e^{{{b:.3f}t}}$')
        plt_obj.title('Ajuste Exponencial - Circuito RC', fontsize=16, fontweight='bold')
        plt_obj.xlabel('Tempo (s)', fontsize=12)
        plt_obj.ylabel('Corrente (A)', fontsize=12)
        plt_obj.legend(fontsize=11)
        plt_obj.grid(True, alpha=0.3)
        
        if modo_interativo:
            plt_obj.show()
            print("\n✓ Gráfico do ajuste exibido em janela")
        else:
            plt_obj.savefig('ajuste_exponencial_rc.png', dpi=150, bbox_inches='tight')
            plt_obj.close()
            print("\nGráfico do ajuste salvo como: ajuste_exponencial_rc.png")
        
    except Exception as e:
        print(f"\nErro ao resolver sistema: {e}")




