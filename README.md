# Códigos referentes a disciplina de Linguagens Formais e Autômatos
## Curso: Ciência da Computação - UFT Campus Palmas
### Trabalho 3
Implementar computacionalmente em um linguagem de programação de alto nível, uma aplicação para validar o preenchimento de um formulário feito por algum usuário. Para isso você deverá utilizar a bilblioteca de expressões da linguagem de programação, que em python é "import re". O formulário deverá conter os seguintes campos:

 
- Nome: no máximo 50 símbolos alfabéticos e espaço [a-zA-Z ].
- CPF: somente algarismos numéricos [0-9] ou algarismos no formato padrão do CPF "000.000.000-00", ou seja, com ponto na posições 3 e 7 da string e hífen na posição 11.
- E-mail: o nome de usuário deverá ter no mínimo 2 símbolos alfanuméricos, ponto ou underline [\w\._] seguido de '@', que por sua vez concatena com o domínio (utilizar a mesma regra do nome do usuário). Para terminar, depois do domínio, deverá ter, obrigatoriamente, um ponto seguido do tipo de registro, que é formado por três símbolos alfabéticos minúsculos [a-z].
- Telefone: dois formatos possíveis, sendo o primeiro constituído por somente 11 números; e o segundo pelo "(00)00000-0000".
