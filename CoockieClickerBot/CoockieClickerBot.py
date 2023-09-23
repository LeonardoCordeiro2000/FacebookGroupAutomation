from threading import Thread
import time
from selenium import webdriver
from selenium.types import WaitExcTypes
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.timeouts import Timeouts
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options = options,service = service)

driver.implicitly_wait(60);


class FacebookBot():

    def login(self):

        loginPage = 'https://www.facebook.com/'
        driver.get(loginPage)
        emailBox = driver.find_element("xpath",'//*[@id="email"]')
        passwordBox = driver.find_element("xpath", '//*[@id="pass"]')
        loginButton = driver.find_element("xpath", "//button[text()='Entrar']")
        email = 'YourEmail'
        password = 'YourPassword'

        emailBox.send_keys(email);
        passwordBox.send_keys(password);

        loginButton.click();
        driver.maximize_window();
    
        self.Posting()


    def Posting(self):

        groups = ["https://www.facebook.com/groups/1510087715938757", 
                  "https://www.facebook.com/groups/pedrugo", 
                  "https://www.facebook.com/groups/282093805203076"]
        

        for g in groups:

            
            writeButton = "//span[text()='Escreva algo...']"
            textBox = "//br[@data-text='true']"
            publishButton = "//span[text()='Publicar']"
            text = "Mono sup gold, procuro duo pra subir de elo junto e jogar aos finais de semana, alguem?"

            driver.get(g)

            driver.find_element("xpath", writeButton).click();

            driver.find_element("xpath", textBox).send_keys(text);

            driver.find_element("xpath", publishButton).click();

            time.sleep(5);

     
bot = FacebookBot()
bot.login()

