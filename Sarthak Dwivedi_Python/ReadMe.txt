Problem1.py
As a follower of http://lifecharger.org/ , a user would like to save some articles in form of screenshots on his machine.
List all articles name present on home page and ask user to select one and save screenshots of that article in a separate folder and keep on asking for next article until user quits.
User wants this to be done using headless mode.

Problem2.py
User is visiting this website(http://automationpractice.com/index.php) for the first time. He wants to create an account and place his first order.
 He wants to import user data from excel/csv and add one column for budget.
Add top 3 products from popular items present on home page to the cart.
Place order only if total amount (rounded off) is less than or equal to budget mentioned in the test data.
If order is placed successfully print “Order placed successfully” else “Order cannot be placed total amount is exceeding your budget. You need ${} more to place your first order”.
It would be good if you can take screenshots in both cases and save them in folders like Success, Failure etc.

Problem3.py
User wants to extract top trending topic of the day from any website (e.g. google trends).
Now he wants to search this topic on google images using selenium and download top 10 images of that topic in a folder. (use external libraries to do this).

#config file
Browser (chrome,firefox)
Headless Mode (True,False)
Timeout
Screenshot folder
Driverexecutable location
URLs
Excel file location

#Testdata is read from excel file based on sheetname and test case name

#Number of Image and Product are also drived from excel file. Is defaulted to given value if not provided

#External Library
openpyxl for excel
Base64 for Image download

