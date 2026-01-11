import sys
import math

def configurar_graficos_arvore():
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
    plt_obj.xlabel('diametro', fontsize=12)
    plt_obj.ylabel('volume', fontsize=12)
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
#PROBLEMA 2
#-----------------------------------------------------------------------

def resolvedor_do_problema_2(plt_obj, modo_interativo):
    print("\n"+"="*60)
    print("PROBLEMA 2 - volumes DE ÁRVORE")
    print("="*60)

    #os dados que eu vou colocar aqui pode vir um for com um input pra serem variaveis depois mais ai tem que mudar a parre da matriz tb
    diametros = [8.3,8.6,8.8,10.5,10.7,10.8,11,11,11.1,11.2,11.3,11.4,11.4,11.7,12,12.9,12.9,13.3,13.7,13.8,14,14.2,14.5,16,16.3,17.3,17.5,17.9,18,18,20.6]
    volumes = [10.3,10.3,10.2,16.4,18.8,19.7,15.6,18.2,22.6,19.9,24.2,21,21.4,21.3,19.1,22.2,33.8,27.4,25.7,24.9,34.5,31.7,36.3,38.3,42.6,55.4,55.7,58.3,51.5,51,77]

    print(f"\nDados experimentais (n = {len(diametros)}):")
    print(f"diametros (s):    {diametros}")
    print(f"volumes (A): {volumes}")

    plotar_grafico(diametros, volumes, "experimental data - trees", plt_obj, modo_interativo)

    w= transforma_dados_caso_exponencial(diametros)
    z= transforma_dados_caso_exponencial(volumes)
    print(f"\nDados linearizados (z = ln(volume)):")
    exibe_alguns_elementos(z,0,len(z))

    # 3. Plota dados linearizados
    plotar_grafico(w, z, "linearized data - trees", 
                   plt_obj, modo_interativo)

    # 4. Monta sistema normal para ajuste linear z = β₀ + β₁*ln(x)
    n = len(w)
    smt_w = sum(w)
    smt_w2 = sum(d * d for d in w)
    smt_z = sum(z)
    smt_wz = sum(w[i] * z[i] for i in range(n))
    #smt=somatorio

    print(f"\nSomatórias para sistema normal:")
    print(f"  n = {n}")
    print(f"  Σln(x) = {smt_w:.4f}")
    print(f"  Σ(ln(x))² = {smt_w2:.4f}")
    print(f"  Σln(y) = {smt_z:.4f}")
    print(f"  Σ(ln(x)*ln(y)) = {smt_wz:.4f}")

    # Sistema normal: [[n, Σd], [Σd, Σd²]] * [β₀, β₁] = [Σz, Σdz]
    A_sistema = [[n, smt_w], [smt_w, smt_w2]]
    b_sistema = [smt_z, smt_wz]

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
        
        print(f"\nParâmetros do modelo Potência (v = ax^b):")
        print(f"  a = exp(β₀) = {a:.6f}")
        print(f"  b = β₁ = {b:.6f}")
        print(f"  Equação Final: Volume = {a:.4f} * (Diâmetro)^{b:.4f}")
        
        # 7. Calcula volume para diâmetros solicitados
        diametros_teste = [15.0, 22.0]
        print(f"\nPrevisões solicitadas:")
        for d_teste in diametros_teste:
            # FÓRMULA CORRIGIDA: a * x^b
            v_predito = a * (d_teste ** b)
            print(f"  Diâmetro {d_teste} pol -> Volume estimado: {v_predito:.4f}")
        
        # 8. Calcula soma dos quadrados dos resíduos
        residuos = []
        soma_quadrados = 0

        for i in range(n):
            v_ajustado = a * (diametros[i] ** b)
            residuo = v_ajustado - volumes[i]
            residuos.append(residuo)
            soma_quadrados += residuo ** 2
        
        print(f"\nAnálise de resíduos:")
        print(f"  Resíduos: {[f'{r:.4f}' for r in residuos]}")
        print(f"  Soma dos quadrados dos resíduos: Σr² = {soma_quadrados:.6f}")
        
        # 9. Plota curva ajustada
        # Para plotar a curva suave, precisamos de mais pontos
        import numpy as np
        d_suave = np.linspace(min(diametros), max(diametros) * 1.1, 100)
        v_suave = a * (d_suave ** b)
        
        # Cria gráfico com pontos e curva
        plt_obj.figure(figsize=(10, 6))
        plt_obj.scatter(diametros, volumes, color='blue', s=100, 
                       label='Experimental Data', edgecolor='black', linewidth=1)
        plt_obj.plot(d_suave, v_suave, 'r-', linewidth=2, 
                    label=f'$i(t) = {a:.3f}e^{{{b:.3f}t}}$')
        plt_obj.title('Exponencial Adjust - trees', fontsize=16, fontweight='bold')
        plt_obj.xlabel('diameter (pol)', fontsize=12)
        plt_obj.ylabel('volume (pol³)', fontsize=12)
        plt_obj.legend(fontsize=11)
        plt_obj.grid(True, alpha=0.3)
        
        if modo_interativo:
            plt_obj.show()
            print("\n✓ Gráfico do ajuste exibido em janela")
        else:
            plt_obj.savefig('ajuste_exponencial_trees.png', dpi=150, bbox_inches='tight')
            plt_obj.close()
            print("\nGráfico do ajuste salvo como: ajuste_exponencial_trees.png")
        
    except Exception as e:
        print(f"\nErro ao resolver sistema: {e}")

