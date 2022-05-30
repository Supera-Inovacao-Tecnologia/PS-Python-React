# Avaliação Python + React

## Descrição

O teste consiste em construir uma API HTTP de um pseudo e-commerce de games utilizando Python (preferencialmente o framework Django), e construir a interface do e-commerce utilizando React Web. 

A lista de produtos está disponível no arquivo products.json, mas sinta-se livre para adicionar outros produtos.

As imagens estão disponíveis no arquivo assets.zip

## Requisitos Funcionais

- O usuário deverá fazer login
- O usuário poderá adicionar e remover produtos do carrinho.
- O usuário poderá ordenar os produtos por preço, popularidade (score) e ordem alfabética. A filtragem deve ser realizada pela API.
- Os valores exibidos no checkout (frete, subtotal e total) devem ser calculados dinamicamente conforme o usuário seleciona ou remove produtos.
- A cada produto adicionado, deve-se somar R$ 10,00 ao frete.
- Quando o valor dos produtos adicionados ao carrinho for igual ou superior a R$ 250,00, o frete é grátis.
- O usuário pode realizar checkout de seu carrinho de compras. 
- O usuário pode consultar os pedidos feitos.

## Requisitos Não Funcionais

- Deverá ser documentado no [README.md](./README.md) como executar/compilar/empacotar o projeto e quais os endpoints solicitados nos requisitos acima. Para esse fim podem ser utilizadas ferramentas de containerização e automatização de builds.
- Utilizar o banco de dados Postgres.
- Para CRUD das entidades no banco de dados, utilizar preferencialmente migrations.

## O que iremos avaliar

Levaremos em conta os seguintes critérios:

- Cumprimento dos requisitos
- Qualidade do projeto da API
- Qualidade do layout e fluidez da UX
- Organização do código e boas práticas
- Domínio das linguagens, bibliotecas e ferramentas utilizadas
- Organização dos commits
- Escrita e cobertura de testes
