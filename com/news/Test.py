from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = '/home/jawa/dev/dev-tools/chromedriver'

options = Options()
# options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("http://lazada.sg/")


# h1 = driver.find_element_by_id('Level_1_Category_No1')
# h1.click()

# link = driver.find_element_by_xpath("//ul/li[@data-cate='cate_1_1']");
# link.click();
# print(link)


searchInput = driver.find_element_by_xpath("//input[@id='q']");
searchInput.send_keys('samsung galaxy tab');
searchInput.submit();

# driver.quit()

# <li class="sub-item-remove-arrow" data-cate="cate_1_1">
#                 <a href="//www.lazada.sg/shop-mobiles/?spm=a2o42.home.cate_1.1.654346b5jJrgze" data-spm-anchor-id="a2o42.home.cate_1.1">
#                     <span data-spm-anchor-id="a2o42.home.cate_1.i0.654346b5jJrgze">Mobiles</span>
#                 </a>
                
#             </li>

# <input type="search" id="q" name="q" placeholder="Search in Lazada" class="search-box__input--O34g" tabindex="1" value="searchlistcategory" data-spm-anchor-id="a2o42.searchlistcategory.search.i0.22ef3f03D9utVc">