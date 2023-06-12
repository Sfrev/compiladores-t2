# UFSCar - Departamento de Computação
# Construção de compiladores
# Analisador Sintático para a linguagem LA

# Autor: Igor Teixeira Machado RA: 769708
# Autor: Júlia Aparecida de Sousa RA: 769707
# Autor: Rafael Vinicius Polato Passador RA: 790036

# Para instalar o ANTLR4 no Windows, basta executar o comando abaixo no terminal
# pip install antlr4-python3-runtime

# Para executar o ANTLR4 no Windows, basta executar o comando abaixo no terminal
# java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 LA.g4

# Para executar o programa, basta executar o comando abaixo no terminal
# python trabalho2.py <arquivo_entrada> <arquivo_saida>

# Para executar o corretor, basta executar o comando abaixo no terminal
# java -jar <caminho_do_corretor> "<python <caminho_programa>>" gcc <pasta_saidas> <pasta_casos_de_teste> "<RAs dos integrantes>" "t2"
# Exemplo:
# java -jar .\compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar "python C:\Repositorio\Compiladores\compiladores-t2\trabalho2.py" gcc C:\Repositorio\Compiladores\compiladores-t1\saidas C:\Repositorio\Compiladores\casos-de-teste "RA" "t2"

# Importação de bibliotecas
import sys
from antlr4 import *
from LALexer import LALexer
from LAParser import LAParser
from antlr4.error.ErrorListener import ErrorListener

# Função para escrever a saída em um arquivo
def saidaArquivo(nomeArquivo, saida):

    arquivo = open(nomeArquivo, 'w')
    for linha in saida:

        arquivo.write(f'{linha}\n')

    arquivo.close()

class LAParserErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        line = offendingSymbol.line
        text = offendingSymbol.text

        if text == '<EOF>':
            text = 'EOF'

        raise Exception(f'Linha {line}: erro sintatico proximo a {text}')

class LALexerErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
         
        lexError = str(e.input)[e.startIndex]

        if lexError == '"':

            raise Exception(f'Linha {line}: cadeia literal nao fechada')
        
        elif lexError == '{':

            raise Exception(f'Linha {line}: comentario nao fechado')
        
        else:
            raise Exception(f'Linha {line}: {lexError} - simbolo nao identificado')

def main(argv):

    # Lendo o camino para o arquivo de entrada e de saída passados na linha de comando
    arquivoEntrada = argv[1]
    arquivoSaida = argv[2]

    # Lendo o arquivo de entrada
    arquivo = FileStream(arquivoEntrada, encoding="utf-8")

    # Criando o analisador léxico
    lexer = LALexer(arquivo)

    # Criando o fluxo de tokens
    stream = CommonTokenStream(lexer)

    # Criando o analisador sintático
    parser = LAParser(stream)

    # Removendo os listeners padrões
    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    
    # Adicionando os listeners personalizados
    lexer.addErrorListener(LALexerErrorListener())
    parser.addErrorListener(LAParserErrorListener())

    # Lista para armazenar a saída
    saida = []
            
    try:
        # Chamando o parser
        parser.programa()

    except Exception as e:

        saida.append(str(e))
        saida.append('Fim da compilacao')
        saidaArquivo(arquivoSaida, saida)

if __name__ == "__main__":
    main(sys.argv)