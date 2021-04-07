# Calculadora Python

- Calculadora com 4 operações (adição, subtração, multiplicação e divisão).<br>
- Desenvolvida com a finalidade de colocar alguns conceitos aprendidos no curso de Python 3 da Alura, na prática !

# Detalhes do sistema

1 - Definir a função principal chamda de "display()":
<br>
<br>
![image](https://user-images.githubusercontent.com/50367720/112857148-eeb83880-9086-11eb-9158-e065e0937105.png)
<br>
<br>
<br>
1.1 - A primeira execução da função display(), é uma chamada para a função "mensagem_inicializacao()":
<br>
<br>
![image](https://user-images.githubusercontent.com/50367720/112857702-8027aa80-9087-11eb-8243-d9f17497409e.png)
<br>
<br>
Nesta função é exibida a mensagem de inicialização da calculadora.
<br>
<br>
<br>
1.2 - Após a exibir a mensagem de inicialização é exibido também as operações disponíveis:
<br>
<br>
![image](https://user-images.githubusercontent.com/50367720/112858115-f1fff400-9087-11eb-9a44-373442fe7a57.png)
<br>
<br>
<br>
1.3 - Logo em seguida é declarado 3 variáveis ("operacao", "primeiro_numero" e "segundo_numero") onde cada uma respectivamente recebe uma função específica ("leia_operacao()", "leia_numero(1)" e "leia_numero(2)"):
<br>
<br>
![image](https://user-images.githubusercontent.com/50367720/112859056-d9dca480-9088-11eb-838d-d74dca9e71e7.png)
<br>
<br>
<br>
1.3.1 - Função "leia_operacao()":
<br>
<br>
![image](https://user-images.githubusercontent.com/50367720/112860928-b0bd1380-908a-11eb-919a-6f685320ef03.png)
<br>
<br>
- Inicia com um looping (while) com parâmetro "True", sendo assim um looping infinito.<br>
-- Dentro dele a variável "entrada" recebe o valor digitado pelo usuário por meio da função "input()".<br>
-- Em seguida é feito uma validação, onde verifica se (if) o que o usuário digitou é um número através da função "isnumeric()".<br>
--- Caso o usuário tenha digitado um número agora esse número é convertido em um número inteiro com a função "int()".<br>
--- E em seguida verifica se (if) esse número está entre 1 e 4.<br>
---- Caso esteja, interrompe e sai do looping (break).<br>
--- Caso não esteja, exibe uma mensagem de erro.<br>
-- Caso não for um número, exibe uma mensagem de erro.<br>
- Retorna o valor digitado pelo usuário<br>
<br>
<br>
<br>
1.3.2 - Função "leia_numero(parâmetro)":
<br>
<br>
<img src="https://user-images.githubusercontent.com/50367720/112878132-f33c1b80-909d-11eb-993a-d5bfeffd80de.png"/>
<br>
<br>
- Inicia com um loopping infinito assim como na função "leia_operacao()".<br>
-- Dentro dele é feita a primeira validação, que testa se (if) o número recebido como parâmetro da função é igual a 1.<br>
--- Caso for igual, a variável "entrada" recebe o valor que o usuário digitou como sendo o primeiro número para o cálculo.<br>
--- Caso for diferente de 1, a variável "entrada" recebe o valor que o usuário digitou como sendo o segundo número para o cálculo.<br>
-- Em seguida é feito outra validação, tentando (try) converter o valor da variável "entrada" em um número decimal com a função float().<br>
--- Caso der certo, a conversão é atribuida a variável "entrada" e para o looping.<br>
-- Caso não der certo a conversão (except).<br>
--- Imprime um erro.<br>
- Retorna o valor digitado pelo usuário.<br>
<br>
<br>
<br>
1.4 - Após a validação dos valores de entrada, agora é executado a função seleciona_operacao(p1, p2, p3) que recebe 3 parâmetros e é a responsável pelo retorno do resultado da operação selecionada:
<br>
<br>
<img src="https://user-images.githubusercontent.com/50367720/112903706-44f49e00-90be-11eb-838a-90c130106970.png"/>
<br>
<br>
<br>
1.4.1 - Dentro da função seleciona_operacao() é feito uma filtragem com base na operação que o usuário digitar e para cada operação é chamado uma função específica que retorna um resultado:
<br>
<br>
- Essas funções são bem simples e similares diferenciando-se apenas pelo operador matemático e são elas "somar(p1, p2)", "subtrair(p1, p2)", "multiplicar(p1, p2)" e "dividir(p1, p2)", recebendo 2 parâmetros cada sendo respectivamente "p1" o "primeiro_numero" e "p2" o "segundo_numero":
<br>
<br>
<img src="https://user-images.githubusercontent.com/50367720/112904807-e29c9d00-90bf-11eb-8180-2346d5ce069a.png">
<br>
<br>
- E por fim imprime o resultado com formatação através de uma interpolação de String.
<br>
<br>
<br>
# FIM xD
