from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def browser_driver_path(browser_name):
    global driver_path
    if browser_name.lower() == 'chrome':
        driver_path = ChromeDriverManager().install()
    elif browser_name.lower() == 'headlesschrome':
        driver_path = ChromeDriverManager().install()
    elif browser_name.lower() == 'firefox':
        driver_path = GeckoDriverManager().install()
    elif browser_name.lower() == 'headlessfirefox':
        driver_path = GeckoDriverManager().install()
    elif browser_name.lower() == 'edge':
        driver_path = EdgeChromiumDriverManager().install()
    return driver_path
