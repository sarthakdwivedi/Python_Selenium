#This page downloads images for trending topic

#imports
import utility
from Pages.Trends.GoogleTrends import GoogleTrends
from Pages.Trends.GoogleImage import GoogleImageSearch


#creating driver
driver = utility.openBrowser()
try:
    #creating object of Google trends class
    trendPage=GoogleTrends(driver)

    #loading trend page
    trendPage.load()

    #getting Trending topic name
    trendingTopic = trendPage.get_Most_Trending_Topic()
    print(trendingTopic)

    #creating object of Google Image search class
    imagePage=GoogleImageSearch(driver)

    #loading image page
    imagePage.load()

    #Searching images for trending topic
    imagePage.search(trendingTopic)

    #downloading images
    imagePage.downloadImages(trendingTopic)

except:
    raise Exception
finally:
    #Quitting the driver
    driver.quit()
    # driver.quit()
