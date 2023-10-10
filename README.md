# Documentação do Site de Agenda

## Visão geral do site


O site de agenda é uma aplicação web que permite aos usuários adicionar, editar e excluir contatos. Ele foi construído usando o framework Django e possui as seguintes funcionalidades:

1. Cadastro e login de usuários
2. Adição de contatos com nome, telefone, e-mail e endereço
3. Edição de contatos existentes
4. Exclusão de contatos existentes
5. Visualização de todos os contatos do usuário

---

# Instalação
Para instalar e executar o site de agenda, siga estas etapas:

### Clone o repositório do GitHub:
` git clone https://github.com/Hericlys/agenda-django.git `

### Instale as dependências:
` pip install -r requirements.txt`

### Crie um banco de dados:
`python manage.py migrate`

### Crie um superusuário para acessar o painel de administração:
`python manage.py createsuperuser`

### Execute o servidor:
`python manage.py runserver`

# Uso
Após instalar e executar o site de agenda, você pode acessá-lo pelo navegador em http://localhost:8000/. Você verá a página inicial, onde poderá criar uma conta ou fazer login se já tiver uma.

<br>
<div align="center">
    <img src="https://cdn.discordapp.com/attachments/927590344760098880/1106933944416481350/pagina_inicial_do_site.png" width="700px">
</div>
<br>

Após fazer login, você verá a página principal da agenda, onde poderá adicionar, editar e excluir contatos. Para adicionar um novo contato, clique no botão "Create contact" e preencha as informações necessárias. Para editar ou excluir um contato existente, clique nos id correspondentes ao lado do contato desejado.

<br>
<div align="center">
    <img src="https://cdn.discordapp.com/attachments/927590344760098880/1106943646013608007/pagina_index.png" width="700px">
</div>
<br>

## Painel de administração

O site de agenda também possui um painel de administração para gerenciar usuários e contatos. Para acessá-lo, faça login como superusuário em http://localhost:8000/admin/. No painel de administração, você pode criar, editar e excluir usuários, contatos e categorias.

<br>
<div align="center">
    <img src="https://cdn.discordapp.com/attachments/927590344760098880/1106944845500653598/pagina_admin.png" width="700px">
</div>
<br>

# Considerações finais

O site de agenda é uma aplicação simples, mas funcional, que permite aos usuários gerenciar seus contatos de forma eficiente. Ele foi construído usando o framework Django **Para fins de estudo com o professor Luiz Otavio miranda**.

---

## sobre o script de criação de contatos:

`python utils/create_contact.py`

### informações:
serve para adcionar contatos para um ususario com dados aléatorios retirados do faker 

### Avisos importantes :

> Para o uso do script de criação de contatos lembre-se de realizar a instalação do faker com o comando: `pip install faker`.

> Se quiser que todos os contatos anteriores sejam apagados antes de inserir novos contatos basta descomentar as linhas especificadas em verde

> Para que os contatos sejam visiveis para um usuario lembre-se de informalo no filtro de busca e descomentar a linha 61 do codigo

<br>
<div align="center">
    <img src="https://cdn.discordapp.com/attachments/927590344760098880/1106986376949403738/script_create_contact.png" width="700px">
</div>
<br>
