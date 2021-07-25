# Detector de falhas em máquinas por análise sonora

Este código está atrelado ao meu trabalho de conclusão de curso em Engenharia Elétrica. 

Para entender como o mesmo foi criado bem como os conceitos utilizados leia o documento "TCC-Vinicio Schmidt.pdf" na pasta Documentos.

# Pré confriguração ambiente Linux

## Instalação do Python3

`$ sudo apt-get install python3`

## Instalação das dependências do PyAudio

`$ sudo apt-get update`

`$ sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 python3-dev python3-tk`

# Pré configuração em ambiente windows (Compatibilidade não testada)

Certifique-se de ter a versão 3.7 (ou superior) do Python instalada na sua máquina bem como o gerenciador de pacotes pip (embutido no instalador do Python).

Para baixar o instalador acesse: www.python.org

## Instalação das dependências do projeto

`$ pip install -r requirements.txt`

### Instalar pyAudio

`$ pip install .\libs\PyAudio-0.2.11-cp38-cp38-win32.whl`

## Rodar a aplicação

### No Windows
`$ python interface/main.py`

### No Linux
`$ python3 interface/main.py`
