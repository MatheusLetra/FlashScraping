# FlashScraping

Este projeto é uma aplicação web simples em Flask que coleta e exibe resultados de partidas de futebol ao vivo a partir do site Flashscore. Utiliza Selenium e BeautifulSoup para a raspagem de dados.

## Estrutura do Projeto

```
flask_app/
│
├── app.py                # Arquivo principal da aplicação Flask
├── scraper.py            # Módulo para raspagem de dados
├── requirements.txt      # Arquivo de configuracao de dependencias
└── templates
    └── index.html       # Template HTML para exibição dos resultados
```

## Pré-requisitos

Antes de começar, verifique se você tem o Python 3.x e o pip instalados. Você também precisará do Google Chrome e do ChromeDriver compatível com sua versão do Chrome.

### Instalação de Dependências

Execute o seguinte comando para instalar as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Configuração do ChromeDriver

1. **Baixar ChromeDriver**: Acesse [ChromeDriver downloads](https://sites.google.com/chromium.org/driver/downloads) e baixe a versão compatível com a sua versão do Google Chrome.
2. **Instalar ChromeDriver**: Extraia o executável e coloque-o em um diretório incluído no seu PATH ou especifique o caminho no código, se necessário.

## Como Executar o Projeto

1. Navegue até o diretório do projeto:

    ```bash
    cd /caminho/para/seu/diretorio/flask_app
    ```

2. Execute a aplicação:

    ```bash
    python app.py
    ```

3. Acesse a aplicação no seu navegador em: [http://localhost:5000](http://localhost:5000)

## Funcionamento

- O endpoint `/` realiza a raspagem dos resultados das partidas ao vivo e os exibe em uma tabela organizada.
- O Selenium é utilizado para interagir com a página do Flashscore e obter os dados em tempo real.
- O BeautifulSoup analisa o HTML para extrair informações relevantes, como os times, placares, campeonatos e minutagem das partidas.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.