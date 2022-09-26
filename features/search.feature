# language: pt

Funcionalidade: fluxo de busca no Airbnb

    @search
    Cenario: realizar busca e ter retorno com sucesso da pesquisa
        Dado que acesso site do airbnb
        E clico no input de pesquisa
        E preencho o input de pesquisa
        Quando clico no botão de busca
        Entao devo ter uma busca com sucesso

    @accommodation
    Cenario: pegar informoações das acomodações de todas as páginas disponíveis
        Dado que tenho retorno com sucesso do resultado da pesquisa
        #Entao devo guardar, em uma lista, as informações obtidas
        #E salvar, na pasta raíz, um csv com o resultado