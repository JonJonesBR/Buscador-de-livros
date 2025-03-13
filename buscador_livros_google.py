import os
import requests
from bs4 import BeautifulSoup
from googlesearch import search

# Definir a pasta de downloads no Android
DOWNLOADS_PATH = "/storage/emulated/0/Download"

# Função para validar links
def validar_link(url):
    try:
        resposta = requests.head(url, allow_redirects=True, timeout=5)
        if resposta.status_code == 200:
            return True
    except requests.RequestException:
        return False
    return False

# Função para baixar arquivos
def baixar_arquivo(url, nome_arquivo):
    try:
        resposta = requests.get(url, stream=True)
        if resposta.status_code == 200:
            caminho_arquivo = os.path.join(DOWNLOADS_PATH, nome_arquivo)
            with open(caminho_arquivo, "wb") as arquivo:
                for chunk in resposta.iter_content(chunk_size=8192):
                    arquivo.write(chunk)
            print(f"\n✅ Download concluído: {caminho_arquivo}\n")
        else:
            print("\n❌ Erro ao baixar o arquivo.\n")
    except Exception as e:
        print(f"\n❌ Erro durante o download: {e}\n")

# Função para obter a entrada do usuário com opção de sair ou voltar ao menu
def entrada_usuario(mensagem):
    resposta = input(mensagem).strip().lower()
    if resposta == "sair":
        print("\n🚪 Encerrando o programa...\n")
        exit()
    elif resposta == "menu":
        print("\n🔄 Retornando ao menu inicial...\n")
        return None
    return resposta

# Função principal de busca
def buscar_livros():
    while True:
        print("\n📚 Buscador de Livros - Termux 📚")
        print("ℹ️ Digite 'sair' a qualquer momento para encerrar ou 'menu' para reiniciar a pesquisa.\n")
        
        termo_pesquisa = entrada_usuario("🔍 Digite o título, autor, assunto ou palavras-chave do livro: ")
        if termo_pesquisa is None:
            continue  # Voltar ao menu

        idioma = entrada_usuario("🌍 Deseja apenas livros em Português do Brasil? (s/n): ")
        if idioma is None:
            continue

        tipo_arquivo = entrada_usuario("📂 Tipo de arquivo (pdf, txt, epub, mobi ou 'todos'): ")
        if tipo_arquivo is None:
            continue

        idioma_query = " site:.br" if idioma == "s" else ""
        formato_query = f'filetype:{tipo_arquivo}' if tipo_arquivo != "todos" else "(filetype:pdf OR filetype:txt OR filetype:epub OR filetype:mobi)"

        query = f'{termo_pesquisa} {formato_query} {idioma_query}'

        print("\n🔎 Pesquisando os melhores links... Aguarde...\n")
        
        links_validos = []
        total_links = 0
        continuar_pesquisa = True

        while continuar_pesquisa:
            novos_links = []
            for url in search(query, num_results=10):
                if validar_link(url) and url not in links_validos:
                    novos_links.append(url)
                    total_links += 1
                    if len(novos_links) >= 5:
                        break

            if not novos_links:
                print("\n❌ Nenhum link válido encontrado.\n")
                break

            links_validos.extend(novos_links)

            print("\n✅ Links encontrados:\n")
            for i, link in enumerate(novos_links, start=len(links_validos) - len(novos_links) + 1):
                print(f"{i}. {link}")

            escolha = entrada_usuario("\n🔄 Deseja mais 5 links? (s/n) ou digite 'menu' para refazer a pesquisa: ")
            if escolha is None:
                break
            elif escolha != "s":
                continuar_pesquisa = False

        if not links_validos:
            continue  # Voltar ao menu principal

        while True:
            escolha = entrada_usuario("\n📥 Deseja baixar algum arquivo? (Digite o número ou 'n' para sair): ")

            if escolha is None:
                break
            elif escolha.isdigit():
                escolha = int(escolha) - 1
                if 0 <= escolha < len(links_validos):
                    url_download = links_validos[escolha]
                    nome_arquivo = url_download.split("/")[-1]
                    print(f"\n📥 Baixando {nome_arquivo}...\n")
                    baixar_arquivo(url_download, nome_arquivo)
                else:
                    print("\n❌ Escolha inválida.")
            elif escolha == "n":
                break

            continuar = entrada_usuario("\n🔄 Deseja fazer uma nova pesquisa? (s/n): ")
            if continuar is None or continuar == "n":
                print("\n🚪 Saindo...\n")
                exit()
            else:
                break  # Voltar ao menu principal

if __name__ == "__main__":
    buscar_livros()