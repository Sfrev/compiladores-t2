import trabalho1 as t1
import os
from antlr4 import *

def custonSort(file_name):
    if os.path.splitext(file_name)[0][1] == '-':
        return int(os.path.splitext(file_name)[0][0])
    else:
        return int(os.path.splitext(file_name)[0][0:2])

def main():

    Path = "C:\Repositorio\Compiladores\casos-de-teste\casos_teste_t1\entrada"
    filelist = sorted(os.listdir(Path), key=custonSort)
    i = 1
    for file in filelist:
        t1.main(Path + "\\" + file, f"saidas/{i}.txt")
        i += 1

if __name__ == "__main__":
    main()