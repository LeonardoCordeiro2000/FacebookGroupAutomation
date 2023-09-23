from re import S
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import schedule

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
            text = "YourPostText"

            driver.get(g)

            driver.find_element("xpath", writeButton).click();

            driver.find_element("xpath", textBox).send_keys(text);

            driver.find_element("xpath", publishButton).click();

            time.sleep(5);

     
class Scheduling:
    def __init__(self):
        self.bot = FacebookBot()
        self.start()

    def run_login(self):
        self.bot.login()

    def start(self):
        schedule.every(30).seconds.do(self.run_login)
        while True:
            schedule.run_pending()
            time.sleep(1)


Scheduler = Scheduling()