from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import time
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/executar')
def executar():
    try:
        # Seu código Selenium aqui
        driver = webdriver.Chrome()

        url = "https://www.nfse.gov.br/EmissorNacional/Notas/Recebidas"
        driver.get(url)

        # login
        username = driver.find_element(By.NAME, 'Inscricao')
        password = driver.find_element(By.NAME, 'Senha')
        username.send_keys("00358519000146")
        password.send_keys("Rcc@2022")

        time.sleep(5)

        password.send_keys(Keys.RETURN)
        time.sleep(5)

        pyautogui.press('tab', presses=16)
        time.sleep(8)

        #1
        pyautogui.press('enter', presses=1)
        time.sleep(5)

        pyautogui.press('tab', presses=2)
        time.sleep(5)

        pyautogui.press('enter', presses=1)
        time.sleep(0.8)

        pyautogui.press('tab', presses=2)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(15)
        #1

        #2       
        pyautogui.press('tab', presses=1)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(5)

        pyautogui.press('tab', presses=2)
        time.sleep(5)

        pyautogui.press('enter', presses=1)
        time.sleep(0.8)

        pyautogui.press('tab', presses=2)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(15)
        #2

        #3
        pyautogui.press('tab', presses=1)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(5)

        pyautogui.press('tab', presses=2)
        time.sleep(5)

        pyautogui.press('enter', presses=1)
        time.sleep(0.8)

        pyautogui.press('tab', presses=2)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(15)
        #3

        #4
        pyautogui.press('tab', presses=1)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(5)

        pyautogui.press('tab', presses=2)
        time.sleep(5)

        pyautogui.press('enter', presses=1)
        time.sleep(0.8)

        pyautogui.press('tab', presses=2)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(15)
        #4

        #5
        pyautogui.press('tab', presses=1)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(5)

        pyautogui.press('tab', presses=2)
        time.sleep(5)

        pyautogui.press('enter', presses=1)
        time.sleep(0.8)

        pyautogui.press('tab', presses=2)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(15)
        #5

        #6
        pyautogui.press('tab', presses=1)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(5)

        pyautogui.press('tab', presses=2)
        time.sleep(5)

        pyautogui.press('enter', presses=1)
        time.sleep(0.8)

        pyautogui.press('tab', presses=2)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(15)
        #6

        #7
        pyautogui.press('tab', presses=1)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(5)

        pyautogui.press('tab', presses=2)
        time.sleep(5)

        pyautogui.press('enter', presses=1)
        time.sleep(0.8)

        pyautogui.press('tab', presses=2)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(15)
        #7

        #8
        pyautogui.press('tab', presses=1)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(5)

        pyautogui.press('tab', presses=2)
        time.sleep(5)

        pyautogui.press('enter', presses=1)
        time.sleep(0.8)

        pyautogui.press('tab', presses=2)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(15)
        #8

        #9
        pyautogui.press('tab', presses=1)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(5)

        pyautogui.press('tab', presses=2)
        time.sleep(5)

        pyautogui.press('enter', presses=1)
        time.sleep(0.8)

        pyautogui.press('tab', presses=2)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(15)
        #9

        #10
        pyautogui.press('tab', presses=1)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(5)

        pyautogui.press('tab', presses=2)
        time.sleep(5)

        pyautogui.press('enter', presses=1)
        time.sleep(0.8)

        pyautogui.press('tab', presses=2)
        time.sleep(0.8)

        pyautogui.press('enter', presses=1)
        time.sleep(20)

        return "Código executado com sucesso!"

    except Exception as e:
        return f"Erro: {str(e)}"

    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True)
