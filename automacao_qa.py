from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://play.watch.tv.br/login")
    pagina.get_by_role("textbox", name="Digite seu email").fill("juliana.mika@watch.tv.br")
    pagina.get_by_role("textbox", name="Digite sua senha").fill("123456Wa")
    pagina.get_by_role("button", name="Entrar").click()
    time.sleep(5)
   

    # pagina.locator("profile-name").click() #profile-select
    # time.sleep(10)

    # pagina.mouse.wheel(delta_x=0 ,delta_y=6881.65)
    # time.sleep(10)
    # expect(pagina.get_by_text("Canais Ao vivo", exact=True)).to_be_visible()
    # expect(pagina.get_by_text("WATCH PARA VOCÊ", exact=True)).to_be_visible()
    

    # expect(pagina.get_by_title("Lançamentos")).to_have_text("Lançamentos")
    # expect(pagina.get_by_text("Sugestões", exact=True)).to_be_visible()
    # expect(pagina.get_by_text("Mais Assistidos", exact=True)).to_be_visible()
    # expect(pagina.get_by_text("Sugestões para Você", exact=True)).to_be_visible()

    

  
    
  






  




