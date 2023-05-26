# :construction: README em construção ! :construction:

# Restaurant Orders Project

<!-- ![app Screen Shot][product-screenshot] -->

<!-- ### Link da documentação do projeto: []() -->


<!-- TABLE OF CONTENTS -->
<details>
  <summary><h2><strong>Sumário</strong></h2></summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o Projeto</a>
      <ul>
        <li><a href="#contexto">Contexto</a></li>
        <li><a href="#tecnologias-utilizadas">Tecnologias Utilizadas</a></li>
        <li><a href="#funcionalidades-implementadas">Funcionalidades Implementadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#para-iniciar-a-aplicação-localmente">Para Iniciar a Aplicação Localmente</a>
      <ul>
        <li><a href="#pré-requisitos">Pré-requisitos</a></li>
        <li><a href="#clonando-o-repositório">Clonando o Repositório</a></li>
        <li><a href="#rodando-serviços-com-docker-compose-e-executando-a-aplicação">Rodando Serviços com docker-compose e Executando a Aplicação</a></li>
        <!-- <li><a href="#acessando-container-e-instalando-dependências">Acessando Container e Instalando Dependências</a></li> -->
        <!-- <li><a href="#subindo-banco-de-dados-e-executando-a-aplicação">Subindo Banco de Dados e Executando a Aplicação</a></li> -->
        <li><a href="#executando-testes-do-back-end-e-análise-de-cobertura">Executando Testes do Back-end e Análise de Cobertura</a></li>
        <li><a href="#parando-a-aplicação-e-descendo-os-containers">Parando a Aplicação e Descendo os Containers</a></li>
      </ul>
    </li>
    <li><a href="#contribuições-e-autoria">Contribuições e Autoria</a></li>
  </ol>
</details>


# Sobre o Projeto
  O projeto Restaurant Orders é uma aplicação Python de uma ferramenta de construção de cardápios. A ferramenta permite geração de cardápios de restaurantes, considerando possíveis restrições alimentares e também a disponibilidade dos ingredientes em estoque, a partir de registros iniciais em arquivos `.csv`.

## Contexto
  Esse projeto foi desenvolvido por _[Juliana Álvares](https://www.linkedin.com/in/juliana-alvares/)_, como parte do processo de aprendizado do Módulo de Back-end, do curso de Desenvolvimento Web da [Trybe](https://www.betrybe.com/) :rocket:
  
  _"A Trybe é uma escola do futuro para qualquer pessoa que queira mudar de vida e construir uma carreira de sucesso em tecnologia, onde a pessoa tem a possibilidade de só pagar quando conseguir um bom trabalho."_

  O programa conta com mais de 1.500 horas de aulas presenciais e online, aborda introdução ao desenvolvimento de software, front-end, back-end, ciência da computação, engenharia de software, metodologias Ágeis e habilidades comportamentais.

## Tecnologias Utilizadas

  #### Linguagens:
  * [![Python][Python-img]][Python-url]

  #### Testes:
  * [![pytest][pytest-img]][pytest-url]

  <!-- #### Auxiliares (Execução):
  * [![Docker][Docker-img]][Docker-url] -->
  <!-- * [![Postman][Postman-img]][Postman-url] -->
  <!-- * [![Railway][Railway-img]][Railway-url] -->

## Funcionalidades Implementadas

  - Gestão de pratos e receitas do Restaurante a partir de arquivo base `.csv`;
  - Geração dos cardápios de forma dinâmica, com base em restrições alimentares e disponibilidade de ingredientes;
  - Controle do estoque de ingredientes a partir de arquivo base `.csv`.

# Para Iniciar a Aplicação Localmente
  Para rodar esta aplicação localmente é necessário garantir o cumprimento dos pré-requisitos, fazer uma cópia do repositório e executar as instruções a seguir.

## Pré-requisitos
  <!-- * [docker-compose](https://docs.docker.com/compose/) em versão 1.29.2 ou superior. -->
  * [python3](https://www.python.org/)
  <!-- * Estar com a porta padrão do `mysql` (`3306`) liberada, pois o serviço `db` está configurado no docker-compose para conexão nesta porta. -->

## Clonando o Repositório
  ```bash
    git clone git@github.com:AlvaresJu/restaurant_orders.git
  ```
## Criando e Ativando o Ambiente Virtual
  ```bash
    cd restaurant_orders/
    python3 -m venv .venv && source .venv/bin/activate
  ```
## Instalando as Dependências no Ambiente Virtual
  ```bash
    python3 -m pip install -r dev-requirements.txt
  ```
<!-- ## Acessando Container e Instalando Dependências
  ```bash
    docker exec -it blogs_api bash
    npm install
  ```  -->
<!-- ## Subindo Banco de Dados e Executando a Aplicação
 *Obs.: comandos a serem executados de DENTRO do Container `node`*
  ```bash
    npm start
  ``` -->
## Executando Testes
  ```bash
    python3 -m pytest
  ```
<!-- ## Parando a Aplicação e Descendo os Containers
  ```bash
    npm run compose:down
  ``` -->

<!-- # Contribuições e Autoria
  Como descrito, este projeto foi proposto pela [Trybe](https://www.betrybe.com/) e desenvolvido por _[Juliana Álvares](https://www.linkedin.com/in/juliana-alvares/)_ durante o curso de Desenvolvimento Web realizado. Por isso, foram disponibilizados pela Trybe alguns arquivos base de configurações e auxiliares ao desenvolvimento do projeto, além de toda a parte do front-end. Segue especificação de autoria dos principais documentos:
  
  Arquivos/diretórios desenvolvidos pela autora do projeto (Juliana Álvares):
  > README.md | images/** | app/frontend/Dockerfile | app/backend/Dockerfile | app/backend/packages.npm | app/backend/src/controllers/** | app/backend/src/database/migrations/** | app/backend/src/database/models/** | app/backend/src/database/seeders/** | app/backend/src/entities/** | app/backend/src/interfaces/** | app/backend/src/middlewares/** | app/backend/src/routes/** | app/backend/src/services/** | app/backend/src/tests/** | app/backend/src/utils/** | app/backend/src/app.ts
  
  Arquivos/diretórios desenvolvidos pela Trybe:
  > .editorconfig | apps_install.sh | db.exemple.sql | dockerfile_dennylist.sh | package.json | package-lock.json | app/docker-compose.yml | app/docker-compose.dev.yml | app/frontend/** | app/backend/.eslintrc.json | app/backend/.env.example | app/backend/package.json | app/backend/package-lock.json | app/backend/.sequelizerc | app/backend/nyc.config.js | app/backend/tsc_eval.sh | app/backend/tsconfig.json | app/backend/src/database/config/** | app/backend/src/database/migrations/99999999999999-create-z.js | app/backend/src/database/models/index.ts | app/backend/src/server.ts -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/screenshot.png
<!-- [product-gif]: images/features.gif -->
[Python-img]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org/
[pytest-img]: https://user-images.githubusercontent.com/25181517/184117132-9e89a93b-65fb-47c3-91e7-7d0f99e7c066.png
[pytest-url]: https://docs.pytest.org/en/7.3.x/
[Docker-img]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
<!-- [Postman-img]: https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white
[Postman-url]: https://www.postman.com/
[Railway-img]: https://img.shields.io/badge/Railway-131415?style=for-the-badge&logo=railway&logoColor=white
[Railway-url]: https://railway.app/ -->