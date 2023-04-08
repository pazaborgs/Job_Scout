# JobScout

JobScout é um projeto web com intuito de facilitar o acompanhamento e gerenciamento de vagas de emprego. O site permite ao usuário cadastrar empresas e suas vagas de emprego, mantendo em um só local a informação sobre todos os processos seletivos do qual participa. A motivação para o desenvolvimento do projeto foi a falta de um sistema organizacional capaz de acompanhar em um só lugar as vagas de emprego que um usuário está inscrito. O objetivo é criar um projeto web capaz de manter informações sobre vagas cadastradas pelo usuário em uma só base de dados, e ser capaz de fazer consultar eficientes nessa base de dados.

## Tecnologias

O projeto será desenvolvido utilizando conhecimentos de banco de dados relacionais e linguagem SQL, controle de versionamento com Git e Github e framework web Django.

## Porque Django?

- Django é um framework maduro, com mais de uma década no mercado e é usado por grandes empresas como Spotify, Spotify, Youtube…
- Por ser um framework maduro no mercado, existem uma enorme quantidade de tutoriais e documentação disponível;
- Django é um framework que vem com “pilhas inclusas”, ou seja, ele é já é capaz por natureza de permitir uma séria de implementações comuns mas complexas de maneira agilizada e em um curto espaço de tempo.

## Iniciando o Projeto

Para iniciarmos nosso projeto, primeiro criaremos um novo aplicativo.

## Templates e Folha de Estilos

### Templates

É comum no desenvolvimento de aplicações com Django manter os arquivos de estruturação html dentro de uma pasta com nome template. Uma boa prática é criar uma nova pasta interna para cada página de aplicação criada, pois ajuda a manter a organização e facilita na hora de buscar arquivos em diretórios.

### Static Files

O termo static files (arquivos estáticos) refere-se a arquivos não variáveis, usados por sites modernos para renderizar coisas como imagens e folhas de estilo, rodar código JavaScript, entre outras coisas. Para configurar os arquivos estáticos, vamos até o arquivo settings.py, em setup, e configuramos da seguinte maneira:

    STATIC_URL = 'static/'
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'setup/static'),)
    STATIC_ROOT = os.path.join('static')

### base.html

O arquivo base.html é responsável por manter os elementos da página html padrão, fixos independente da página. No nosso caso, temos como fixo somente a barra de navegação e o rodapé página. Para carregarmos os arquivos estáticos, o CSS da página, carregamos com o uso da tag static precedido por load, tudo isso entre chaves e %, para indicar que a linha representa código python:

    {% load static %}

Vale lembrar que os arquivos carregados vem da pasta static configurada anteriormente. No código html, carregamos a folha de estilos css base.css, que está na pasta styles, dentro de static (nossa pasta padrão para arquivos estáticos):

    ```html
    {% load static %}

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link
        href="https://fonts.googleapis.com/css2?family=Nunito&display=swap"
        rel="stylesheet"
        />
        <link
        href="https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css"
        rel="stylesheet"
        />
        <link
        rel="stylesheet"
        href="https://unpkg.com/boxicons@latest/css/boxicons.min.css"
        />
        <link rel="stylesheet" href="{% static '/styles/base.css' %}" />
        {% block 'head' %} {% endblock%}
        <title>Job Scout</title>
    </head>
    <body>
        <nav class="navbar navbar--light">
        <div class="navbar__logo">
            <img src="" alt="Logo" />
            <span>Logo</span>
        </div>
        <div class="navbar__itens">
            <ul>
            <li><a href="#">Jobs</a></li>
            <li><a href="#">About Us</a></li>
            <li><a href="#">Contact</a></li>
            </ul>
        </div>
        <div class="navbar__btns">
            <button class="navbar__btns__login" href="#">Login</button>
            <button class="navbar__btns__signin" href="#">Sign In</button>
            <div class="bx bx-menu" id="menu-icon"></div>
        </div>
        </nav>

        {% block 'body' %} {% endblock%}

        <footer class="footer footer--light">
        <div class="footer__socials">
            <ul>
            <li>
                <a href="#"><i class="ri-github-fill"></i></a>
            </li>
            <li>
                <a href="#"><i class="ri-linkedin-fill"></i></a>
            </li>
            <li>
                <a href="#"><i class="ri-instagram-line"></i></a>
            </li>
            <li>
                <a href="#"><i class="ri-mail-line"></i></a>
            </li>
            </ul>
        </div>
        <div class="footer__piinfo">
            <p>Projeto Integrador em Computação I — Eixo Computação 2021</p>
        </div>
        <div class="footer__credits">
            <p>Patrick Regis | Renato Aguetoni</p>
        </div>
        </footer>
    </body>
    </html>

    ```

Note como a referência ao arquivo css funciona, usando a tag link, usamos a palavra static, entre chaves e %, seguida do diretório onde se encontram nossos arquivos estáticos. As tags “block” e “endblock” são blocos de montagem do Django. Elas representam respectivamente onde um código html começa e termina. Isso é necessário pois esta página html é apenas um modelo básico. Esses componentes permitem que na hora de estendermos essa página para outros aplicativos, possamos adicionar conteúdo html entre essas tags, mantendo a barra de navegação e o rodapé intactos.

- [CSS da base](/setup/static/styles/base.css)

Com a barra de navegação e o cabeçalho feitos, podemos iniciar a criação do formulário responsável por cadastrar uma nova empresa. Cadastraremos essa página como nova_empresa.html:

    ```html
    {% extends "base.html" %}
    {% load static %}

    {% block 'head' %}
        <link href="{% static 'empresa/css/empresas.css' %}" rel="stylesheet">
    {% endblock%}

    {% block 'body' %}

        <section class="wrapper">
            <div class="box">

                {% if messages %}
                    {% for message in messages %}
                        <div class="alert {{message.tags}}" role="alert">
                            {{message}}
                        </div>
                    {% endfor %}
                {% endif %}

                <div class="header">
                    <h3 class="title">Nova empresa</h3>
                </div>

                <div class="body-box">
                    <form action= "{% url 'nova_empresa' %}" method="post" enctype="multipart/form-data" >
                        {% csrf_token %}

                        <div class="row">
                            <div class="col-md">
                                <label>Nome:</label>
                                {{form.name}}
                            </div>
                            <div class="col-md">
                                <label>E-mail:</label>
                                {{form.email}}
                            </div>
                            <div class="col-md">
                                <label>Sede:</label>
                                {{form.headquarters}}
                            </div>
                        </div>
                        <br>
                        <div class ="row">
                            <div class="col-md">
                                <label>Tamanho da Empresa:</label>
                                {{form.company_size}}
                                </select>
                            </div>
                            <div class="col-md">
                                <label>Nicho de mercado:</label>
                                {{form.marketing_niche}}
                            </div>
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-md">
                                <label>Tecnologias:</label>
                                {{form.technologies}}
                            </div>
                            <div class="col-md">
                                <label>Especializações:</label>
                                {{form.specializations}}
                            </div>
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-md">
                                <label>Logo:</label>
                                {{form.logo}}
                            </div>
                        </div>
                        <br>
                        <input type="submit" value="Nova empresa" class="form__submitbtn">
                    </form>

                </div>
            </div>
        </section>

    {% endblock%}

    ```

Na primeira linha, estendemos o html configurado em base.html, ou seja, teremos um html igual ao da base e podemos adicionar conteúdo nos blocos de componente Django do tipo body que definimos no html da base. Também iremos adicionar conteúdo bloco de construção 'head' para separar o css de cada nova página que criarmos,

Note que no html do app empresas temos vários inputs com informações que caracterizam a empresa a ser cadastrada. Usaremos esses dados em conjunto com o Django para modelar um banco de dados eficiente e que atenda as necessidades da nossa aplicação. O framework Django é capaz de abstrair a modelagem do banco de dados. Na prática, isso quer dizer que não usaremos comandos SQL, mas sim modelamos relações e atributos declarando classes:

    ```python
    from django.db import models

    class Technologies(models.Model):
        technology = models.CharField(max_length=30)

        def __str__(self):
            return self.technology

    class Specializations(models.Model):
        specialization = models.CharField(max_length=30)

        def __str__(self):
            return self.specialization

    class Company(models.Model):

        choices_size = (
            ('Micro', 'Até 19 colaboradores'),
            ('Pequena', '20 à 99 colaboradores'),
            ('Media', '100 à 499 colaboradores'),
            ('Grande', 'Acima de 500 colaboradores'),
        )
        choices_niche = (
            ('M', 'Marketing'),
            ('T', 'Tecnologia'),
            ('N', 'Nutrição'),
            ('D', 'Design'),
        )

        name = models.CharField(max_length=30)
        email = models.EmailField()
        headquarters = models.CharField(max_length=30)
        company_size = models.CharField(max_length=30, choices= choices_size)
        marketing_niche = models.CharField(max_length=3, choices=choices_niche)
        technologies = models.ManyToManyField(Technologies)
        specializations = models.ManyToManyField(Specializations)
        logo = models.ImageField(upload_to='company_logo')

        def __str__(self) -> str:
            return self.name
    ```

Em Django, declaramos as relações em um banco de dados como classes. No exemplo acima, a relação Company tem uma série de atributos (colunas) como logo, nome, email, sede, entre outros. Note que:

- Declaramos as colunas definindo seu nome e o tipo de dado que a coluna terá;
- No campo tecnologias, declaramos um campo de relação M para N como ManytoManyField e indicamos a relação na qual será responsável por fazer esse pareamento. Com Django é fácil modelar campos de dados multivalorados;
- Também é possível declarar facilmente campos de escolha (Choices). Para isso, criamos uma variável responsável por manter as possíveis escolhas do usuário e a referenciamos utilizando a sintaxe choices=variável. No código, nossas variáveis choice são choices_niche e choices_size.

## Configurando os Formulários

Manusear formulários é uma tarefa complexa. Felizmente podemos criar um formulário Django e deixar todo o processo de processamento do formulário nas mãos do framework. O formulário Django simplifica e automatiza uma vasta porção do trabalho complexo relacionado a formulários, além de manter o código mais seguro e a prova de falhas.

O Django manuseia as seguintes tarefas quando falamos de formulários:

- Preparar e reconstruir dados para renderiza-la;
- Criar formulários HTML para os dados;
- Receber e processar formulários com dados enviados pelo usuário.

Para usar formulários Django, criamos no aplicativo empresas um arquivo chamado forms.py e dentro dele importamos os recursos disponibilizados pelo django para lidar com formulários: Como já definimos nossos models, criaremos uma classe vamos exdende-la de forms.ModelsForm. Após, criaremos outra classe com o nome Meta e nela definiremos qual relação do banco de dados iremos usar e quais campos nosso formulário terá. No nosso caso, usaremos todos os campos definidos na relação Company:

    ```python
    from django import forms
    from empresas.models import Company

    class CadastroEmpresa(forms.ModelForm):

        class Meta:
            model = Company
            fields = '__all__'

    ```

Depois, para renderizar no html é so usar a sintaxe de variável comum, entre {{}}. Segue um exemplo abaixo:

    ```html
    <div class="row">
        <div class="col-md">
            <label>Nome:</label>
            {{form.name}}
        </div>

        <div class="col-md">
            <label>E-mail:</label>
            {{form.email}}
        </div>

    ```

### Validados os Dados

Vamos configurar validações para que o formulário somente recebe dados consistentes com os formatos definidos no banco de dados. Inicialmente, precisamos das seguintes validações:

1. Garantir que nenhum campo esteja vazio.
2. Definir um tamanho máximo para o arquivo de logo. Se exceder o limite, retorna um erro e redireciona o usuário para pagina de cadastro novamente.
3. Garantir que o nicho escolhido estará obrigatoriamente nas opções dadas no seletos. Se de alguma forma entrar algum dado inconsistente, retorna um erro e redireciona o usuário para pagina de cadastro novamente.

A validação 1 e 3 o formulário Django já realiza para nós. Como nas models os campos foram definidos como obrigatórios, não será possível cadastrar o formulário com campos vazios ou nichos e tamanhos de empresa que não se encontrem nas variáveis choice dentro de models.py

Para garantirmos a validação número 2, no arquivo forms.py faremos:

    ```python
    def clean_logo(self):
            data =  self.cleaned_data.get('logo')
            filesize= data.size

            if filesize > 100_000_000:
                raise forms.ValidationError("You cannot upload file more than 10Mb")
            else:
                return data

    ```

Criamos uma função que terá como argumento o logo cadastrado pelo usuário. Utilizaremos esse logo com o método cleaned_data, que retorna um dicionário com campos de input e seus valores validados. Montamos então um pequeno laço condicional que verifica se o arquivo passado excede o limite de 10Mb. Caso seja muito grande, levantamos um ValidationError, um erro de validação e mandamos o usuário de volta para a página com o formulário.

## Configurando as Mensagens de Erro

É muito comum em aplicações web a necessidade de renderizar mensagens flash (flash messages) ao usuário, após o processamento de um formulário ou input. Essas mensagens flash servem para informar ao usuário o resultado da transação, se ela foi um sucesso, se houve falhas, entre outros.

O Django provê um suporte completo para implementação dessas mensagens, através do framework de mensagens. O message framework permite temporariamente armazenar mensagens em uma requisição e recupera-la para mostrar com uma request subsequente. Cada mensagem é etiquetada com um nível específico, que determina sua prioridade (info, warning, error)

O arquivo padrão settings.py criado por django-admin startproject já contem todas as configurações necesárias para habilitar as mensagens.

The messages framework is based on a configurable level architecture similar to that of the Python logging module. Message levels allow you to group messages by type so they can be filtered or displayed differently in views and templates.

The built-in levels, which can be imported from django.contrib.messages directly, are:

- Constant Purpose
- DEBUG Development-related messages that will be ignored (or removed) in a production deployment
- INFO Informational messages for the user
- SUCCESS An action was successful, e.g. “Your profile was updated successfully”
- WARNING A failure did not occur but may be imminent
- ERROR An action was not successful or some other failure occurred

The MESSAGE_LEVEL setting can be used to change the minimum recorded level (or it can be changed per request). Attempts to add messages of a level less than this will be ignored.

Para configurar as mensagens, iremos até settings.py e faremos:

    from django.contrib.messages import constants

    MESSAGE_TAGS = {
        constants.DEBUG: 'alert-primary',
        constants.ERROR: 'alert-danger',
        constants.SUCCESS: 'alert-success',
        constants.INFO: 'alert-info',
        constants.WARNING: 'alert-warning',
    }

Para usar mensagens nas views e nos templates, usamos:

    from django.contrib import messages
    messages.add_message(request, messages.INFO, 'Hello world.')

Para renderizar e mostrar a mensagem de error, nos templates usaremos:

    {% if messages %}
        {% for message in messages %}
            <section class="alert {{message.tags}}">
                {{message}}
            </section>
        {% endfor %}
    {% endif %}

Ao terminar, para salvar tudo no banco de dados, usaremos:

    company.save()
    company.technologies.add(*technologies)
    company.save()
    company.specializations.add(*specializations)

    messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
    return redirect('/home/empresas')

MANYTOMANY FIELD

This is okay. The core functionality is there but the form needs a lot of work.

For one, I need to cmd-click to select multiple users. This is bad for user experience; checkboxes would be much more user-friendly.

The labels have been taken straight from admin. I want the user to see just the first name, not the user’s email as well.

We need a custom form

In Django, we can use class-based views to generate forms without defining one in forms.py. We can create a custom form class in forms.py where we can choose which of Django’s form widgets get used for each field.

## Listando as Empresas Cadastradas

Com o cadastro finalizado, agora precisamos de uma página para exibir as empresas cadastradas no banco de dados. Para isso, criaremos uma nova url no aplicativo empresas:

    path('empresas_cadastradas', empresas_cadastradas, name="empresas_cadastradas")

Criaremos tambem uma função nas views responsável por renderizar o html da página. Além disso, essa função será responsável por enviar a página as empresas, suas tecnologias e suas especializações:

    ```python
    def empresas_cadastradas(request):

        companies = Company.objects.all()
        technologies = Technologies.objects.all()
        specializations = Specializations.objects.all()
        return render(request, 'empresas_cadastradas.html', {'companies': companies, 'technologies': technologies, 'specializations': specializations})
    ```

- [HTML empresas cadastradas](/templates/empresas_cadastradas.html)
- [CSS empresas cadastradas](/setup/static/styles/empresas_cadastradas.css)

### Deletando as Empresas

Vamos adicionar a funcionalidade de deletar empresas do banco de dados. Para isso, primeiramente criaremos uma nova url para direcionarmos a informação do click no botão deletar. Essa url será responsável por processar a requisição e nos mandar de volta para a tela de empresas cadastradas:

    ```python
    path('excluir_empresa/<int:id>', excluir_empresa, name="excluir_empresa")
    ```

Criaremos também a view responsável por essa url. Nossa view irá ter como argumento a requisçao HTTP e o id passado por url. Com o id da empresa em mãos, faremos uma busca no banco de dados pela empresa que contém esse id e iremos deleta-la usando o método delete():

    def excluir_empresa(request, id):
        company = Company.objects.get(id = id)
        company.delete()
        messages.add_message(request, constants.SUCCESS, 'Empresa excluída com sucesso')
        return redirect('/home/empresas_cadastradas')
