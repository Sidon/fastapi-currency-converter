# FastAPI Currency Converter  
  
Este projeto é uma API que fornece conversão monetária, respondendo em JSON. As conversões são realizadas com cotações atualizadas em tempo real,  de diferentes moedas.  
  
A requisição deve incluir os parâmetros: moeda de origem, valor a ser convertido e moeda final.  
  
Exemplo: `?from=BTC&to=EUR&amount=123.45`  
  
  
## Índice  
- [Clonando o projeto](#clonando-o-projeto)  
- [Configuração](#configuração)  
- [Executando o projeto](#executando-o-projeto)  
  - [Execução local](#execução-local)  
  - [Execução através do docker](#execução-através-do-docker)  
- [Acessando via browser](#acessando-via-browser)  
  - [Requisição](#requisição)  
- [Usando o comando Curl](#usando-o-comando-curl)  
  - [Chamada](#chamada)  
  - [Retorno](#retorno)  
- [Stack de desenvolvimento](#stack-de-desenvolvimento)  
  
  
## Clonando o projeto  
  
Para clonar o projeto, basta executar o seguinte comando no terminal:  
```shell  
git clone git@github.com:Sidon/fastapi-currency-converter.git
```  
  
## Configuração   
  
Os valores dos ativos são obtidos através da API [fixer.io](https://fixer.io) e utiliza uma chave pessoal temporária.   
No entanto, essa chave pode ser substituída no arquivo `.env` na raiz do projeto.  
  
## Executando o projeto  
  
Para executar o projeto, a primeira coisa a se fazer é ir para o diretorio do mesmo, para isso, após cloná-lo, execute o comando:  
```shell cd fastapi-currency-converter
```  
O projeto pode ser executado em uma máquina linux, de duas maneiras, localmente ou através do docker  
  
### Execução local
O sistema foi desenvolvido utilizando o python 3.10, para execução local é necessário um ambiente com uma versão do python compativel.
Estando na diretório raiz do projeto, ative a virtuaenv python de sua preferencia e instale as dependencias com o comando:  
```shell 
pip install -r requeriments
```  
### Execução através do docker  
Certifique-se de que tenha o docker e o docker compose instalado com o comando abaixo, observando a saida.   
As versões podem não ser, necessariamente, as mesmas dos exemplos abaixo:  
   
```shell
❯ docker --version 
Docker version 23.0.0, build e92dd87  

❯ docker compose version 
Docker Compose version v2.15.1  
```  
Execute o projeto com o comando:  
```shell
docker-compose -u
```  
## Acessando via browser  
Acesse apontando o browse para o endereço: [http://localhost:8000](http://localhost:8000)  
  
## Requisição  
O endpoint de entrada apresenta um front-end simples onde se pode fazer a consulta  atraves do preenchimento dos campos, mas é possível, também fazer requisições diretas para se obter o JSON resultante via browser, para isso a requisição deve incluir os parâmetros:  moeda de origem, valor a ser convertido e moeda final.  
  
Exemplo:  
[http://0.0.0.0:8000/convert?from_currency=USD&to_currency=BTC&amount=21700](http://0.0.0.0:8000/convert?from_currency=USD&to_currency=BTC&amount=21700)  
   
## Usando o comando Curl  
  
### Chamada:  
```bash  
curl -X 'GET' \ 
'http://0.0.0.0:8000/convert?from_currency=USD&to_currency=BTC&amount=21700'\
-H 'accept: application/json'
```  
  
### Retorno:  
```bash  
{
    "success": true,
    "query": {
        "from": "USD",
        "to": "BTC",
        "amount": 21700
    },
    "info": {
        "timestamp": 1676050803,
        "rate": 0.000046215603
    },
    "date": "2023-02-10",
    "result": 1.002879
}
```  
  
## Stack de desenvolvimento
O Sistema foi desenvolvido em uma máquina com o so ubuntu 22.04LTS, em uma environment python 3.10 com as seguintes dependencias:  
- `pydantic`~=1.10.4  
- `fastapi`~=0.90.0  
- `requests`~=2.28.2  
- `uvicorn`~=0.20.0  
- `python-dotenv`~=0.21.1  
- `python-multipart`~=0.0.5  
- `Jinja2`~=3.1.2  
- `starlette`~=0.23.0