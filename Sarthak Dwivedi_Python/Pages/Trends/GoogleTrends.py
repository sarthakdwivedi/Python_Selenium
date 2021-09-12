#Imports
import config
import utility

#class to handle Google Trends
class GoogleTrends:

    #Declaration
    __trendingTopicLocator = "a[track*='trending'] div.list-item-title"
    __trendingTopicLocatorType = "cssSelector"

    #condtructor
    def __init__(self, driver):
        self.driver = driver

    #loading page
    def load(self):
        self.driver.get(config.trendUrl)

    #getting most trending topic
    def get_Most_Trending_Topic(self):
        return utility.readText(self.driver, self.__trendingTopicLocatorType, self.__trendingTopicLocator)
