from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Lista de contatos
contatos = [
    "+55 31 97171-5402", "+55 31 99526-5999", "+55 31 99973-8412",
    "+55 31 99181-0745", "+55 31 99501-1914", "+55 31 99329-6193",
    "+55 31 99978-1549", "+55 31 98400-1136", "+55 31 99292-0271",
    "+55 31 97103-4401", "+55 31 99116-5156", "+55 31 99561-1124",
    "+55 82 98870-2788", "+55 31 98651-4561", "+55 31 99180-8617",
    "+55 31 98109-8151", "+55 31 97354-5497"
]

nome_do_grupo = "Diretoria de Projetos"

caminho_driver = r"C:\Users\felip\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(caminho_driver)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20)

driver.get("https://web.whatsapp.com")
print("🔐 Escaneie o QR Code e pressione Enter para continuar...")
input()

# Acessa o grupo pelo nome
def abrir_grupo(nome):
    campo_pesquisa = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title="Caixa de texto de pesquisa"]')))
    campo_pesquisa.click()
    time.sleep(1)
    campo_pesquisa.send_keys(nome)
    time.sleep(2)
    grupo = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[@title="{nome}"]')))
    grupo.click()
    time.sleep(2)

abrir_grupo(nome_do_grupo)

# Abre informações do grupo (cabeçalho)
try:
    cabecalho = wait.until(EC.element_to_be_clickable((By.XPATH, '//header')))
    cabecalho.click()
    time.sleep(2)
except Exception as e:
    print("❌ Erro ao tentar abrir o cabeçalho do grupo:", e)
    driver.quit()
    exit()

# Clica em "Adicionar participante"
try:
    adicionar_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Adicionar participante" or text()="Add participant"]')))
    adicionar_btn.click()
    time.sleep(2)
except Exception as e:
    print("❌ Não foi possível clicar em 'Adicionar participante':", e)
    driver.quit()
    exit()

# Adiciona contatos
for contato in contatos:
    try:
        campo_busca = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')))
        campo_busca.clear()
        campo_busca.send_keys(contato)
        time.sleep(2)

        try:
            user = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[@title="{contato}"]')))
            user.click()
            print(f"[✔️] Contato '{contato}' adicionado à seleção.")
        except:
            print(f"[❌] Contato '{contato}' não encontrado ou indisponível.")
            continue
    except Exception as e:
        print(f"[⚠️] Erro ao processar contato '{contato}':", e)

# Confirma a adição
try:
    confirmar = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="checkmark"]')))
    confirmar.click()
    print("✅ Participantes adicionados com sucesso!")
except Exception as e:
    print("❌ Erro ao confirmar adição de participantes:", e)

driver.quit()
