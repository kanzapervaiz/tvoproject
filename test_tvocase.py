import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def driver():
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_option)
    yield driver
    driver.quit()

def test_page_title(driver):
    driver.get("https://tvolearn.com/pages/grade-5-mathematics")
    assert "Grade 5 - Mathematics" in driver.title, "Title does not match the expected result"

def test_url(driver):
    assert "https://tvolearn.com/pages/grade-5-mathematics" == driver.current_url, "URL is not expected result"

def test_header(driver):
    header = driver.find_element(By.TAG_NAME, "h1")
    assert "Grade 5" == header.text, "header does not match the expect result"

def navigation_menu(driver):
    navigation = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "nav"))
    )
    menu = navigation.get_attribute("class")
    assert "grid__item medium-up--five-sixths small--hide" in menu, "f Navigation menu class does not match. Found: {menu}"

def test_links(driver):
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        link_href = link.get_attribute("href")
        print(f"Link: {link_href}")
        assert link_href != "", "Link does not have an href attribute"
        assert link_href.startswith("http"), f"Invalid link source: {link_href}"


def test_images(driver):
    images = driver.find_elements(By.TAG_NAME, "img")
    for image in images:
        img_src = image.get_attribute("src")
        if img_src:
            print(f"Image source: {img_src}")
            assert img_src != "", "Image source is empty"
            assert img_src.startswith("http"), f"Invalid image source: {img_src}"
        else:
            print("no valid source for image")

def test_media(driver):
    media_elements = driver.find_elements(By.TAG_NAME, "video") + driver.find_elements(By.TAG_NAME, "audio")
    for media in media_elements:
        media_src = media.get_attribute("src")
        print(f"Media source: {media_src}")
        assert media_src != "", f"Media source is empty for {media.tag_name}"
        assert media_src.startswith("http"), f"Invalid media source: {media_src}"

def test_footer(driver):
    footer = driver.find_element(By.TAG_NAME, "footer")
    footer_class = footer.get_attribute("class")
    assert footer_class != "", "Footer does not have a class attribute"

    footer_text = footer.text.strip()
    print(f"Footer text: {footer_text}")
    assert footer_text != "", "Footer text is empty"
    assert "Copyright" in footer_text, "Footer text does not contain 'Copyright' or expected footer content"




