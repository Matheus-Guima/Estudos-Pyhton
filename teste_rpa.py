import pyautogui
import time

pyautogui.alert("Início da automação!")
pyautogui.PAUSE = 0.3

#Abrindo o google Chrome
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write("https://drive.google.com/drive/u/1/my-drive")
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('F11')
time.sleep(1)

#retorna a área de trabalho
pyautogui.hotkey('winleft', 'd')

#posicionando mouse no arquivo
pyautogui.moveTo(730, 200)
time.sleep(1)
pyautogui.mouseDown()
pyautogui.moveTo(975, 800)

#Janela do Google
pyautogui.hotkey('alt', 'tab')
time.sleep(1.5)

#Largar aqruvio
pyautogui.mouseUp()
time.sleep(2)

pyautogui.alert("Fim do robô")