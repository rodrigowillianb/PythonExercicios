import pyautogui
import  time
pyautogui.PAUSE = 2
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('youtube.com')
pyautogui.press('enter')
time.sleep(5)
pesquisa_botao=pyautogui.locateOnScreen('pesquisa_youtube.png',confidence=0.7)
pyautogui.click(pesquisa_botao)
time.sleep(1.5)
pyautogui.write('Enter sandman Metallica')
pyautogui.press('enter')