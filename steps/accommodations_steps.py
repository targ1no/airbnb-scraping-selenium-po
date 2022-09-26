from behave import given, when, then
from nose.tools import assert_equal

from utils import Utils
from pages.header_page import HeaderPage
from pages.results_page import ResultsPage

utils = Utils()
header_page = HeaderPage()
results_page = ResultsPage()

@given(u'que tenho retorno do resultado da pesquisa')
def step_impl(context):
    utils.navigate('https://www.airbnb.com.br/')
    header_page.where_btn()
    header_page.input_search('Fortaleza')
    header_page.search_btn()
    assert_equal(results_page.get_title_text(), 'Fortaleza - CE')
    
    results_page.get_accommodations_info()

@then(u'devo guardar as informações obtidas em uma lista')
def step_impl(context):
    pass

@then(u'e salvar em csv na pasta raíz')
def step_impl(context):
    pass