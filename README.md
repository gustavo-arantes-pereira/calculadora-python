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
![image](https://user-images.githubusercontent.com/50367720/112878132-f33c1b80-909d-11eb-993a-d5bfeffd80de.png)
<br>
<br>
- Inicia com um loopping infinito assim como na função "leia_operacao()".
-- Dentro dele é feita a primeira validação, que testa se (if) o número recebido como parâmetro da função é igual a 1.
--- Caso for igual, a variável "entrada" recebe o valor que o usuário digitou como sendo o primeiro número para o cálculo.
--- Caso for diferente de 1, a variável "entrada" recebe o valor que o usuário digitou como sendo o segundo número para o cálculo.
-- Em seguida é feito outra validação, tentando (try) converter o valor da variável "entrada" em um número decimal com a função float().
--- Caso der certo, a conversão é atribuida a variável "entrada" e para o looping.
-- Caso não der certo a conversão (except).
--- Imprime um erro.
- Retorna o valor digitado pelo usuário.
<br>
<br>
<br>
1.4 - Após a validação dos valores de entrada, agora executamos a função seleciona_operacao()
