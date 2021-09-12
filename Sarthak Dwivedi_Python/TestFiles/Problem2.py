#imports
import config
import utility
from Pages.AutomationPractice.MyStore import MyStore

try:
    #creating driver
    driver=utility.openBrowser();

    #creating object of Mystore class
    myStore=MyStore(driver)

    #loading My store
    myStore.load()

    #signing up
    myStore.signup()

    #goToHome page after signup
    myStore.goToHomePage()

    #add products to cart
    myStore.addPopularProductsToCart()

    #checking the balance
    if myStore.getProjectedBalance()>=0:

        #placing order
        if myStore.place_Order():
            print("Order placed successfully")
            utility.takeScreenshot(driver, str(config.myStorePassScreenshotLocation))
        else:
            utility.takeScreenshot(driver, str(config.myStoreFailureScreenshotLocation))
    else:
        print("Order cannot be placed total amount is exceeding your budget. You need $"+str(abs(myStore.getProjectedBalance()))+" more to place your first order")
        utility.takeScreenshot(driver, str(config.myStoreFailureScreenshotLocation))
except:
    #taking screenshot in case of failure
    utility.takeScreenshot(driver,str(config.myStoreFailureScreenshotLocation))
    raise Exception

finally:
    #quitting driver
    driver.quit()