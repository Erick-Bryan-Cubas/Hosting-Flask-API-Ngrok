# Hospede API Flask com o Ngrok

## O que é o Ngrok?

O Ngrok é uma ferramenta que permite criar túneis seguros para a internet. Com ele, é possível expor um servidor local para a internet, permitindo que outras pessoas acessem o seu servidor local.

### Por que usar o Ngrok?

O Ngrok é muito útil para desenvolvedores que estão criando APIs, por exemplo. Com ele, é possível testar a API localmente e, ao mesmo tempo, permitir que outras pessoas acessem a API.

### Instalando o Ngrok

```shell
choco install ngrok
```

## Crie um ambiente virtual e instale as dependências

Para criar um ambiente virtual, execute os seguintes comandos:

```shell
python -m venv flask-ngrok-venv
.\flask-ngrok-venv\Scripts\activate
pip install -r .\docs\requirements.txt
```

## Execute a aplicação Flask e o Ngrok

Execute a aplicação Flask:

```shell
python .\src\app.py
```

Em outro terminal, navegue até o diretório onde o executável ngrok está localizado:

```shell
cd '\ProgramData\chocolatey\lib\ngrok\tools'
```

E execute o comando para iniciar o ngrok:

```shell
./ngrok http 5000
```
![ngrok](images/ngrok-001.png)

No navegador, acesse o link gerado pelo ngrok:
![ngrok](images/ngrok-002.png)

Insira o endpoint da API e o método HTTP:

`/calculator/?name=bryan&var_first=10&var_second=5`

![ngrok](images/ngrok-003.png)

O resultado será exibido no navegador:

```json
{
"name": "bryan",
"addition": 15.0,
"subtraction": 5.0,
"multiplication": 50.0,
"division": 2.0
}
```

No terminal onde o ngrok foi iniciado, é possível visualizar as requisições feitas para a API:

![ngrok](images/ngrok-004.png)