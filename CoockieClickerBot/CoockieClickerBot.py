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

#Mudar variaveis de metodos para campos da classe FacebookBot
#Mudar o nome das variaveis para ingles
#Ajustar valores das variaveis
#Melhorar a passagem de informações no código como: links, grupos e credenciais
class FacebookBot():

    def login(self):

        loginPage = 'https://www.facebook.com/'
        driver.get(loginPage)
        emailBox = driver.find_element("xpath",'//*[@id="email"]')
        passwordBox = driver.find_element("xpath", '//*[@id="pass"]')
        loginButton = driver.find_element("xpath", "//button[text()='Entrar']")
        email = 'YourEmail'
        password = 'YourPass'

        emailBox.send_keys(email);
        passwordBox.send_keys(password);

        loginButton.click();
        driver.maximize_window();
    
        self.Posting()


    def Posting(self):

        group = "//span[text()='League of Legends - Brasil']"
        writeButton = "//span[text()='Escreva algo...']"
        textBoxFacebook = "//br[@data-text='true']"
        publishButton = "//span[text()='Publicar']"

        driver.find_element("xpath", group).click();

        driver.find_element("xpath", writeButton).click();

        driver.find_element("xpath", textBoxFacebook).send_keys("Mono sup gold, procuro duo pra subir de elo junto e jogar aos finais de semana, alguem?");

        driver.find_element("xpath", publishButton).click();

        time.sleep(5);

     
bot = FacebookBot()
bot.login()

