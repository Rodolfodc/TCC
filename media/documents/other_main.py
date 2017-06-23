import particle
import rabinM

def main():
    space = []
    num_of_elements = 30
    key_size = 1024
    num_of_particles = 10
    C1 = 2
    C2 = 2
    W = 0.5
    Vmax = 15
    iMax = 100
    flag = False
    fitness = 1
    best_element = []
    key = []
    p = 0.8 # patamar desejado do p-valor
    group_size = 90 # numero de chaves do grupo

    generated_elements = []
    keys_counter = 0
    
    print("\n___________________________Bem vindo ao gerador de chaves____________________________\n")
    group_size = int(input("\nQuantidade de chaves do grupo: "))
    key_size = int(input("\nDigite o tamanho o chave a ser gerada: "))
    num_of_elements = int(input(r"Digite o numero de elementos do espaco a ser gerado: "))
    print("\nGerando espaco...")
    space = rabinM.generateSpace(num_of_elements, key_size)
    print("\nEspaco gerado!")
    num_of_particles = int(input("\nNumero de particulas: "))
    C1 = float(input("C1: "))
    C2 = float(input("C2: "))
    W = float(input("W(coefiente de inercia): "))
    Vmax = int(input("Velocidade maxima: "))
    iMax = int(input("Numero de iteracoes maximas: "))
    flag = input("Coef. de consticao sera valido?(s/n): ")
    if flag.upper() == 'S' or flag.upper() == "SIM":
        flag = True
    else:
        flag = False
    p = float(input("Valor do parametro da fitness: "))
    fitness = int(input("Escolha UMA fitness ou as duas(digite 12 neste caso):\n1-frequencia\n2-runs\n\nopcao: "))
    if fitness == 12:
        fitness = [1,2]
    elif fitness == 1:
        fitness = [1]
    else:
        fitness = [2]

    file = open(r"keys_1.txt", "w+")
    while(keys_counter < group_size):
        if keys_counter > 0:
            space = rabinM.generateSpace(num_of_elements, key_size, generated_elements, space)
        pso = particle.PSO(num_of_particles, num_of_elements, C1, C2, W, Vmax, iMax, flag, fitness, p, space)
        best_element = pso.execution()
##        print("Melhor elemento encntrado!!")
##        d = rabinM.generateDFromElement(best_element)
##        key = best_element[2:4]
##        key.append(d[5])
        keys_counter += 1
        generated_elements.append(best_element[:4])
        space.remove(best_element)

    for i in range(len(generated_elements)):
        seq_bin = bin(generated_elements[i][3])[2:]
        while(len(seq_bin) < 1024):
            seq_bin = "0" + seq_bin
        file.write(seq_bin + "\n")
    print("\n\nConjunto gerado e salvo em \\keyGeneratorSystem\\arquivo")
    file.close()

if __name__ == '__main__' :
    main()
    
    
    
    
