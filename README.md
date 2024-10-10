# AuthAPI
# O que é o projeto
Este projeto é uma API RESTful desenvolvida em Python utilizando o framework FastAPI. 
Sua principal função é fornecer um sistema de autenticação utilizando 
tokens JWT (JSON Web Tokens). 
Além disso, a API oferece funcionalidades básicas de CRUD (Create, Read, Update, Delete) 
para gerenciar informações de usuários, incluindo o upload de fotos de perfil. 
A API também armazena as sessões dos usuários após o login.

# Contexto de Uso
A API foi desenvolvida como um projeto pessoal com o objetivo de explorar e 
consolidar conhecimentos em desenvolvimento de APIs, autenticação, e gerenciamento de
dados utilizando Python. Ela pode servir como base para a construção de 
aplicações web ou mobile que requerem um sistema de autenticação.
# Recursos Disponíveis

### Autenticação:
* Criação de usuários
* Login com validação de credenciais
* Geração de tokens JWT para autenticação segura
### Gerenciamento de Usuários:

* Criação, leitura, atualização e deleção de usuários
* Token fixo para criação de usuários
* Upload de fotos de perfil
* Endpoint para verificar se o token permanece válido 
### Sessões:

* Armazenamento de sessões após o login
* Validação de tokens em requisições subsequentes

# Proposta e Público Alvo
A proposta deste projeto é fornecer uma API completa e bem documentada para auxiliar desenvolvedores iniciantes e intermediários a entender os conceitos de desenvolvimento de APIs, autenticação e gerenciamento de dados utilizando Python e FastAPI. O público-alvo deste projeto inclui:

* Desenvolvedores Python: Que buscam aprender sobre desenvolvimento de APIs e autenticação.
* Estudantes: Interessados em aprofundar seus conhecimentos em desenvolvimento web e tecnologias relacionadas.
* Enthusiastas de tecnologia: Que desejam explorar as possibilidades do framework FastAPI.

# Documentação
## Sumário:
1. [Guia How-to](/doc/how-to.md)
   1. Passo a passo para iniciar a aplicação
   2. Passo a passo para iniciar a aplicação docker compose
4. [Tutoriais](/doc/tutoriais.md)
   1. Configurações adicionais
   2. Configurações de criptografia
7. [Documentação do usuário](/doc/user-doc.md)
   1. Criação de contas
   2. Acesso aos endpoints
   3. Log in na aplicação
   4. Alteração de senha
   5. Upload/alteração de foto
   6. Consumindo a API com Postman
   7. Consumindo a API com js
15. [Documentação do sistema](/doc/sys-doc.md)
    1. Design da aplicação
       1. Diagrama de entidade e relacionamento
       2. Diagramas de caso de uso
          1. Caso de uso - Criação de Pessoas
          2. Caso de uso - Log in
          3. Caso de uso - Alteração de senha
          4. Caso de uso - Armazenamento de sessões
       1. Diagramas de sequência
          1. Diagrama de sequência - Criação de pessoas
          2. Diagrama de sequência - Log in
          3. Diagrama de sequência - Alteração de senha
          4. Armazenamento de sessões
       1. Fluxo dos dados
2. [Documentação de desenvolvimento](/doc/dev-doc.md)
   1. Swagger
   2. Models
   3. Banco de dados
   4. Migrações
   5. Rotas
   6. Controllers
   7. Segurança
   8. Middlewares
   9. Dependências
3. [Guia de testes](/doc/test-doc.md)
   4. Testando com o swagger
   5. Teste de integração
   6. Testes unitários
   7. Teste de stress
   8. Troubleshooting
4. [Guia de deploy](/doc/depl-doc.md)
   1. Deploy na AWS
   2. Deploy em um PaaS (Render)