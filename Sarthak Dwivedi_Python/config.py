from pathlib import Path
Timeout=10
browser="chrome"
headless=False
lifeChargerUrl="http://lifecharger.org/ "
trendUrl="https://trends.google.com/"
myStoreURL="http://automationpractice.com/index.php"
googleImageUrl="https://www.google.com/imghp"
lifeHackerScreenshotLocation=Path(__file__).parent /"Screenshots/LifeHackerScreenshots/"
trendingImageLocation=Path(__file__).parent /"Screenshots/TrandingImages/"
chrome_location=Path(__file__).parent /"driverExecutable/chromedriver"
firefox_location = Path(__file__).parent /"driverExecutable/geckodriver"
excelFilePath= Path(__file__).parent /"data/data.xlsx"
myStoreFailureScreenshotLocation=Path(__file__).parent /"Screenshots/MyStore/FailureScreenshots/"
myStorePassScreenshotLocation=Path(__file__).parent /"Screenshots/MyStore/PassScreenshots/"
