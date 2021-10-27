import jsonpickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support     import expected_conditions as EC
import time
import numpy as np

# driver = webdriver.Chrome(DRIVER_PATH)

# driver.get("https://www.google.com/")
# print(driver.title)
#
# searchBox = driver.find_element_by_name("q")
# searchBox.send_keys("youtube")
# searchBox.send_keys(Keys.RETURN)
#
#
# try:
#    resultsElement = WebDriverWait(driver, 10).until(
#       EC.presence_of_element_located((By.ID, "res"))
#    )
#    searchResults = resultsElement.find_elements_by_class_name("g")
#    for result in searchResults:
#       resTitle = result.find_element_by_class_name("DKV0Md")
#       print(resTitle.text)
#
# finally:
#    time.sleep(2)
#    driver.quit()


# driver.get("https://pt.wikipedia.org/wiki/Predefini%C3%A7%C3%A3o:Tabela_Covid-19_Portugal_regi%C3%A3o/dia_(DGS)")
# content = driver.find_element_by_id("mw-content-text")

# try:
#    rows = driver.find_elements_by_xpath("//table/tbody/tr")
#    rows = rows[3:-4] # remove headers and fotters
#
#    for rowIdx in range(len(rows)):
#       print(rows[rowIdx].text)
#
#
# finally:
#    time.sleep(2)
#    driver.quit()


class CoronaCrawler:
   def __init__(self, driverPath):
      self.driverPath = driverPath

   def close(self):
      self.driver.quit()

   def __fetchData(self):
      self.driver = webdriver.Chrome(self.driverPath)
      self.driver.get("https://pt.wikipedia.org/wiki/Predefini%C3%A7%C3%A3o:Tabela_Covid-19_Portugal_regi%C3%A3o/dia_(DGS)")

      try:
         rows = self.driver.find_elements_by_xpath("//table/tbody/tr")
         numRows = len(rows)
         numCols = len(self.driver.find_elements_by_xpath("//table/tbody/tr[4]/td")) # 4 is a data tr

         return rows, numRows, numCols
      except:
         self.driver.quit()

   def __saveData(self, filename, values):
      f = open(filename, 'w')
      f.write(jsonpickle.encode(values))

   def __loadData(self, filename):
      f = open(filename, 'r')
      values = jsonpickle.decode(f.read())
      return values


   def downloadPortugalDailyTotalsData(self):
      rows, _, numCols = self.__fetchData()
      rows = rows[3:-4]  # remove headers and footers

      colsInterest = [1, 2, 3, 4, 5]

      # Build, populate and save data matrix
      data = np.zeros((len(rows), len(colsInterest)))
      if rows:
         for rowIdx in range(len(rows)):
            for colIdx in range(len(colsInterest)):
               valueString = rows[rowIdx].find_element_by_xpath("./td[" + str(colsInterest[colIdx]) + "]").text
               valueString = valueString.replace(",", ".")
               if valueString != "—": # No data character
                  data[rowIdx, colIdx] = float(valueString)
         self.__saveData("Portugal_daily_totals", data)
      else:
         print("No data found")
         return None

      data = self.__loadData("Portugal_daily_totals")
      print(data)

   def getPortugalDailyTotalsData(self):
      data = self.__loadData("Portugal_daily_totals")
      return data


if __name__ == "__main__":
   DRIVER_PATH = "res/chromedriver.exe"

   crawler = CoronaCrawler(DRIVER_PATH)
   crawler.downloadPortugalDailyTotalsData()
   crawler.close()