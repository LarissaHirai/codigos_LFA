# Códigos referentes a disciplina de Linguagens Formais e Autômatos
## Curso: Ciência da Computação - UFT Campus Palmas
### Trabalho 1
Implementar computacionalmente a função de transição estendida do Autômato Finito Determinístico (AFD). A função de transição estendida é um função que toma um estado q ∈ Q e uma palavra w ∈ Σ* e retorna um estado p ∈ Q, ou seja, δ(q,w)=p. Em outras palavras, definimos δ por indução sobre o comprimento da palavra de entrada:

 
- Base: δ(q,ε)=q
- Isto é, se estamos no estado q e lemos nenhuma entrada, então ainda continuamos no estado q.

 
Indução: Suponha que w é uma palavra da forma xa, ou seja, a é o último símbolo de w, e x é a palavra que consiste em tudo, menos o último símbolo. Exemplo, w=1101 é desmembrado em x=110 e a=1. Assim, o passo de indução é: δ(q,w) = δ(δ(q,x),a)
Como tarefa, a implementação pode ser feita em qualquer linguagem de programação de alto nível e deverá ser utilizado, para isto, o AFD abaixo:

- [AFD](https://ava.uft.edu.br/palmas/pluginfile.php/368113/mod_assign/intro/Captura%20de%20Tela%202023-05-23%20%C3%A0s%2014.53.36.png)