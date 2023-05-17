from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
from playwright.sync_api import Page, expect
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://play.watch.tv.br/login")
    pagina.locator('xpath=/html/body/app-root/div/div/app-page/div/section/app-login/div/form/div[2]/app-input[1]/div/input').click()
    pagina.fill('xpath=/html/body/app-root/div/div/app-page/div/section/app-login/div/form/div[2]/app-input[1]/div/input', "juliana.mika@watch.tv.br")
    pagina.fill('xpath=/html/body/app-root/div/div/app-page/div/section/app-login/div/form/div[2]/app-input[2]/div/input', "123456Wa")
    pagina.get_by_role("button").click()
    time.sleep(5)
    pagina.locator('xpath=/html/body/app-root/div/div/app-page/div/section/app-profile-select/div[1]/div/div[1]/div[1]/div[2]/div/img').click()
    time.sleep(10)
    
    
    
    time.sleep(10)
    expect(pagina.get_by_text("Canais Ao vivo", exact=True)).to_be_visible()
    expect(pagina.get_by_text("WATCH PARA VOCÊ", exact=True)).to_be_visible()
    lancamentos = pagina.locator('xpath=/html/body/app-root/div/div/app-page/div/section/app-home/main/div[2]/div[3]/div/div/div/div/app-section/div/div/div[1]')
await lancamentos.scroll_into_view_if_needed
    time.sleep(10)
    # expect(pagina.get_by_text("Lançamentos", exact=True)).to_be_visible()
    # expect(pagina.get_by_text("Sugestões", exact=True)).to_be_visible()
    # expect(pagina.get_by_text("Mais Assistidos", exact=True)).to_be_visible()
    # expect(pagina.get_by_text("Sugestões para Você", exact=True)).to_be_visible()

    
    
    


    # hbo = pagina.locator('xpath=/html/body/app-root/div/div/app-page/div/section/app-home/main/div[1]/div[2]/div/div/app-default-section-description/div/div[2]/swiper/div[3]/div[1]/app-default-card/a/div').click()
    #categorias
    pagina.locator('xpath=/html/body/app-root/div/div/app-page/div/app-header/nav/div[1]/div/ul/li[2]/div/a/div').click()
    time.sleep(5)
  





