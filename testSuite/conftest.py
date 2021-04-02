import datetime
from pytest import fixture,mark
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = ''


# @fixture(params=["chrome", "firefox"], scope='session')
@fixture(params=["chrome"], scope='session')
def setup(request):

    global driver
    if request.param == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        print("Chrome Run started at:: " + str(datetime.datetime.now()))
        print("**--------------------------------------------------------------**")
    elif request.param == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        print("Firefox Run started at:: " + str(datetime.datetime.now()))
        print("**--------------------------------------------------------------**")

    yield driver
    driver.close()
    print("**-------------------------------------------------------------**")
    print(f"{request.param} Run completed at:: " + str(datetime.datetime.now()))
# @fixture()
# def setup(browser):
#     global driver
#     if browser == 'chrome':
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         print("Launching chrome browser.........")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#         print("Launching firefox browser.........")
#     return driver
#
#
# def pytest_addoption(parser):    # This will get the value from CLI /hooks
#     parser.addoption("--browser")


# @fixture()
# def browser(request):  # This will return the Browser value to setup method
#     return request.config.getoption("--browser")
