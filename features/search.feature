# language: pt

Funcionalidade: fluxo de busca no Airbnb

    @search
    Cenario: realizar busca e ter retorno das acomodações
        Dado que acesso site do airbnb
        E clico no input de pesquisa
        E preencho o input de pesquisa
        Quando clico no botão de busca
        Entao devo visualizar o resultado da pesquisa

    @accommodation
    Cenario: pegar infos das acomodações de todas as páginas disponíveis
        Dado que tenho retorno do resultado da pesquisa
        #Entao devo guardar as informações obtidas em uma lista
        #E salvar em csv na pasta raíz