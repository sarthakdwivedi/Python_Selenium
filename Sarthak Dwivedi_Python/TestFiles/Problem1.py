#Imports
import utility
from Pages.LifeCharger.LifeChargerPage import LifeCharger

#Creating Driver

driver=utility.openBrowser()

#Creating object of LifeChargerClass
try:
    lifeChargerPage=LifeCharger(driver)

    #Loading Life Charger Page
    lifeChargerPage.load();

    print("Please select an article from below list:")

    #Starting loop to Print Article List and take input from user
    while True:
        #Printing Article Names
        lifeChargerPage.list_Article_Name()

        #Getting user's input
        articleRequired=input("Enter Article Title:").strip()

        #Checking if Article is present
        if lifeChargerPage.is_article_present(articleRequired):

            #Taking Screenshot
            lifeChargerPage.getScreenshotOfArticle(articleRequired)

            #Going back to HomePage
            lifeChargerPage.goBackToHomePage()

            print ("Please select Next Title or Press Enter to exit")
        elif len(articleRequired)==0: #If user do not provide an input
            break;
        else:#if the article entered not found
            print ("article not found. Select again")

    print("Thank You!!")
except:
    print ("Error while executing")
    raise Exception

finally:
    #Quitting driver
    driver.quit()