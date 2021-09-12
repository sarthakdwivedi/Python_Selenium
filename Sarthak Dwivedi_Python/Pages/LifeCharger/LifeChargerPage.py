from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import config
import utility


class LifeCharger:
    #Declaration
    __articles = []
    __articleNames = []

    #Locator
    __articleLocator = "article h2 a"
    __articleLocatorType = "cssSelector"
    __titleLocator = "h2"
    __titleLocatorType = "tag"

    #constructor
    def __init__(self, driver):

        self.driver = driver


    #Function to get Screenshot of the article name
    def getScreenshotOfArticle(self, articleName):
        #filtering articles to get element having article name
        article = [artic for artic in self.articles if str(artic.text).lower().__contains__(articleName.lower())][0]
        
        #clicking Article to open the page
        article.click();
       
        # Waiting till url is changed
        WebDriverWait(self.driver, config.Timeout).until(expected_conditions.url_changes)
        
        #formatting file name
        name = str(utility.getElement(self.driver, self.__titleLocatorType, self.__titleLocator).text)
        fileName = name.replace("|", "").replace(",", "").replace("  ", " ").replace(" ", "_")
        
        #taking screenshot
        utility.takeFullScreenShot(self.driver, str(config.lifeHackerScreenshotLocation) + "/" + fileName + ".png")

    
    #Function to get Article Lists
    def getArticleList(self):
        self.articles = utility.getElements(self.driver, self.__articleLocatorType, self.__articleLocator)
        
        #Storing article Names
        for article in self.articles:
            name = str(article.text).strip()
            self.__articleNames.append(name)

    #Printing article list
    def list_Article_Name(self):
        self.getArticleList()
        for article in self.__articleNames:
            print(article)

    #Function to check if articlename is present in article list
    def is_article_present(self, articleName):
        articleName = articleName.lower();
        temp=map(lambda x:x.lower(),self.__articleNames)
        if articleName in list(temp):
            return True;
        else:
            return False
    
    #Function to load Life charger page
    def load(self):
        self.driver.get(config.lifeChargerUrl)

    #Function to navigate back to home page
    def goBackToHomePage(self):
        self.driver.back()
        WebDriverWait(self.driver, config.Timeout).until(expected_conditions.url_changes)