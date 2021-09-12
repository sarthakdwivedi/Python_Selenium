# imports
import string

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import config
import utility
import random

'''Class to handle My store operations'''


class MyStore:
    # declaration and intialization
    __data = dict()
    __signIn_Locator = "Sign in"
    __signIn_LocatorType = "linktext"
    __email_Locator = "email_create"
    __email_LocatorType = "id"
    __createButton_LocatorType = "id"
    __createButton_Locator = "SubmitCreate"

    __firstName_Locator = "customer_firstname"
    __lastName_Locator = "customer_lastname"
    __password_Locator = "passwd"
    __address_Locator = "address1"
    __city_Locator = "city"
    __state_Locator = "id_state"
    __zipcode_Locator = "postcode"
    __country_Locator = "uniform_id_country"
    __mobile_Locator = "phone_mobile"
    __alias_Locator = "address_alias"
    __register_Locator = "submitAccount"
    __logo_Locator = "a[title='My Store']"

    __firstName_LocatorType = "id"
    __lastName_LocatorType = "id"
    __password_LocatorType = "id"
    __address_LocatorType = "id"
    __city_LocatorType = "id"
    __state_LocatorType = "id"
    __zipcode_LocatorType = "id"
    __country_LocatorType = "id"
    __mobile_LocatorType = "id"
    __alias_LocatorType = "id"
    __register_LocatorType = "id"
    __logo_LocatorType = "cssselector"

    __addToCart_Locator = "ul#homefeatured a[title='Add to cart']"
    __addToCart_LocatorType = "cssselector"

    __product_Locator = "ul#homefeatured li"
    __product_LocatorType = "cssselector"

    __continueShopping_Locator = "span.continue"
    __continueShopping_LocatorType = "cssselector"

    __checkout_Locator = "a[title='Proceed to checkout']"
    __checkout_LocatorType = "cssselector"

    __address_checkout_Locator = "processAddress"
    __address_checkout_LocatorType = "name"

    __shipping_checkout_Locator = "processCarrier"
    __shipping_checkout_LocatorType = "name"

    __summary_checkout_Locator = " a.standard-checkout[title='Proceed to checkout']"
    __summary_checkout_LocatorType = "cssselector"

    __total_Locator = "total_price"
    __total_LocatorType = "id"

    __termAndCondition_Locator = "input[type='checkbox']"
    __termAndCondition_LocatorType = "cssselector"

    __payByCheque_Locator = "a.cheque"
    __payByCheque_LocatorType = "cssselector"

    __confirmOrder_Locator = "div#center_column button[type='submit']"
    __confirmOrder_LocatorType = "cssselector"

    __suceessMessage_Locator = "p.alert"
    __suceessMessage_LocatorType = "cssselector"

    __overlay_Locator = "div.layer_cart_overlay"
    __overlay_LocatorType = "cssselector"

    # Constructor having argument as Webdriver
    def __init__(self, driver):
        self.driver = driver

    # Function to load to the page
    def load(self):
        self.driver.get(config.myStoreURL)

    # Function to do sign up operation
    def signup(self):

        # getting data from excel
        self.__data = utility.getDataForTestCaseFromExcel("MyStore", "MyStore")

        # clicking on signIn
        utility.click(self.driver, self.__signIn_LocatorType, self.__signIn_Locator)

        # waiting for element
        utility.waitForElementToBeVisible(self.driver, self.__email_LocatorType, self.__email_Locator)

        # writing email
        #mail=self.get_random_string(8)+"@"+self.get_random_string(5)+'.com'
        utility.writeText(self.driver, self.__email_LocatorType, self.__email_Locator, self.__data.get("email"))
        #utility.writeText(self.driver, self.__email_LocatorType, self.__email_Locator, mail)
        # clicking create button
        utility.click(self.driver, self.__createButton_LocatorType, self.__createButton_Locator)

        # waiting for firstname element to be visible
        utility.waitForElementToBeVisible(self.driver, self.__firstName_LocatorType, self.__firstName_Locator)

        # filling up the form
        utility.writeText(self.driver, self.__firstName_LocatorType, self.__firstName_Locator,
                          self.__data.get("firstname"))
        utility.writeText(self.driver, self.__lastName_LocatorType, self.__lastName_Locator,
                          self.__data.get("lastname"))
        utility.writeText(self.driver, self.__password_LocatorType, self.__password_Locator,
                          self.__data.get("password"))
        utility.writeText(self.driver, self.__address_LocatorType, self.__address_Locator,
                          self.__data.get("address"))
        utility.writeText(self.driver, self.__city_LocatorType, self.__city_Locator, self.__data.get("city"))

        # Selecting state
        state = utility.getElement(self.driver, self.__state_LocatorType, self.__state_Locator)
        stateSelect = Select(state)
        stateSelect.select_by_visible_text(self.__data.get("state"))

        # updating zipcode and mobile
        utility.writeText(self.driver, self.__zipcode_LocatorType, self.__zipcode_Locator,
                          self.__data.get("zipcode"))

        utility.writeText(self.driver, self.__mobile_LocatorType, self.__mobile_Locator,
                          self.__data.get("mobile"))

        utility.click(self.driver, self.__register_LocatorType, self.__register_Locator)

        # waiting for Logo to be clickable
        utility.waitForElementToBeClickable(self.driver, self.__logo_LocatorType, self.__logo_Locator)

    # function to handle navigation to homepage
    def goToHomePage(self):

        # click Logo
        utility.click(self.driver, self.__logo_LocatorType, self.__logo_Locator)

        # wait until user is navigated to url
        WebDriverWait(self.driver, int(config.Timeout)).until(
            expected_conditions.url_to_be(config.myStoreURL))

    # function to add number of popular products to cart and proceed after adding to cart
    def addPopularProductsToCart(self):

        number = int(self.__data.get("numberofproducts", 3))
        # getting addToCart element
        addToCart = utility.getElements(self.driver, self.__addToCart_LocatorType, self.__addToCart_Locator)

        # checking if number provided is more than available
        if number > len(addToCart):
            print("Number of products provided i.e." + str(
                number) + " is more than actual available products i.e. " + str(
                len(addToCart)) + ". Resetting number to maximum available")
            number = len(addToCart)

        # getting product element
        products = utility.getElements(self.driver, self.__product_LocatorType, self.__product_Locator)

        # action object to handle move
        actions = ActionChains(self.driver)

        # for loop for adding product
        for index in range(number):

            # moving to product
            actions.move_to_element(products.pop(0)).perform()

            # clicking add to cart
            addToCart.pop(0).click();

            # wait till popup appears
            utility.waitForElementToBeVisible(self.driver, self.__overlay_LocatorType, self.__overlay_Locator)

            # Hit countinue if more products are to be added
            if index < number - 1:
                utility.click(self.driver, self.__continueShopping_LocatorType,
                              self.__continueShopping_Locator)

            # click proceed if all the products have been added
            else:
                utility.click(self.driver, self.__checkout_LocatorType, self.__checkout_Locator)

            # waiting till pop disappears
            WebDriverWait(self.driver, int(config.Timeout)).until(
                expected_conditions.invisibility_of_element_located(
                    (utility.getType(self.__overlay_LocatorType), self.__overlay_Locator)))

    # Function to check if the total amount is under budget
    def getProjectedBalance(self):

        # getting total
        totalAmount = float(self.getTotal())

        # rounding off
        totalAmount = round(totalAmount, 0)

        # checking total amount w.r.t. budget
        return int(self.__data.get("budget")) - totalAmount

    # Function to handle Place order operation
    def place_Order(self):

        # clicking checkout
        utility.click(self.driver, self.__summary_checkout_LocatorType, self.__summary_checkout_Locator)

        # waiting to read address page
        utility.waitForElementToBeClickable(self.driver, self.__address_checkout_LocatorType, self.__address_checkout_Locator)
        # WebDriverWait(self.driver, 10).until(
        #     expected_conditions.element_to_be_clickable(
        #         (utility.getType(self.__address_checkout_LocatorType), self.__address_checkout_Locator)))

        # clicking proceed on address
        utility.click(self.driver, self.__address_checkout_LocatorType, self.__address_checkout_Locator)

        try:
            utility.waitForElementToBeVisible(self.driver, self.__shipping_checkout_LocatorType,
                                              self.__shipping_checkout_Locator)
        except:
            # print("TimeoutError")
            pass
        finally:
            # accepting term and conditions
            utility.getElement(self.driver, self.__termAndCondition_LocatorType,
                          self.__termAndCondition_Locator).click()
        # clicking proceed on shipping page
        utility.click(self.driver, self.__shipping_checkout_LocatorType, self.__shipping_checkout_Locator)
        try:
            utility.waitForElementToBeVisible(self.driver, self.__payByCheque_LocatorType, self.__payByCheque_Locator)
        except:
            # print("TimeoutError")
            pass
        finally:
            # clicking pay by cheque
            utility.click(self.driver, self.__payByCheque_LocatorType, self.__payByCheque_Locator)

        try:
            utility.waitForElementToBeVisible(self.driver, self.__confirmOrder_LocatorType, self.__confirmOrder_Locator)
        except:
            # print("TimeoutError")
            pass
        finally:
            # confirming order
            utility.click(self.driver, self.__confirmOrder_LocatorType, self.__confirmOrder_Locator)

        # waiting for success message to be visible
        utility.waitForElementToBeVisible(self.driver, self.__suceessMessage_LocatorType, self.__suceessMessage_Locator)

        # checking if order is complete or not
        if utility.readText(self.driver, self.__suceessMessage_LocatorType,
                            self.__suceessMessage_Locator) == "Your order on My Store is complete.":
            return True
        else:
            return False

    # Function to get total

    def getTotal(self):
        return utility.readText(self.driver, self.__total_LocatorType, self.__total_Locator).replace("$", "")

    # Function to generate random email

    def get_random_string(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
