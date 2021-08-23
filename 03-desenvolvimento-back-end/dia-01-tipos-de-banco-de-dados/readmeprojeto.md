### Termos e acordos
​
Ao iniciar este projeto, você concorda com as diretrizes do Código de Ética e Conduta e do Manual da Pessoa Estudante da Trybe
​
# Boas vindas ao repositório do projeto All For One
​
Você já usa o GitHub diariamente para desenvolver os exercícios, certo? Agora, para desenvolver os projetos, você deverá seguir as instruções a seguir. Fique atento a cada passo, e se tiver qualquer dúvida, nos envie por _Slack_! #vqv 🚀
​
Aqui você vai encontrar os detalhes de como estruturar o desenvolvimento do seu projeto a partir desse repositório, utilizando uma branch específica e um _Pull Request_ para colocar seus códigos.
​
# Sumário
​
- [Habilidades](#habilidades)
- [Entregáveis](#entregáveis)
  - [O que deverá ser desenvolvido](#o-que-deverá-ser-desenvolvido)
  - [Desenvolvimento](#desenvolvimento)
  - [Data de entrega](#data-de-entrega)
- [Instruções para entregar seu projeto](#instruções-para-entregar-seu-projeto)
  - [Antes de começar a desenvolver](#antes-de-começar-a-desenvolver)
  - [Durante o desenvolvimento](#durante-o-desenvolvimento)
- [Como desenvolver](#como-desenvolver)
  - [Instruções para restaurar o banco de dados Northwind](#instruções-para-restaurar-o-banco-de-dados-northwind)
  - [Instruções para testar suas queries](#instruções-para-testar-suas-queries)
- [Requisitos do projeto](#requisitos-do-projeto)
  - [Lista de requisitos](#lista-de-requisitos)
    - [Desafios Iniciais](#desafios-iniciais)
    - [Desafios sobre filtragem de dados](#desafios-sobre-filtragem-de-dados)
    - [Desafios de manipulação de tabelas](#desafios-de-manipulação-de-tabelas)
- [Depois de terminar o desenvolvimento (opcional)](#depois-de-terminar-o-desenvolvimento-opcional)
- [Revisando um pull request](#revisando-um-pull-request)
- [Avisos Finais](#avisos-finais)
​
---
​
# Habilidades
Nesse projeto, você será capaz de:
​
- Entender o que são bancos de dados
- Entender como a linguagem de consulta estruturada (SQL) é usada
- Compreender como as tabelas se encaixam no conceito de banco de dados
- Montar um ambiente de desenvolvimento local para praticar SQL
- Entender como usar o MySQL Workbench
- Compreender o que é uma query SQL e quais são seus tipos de comando
- Gerar valores com `SELECT`
- Selecionar colunas individualmente com `SELECT`
- Renomear e gerar colunas em uma consulta com `AS`
- Concatenar colunas e valores com `CONCAT`
- Remover dados duplicados em uma consulta com `DISTINCT`
- Contar a quantidade de resultados em uma consulta com `COUNT`
- Limitar a quantidade de resultados em uma consulta com `LIMIT`
- Pular resultados em uma consulta com `OFFSET`
- Ordernar os resultados de uma consulta com `ORDER BY`
- Filtrar resultados de consultas com o `WHERE`
- Utilizar operadores booleanos e relacionais em consultas
- Criar consultas mais dinâmicas e maleáveis com `LIKE`
- Fazer consultas que englobam uma faixa de resultados com `IN` e `BETWEEN`
- Encontrar e separar resultados que incluem datas.
- Inserir dados em tabelas com `INSERT`
- Atualizar dados em tabelas com `UPDATE`
- Apagar dados em tabelas com `DELETE`
​
---
​
# Entregáveis
​
## O que deverá ser desenvolvido
​
Hoje você fará um projeto com o codinome *All For One* em que praticará todos os conceitos de SQL já ensinados até aqui. Porém, você vai usar um banco de dados totalmente diferente, então dê tchau para o `sakila` e dê boas vindas ao `Northwind`, que será usado neste projeto. As instruções de como restaurar o banco podem ser lidas a seguir.
​
---
​
## Desenvolvimento
​
Temos, nesse projeto, uma série de desafios com diferentes níveis de complexidade que devem ser resolvidos cada um em seu arquivo próprio.
​
1. Leia a pergunta e crie na raiz do projeto um arquivo chamado desafioN.sql, em que N é o número do desafio;
​
2. O arquivo deve conter apenas o código SQL do desafio resolvido. **Não se esqueça de incluir o ponto e vírgula (";")** no final de suas queries e também de colocar o nome do **banco_de_dados.tabela_por_completo**, como no exemplo a seguir:
​
```sql
SELECT * FROM northwind.orders;
```
​
3. Faça isso até finalizar todos os desafios.
​
4. Para entregar o seu projeto você deverá criar um _Pull Request_ neste repositório. Este _Pull Request_ deverá conter os arquivos `desafio1.sql`, `desafio2.sql` e assim por diante até o `desafio27.sql`, que conterão seu código `SQL` de cada desafio, respectivamente.
​
5. **Não é necessário colocar** `USE northwind` ou `SET SQL_SAFE_UPDATES = 0;` no início dos seus arquivos.
​
### ⚠️ É importante que seus arquivos tenham exatamente estes nomes! ⚠️
​
Você pode adicionar outros arquivos se julgar necessário. Qualquer dúvida, procure a monitoria.
​
Lembre-se que você pode consultar nosso conteúdo sobre [Git & GitHub](https://course.betrybe.com/intro/git/) sempre que precisar!
​
---
​
## Data de entrega
​
- Projeto individual.
​
- Serão `X` dias de projeto.
​
- Data de entrega para avaliação final do projeto: `DD/MM/YYYY - 14:00h`.
​
# Instruções para entregar seu projeto
​
## Antes de começar a desenvolver
​
1. Clone o repositório
  * `git clone https://github.com/tryber/sd-011-mysql-all-for-one.git`.
  * Entre na pasta do repositório que você acabou de clonar:
    * `cd sd-011-mysql-all-for-one`
​
2. Instale as dependências [**Caso existam**]
  * `npm install` [**exemplo**]
​
3. Crie uma branch a partir da branch `master`
  * Verifique que você está na branch `master`
    * Exemplo: `git branch`
  * Se não estiver, mude para a branch `master`
    * Exemplo: `git checkout master`
  * Agora, crie uma branch onde você vai guardar os `commits` do seu projeto
    * Você deve criar uma branch no seguinte formato: `nome-de-usuario-nome-do-projeto`
    * Exemplo: `git checkout -b seunome-mysql-all-for-one`
​
4. Para cada exercício você deve criar um novo arquivo sql seguindo a seguinte estrutura:
  * desafio1.sql, desafio2.sql...desafioN.sql
​
5. Adicione as mudanças ao _stage_ do Git e faça um `commit`
  * Verifique que as mudanças ainda não estão no _stage_
    * Exemplo: `git status` (deve aparecer o arquivo que você alterou como desafio1.sql)
  * Adicione o novo arquivo ao _stage_ do Git
      * Exemplo:
        * `git add .` (adicionando solução para desafio 1)
        * `git status` (deve aparecer listado o arquivo _desafio1.sql_ em verde)
  * Faça o `commit` inicial
      * Exemplo:
        * `git commit -m 'iniciando o projeto MySQL All For One'` (fazendo o primeiro commit)
        * `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )
​
6. Adicione a sua branch com o novo `commit` ao repositório remoto
  * Usando o exemplo anterior: `git push -u origin seunome-mysql-all-for-one`
​
7. Crie um novo `Pull Request` _(PR)_
  * Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/tryber/sd-011-mysql-all-for-one/pulls)
  * Clique no botão verde _"New pull request"_
  * Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
  * Clique no botão verde _"Create pull request"_
  * Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
  * **Não se preocupe em preencher mais nada por enquanto!**
  * Volte até a [página de _Pull Requests_ do repositório](https://github.com/tryber/sd-011-mysql-all-for-one/pulls) e confira que o seu _Pull Request_ está criado
​
---
​
## Durante o desenvolvimento
​
⚠ Lembre-se que garantir que todas as _issues_ comentadas pelo CodeClimate estão resolvidas! ⚠
​
## ⚠️ É importante que seus arquivos tenham exatamente estes nomes e esteja na raiz do projeto! ⚠️
​
* Faça `commits` das alterações que você fizer no código regularmente
​
* Lembre-se de sempre após um (ou alguns) `commits` atualizar o repositório remoto
​
* Os comandos que você utilizará com mais frequência são:
  1. `git status` _(para verificar o que está em vermelho - fora do stage - e o que está em verde - no stage)_
  2. `git add` _(para adicionar arquivos ao stage do Git)_
  3. `git commit` _(para criar um commit com os arquivos que estão no stage do Git)_
  4. `git push -u nome-da-branch` _(para enviar o commit para o repositório remoto na primeira vez que fizer o `push` de uma nova branch)_
  5. `git push` _(para enviar o commit para o repositório remoto após o passo anterior)_
​
---
​
# Como desenvolver
​
## Instruções para restaurar o banco de dados `Northwind`
​
1. Faça o download do arquivo de backup [aqui](northwind.sql) clicando em "Raw", depois clicando com botão direito e selecionando "Salvar como" para salvar o arquivo em seu computador.
2. Abra o arquivo com algum editor de texto, e selecione todo o conteúdo do arquivo usando `CTRL-A`.
3. Abra o MySQL Workbench.
4. Abra uma nova janela de query e cole dentro dela todo o conteúdo do arquivo `northwind.sql`.
5. Selecione todo o código com o atalho `CTRL-A` e depois clique no icone de trovão para executar a query.
​
    ![Restaurando o banco Northwind](images/restore_northwind.png)
6. Aguarde alguns segundos (espere em torno de 30 segundos antes de tentar fazer algo).
7. Clique no botão apontado na imagem a seguir para atualizar a listagem de banco de dados.
​
    ![Tabelas do banco Northwind](images/refresh_databases.png)
7. Verifique se o banco restaurado possui todas as seguintes tabelas:
​
    ![Tabelas do banco Northwind](images/northwind.png)
8. Clique com botão direito em cada tabela e selecione "Select Rows" e certifique-se que todas as tabelas possuem registros. Caso tenha alguma faltando, faça o passo a seguir. Caso contrário, pode ir para próxima seção.
9. Caso existam tabelas faltando, drope o banco de dados, clicando com o botão direito em cima do banco de dados northwind e selecionando "Drop Schema", e refaça os passos novamente, dessa vez aguardando um tempo maior quando executar o script de restauração.
​
    ![Drop Schema](images/drop_database.png)
​
---
​
## Instruções para testar suas queries
​
Para executar localmente os testes, é preciso escrever o seguinte comando no seu terminal:
```sh
MYSQL_USER=<SEU_NOME_DE_PESSOA_USUARIA> MYSQL_PASSWORD=<SUA SENHA> HOSTNAME=<NOME_DO_HOST> npm test
```
​
Ou seja, suponha que para poder acessar a base de dados feita neste projeto você tenha `root` como seu nome de pessoa usuária, `password` como senha e `localhost` como host. Logo, você executaria:
```sh
MYSQL_USER=root MYSQL_PASSWORD=password HOSTNAME=localhost npm test
```
​
Usando o exemplo anterior de base, suponha que você não tenha setado uma senha para `root`. Neste caso, você executaria:
```sh
MYSQL_USER=root MYSQL_PASSWORD= HOSTNAME=localhost npm test
  ```
---
​
:warning: **Não é necessário colocar** `USE northwind` ou `SET SQL_SAFE_UPDATES = 0;` no início dos seus arquivos :warning:
​
---
​
# Requisitos do projeto
​
Monte queries para encontrar as informações esperadas pelos desafios:
​
## Lista de Requisitos
​
## Desafios Iniciais
​
#### 1 - Exiba apenas os nomes dos produtos da tabela `products`.
​
#### 2 - Exiba os dados de todas as colunas da tabela `products`.
​
#### 3 - Escreva uma query que exiba os valores da coluna que contém a primary key da tabela `products`.
​
#### 4 - Conte quantos registros existem na coluna `product_name` da tabela `products`.
#### 5 - Monte uma query que exiba os dados da tabela `products` a partir do quarto registro até o décimo terceiro. Tanto o quarto quanto o décimo terceiro registros, precisam aparecer na consulta. Obs.: não use `where` ou `order by`.
​
#### 6 - Exiba os dados das colunas `product_name` e `id` da tabela `products` de maneira que os resultados estejam em ordem alfabética dos nomes.
​
#### 7 - Mostre apenas os ids dos 5 últimos registros da tabela `products` (a ordernação deve ser baseada na coluna `id`).
#### 8 - Faça uma consulta que retorne três colunas. Na primeira coluna, exiba a soma de `5 + 6` (essa soma deve ser realizada pelo SQL). Na segunda coluna deve haver a palavra \"de\". E por fim, na terceira coluna, exiba a soma de `2 + 8` (essa soma deve ser realizada pelo SQL). A primeira coluna deve se chamar \"A\", a segunda coluna deve se chamar \"Trybe\" e a terceira coluna deve se chamar \"eh\". Não use colunas pre-existentes, apenas o que for criado na hora.
​
---
​
## Desafios sobre filtragem de dados
​
#### 9 - Mostre t...
 Este snippet ficou truncado na exibição. Veja-o na íntegra
Compartilhado em
sd-11
há 40 minutos·de uma conversa

