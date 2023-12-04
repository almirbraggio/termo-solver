# termo-solver

Usa uma lista de palavras como arquivo de entrada para dar sugestões ao term.ooo do dia.
O script formata uma ou mais expressões regulares, de acordo com os parâmetros de entrada, sendo:

- file (requerido): arquivo de texto com palavras a buscar, uma palavra por linha
- inc (requerido): letras que são incluídas na busca
- exc (requerido): letras que são excluídas da busca
- --starts (opcional): quando se sabe com quais letras a palavra inicia
- --ends (opcional): quando se sabe com quais letras a palavra termina

## Exemplo de uso

Para buscar uma palavra, execute o comando:

```
python3 main.py
usage: main.py [-h] [--starts starts] [--ends ends] file inc exc
```

Por exemplo, supondo que a palavra teste inicial foi `coisa`, agora eu sei que a palavra tem a voga `o` e não tem as letras `cisa`. O comando executado seria:

```
python3 main.py five-letters o cisa
```

Na segunda tentativa, supondo que foi utilizado uma das 911 palavras sugeridas, no caso a palavra `ovulo`. Agora sabemos que a palavra tem a vogal `u`, e termina com a vogal `o`. Também sabemos que não possui as letras `vl`.

```
python3 main.py --ends o five-letters ou cisavl
```

Na terceira tentativa, supondo que foi utilizado uma das 112 palavras sugeridas, no caso a palavra `bruxo`. Agora sabemos que a palavra começa com `bru` e termina com `o`, e não tem a letra `x`

```
python3 main.py --starts bru --ends o five-letters oubr cisavlx
```

A busca retorna as 4 palavras possíveis. Na quarta tentativa, a palavra `bruto` foi utilizada, com acerto!

# Instalação/Execução

## Primeiro uso

Para criar o ambiente virtual:
`python3 -m venv venv`

Para acessar o ambiente:
`source venv/bin/activate`

Para instalar os requisitos:
`(venv) pip3 install -r requirements.txt`

## Execução

Acessar o ambiente:
`source venv/bin/activate`

Executar o main:
`(venv) python main.py`

## Novas Bibliotecas

Acessar o VENV e criar o arquivo de requisitos:
`(venv) pip3 freeze > requirements.txt`

# Autor

Almir A. Braggio