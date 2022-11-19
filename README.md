Simulador Universal de Máquina de Turing
===============


O simulador foi desenvolvido para atender a atividade 2 proposta na disciplina de ITC (Introdução à Teoria da Computação).

Seus integrantes são:
```
Eduardo Costa Miranda Azevedo --- 12677151
Gustavo de Oliveira Martins ----- 12625531
Ivan Barbosa Pinheiro -----------  9050552
Raquel de Jesus Santos Valadão -- 12674022
Ryan Souza Sá Teles ------------- 12822062
```

Instalação e Execução 
----------

A instalação é bem simples, basta ter o Python instalado em sua máquina, caso não tenha siga o tutorial conforme sua plataforma que pode ser encontrado acessando este link https://www.python.org/, com o Python instalado basta baixar o arquivo "main.py" e executá-lo conforme sua plataforma.

Como usar
-----

Digamos que você tenha a seguinte Máquina de Turing que processa a linguagem aⁿbⁿcⁿ, com n > 0, e você queira verificar algumas cadeias de símbolos terminais:

![Máquina de Turing](https://i.imgur.com/NumYK4p.png)

Para definir esta máquina e realizar estas verificações é bem simples, você deve criar um arquivo texto que siga o modelo abaixo:

```pascal
6
3 a b c
4 # * @ B
5
18
0 a 1 # R
1 # 1 # R
1 a 1 a R
1 * 1 * R
1 b 2 * R
2 b 2 b R
2 @ 2 @ R
2 c 3 @ L
3 # 3 # L
3 * 3 * L
3 @ 3 @ L
3 b 3 b L
3 a 1 # R
3 B 4 B R
4 # 4 # R
4 * 4 * R
4 @ 4 @ R
4 B 5 B R
10
abbcca
aabbcc
bac
aaabbbcccc
-
abcabc
abc
abcc
c
aaabbbbccc
```

Não entendeu? Segue a definição de cada campo para facilitar:

```js
6             <- Quantidade estados
3 a b c       <- Quantidade de simbolos terminais, seguido deles.
4 # * @ B     <- Quantidade de marcadores de fita, seguido deles.
5             <- O estado de aceitação da minha máquina.
18            <- Quantidade de transições
0 'a' 1 '#' R <- Do estado 0 se leio 'a' vou para o estado 1 escrevo '#' e movo para  direita
1 '#' 1 '#' R <- Do estado 1 se leio '#' vou para o estado 1 escrevo '#' e movo para  direita
1 'a' 1 'a' R <- Do estado 1 se leio 'a' vou para o estado 1 escrevo 'a' e movo para  direita
1 '*' 1 '*' R <- Do estado 1 se leio '*' vou para o estado 1 escrevo '*' e movo para  direita
1 'b' 2 '*' R <- Do estado 1 se leio 'b' vou para o estado 2 escrevo '*' e movo para  direita
2 'b' 2 'b' R <- Do estado 2 se leio 'b' vou para o estado 2 escrevo 'b' e movo para  direita
2 '@' 2 '@' R <- Do estado 2 se leio '@' vou para o estado 2 escrevo '@' e movo para  direita
2 'c' 3 '@' L <- Do estado 2 se leio 'c' vou para o estado 3 escrevo '@' e movo para esquerda
3 '#' 3 '#' L <- Do estado 3 se leio '#' vou para o estado 3 escrevo '#' e movo para esquerda
3 '*' 3 '*' L <- Do estado 3 se leio '*' vou para o estado 3 escrevo '*' e movo para esquerda
3 '@' 3 '@' L <- Do estado 3 se leio '@' vou para o estado 3 escrevo '@' e movo para esquerda
3 'b' 3 'b' L <- Do estado 3 se leio 'b' vou para o estado 3 escrevo 'b' e movo para esquerda
3 'a' 1 '#' R <- Do estado 3 se leio 'a' vou para o estado 1 escrevo '#' e movo para  direita
3 'B' 4 'B' R <- Do estado 3 se leio 'B' vou para o estado 4 escrevo 'B' e movo para  direita
4 '#' 4 '#' R <- Do estado 4 se leio '#' vou para o estado 4 escrevo '#' e movo para  direita
4 '*' 4 '*' R <- Do estado 4 se leio '*' vou para o estado 4 escrevo '*' e movo para  direita
4 '@' 4 '@' R <- Do estado 4 se leio '@' vou para o estado 4 escrevo '@' e movo para  direita
4 'B' 5 'B' R <- Do estado 4 se leio 'B' vou para o estado 5 escrevo 'B' e movo para  direita
10            <- Quantidade de cadeias a serem verificadas
abbcca        <- Cadeia 1
aabbcc        <- Cadeia 2
bac           <- Cadeia 3
aaabbbcccc    <- Cadeia 4
-             <- Cadeia 5 (Representação da cadeia nula)
abcabc        <- Cadeia 6
abc           <- Cadeia 7
abcc          <- Cadeia 8
c             <- Cadeia 9
aaabbbbccc    <- Cadeia 10
```

No diretório  "Casos de Teste" já existem alguns exemplos(inclusive o exemplo acima seria o "0.in".

```
0.in -> processa a linguagem aⁿbⁿcⁿ, com n > 0
1.in -> processa a linguagem dos número binários semelhantes divididos por '#' (marcador)
2.in -> processa a linguagem dos palindromos de 'a' e 'b'
```

Após a criação deste documento de texto você deve executar o programa "main.py" (no nosso caso utilizamos um ambiente linux, então o comando é "python3 main.py", mas pode variar dependendo de seu sistema operacional)

Ao abrir uma tela de solicitação de arquivo, selecione o arquivo que deseja verificar.

Caso o arquivo seja válido e esteja no modelo correto, ele interpretará as cadeias e criará um arquivo de saída dentro de uma pasta que será criada chamada "saidas" (como por exemplo a saída do "in0.txt").

```
rejeita
aceita
aceita
aceita
rejeita
rejeita
aceita
rejeita
rejeita
rejeita
```
