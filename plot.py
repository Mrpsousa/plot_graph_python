import numpy as np
import matplotlib.pyplot as plt



# Cria eixo x para produto A e produto B com uma separação de 0.25 entre as barras
def plot_graph(algoritimo_A, algoritimo_B, algoritimo_C, quant_teste):
    x1 =  np.arange(len(algoritimo_A))
    x2 = [x + 0.25 for x in x1]
    x3 = [x + 0.25 for x in x2]

    # Plota as barras
    plt.bar(x1, algoritimo_A, width=0.25, label = 'Algoritimo A', color = 'c')
    plt.bar(x2, algoritimo_B, width=0.25, label = 'Algoritimo B', color = 'y')
    plt.bar(x3, algoritimo_C, width=0.25, label = 'Algoritimo C', color = 'r')

    # coloca o nome dos meses como label do eixo x
    meses = []
    i = 0
    for i in range(quant_teste):
        meses.append('teste - '+ str(i))

    
    plt.xticks([x + 0.25 for x in range(len(algoritimo_A))], meses)

    # inseri uma legenda no gráfico
    plt.legend()

    plt.title("Tempo de execução")
    plt.show()


#valores de exemplo
algoritimo_A = [6,7,8,4,4]
algoritimo_B = [3,12,3,4.1,6]
algoritimo_C = [4,9,2,8.1,8]
quant_teste = 5


plot_graph( algoritimo_A, algoritimo_B, algoritimo_C, quant_teste) #running