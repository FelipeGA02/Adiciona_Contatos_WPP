from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

# Substitua pelos contatos que deseja adicionar
contatos = [
    "+55 31 91234-5678"
31 97171-5402
31 99526-5999 
31999738412
31991810745
31-995011914
31993296193
31999781549
31984001136
31 992920271
31971034401
31991165156
(31) 99561-1124
82988702788
(31) 986514561
(31) 99180-8617
+55 31 981098151
(31)973545497
]

# Nome do grupo
nome_do_grupo = "Meu Grupo de Teste"

caminho_driver = r"C:\Users\felip\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(caminho_driver)
driver = webdriver.Chrome(service=service)

driver.get("https://web.whatsapp.com")
print("Escaneie o QR Code e pressione Enter")
input()

# Acessar o grupo
def abrir_grupo(nome):
    campo_pesquisa = driver.find_element(By.XPATH, '//div[@title="Caixa de texto de pesquisa"]')
    campo_pesquisa.click()
    time.sleep(1)
    campo_pesquisa.send_keys(nome)
    time.sleep(2)
    grupo = driver.find_element(By.XPATH, f'//span[@title="{nome}"]')
    grupo.click()
    time.sleep(2)

abrir_grupo(nome_do_grupo)

# Clicar no título do grupo
driver.find_element(By.XPATH, '//header//div[contains(@class,"_amie")]').click()
time.sleep(2)

# Clicar em "Adicionar participante"
driver.find_element(By.XPATH, '//div[text()="Adicionar participante"]').click()
time.sleep(2)

# Adicionar os contatos
for contato in contatos:
    campo_busca = driver.find_element(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
    campo_busca.clear()
    campo_busca.send_keys(contato)
    time.sleep(2)
    try:
        user = driver.find_element(By.XPATH, f'//span[@title="{contato}"]')
        user.click()
        print(f"[✔️] Contato '{contato}' adicionado à seleção.")
        time.sleep(1)
    except:
        print(f"[❌] Contato '{contato}' não encontrado.")
        continue

# Confirmar adição
driver.find_element(By.XPATH, '//span[@data-icon="checkmark"]').click()
print("Participantes adicionados.")
