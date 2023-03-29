# Porque Django?

- Django é um framework maduro, com mais de uma década no mercado e é usado por grandes empresas como Spotify, Spotify, Youtube…
- Por ser um framework maduro no mercado, existem uma enorme quantidade de tutoriais e documentação disponível;
- Django é um framework que vem com “pilhas inclusas”, ou seja, ele é já é capaz por natureza de permitir uma séria de implementações comuns mas complexas de maneira agilizada e em um curto espaço de tempo.

## CSS  / Templates

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

    {% load static%}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{% static '/styles/base.css' %}">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter&display=swap" rel="stylesheet">
        <link href="https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css" rel="stylesheet">
        <link rel="stylesheet"
    href="https://unpkg.com/boxicons@latest/css/boxicons.min.css">
        <title>Job Scout</title>
    </head>
    <<body>
        <nav class="nav-bar">
            <div class="nav-logo">
                <img src="" alt="Logo">
            </div>
            <div class="nav-links">
                <ul class="nav-itens">
                    <li><a href="#">Jobs</a></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </div>
            <div class="nav-buttons">
                <button class="nav-login" href="#">Login</button>
                <button class="nav-signin" href="#">Sign In</button>
                <div class="bx bx-menu" id="menu-icon"></div>
            </div>
        </nav>
        {% block 'body' %}
        {% endblock %}
        <footer class="ft-box">
            <div class="ft-socials">
                <ul class="ft-icons">
                    <li><a href="#"><i class="ri-github-fill"></i></a></li>
                    <li><a href="#"><i class="ri-linkedin-fill"></i></a></li>
                    <li><a href="#"><i class="ri-instagram-line"></i></a></li>
                    <li><a href="#"><i class="ri-mail-line"></i></a></li>
                </ul>
            </div>
            <div class="pi-info">
                <p> Projeto Integrador em Computação  I -- Eixo Computação 2021 </p>
            </div>
            <div class="creators">
                <p>Patrick Regis | Renato Aguetoni</p>
            </div>
        </footer>
    </body>
    </html>

Note como a referência ao arquivo css funciona, usando a tag link, usamos a palavra static, entre chaves e %, seguida do diretório onde se encontram nossos arquivos estáticos. As tags “block” e “endblock” são blocos de montagem do Django. Elas representam respectivamente onde um código html começa e termina. Isso é necessário pois esta página html é apenas um modelo básico. Esses componentes permitem que na hora de estendermos essa página para outros aplicativos, possamos adicionar conteúdo html entre essas tags, mantendo a barra de navegação e o rodapé intactos. Segue o css da base:

    * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    }

    :root{

    }

    body {
        min-height: 100vh;
        background: #fff;
        color: black;
        padding-top: 64px;
    }

    .nav-bar {
        position: fixed;
        width: 100%;
        display: flex;
        height: 64px;   ;
        justify-content: space-between;
        align-items: center;
        z-index: 1000;
        right: 0;
        top: 0;
        background: transparent;
        padding: 28px 12%;
        font-family: 'Inter', sans-serif;
        transition: all .50s ease;
    }

    .nav-logo{
        font-weight:900;
        font-size: 1.3rem;
    }

    .nav-itens {
        list-style: none;
        display: flex;
    }

    .nav-itens a {
        color: black;
        font-size: 1.1rem;
        font-weight: 500;
        padding: 5px 0;
        margin: 0 30px;
        transition: all .50s ease;
        text-decoration: none;
    }

    .nav-itens a:hover {
        color: red;
    }

    .nav-buttons {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .nav-login {
        padding: 10px 40px;
        font-size: 1rem;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: all .50s ease;
    }

    .nav-login:hover {
        background-color: #a1a1a1;
    }

    .nav-signin {
        padding: 10px 40px;
        font-size: 1.1rem;
        font-weight: 500;
        border: none;
        border-radius: 5px;
        color: #f2f2f2;
        background-color: #202020;
        cursor: pointer;
        transition: all .50s ease;
    }

    .nav-signin:hover {
        background-color: #3d3d3d;
    }

    # menu-icon{
        align-items: center;
        font-size: 2rem;
        z-index: 10001;
        display: none;
    }

    @media (max-width: 1280px){
        .nav-bar{
            padding: 14px 2%;
            transition: .2s;
        }

        .nav-itens a{
            padding: 5px 0;
            margin: 0px 20px;
        }
    }

    @media (max-width: 1090px){
        #menu-icon{
            display: block;
        }

        .nav-itens{
            position: absolute;
            top:100%;
            right: -100%;
            width: 270px;
            height: 29vh;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            border-radius: 10px;
            transition: all .50 ease;
            background-color: #202020;
        }

        .nav-itens a{
            display: block;
            margin: 12px 0;
            padding: 0 25px;
            transition: all .50 ease;
            color: #f2f2f2
        }

        .nav-itens a:hover{
           color:cyan;
           transform: translateY(5px);
        }

        .nav-itens .open{
            right: 2%;
        }

        .pi-info{
            display: none;
        }

    }

    .ft-box {
        width: 100%;
        z-index: 1000;
        display: flex;
        flex-direction: column;
        align-items: center;
        font-family: 'Inter', sans-serif;
        background-color: transparent;
        padding: 28px 12%;
        gap: 8px;
    }

    .ft-icons {
        display: flex;
        list-style: none;
        font-size: 1.8rem;
        gap: 24px;
    }

    .ft-icons a {
        text-decoration: none;
        color: black;
    }

    .ft-icons a:hover {
        color: red;
        transition: all .50s ease;
    }

    .pi-info {
        font-size: 12px;
        text-align: center;
    }

    .creators {
        font-size: 10px;
        text-align: center;
    }

Com a barra de navegação e o cabeçalho feitos, podemos iniciar a criação do formulário responsável por cadastrar uma nova empresa:


{% extends "base.html" %}

{% block 'body' %}

    <div class="wrapper">
        <div class="box">
            <div class="header">
                <h3 class="title">Nova empresa</h3>
            </div>

            <div class="body-box">
                <form action="" method="" enctype="multipart/form-data">

                    <div class="row">
                        <div class="col-md">
                            <label>Nome:</label>
                            <input type="text" class="form-control" name="name" placeholder="Digite seu nome...">
                        </div>

                        <div class="col-md">
                            <label>E-mail:</label>
                            <input type="email" class="form-control" name="email" placeholder="email@gmail.com">
                        </div>

                        <div class="col-md">
                            <label>Sede:</label>
                            <input type="text" class="form-control" name="headquarters" placeholder="Digite o local onde fica a sede da empresa...">
                        </div>
                    </div>
                    <br>

                    <div class ="row">   
                        <div class="col-md">
                            <label>Tamanho da Empresa:</label>
                            <select class ="form-control" name="company-size">
                                <option value="Pequena">Pequena</option>
                                <option value="Media">Média</option>
                                <option value="Grande">Grande</option>
                            </select>
                        </div>
                        <div class="col-md">
                            <label>Nicho de mercado:</label>
                            <select class="form-control" name="niche">
                                <option value="M">Marketing</option>
                                <option value="N">Nutrição</option>
                                <option value="D">Design</option>
                            </select>
                        </div>
                    </div>
                    <br>

                    <div class="row">
                        <div class="col-md">
                            <label>Tecnologias:</label>
                            <select class="form-control" name="technologies" multiple>                                
                                <option value=""></option>
                            </select>
                        </div>
                    </div>
                    <br>

                    <div class="row">
                        <div class="col-md">
                            <label>Especializações:</label>
                            <textarea class="form-control" name="specializations"></textarea>
                        </div>
                    </div>
                    <br>

                    <div class="row">
                        <div class="col-md">
                            <label>Logo:</label>
                            <input type="file" class="form-control" name="logo">
                        </div>
                    </div>
                    <br>
                    <input type="submit" value="Nova empresa" class="btn btn-lg btn-orange">
                </form>
                
            </div>
        </div>
    </div>

{% endblock%}

Na primeira linha, estendemos o html configurado em nase.html, ou seja, teremos um html igual ao da base e podemos adicionar conteúdo nos blocos de componente Django do tipo body que definimos no html da base.

Note que no html do app empresas temos vários inputs com informações que caracterizam a empresa a ser cadastrada. Usaremos esses dados em conjunto com o Django para modelar um banco de dados eficiente e que atenda as necessidades da nossa aplicação.

O framework Django é capaz de abstrair a modelagem do banco de dados. Na prática, isso quer dizer que não usaremos comandos SQL, mas sim modelamos relações e atributos declarando classes:

from django.db import models

class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=30)

    def __str__(self):
        return self.tecnologia

class Empresa(models.Model):

    choices_size = (
        ('Pequena', 'Até 10 pessoas'),
        ('Média', 'Até 100 pessoas'),
        ('Grande', 'Mais de 1000 pessoas'),
    )
    choices_niche = (
        ('M', 'Marketing'),
        ('N', 'Nutrição'),
        ('D', 'Design'),
    )

    logo = models.ImageField(upload_to='logo_empresa')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    headquarters = models.CharField(max_length=30)
    technologies = models.ManyToManyField(Tecnologias)
    marketing_niche = models.CharField(max_length=3, choices=choices_niche)
    specifications = models.TextField()

    def __str__(self) -> str:
        return self.nome

Declaramos relações em Django como classes. No exemplo acima, a relação Empresa tem uma série de atributos (colunas) como logo, nome, email, sede, entre outros. Além disso, note como o Django também abstrai relações múltiplas. No campo tecnologias, declaramos um campo de relação M para N como ManytoManyField e indicamos a relação na qual será responsável por fazer esse pareamento.
