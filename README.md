# FastAPI Currency Converter

Este projeto é uma API que fornece conversão monetária, respondendo em JSON. A moeda base é o USD e as conversões são realizadas com cotações atualizadas de diferentes moedas.

A requisição deve incluir os parâmetros: moeda de origem, valor a ser convertido e moeda final.

Exemplo: `?from=BTC&to=EUR&amount=123.45`

## Clonando o projeto

Para clonar o projeto, basta executar o seguinte comando no terminal:
```shell
git clone git@github.com:Sidon/fastapi-currency-converter.git
```
## Executando o projeto

Para executar o projeto, a primeira coisa a se fazer é ir para o diretorio do mesmo, para isso, após cloná-lo, execute o comando:
```shell 
cd fastapi-currency-converter
```
O projeto pode ser executado em uma máquina linux, de duas maneiras, localmente ou através do docker

### Execução local
Estando na diretório raiz do projeto, ative a virtuaenv python de sua preferencia e instale as dependencias com o comando:
```shell 
pip install -r requeriments
```

### Execução através do docker
Certifique-se de que tenha o docker e o docker compose instalado com o comando, observando a saida, as versões podem não ser, necessariamente, as mesmas dos exemplos abaixo:
 
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

## Exemplo de requisão atraves do Curl

### Chamada:
```bash
curl -X 'GET' \
  'http://0.0.0.0:8000/convert?from_currency=USD&to_currency=BTC&amount=21700' \
  -H 'accept: application/json'
```

### Retorno:
```bash
{ "success": true, "query": { "from": "USD", "to": "BTC", "amount": 21700 }, "info": { "timestamp": 1676050803, "rate": 0.000046215603 }, "date": "2023-02-10", "result": 1.002879 }
```