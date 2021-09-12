# imports
from selenium.webdriver.common.keys import Keys

import config
import utility


# class for google image
class GoogleImageSearch:
    # variable declaration
    __imageLocator = "div[data-id] img"
    __imageLocatorType = "cssSelector"
    __searchLocator = "input[title='Search']"
    __searchLocatorType = "cssSelector"

    __data = dict()

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # loading of page
    def load(self):
        self.driver.get(config.googleImageUrl)
        # getting data from excel
        self.__data = utility.getDataForTestCaseFromExcel("Trends","Trends")

    # function to handle search operation
    def search(self, text):
        utility.writeText(self.driver, self.__searchLocatorType, self.__searchLocator,text)
        element=utility.getElement(self.driver,self.__searchLocatorType, self.__searchLocator)
        element.send_keys(Keys.ENTER)

    # function to download image
    def downloadImages(self, name):
        number = None

        # setting Number of images
        if len(self.__data) > 0:
            number = int(self.__data.get("numberofimage", 10))
        else:
            number = 10
        images = utility.getElements(self.driver, self.__imageLocatorType, self.__imageLocator)

        # resetting if number provided is more than actual number

        if (number > len(images)):
            print("Number of products provided i.e." + str(
                number) + " is more than actual available products i.e. " + str(len(
                images)) + ". Resetting number to maximum available")

            number = len(images)
        for index in range(int(number)):
            utility.downloadImage(str(images[index].get_attribute("src")).replace("data:image/jpeg;base64,", ""),
                                  str(config.trendingImageLocation) + "/" + name + str(index) + ".png")
