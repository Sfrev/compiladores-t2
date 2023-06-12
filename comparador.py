#Comparador de arquivos

import os

def custonSort(file_name):
    if os.path.splitext(file_name)[0][1] == '-':
        return int(os.path.splitext(file_name)[0][0])
    else:
        return int(os.path.splitext(file_name)[0][0:2])

def main():
    PathSaidas = "C:\Repositorio\Compiladores\casos-de-teste\casos_teste_t1\saida"
    PathTestes = "C:\Repositorio\Compiladores\T1\saidas"

    filelistSaidas = sorted(os.listdir(PathSaidas), key=custonSort)
    filelistTestes = sorted(os.listdir(PathTestes), key=lambda x: int(os.path.splitext(x)[0]))
    for i in range(len(filelistSaidas)):
        arquivo1 = open(PathSaidas + "\\" + filelistSaidas[i], 'r').read()
        arquivo2 = open(PathTestes + "\\" + filelistTestes[i], 'r').read()


        if arquivo1 == arquivo2:
            print(f'Arquivo: {filelistSaidas[i]} IGUAL ao arquivo: {filelistTestes[i]}')
            print(f"Caso {i+1} OK")
        else:
            print(f'Arquivo: {filelistSaidas[i]} DIFERENTE ao arquivo: {filelistTestes[i]}')
            print(f"Caso {i+1} Errado")
        i += 1

if __name__ == "__main__":
    main()