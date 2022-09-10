from behave import given, when, then
from nose.tools import assert_equal

from utils import Utils
from pages.header_page import HeaderPage
from pages.results_page import ResultsPage

utils = Utils()
header_page = HeaderPage()
results_page = ResultsPage()

@given(u'que acesso site do airbnb')
def step_impl(context):
    utils.navigate('https://www.airbnb.com.br/')

@given(u'clico no input de pesquisa')
def step_impl(context):
    header_page.where_btn()

@given(u'preencho o input de pesquisa')
def step_impl(context):
    header_page.input_search('Fortaleza')

@when(u'clico no botão de busca')
def step_impl(context):
    header_page.search_btn()

@then(u'devo visualizar o resultado da pesquisa')
def step_impl(context):
    assert_equal(results_page.get_title_text(), 'Fortaleza - CE')