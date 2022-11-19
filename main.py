'''
============================================
O simulador foi desenvolvido para atender a 
atividade 2 proposta na disciplina de ITC 
(Introdução à Teoria da Computação) do curso
de Sistemas de Informação no ICMC - USP.

Seus integrantes são:

Eduardo Costa Miranda Azevedo     - 12677151
Gustavo de Oliveira Martins       - 12625531
Ivan Barbosa Pinheiro             -  9050552
Raquel de Jesus Santos Valadão    - 12674022
Ryan Souza Sá Teles               - 12822062
============================================
'''

'''
Classe Fita criada para auxiliar o deslocamento da cabeça da máquina e registrar as cadeias a serem processadas.
'''
class Fita():
  '''
  Método construtor da classe Fita e responsável por populá-la com a string passada, e adicionar a cadeia vazia caso não seja fornecido a mesma.
  '''
  def __init__(self,fita = "B-B"):
    self.fita = dict(enumerate(fita))

  '''
  Método que retorna a posição na fita, caso não encontre é retornado -1.
  '''
  def __getitem__(self,posicao):
    if posicao in self.fita:
      return self.fita[posicao]
    else:
      return -1

  '''
  Método que seta uma posição da fita com um elemento passado
  '''
  def __setitem__(self, posicao, elemento):
    self.fita[posicao] = elemento

'''
Classe MaquinaDeTuring criada para receber especificações e processar cadeias a fim de validar linguagens
'''
class MaquinaDeTuring():
	
  '''
  Método construtor da classe MaquinaDeTuring.
  Recebe uma lista de estados, uma lista de símbolos terminais, uma lista de marcadores e um possível estado de aceitação.
  Por fim retorna uma instância do objeto MaquinaDeTuring.
  '''
  def __init__(self, estados, simbolosTerminais, marcadoresFita, estadoDeAceitacao):
    self.estados = estados
    self.simbolosTerminais = simbolosTerminais
    self.marcadoresFita = marcadoresFita
    self.estadoDeAceitacao = estadoDeAceitacao


  '''
  Método que imprime os atributos da máquina de Turing
  '''
  def imprimirMaquinaDeTuring(self):
    print("-"*50)
    print("Estados :: ")
    for index, estado in enumerate(self.estados):
      print("q",index, estado)
    print("\nEstados de aceitação :: ")
    print(self.estadoDeAceitacao)
    print("\nSímbolos terminais :: ")
    print(self.simbolosTerminais)  
    print("\nMarcadores Fita :: ")
    print(self.marcadoresFita)  
    print("-"*50)

  '''
  Método que processa a cadeia conforme as especificações da máquina retornando True caso aceite a cadeia e False caso a rejeite.
  '''
  def processarCadeiaComFita(self, cadeia):
    if cadeia == "B-B":
      return True if self.estadoDeAceitacao == 0 else False
        
    cabeca = 1
    estadoAtual = 0
    fita = Fita(cadeia)
	
    while not estadoAtual == self.estadoDeAceitacao:
      mudou = False
      for transicao in self.estados[estadoAtual]:
        [simbolo,estado,marcador,direcao] = transicao
        if fita[cabeca] == simbolo:  
          estadoAtual = int(estado)
          fita[cabeca] = marcador
          cabeca += self.moverCabeca(direcao)
          mudou = True
        if mudou:
          break
      if not mudou:
        return False
    return True

  '''
  Método que recebe uma lista de cadeias e passa uma por uma para o método processarCadeiaComFita e imprime se aceita ou não aquela cadeia, com base no retorno booleano
  '''
  def imprimirProcessamentoDeCadeias(self, cadeias):
    for cadeia in cadeias:
      if self.processarCadeiaComFita(cadeia):
        print("aceita")
      else:
        print("rejeita")

  '''
  Método que interpreta o caractere "L" e retorna o valor -1, caso leia o caractere "S" retorna 0 e retorna 1 caso contrário, isso se faz necessário para a movimentação da cabeça da máquina para ler os símbolos da fita
  '''
  def moverCabeca(self,direcao):
    if direcao == "L":
      return -1
    if direcao == "S":
      return 0
    return 1

'''
Função que lê da entrada do teclado as especificações de uma máquina de Turing e retorna uma instância da classe MaquinaDeTuring 
'''
def lerExpecificacoesDaMaquina():
  try:
    nroEstados = int(input())
    estados = [list() for i in range(nroEstados)]
    simbolosTerminais = input().split()
    simbolosTerminais.pop(0)
    marcadoresFita = input().split()
    marcadoresFita.pop(0)
    estadoDeAceitacao = int(input())
    nroDeTransicoes = int(input())
    for i in range(nroDeTransicoes):
        origem, simboloTerminal, destino, marcador, direcao = input().split()
        estados[int(origem)].append([simboloTerminal, destino, marcador, direcao])
    return MaquinaDeTuring(estados, simbolosTerminais, marcadoresFita, estadoDeAceitacao)
    
  except:
    print("Erro na entrada de especificação da máquina de Turing!")
    exit()

'''
Função que lê do teclado a quantidade de cadeias a serem processadas e as suas respectivas cadeias, e as adiciona em uma lista que por fim é retornada.
'''
def lerCadeias():
  try:
    nroCadeias = int(input())
    listaDeCadeias = []
    for i in range(nroCadeias):
      entrada = input()
      if entrada[-1] == "\r":
          cadeiaComB = "B" + entrada[:-1] + "B"
      else:
          cadeiaComB = "B" + entrada + "B"
      if cadeiaComB == "B-B":
        cadeiaComB = "BB"
      listaDeCadeias.append(cadeiaComB)
    return listaDeCadeias
  except:
    print("Erro na entrada das cadeias a serem processadas!")
    exit()


'''
Função main do programa


1 - maquinaDeTuring recebe uma instancia da classe MaquinaDeTuring
2 - cadeias recebe uma lista de cadeias a serem processadas
3 - com o objeto maquinaDeTuring eu evoco o método imprimirProcessamentoDeCadeias passando por parâmetro as cadeias lidas e este imprime no StdOut quais foram aceitas e quais não foram.
'''

maquinaDeTuring = lerExpecificacoesDaMaquina()
cadeias = lerCadeias()

#Funções de impressão para debug
#maquinaDeTuring.imprimirMaquinaDeTuring()
#print(cadeias)

maquinaDeTuring.imprimirProcessamentoDeCadeias(cadeias)