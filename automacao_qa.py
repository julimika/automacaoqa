from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
import time
from config import (username, password)

#fluxo de login
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    Page = browser.new_page()
    Page.goto("https://play.watch.tv.br/login")
    Page.get_by_role("textbox", name="Digite seu email").fill(username)
    Page.get_by_role("textbox", name="Digite sua senha").fill(password)
    Page.get_by_role("button", name="Entrar").click()
    time.sleep(5)
    # Page.locator("xpath", '//*[@id="page"]/div/app-page/div/section/app-select-master/app-profile-select/div[1]/div/div[1]/div[1]').click()
    # time.sleep(5)
   

    # Page.locator("profile-name").click() #profile-select
    # time.sleep(10)
 
    # Page.mouse.wheel(delta_x=0 ,delta_y=6881.65)
    # time.sleep(10)
    # expect(Page.get_by_text("Canais Ao vivo", exact=True)).to_be_visible()
    # expect(Page.get_by_text("WATCH PARA VOCÊ", exact=True)).to_be_visible()
    

    # expect(Page.get_by_title("Lançamentos")).to_have_text("Lançamentos")
    # expect(Page.get_by_text("Sugestões", exact=True)).to_be_visible()
    # expect(Page.get_by_text("Mais Assistidos", exact=True)).to_be_visible()
    # expect(Page.get_by_text("Sugestões para Você", exact=True)).to_be_visible()

    

  
    
  






  




