import requests
import time
from bs4 import BeautifulSoup
import cmd

# Classe que representa um Job (vaga), contendo título e link.
class Job():
    def __init__(self, title, link):
        self.title = title
        self.link = link

    # Método para retornar os dados da vaga no formato JSON.
    def to_json(self):
        return {
            'title': self.title,
            'link': self.link
        }

# Classe CLI que permite a interação via terminal para busca de empregos.
class MyCLI(cmd.Cmd):
    prompt = 'stack level location -->> '  # Prompt que aparece no terminal.
    intro = '''
- Bem-vindo ao Scraper de vagas do LinkedIn!
- Para buscar vagas, digite conforme o exemplo abaixo:
- 'stack level remote' para vagas remotas.
- 'stack level location' para vagas em um local específico.
- Exemplos: 'react senior remote', 'laravel entry brazil'
'''

    def __init__(self):
        super().__init__()

    # Comando para encerrar o CLI.
    def do_quit(self, line):
        """Encerra o CLI."""
        return True

    # Define o comportamento padrão para entradas no terminal (busca de vagas).
    def default(self, line):
        search_items = line  # Recebe os termos de busca digitados.
        self.search_jobs(search_items)

    # Função principal para buscar vagas no LinkedIn.
    def search_jobs(self, search_items):
        print('Procurando por vagas...')
        data = search_items
        palavra = ''
        palavras = []

        # Converte a string de busca em uma lista de palavras (por exemplo, 'python junior brasil').
        for word in data:
            if word == ' ':
                palavras.append(palavra)
                palavra = ''
            else:
                palavra += word
        palavras.append(palavra)  # Adiciona a última palavra.

        # Verifica se a vaga é remota ou não e ajusta a localização e geoId conforme necessário.
        if palavras[2].lower() == 'remote':
            location = 'Worldwide'
            geoId = '92000000'  # GeoID para vagas remotas globais.
        elif palavras[2].lower() == 'brasil':
            location = 'Brasil'
            geoId = '106057199'  # GeoID para o Brasil.
        else:
            # Se a localização tiver mais de 2 palavras, junta todas a partir da terceira.
            if len(palavras) >= 4:
                location = ' '.join(palavras[2:])
            else:
                location = palavras[2]
            geoId = '103644278'  # GeoID padrão.

        stack = palavras[0]  # Linguagem ou stack de tecnologia (por exemplo, 'python').
        level = palavras[1]  # Nível de experiência (por exemplo, 'junior').

        # Monta a URL de busca no LinkedIn.
        url = f'https://www.linkedin.com/jobs/search?keywords={stack}%20{level}&location={location}&geoId={geoId}&trk=public_jobs_jobs-search-bar_search-submit'

        # Loop para tentar novamente em caso de erro de requisição.
        while True:
            try:
                # Atraso para evitar o erro 429 (Too Many Requests).
                time.sleep(2)

                # Faz a requisição HTTP.
                html = requests.get(url)
                if html.status_code == 200:
                    bs = BeautifulSoup(html.text, 'html.parser')

                    # Busca pelos links e títulos das vagas.
                    jobs_list = bs.find_all('a', {'class': 'base-card__full-link'})

                    Jobs = set()  # Utiliza set para evitar duplicatas.
                    for job in jobs_list:
                        title = job.get_text(strip=True)  # Extrai o título da vaga.
                        link = job['href']  # Extrai o link da vaga.
                        Jobs.add(Job(title, link))  # Adiciona a vaga ao set.

                    # Salva os resultados em um arquivo .txt.
                    self.save_to_file(Jobs)
                    break  # Encerra o loop se a requisição foi bem-sucedida.

                else:
                    print(f"Erro na requisição: {html.status_code}")
                    time.sleep(5)  # Espera 5 segundos antes de tentar novamente.
                    print("Tentando novamente em 5 segundos...")

            except Exception as e:
                print(f"Erro: {e}")
                time.sleep(5)  # Espera 5 segundos antes de tentar novamente.
                print("Tentando novamente em 5 segundos...")

    # Função para salvar os resultados em um arquivo de texto.
    def save_to_file(self, jobs):
        """Salva os resultados da busca em um arquivo .txt."""
        filename = 'jobs_results.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            for job in jobs:
                file.write(f"{job.title}\n{job.link}\n\n")  # Escreve o título e o link com um espaço de linha.
        print(f"Resultados salvos em {filename}")

# Inicia o loop do CLI.
if __name__ == '__main__':
    MyCLI().cmdloop()
