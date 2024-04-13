# Trabalho 1: Módulos e Manipulação de Arquivos Texto
Elaborar um programa que exiba um menu inicial, com as opções disponíveis, e realize o
cadastro e manutenção de dados armazenados em arquivo texto. Considerações:
Esta atividade poderá ser feita em grupos de até quatro pessoas.
- O programa deve conter uma função com passagem de parâmetros, contendo
parâmetros obrigatórios e parâmetros opcionais (com valores default).
- O programa deve conter uma função que verifique se o arquivo existe ou não. Caso
não exista, exiba mensagem e retorne o valor False. Caso contrário, retorne o valor
True. Essa função deve ser chamada nos módulos de listagem, alteração e exclusão
de dados.
- Cada grupo pode escolher sobre os dados que serão cadastrados pelo seu
programa - com 4 campos. Por exemplo, cadastro de vinhos (marca, tipo, teor
alcoólico e preço), cadastro de filmes (título, gênero, duração e nota), cadastro de
contas a pagar (descrição, data, valor, pago [S/N]), ordens de serviço (defeito,
empresa, preço, status), cervejas (...), etc.
- Realizar as rotinas de inclusão de dados e listagem de dados. Na listagem, os dados
devem estar alinhados conforme os exemplos de aula. Ao final da listagem exibir o
nº de itens cadastrados e média ou total de algum campo numérico. *
## Escolher entre as seguintes opções: **
- Realizar módulo de alteração de dados (a partir do nº da linha) - Realizar
módulo de listagem em grupos (vinhos Tinto Seco e Outros, contas pagas e a
pagar, OS com status Ok e outras).
- Realizar módulo de transferência de dados do arquivo original (vinhos, filmes,
contas, os…) para um arquivo secundário (vinhos_avaliados,
filmes_avaliados…). Incluir item no menu com a listagem de dados do
arquivo secundário.
- Realizar módulo de exclusão de dados por números de linhas. O módulo
deve permitir a leitura de várias linhas separadas por vírgula. Exemplo -
Números das linhas a serem excluídas: 1, 3, 6
- Realizar módulo para pesquisa de dados, onde o usuário pode digitar um
valor de texto ou número - se for texto comparar com os campos de texto
cadastrados, se for número comparar com os campos numéricos
