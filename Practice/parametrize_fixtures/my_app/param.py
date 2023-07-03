# Import pytest module
import pytest

# Define a custom fixture that returns a web driver object
@pytest.fixture
def driver(request, webdriver= ):
    browser = request.param
    # Create a web driver instance based on the browser option
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Invalid browser option: {browser}")
    # Return the driver object
    yield driver
    driver.quit()

# Define a parametrized test function that uses the driver fixture
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
def test_home_page(driver):
    # Navigate to the home page
    driver.get("https://www.github.com")
    assert driver.title == "github.com"
