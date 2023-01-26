from selenium import webdriver
from axe_selenium_python import Axe


def test_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    axe = Axe(driver)

    axe.inject()

    results = axe.run()

    axe.write_results(results, 'results/a11y.json')
    driver.close()

    assert len(results["violations"]) == 0, axe.report(results["violations"])
