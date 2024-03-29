from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_USERNAME = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    REGISTER_EMAIL = (By.NAME, "registration-email")
    REGISTER_PASSWORD = (By.NAME, "registration-password1")
    REGISTER_PASSWORD_REPEAT = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PAGE_ARTICLE = (By.CSS_SELECTOR, "article.product_page")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_TITLE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > p")
    BOOK_PRICE_IM_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


class BasketPageLocators:
    BASKET_PAGE_HEADER = (By.CSS_SELECTOR, ".page-header > h1")
    BASKET_FIRST_PRODUCT = (By.CSS_SELECTOR, ".basket_summary > .basket-items:nth-child(1)")
    BASKET_NO_PRODUCTS_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
