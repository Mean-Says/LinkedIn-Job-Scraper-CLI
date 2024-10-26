
# LinkedIn Job Scraper CLI

Este projeto é uma ferramenta de linha de comando (CLI) para buscar vagas de emprego no LinkedIn com base em stack, nível e localização (ou opção remota). A aplicação é construída em Python e utiliza as bibliotecas `requests` e `BeautifulSoup` para fazer scraping de vagas no LinkedIn e salvar os resultados em um arquivo `.txt`.

## Funcionalidades

- Pesquisar vagas de emprego no LinkedIn com base em uma stack, nível de experiência e localização (ou opção remota).
- Suporta a pesquisa de vagas em qualquer localidade do mundo ou em modo remoto.
- Salva os resultados da busca (título da vaga e link) em um arquivo `jobs_results.txt`.
- Faz tentativas repetidas em caso de erros de requisição HTTP, como o erro 429 (Too Many Requests).

## Tecnologias Utilizadas

- **Python**: Linguagem de programação usada para construir o projeto.
- **Requests**: Biblioteca para fazer requisições HTTP.
- **BeautifulSoup**: Biblioteca para parsear e extrair dados do HTML.

## Requisitos

- **Python 3.6+**
- **Bibliotecas necessárias**:
    - `requests`
    - `beautifulsoup4`

Para instalar as bibliotecas necessárias, execute:

```bash
pip install requests beautifulsoup4
```

## Como usar

1. Clone este repositório:

   ```bash
   git clone https://github.com/Mean-Says/LinkedIn-Job-Scraper-CLI
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd linkedin-job-scraper-cli
   ```

3. Execute o programa:

   ```bash
   python scraper.py
   ```

4. Ao iniciar, você verá uma mensagem de introdução explicando como fazer uma busca. O prompt irá solicitar que você digite três itens: **stack**, **level**, e **location** (ou a palavra "remote" para buscar vagas remotas).

   Exemplos de comandos:
   - Para buscar vagas remotas de desenvolvedor Python junior:
     ```
     python junior remote
     ```

   - Para buscar vagas de desenvolvedor React sênior no Brasil:
     ```
     react senior brasil
     ```

   Após digitar o comando, a ferramenta irá buscar as vagas no LinkedIn e, se for bem-sucedida, salvará os resultados no arquivo `jobs_results.txt`.

5. Para sair da CLI, basta digitar `quit`.

## Estrutura do Projeto

```
.
├── scraper.py          # Código principal da CLI
├── jobs_results.txt    # Arquivo gerado com os resultados da busca
└── README.md           # Descrição do projeto
```

## Notas

- O scraper está sujeito a limitações do LinkedIn, como bloqueios temporários devido a um número excessivo de requisições (erro 429). Nesses casos, o programa automaticamente espera alguns segundos e tenta novamente.
- **Atenção**: O scraping de dados de sites pode violar os termos de uso do LinkedIn. Certifique-se de que o uso desta ferramenta esteja em conformidade com as políticas do site.

---

### Melhorias Futuras

- Adicionar suporte para outras plataformas de emprego além do LinkedIn.
- Melhorar a formatação dos resultados gerados no arquivo de texto.
- Implementar filtros de pesquisa mais avançados, como tipo de contrato e empresa.

---


