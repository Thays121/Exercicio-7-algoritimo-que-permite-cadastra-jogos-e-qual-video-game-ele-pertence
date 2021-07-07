def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criaçao do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo):
    try:
        a =open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
        try:
            a = open(nomeArquivo, 'at')
        except:
            print('Erro ao abrir o arquivo')
        else:
            a.write('{};{}\n'.format(nomeJogo, nomeVideogame))
        finally:
            a.close()

#Programa princial
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inesistente')
    criaArquivo(arquivo)
while True:
    print('MENU')
    print('1 - Cadastra novo item')
    print('2 - Listar cadastro')
    print('3 - Sair ')

    op = valida_int('Escolha a opçaõ desejada:',1,3)
    if op == 1:
        print('Opção de cadastrar novo item selecionada...\n')
        nomeJogo = input('Nome do jogo')
        nomeVideogame = input('Nome do Videogame')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif op == 2:
        print('Opção de lista selecionada...\n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break