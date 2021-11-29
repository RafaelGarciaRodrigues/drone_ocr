#LISTA DE PACOTES GERAL
# pip install pyinstaller GoogleNews newspaper3k
# pip install Pillow opencv-python pyautogui pyscreenshot normalize matplotlib seaborn dataframe_image
# pip install pandas xlrd openpyxl pandasql XlsxWriter mysql-connector-python schedule

# pip install pymssql pyodbc pyinstaller GoogleNews newspaper3k Pillow opencv-python pyautogui selenium pyscreenshot normalize matplotlib seaborn dataframe_image pandas xlrd xlwt openpyxl pandasql XlsxWriter mysql-connector-python schedule streamlit scipy scikit-learn kneed factor-analyzer prince wordcloud pyzbar
#   bokeh plotly-express plotly

###NO WINDOWS
# python -m pip install -U pyinstaller GoogleNews newspaper3k
# python -m pip install -U Pillow opencv-python pyautogui pyscreenshot normalize matplotlib seaborn dataframe_image
# python -m pip install -U pandas xlrd openpyxl pandasql XlsxWriter mysql-connector-python schedule factor-analyzer

# pip install mysql-connector-python
# pip install pyodbc
# pip install Pillow
# pip install opencv-python
# pip install pyautogui
# pip install pyinstaller
# pyinstaller [NOME DO ARQUIVO]
# pip install GoogleNews
# pip install newspaper3k
# pip install python-pptx
# pip install pyscreenshot
# pip install normalize
# pip install matplotlib
# pip install streamlit
# pip install seaborn
# pip install dataframe_image
# PARA ABRIR EXCEL
    # pip install pandas
    # pip install xlrd
    # pip install openpyxl
    # pip install pandasql
    # pip install XlsxWriter
# pip install scipy
# pip install -U scikit-learn
# pip install factor-analyzer
# pip install prince
# pip install pycaret-ts-alpha

# CORES PANDAS
# https://matplotlib.org/stable/gallery/color/named_colors.html

import mysql.connector
from bs4 import BeautifulSoup
import webbrowser
import pyautogui
import time

from datetime import datetime
import datetime as dt
from datetime import date

import pyscreenshot as ImageGrab
import pyperclip
import random
import os
import re
import dataframe_image as dfi
import pandas as pd
import pickle
import pandasql as ps
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import math
import prince
from scipy.stats import shapiro

from scipy.stats import chi2_contingency
from scipy.stats import chi2
import numpy as np
import requests
import getpass
import pyodbc
import pymssql
import requests
import json
from random import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#CIÊNCIA DE DADOS

##############################################################################################################
# OPÇÕES PADROES DO PANDAS
pd.set_option("display.expand_frame_repr", False)
pd.options.display.max_seq_items = None
pd.options.display.float_format = '{:,.2f}'.format
RF = os.getcwd() + '\\RAFAEL\\'


def USUARIO_LOGADO():
    return getpass.getuser()

def DIRETORIO_ATUAL():
    return os.getcwd()

def AGORA():
    now = datetime.now()
    return now

def HOJE():
    data_atual = date.today()
    return data_atual

def DORME(S):
    print('DORMINDO ',S,'s ...')
    time.sleep(S)

def DIFERENCA_TEMPO(INICIO,FINAL):

    a = INICIO
    b = FINAL
    f = "%Y-%m-%d %H:%M:%S"

    MSG(a, 'AZUL')

    ini = datetime.strptime(a, f)
    fim = datetime.strptime(b, f)

    #dif = abs(relativedelta(ini, fim))

    #return dif



def MSG(TXT,COR):
    # https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/
    def COLOR(X):
        return {
            'BRANCO': "\033[1;97m",
            'PRETO': "\033[1;30m",
            'VERMELHO': "\033[1;31m	",
            'VERDE': "\033[1;32m",
            'AMARELO': "\033[1;33m",
            'AZUL': "\033[1;34m",
            'MAGENTA': "\033[1;35m",
            'CYAN': "\033[1;36m",
            'CINZA_CLARO': "\033[1;37m",
            'CINZA_ESCURO': "\033[1;90m",
            'VERMELHO_CLARO': "\033[1;91m",
            'VERDE_CLARO': "\033[1;92m",
            'AMARELO_CLARO': "\033[1;93m",
            'AZUL_CLARO': "\033[1;94m",
            'MAGENTA_CLARO': "\033[1;95m",
            'CYAN_CLARO': "\033[1;96m",
            'NEGRITO': "\033[;1m",
            'MAGENTA_CLARO': "\033[1;95m",
            'INVERTE': "\033[;7m"
        }.get(X, '\033[1;97m')
    print(COLOR(COR))
    print('***************************************************************************************')
    print(TXT)
    print(AGORA())
    print('***************************************************************************************')
    print('\033[0;0m')

def MSG2(df,TEXTO):
    print("\033[1;92m")
    print(TEXTO + ' <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    print(AGORA())
    print(df.head())
    print("\033[1;94m")
    print(df.info())
    print('..........................................................................................')
    print(dict(df.dtypes))
    print('..........................................................................................')
    print("\033[1;94m")
    print(df.describe(include = ['object', 'float', 'int'],percentiles = [.25, .50, .75, .95]))
    print('DADOS AUSENTES...')
    Ausentes = pd.DataFrame()
    Ausentes['ausentes'] = df.isnull().sum()
    Ausentes['perc'] = df.isnull().sum() * 100 / len(df)
    Ausentes = Ausentes.sort_values(['perc'], ascending=[False])
    print(Ausentes.T)
    print('..........................................................................................')
    print('\033[0;0m')



def PALETA(N):
    if N == 0:
        COR = '#0d6efd' #PRIMARY
    if N == 1:
        COR = '#6c757d' #SECONDARY
    if N == 2:
        COR = '#ffc107' # WARNING
    if N == 3:
        COR = '#198754' #SUCESS
    if N == 4:
        COR = '#dc3545' # DANGER
    return COR

def ABRIR_EXE(CAMINHO,DELAY):
    import ctypes
    MSG('ABRINDO ' + CAMINHO,'CYAN')
    #os.system(CAMINHO) # ABRE DENTRO DO PYTHON
    shell32 = ctypes.windll.shell32
    shell32.ShellExecuteA(0,"open",CAMINHO,0,0,5)
    MSG('ESPERANDO ' + str(DELAY) + ' SEGUNDOS', 'CYAN')
    time.sleep(DELAY)


def CRIA_PASTA_AUXILIAR():
    import os
    if os.path.isdir(".\\ARQUIVOS_AUXILIARES"):
        print("PASTA ARQUIVOS_AUXILIARES EXISTE")
    else:
        print("PASTA ARQUIVOS_AUXILIARES NÃO EXISTE")
        os.mkdir('.\\ARQUIVOS_AUXILIARES')


def ESCREVER(TEXTO, ESPERA):
    pyautogui.typewrite(TEXTO, interval=0.01)
    print('>>> ' + TEXTO + ' ' + '...\n')
    time.sleep(ESPERA)

def ALT_ENTER():
    pyautogui.keyDown('alt')
    pyautogui.press('enter')
    pyautogui.keyUp('alt')

def TECLA(TECLA,DELAY):
    x, y = pyautogui.position()
    print("X >> " + str(x) + "| Y >> " + str(y))
    pyautogui.press(TECLA)
    print('TECLA >>> ' + TECLA + " ("+str(DELAY)+"s)")
    time.sleep(DELAY)

def LER_ARQUIVO(URL, QUEBRA):
    arquivo = open(URL, 'r', encoding = 'utf-8') # iso -8859 -1
    LINHAS = ''
    for LINHA in arquivo:
        if QUEBRA == 1:
            LINHAS = LINHAS + LINHA.replace('\n', ' ')
        else:
            LINHAS = LINHAS + LINHA
    arquivo.close()
    MSG('ARQUIVO ' + URL + ' ABERTO', 'VERDE')
    return LINHAS

def RODAR(QUANTO, ESPERA):
    pyautogui.scroll(QUANTO)
    time.sleep(ESPERA)


def SEGURA_APERTA(SEGURA,APERTA, ESPERA):
    pyautogui.hotkey(SEGURA,APERTA)
    time.sleep(ESPERA)


def SEGURA_MOUSE(BOTAO,TEMPO):
    if BOTAO == "E":
        pyautogui.mouseDown()
        time.sleep(TEMPO)
        pyautogui.mouseUp()
    if BOTAO == "D":
        pyautogui.mouseDown(button='right')
        time.sleep(TEMPO)
        pyautogui.mouseUp(button='right')

def SCREENSHOT(X1,Y1,X2,Y2,NOME):
    time.sleep(1)
    imagem = ImageGrab.grab(bbox=(X1,Y1,X2,Y2))  # X1,Y1,X2,Y2
    imagem.save(NOME)

def ESCREVER_ARQUIVO(ARQUIVO,TEXTO):
    with open(ARQUIVO, 'w', encoding = 'utf-8') as arquivo:
        arquivo.write('\n'+TEXTO)
        arquivo.close()
    MSG('ARQUIVO ' + ARQUIVO + ' CRIADO','VERDE')

def MEIO_TELA(DELAY,X,Y,CLICA):
    time.sleep(DELAY)
    tamanho = pyautogui.size()
    MeioX = (tamanho.width / 2) + X
    Meioy = (tamanho.height / 2) + Y
    pyautogui.moveTo(MeioX, Meioy, duration=0.1)
    if CLICA == 1:
        pyautogui.click()
    print("MEIO DA TELA >>> ("+str(DELAY)+"s)")

def UP_DRIVE(DRIVE,ARQUIVO_PARA_SUBIR):
    ABA = webbrowser.open(DRIVE)
    CLICA('UpLoadGoogleDriver.png', 'NOVO', 5, 1, 1)
    CLICA('UpLoadDeArquivo.png', 'UPLOAD', 2, 3, 1)
    ESCREVER(ARQUIVO_PARA_SUBIR, 2)
    TECLA('enter', 10)
    CLICA('AtualizarItensExistentes.png', 'UPLOAD', 1, 10, 1)
    SEGURA_APERTA('ctrl', 'w', 1)
    SEGURA_APERTA('alt', 'tab', 1)

def COLA(TEXTO, DELAY,ACAO):
    pyperclip.copy(TEXTO)
    pyautogui.hotkey('ctrl', 'v', interval=0.15)
    print('COLA >>> ' + TEXTO + " ("+str(DELAY)+"s)")
    if len(ACAO) > 0:
        TECLA(ACAO,DELAY)

def CRIA_DF(data,COLUNAS):
    # COLUNAS = ['CAMPO1', 'CAMPO2']
    df = pd.DataFrame(data, columns=COLUNAS)
    MSG('DATA FRAME CRIADO', 'VERDE')
    MSG(df, 'VERDE')
    return df

def SALVA_DF_FORMATO_PANDAS(df,NOME_ARQUIVO):
    print('>>> SALVANDO PKL')
    df.to_pickle(NOME_ARQUIVO + '.pkl')
    MSG2(df, "SALVO XLSM:\n" + NOME_ARQUIVO + '.pkl')

def SALVA_DF_EXCEL(df,ARQUIVO,PLANILHA):
    ARQUIVO = ARQUIVO.replace('.xlsx','')
    ARQUIVO = ARQUIVO.replace('.xls', '')
    ARQUIVO = ARQUIVO + '.xlsx'
    df.to_excel(ARQUIVO, sheet_name=PLANILHA, index=False)
    MSG2(df,"SALVO XLSX:\n" + ARQUIVO)
    return df


def SALVA_DF_CSV(DF,ARQUIVO):
    try:
        DF.to_csv(ARQUIVO)
        MSG("SALVO CSV: " + ARQUIVO, "CYAN")
        MSG(DF,'CYAN')
    except:
        MSG("ERRO AO SALVAR " + ARQUIVO, 'VERMELHO')
        pass



def DATAFRAME_PNG(DF,ARQUIVO):
    dfi.export(DF, ARQUIVO)
    print("PNG GERADO DE " + DF)

def EXISTE_NA_TELA(IMG):
    n=0
    EXISTE = 0
    while n<10:
        time.sleep(0.25)
        BOT = pyautogui.locateCenterOnScreen(IMG, confidence=0.85)
        if BOT:
            EXISTE = 1
            MSG("ENCONTROU " + IMG + " NA TELA", "VERDE")
            break
        else:
            n+=1
    return EXISTE

def FECHA_JANELA_E_RETORNA(DELAY_ANTES, DELAY_DEPOIS):
    SEGURA_APERTA('ctrl', 'w', 1)
    SEGURA_APERTA('alt', 'tab', 1)

def ABRE_PAGINA_WEB(URL,IMAGEM,ESPERA_ANTES,ESPERA_DEPOIS):
    MEIO_TELA(ESPERA_ANTES, 0, 0, 0)
    ABA = webbrowser.open(URL)
    if len(IMAGEM)>0:
        ESPERA_NA_TELA(IMAGEM, 60, .8,10000)
    MSG("PAGINACARREGADA : " + URL, "VERDE")
    time.sleep(ESPERA_DEPOIS+2)

def BUSCA_TEXTO_ENTRE_CARACTERES(TEXTO,INICIO,FINAL):
    start = TEXTO.find(INICIO) + len(INICIO)
    end = TEXTO.find(FINAL)
    ACHADO = TEXTO[start:end]
    return ACHADO


def ESPERA_NA_TELA(OPCOES,LIMITE,CONFIANCA,LIMITE_Y):
    # LIMITE_Y POSIÇÃO MÁXIMA DO OBJETO NA TELA VERTICALMENTE PARA QUE SEJA CONSIDERADO
    x=0
    n=0
    while x == 0:
        print("["+str(n)+"]", end="")
        time.sleep(.25)
        if n > LIMITE:
            OPCAOn = -1
            x = 1
        n+=1
        for OPCAO in OPCOES:
            BOT = pyautogui.locateCenterOnScreen(OPCAO, confidence=CONFIANCA)
            if BOT:
                if BOT[1] <= LIMITE_Y:
                    x = 1
                    OPCAOn = OPCOES.index(OPCAO)
                    break

    MSG("OPÇÃO ENCONTRADA: ["+str(OPCAOn)+"] " + str(OPCAO), "VERDE")
    return OPCAOn

def CLICA(IMAGEM, TEXTO_SAIDA, ESPERA_ANTES,ESPERA_DEPOIS,CLICAR,TRAVAR,DE):
    if TRAVAR ==1:
        MEIO_TELA(ESPERA_ANTES + 0.25, 0, 0, 0)
    else:
        time.sleep(ESPERA_ANTES)
    if ESPERA_NA_TELA(IMAGEM, 45, .8,10000) >= 0:
        for I in IMAGEM:
            BOT = pyautogui.locateCenterOnScreen(I, confidence=0.75)
            if BOT:
                if CLICAR == 1:
                    if DE == "D":
                        BOT = pyautogui.locateCenterOnScreen(I, confidence=0.75)
                        pyautogui.moveTo(BOT[0], BOT[1], duration=0.1)
                        pyautogui.rightClick()
                    if DE == "E":
                        BOT = pyautogui.locateCenterOnScreen(I, confidence=0.75)
                        pyautogui.moveTo(BOT[0], BOT[1], duration=0.1)
                        pyautogui.click()
                    if DE == "E2":
                        BOT = pyautogui.locateCenterOnScreen(I, confidence=0.75)
                        pyautogui.moveTo(BOT[0], BOT[1], duration=0.1)
                        pyautogui.doubleClick()
                    print("CLICOU EM: " + I + " >>> " + TEXTO_SAIDA + " (" + str(ESPERA_DEPOIS) + "s)")
                else:
                    print("POSICIONOU SOBRE: " + I + " >>> " + TEXTO_SAIDA + " (" + str(ESPERA_DEPOIS) + "s)")
                MEIO_TELA(ESPERA_DEPOIS + 0.25, 0, 0, 0)
                return 1
    else:
        MSG("NÃO ACHOU A IMAGEM NA TELA", "VERMELHO")
        MEIO_TELA(ESPERA_DEPOIS + 0.25, 0, 0, 0)
        return 0




def TABS(N,ESPERA_ANTES,ESPERA_DEPOIS,ENTER):
    time.sleep(ESPERA_ANTES)
    for x in range(N):
        TECLA("tab",0)
    if ENTER == 1:
        time.sleep(0.5)
        TECLA("enter",0)
    time.sleep(ESPERA_DEPOIS)

def DELETA_ARQUIVO(ARQUIVO):
    try:
        os.remove(ARQUIVO)
        MSG('ARQUIVO [' +ARQUIVO+ '] DELETADO', 'VERDE')
    except:
        MSG('ERRO AO DELETAR [' + ARQUIVO + ']', 'VERMELHO')
        pass


def MOVE_ARQUIVO(DELAY_ANTES,ORIGEM,DESTINO,DELAY_DEPOIS):
    time.sleep(DELAY_ANTES)
    DELETA_ARQUIVO(DESTINO)
    os.link(ORIGEM, DESTINO)
    DELETA_ARQUIVO(ORIGEM)
    time.sleep(DELAY_DEPOIS)
    MSG('ARQUIVO MOVIDO DE ['+ORIGEM+'] PARA ['+DESTINO+']','VERDE')


def ENVIA_WHATSAPP(NUMEROS,MENSAGENS,ANEXOS):
    for NUMERO in NUMEROS:
        MSG("ENVIANDO MENSAGEM PARA " + str(NUMERO), "VERDE")
        ABRE_PAGINA_WEB("https://web.whatsapp.com/send?phone=+" + str(NUMERO), .5, .5)
        CLICA([RF+r"Iniciar_Conversas_WhatsAPP_1.png"],"ABRIR",.5,.5,1,0,"E")
        ESPERA_NA_TELA([RF + r"WhatsApp_Aberto_1.png", RF + r"WhatsApp_Aberto_2.png"], 30, .8,10000)

        if len(MENSAGENS) > 0:
            for MENSAGEM in MENSAGENS:
                COLA(MENSAGEM, .25)
                TECLA("enter", .25)
        if len(ANEXOS) > 0:
            for ANEXO in ANEXOS:
                print("ANEXAR " + ANEXO)
                CLICA([RF + "Clips_WhatsAPP_1.png", RF + "Clips_WhatsAPP_2.png", RF + "Clips_WhatsAPP_3.png"],"CLIPS",.25,.25,1,0,"E")
                CLICA([RF + "Anexar_Imagem_WhatsAPP_1.png", RF + "Anexar_Imagem_WhatsAPP_2.png",RF + "Anexar_Imagem_WhatsAPP_3.png"],"ANEXAR IMAGEM", .25, .25, 1, 0,"E")
                CLICA([RF + "Botao_Abrir_Caixa_Windows_1.png", RF + "Botao_Abrir_Caixa_Windows_2.png",RF + "Botao_Abrir_Caixa_Windows_3.png"], "CLIPS",.25, .25, 1, 0,"E")
                COLA(ANEXO, .5)
                CLICA([RF + "Botao_Abrir_Caixa_Windows_1.png", RF + "Botao_Abrir_Caixa_Windows_2.png",RF + "Botao_Abrir_Caixa_Windows_3.png"], "CLIPS", .25, .25, 1, 0,"E")
                TECLA("enter", .25)


def GRUPO_WHATS_APP(NOME_GRUPO,MENSAGENS,ANEXOS):
    MSG("ENVIANDO MENSAGEM GRUPO ", "VERDE")
    ABRE_PAGINA_WEB("https://web.whatsapp.com/send?phone=+5511994278062",[RF + r"WhatsApp_Aberto_1.png", RF + r"WhatsApp_Aberto_2.png",RF + r"PesquisarGrupoWhatsApp.png"], .5, .5)
    CLICA([RF + r"PesquisarGrupoWhatsApp.png"],"BUSCA",.5,.5,1,0,"E")
    COLA(NOME_GRUPO,1)
    ESPERA_NA_TELA([RF+"JaCarregouGrupoWhatsApp.png"],10,.8,1000)
    TECLA("tab", 1)
    TECLA("enter", 1)

    if len(MENSAGENS) > 0:
        for MENSAGEM in MENSAGENS:
            COLA(MENSAGEM, .25)
            TECLA("enter", .25)


        if len(ANEXOS) > 0:
            for ANEXO in ANEXOS:
                print("ANEXAR " + ANEXO)
                CLICA([RF + "Clips_WhatsAPP_1.png", RF + "Clips_WhatsAPP_2.png", RF + "Clips_WhatsAPP_3.png"],"CLIPS",.25,.25,1,0,"E")
                CLICA([RF + "Anexar_Imagem_WhatsAPP_1.png", RF + "Anexar_Imagem_WhatsAPP_2.png",RF + "Anexar_Imagem_WhatsAPP_3.png"],"ANEXAR IMAGEM", .25, .25, 1, 0,"E")
                CLICA([RF + "Botao_Abrir_Caixa_Windows_1.png", RF + "Botao_Abrir_Caixa_Windows_2.png",RF + "Botao_Abrir_Caixa_Windows_3.png"], "CLIPS",.25, .25, 1, 0,"E")
                COLA(ANEXO, .5)
                CLICA([RF + "Botao_Abrir_Caixa_Windows_1.png", RF + "Botao_Abrir_Caixa_Windows_2.png",RF + "Botao_Abrir_Caixa_Windows_3.png"], "CLIPS", .25, .25, 1, 0,"E")
                TECLA("enter", .25)


def ATUALIZA_ALEXA(NOME_ARQUIVO,FRASE_DA_ALEXA):

    ABRE_PAGINA_WEB('http://177.55.114.52/dash/Alexa/ATUALIZA_COMANDOS/form_txt.php',[r'RAFAEL\PaginaAlexaAberta.png'],.5,1)
    MEIO_TELA(.25,0,0,1)
    TECLA('tab',.5)
    COLA(NOME_ARQUIVO,.5,'tab')
    COLA(FRASE_DA_ALEXA, .5, 'tab')
    TECLA('enter',3)
    SEGURA_APERTA('ctrl','w',.5)

def CONSULTA_MYSQL(QUERY,USER,KEY,HOST,DB):
    cnx = mysql.connector.connect(user=USER, password=KEY,host=HOST,database=DB)
    df = pd.read_sql(QUERY, cnx)
    MSG(df,'AMARELO_CLARO')
    cnx.close()
    return df

def CONSULTA_SQL(QUERY,USER,KEY,HOST,DB,PORTA,MODO):

    """
        FOI DIVIDIDO EM MODO 1 E 2 DEVIDO INCOMPATIBILIDADE DO MODO 2 EM ALGUNS COMPUTADORES
        NO MODO 2, DECLARAR A PORTA JUNTO COM O HOST EX: 111.11.111.1,5004
        O DRIVE DEVE SER BAIXADO NO COMPUTADOR (BUSCAR NO GOOGLE ODBC Driver 17 for SQL Server)
    """

    if MODO == 1:
        conn = pymssql.connect(host=HOST, database=DB, port=PORTA, user=USER, password=KEY)
        df = pd.read_sql(QUERY, conn)

    if MODO == 2:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + HOST + ';DATABASE=' + DB + ';UID=' + USER + ';PWD=' + KEY)
        df = pd.read_sql(QUERY, cnxn)

    MSG(df,'AMARELO')
    MSG(df.info(), 'AMARELO')
    SALVA_DF_EXCEL(df,'BASE_SQL.xlsx','DADOS')
    return df

def SCRAPPING_HTML(URL):
    HTML = requests.get(URL).content
    TEXTO = BeautifulSoup(HTML, 'html.parser')
    MSG(TEXTO, 'AMARELO_CLARO')
    return TEXTO



def CONVERTE_DF_HTML(df,TITULO):
    #https://datatables.net/
    ATUAL = datetime.now().strftime('%d/%m/%Y %H:%M')
    ID_TABELA = 'id_tab_'+TITULO.replace(' ','_')
    BASE = LER_ARQUIVO('RAFAEL\\CANVASJS\\T_BASE_v1.html',0)
    df = df.fillna(0)
    MSG(df.head(),'AMARELO')
    HTML = df.to_html()
    HTML = HTML.replace('<table border="1" class="dataframe">', '<table class="table table-bordered" id="' + ID_TABELA + '" width="100%" cellspacing="0">')
    JS = '//JS DA TABELA ' + ID_TABELA + '\nif (document.getElementById("' + ID_TABELA + '")) {new simpleDatatables.DataTable(document.getElementById("' + ID_TABELA + '"));}\n'
    BASE = BASE.replace("_TITULO_DA_TABELA_", TITULO)
    BASE = BASE.replace("_DADOS_DA_TABELA_HTML_", HTML)
    #SALVA ARQUIVO NA PASTA
    if os.path.isdir(".\\GRAFICOS_CANVAS"):
        print("PASTA GRAFICOS_CANVAS EXISTE")
    else:
        print("PASTA GRAFICOS_CANVAS NÃO EXISTE")
        os.mkdir('.\\GRAFICOS_CANVAS')
    ESCREVER_ARQUIVO('GRAFICOS_CANVAS\\tab_'+TITULO.replace(' ','_')+'.html', BASE)
    return JS, HTML


def GRAF_CANVASJS_RELATORIO(df,l_X,l_Y,l_EIXO,l_COR,l_TIPO,l_INDEX_LABEL,LABEL_X,ROTULO_X,ROTULO_Y1,ROTULO_Y2,ARQUIVO_SAIDA,TITULO,INTERVALO_X):
    # l_INDEX_LABEL DEVE SER UMA COLUNA DO DF, OU REPETIR O Y INFORMANDO '' NO CAMPO DA FUNÇÃO
    # SE DEIXAR A COR DA SÉRIE DE DADOS ESTIVER EM BRANCO ['','#FF0000'] A COR SERÁ DETERMINADA PELA COLUNA df[COR].


    ATUAL = datetime.now().strftime('%d/%m/%Y %H:%M')
    BASE = LER_ARQUIVO('RAFAEL\\CANVASJS\\G_BASE_RELATORIO_v1.html',0)
    SERIES = ''
    for X,Y,EIXO,COR,TIPO, IxLb in zip(l_X,l_Y,l_EIXO,l_COR,l_TIPO,l_INDEX_LABEL):
        if isinstance(IxLb, str):
            if IxLb == '':
                IxLb = [''] * len(X)
            if IxLb == 'Y':
                IxLb = Y

        DADOS = ''
        if COR == '':
            for vX, vY, LABEL, IxLb, CORy in zip(list(X),list(Y), LABEL_X, IxLb, df['COR']):
                DADOS = DADOS + '   { x: ' + str(vX) + ', y: ' + str(vY) + ' , label: "' + str(LABEL) + '",indexLabel:"' + str(IxLb) + '" , color: "' + str(CORy) + '" },\n'
        else:
            for vX, vY, LABEL, IxLb in zip(list(X),list(Y), LABEL_X, IxLb):
                DADOS = DADOS + '   { x: ' + str(vX) + ', y: ' + str(vY) + ' , label: "' + str(LABEL) + '",indexLabel:"' + str(IxLb) + '" },\n'
        SERIE = '\n{\nmarkerType: "circle",\nyValueFormatString: "#.##0k",\ntype: "'+TIPO+'",\nshowInLegend: true,\nlegendText: "'+Y.name+'",\ncolor: "'+str(COR)+'",\nindexLabel: "{'+str(IxLb)+'}",\nindexLabelFontSize: 12,\naxisYType: "'+EIXO+'",\ndataPoints: [\n'+DADOS+'\n]\n},\n\n'
        SERIES = SERIES + SERIE
    BASE = BASE.replace("ID_GRAFICO", TITULO.replace(' ','_'))
    BASE = BASE.replace("_TITULO_", TITULO)
    BASE = BASE.replace("_EIXO_X_", ROTULO_X)
    BASE = BASE.replace("_EIXO_Y1_", ROTULO_Y1)
    BASE = BASE.replace("_EIXO_Y2_", ROTULO_Y2)
    BASE = BASE.replace("_INTERVALO_X_", str(INTERVALO_X))
    BASE = BASE.replace("_SERIES_", SERIES)
    BASE = BASE.replace("nan", "0")
    BASE = BASE.replace("_AGORA_", ATUAL)
    #SALVA ARQUIVO NA PASTA
    if os.path.isdir(".\\GRAFICOS_CANVAS"):
        print("PASTA GRAFICOS_CANVAS EXISTE")
    else:
        print("PASTA GRAFICOS_CANVAS NÃO EXISTE")
        os.mkdir('.\\GRAFICOS_CANVAS')
    ESCREVER_ARQUIVO('GRAFICOS_CANVAS\\graf_'+ARQUIVO_SAIDA,BASE)
    MSG('GRÁFICO GERADO: ' + TITULO,'AMARELO')
    MSG(df, 'AMARELO')
    # JS PARA EMBEDAR
    GRAFICO_EMBEDAR_JS = BUSCA_TEXTO_ENTRE_CARACTERES(BASE,'//INICIO_JS_GRAFICO','//FIM_JS_GRAFICO')
    # DIV PARA EMBEDAR
    GRAFICO_EMBEDAR_DIV = BUSCA_TEXTO_ENTRE_CARACTERES(BASE, '<!--INICIO_DIV_EMBEDAR-->', '<!--FINAL_DIV_EMBEDAR-->')
    return GRAFICO_EMBEDAR_JS, GRAFICO_EMBEDAR_DIV


def GRAF_CANVASJS(df,l_X,l_Y,l_EIXO,l_LABEL,l_COR,l_TIPO,ROTULO_X,ROTULO_Y1,ROTULO_Y2,ARQUIVO_SAIDA,EXPLICACAO,TITULO,INTERVALO_X):
    ATUAL = datetime.now().strftime('%d/%m/%Y %H:%M')
    BASE = LER_ARQUIVO('RAFAEL\\CANVASJS\\G_BASE_RELATORIO_v1.html',0)
    SERIES = ''
    for X, Y, EIXO, COR, TIPO in zip(l_X, l_Y, l_EIXO, l_COR, l_TIPO):
        DADOS = ''
        for vX, vY, LABEL in zip(list(X), list(Y), l_LABEL):
            DADOS = DADOS + '   { x: ' + str(vX) + ', y: ' + str(vY) + ' , label: "' + str(LABEL) + '" , color: "' + str(COR) + '" },\n'
        SERIE = '\n{\nmarkerType: "circle",\ntype: "' + TIPO + '",\nshowInLegend: true,\nlegendText: "' + Y.name + '",\ncolor: "' + str(COR) + '",\nindexLabel: "{}",\nindexLabelFontSize: 12,\naxisYType: "' + EIXO + '",\ndataPoints: [\n' + DADOS + '\n]\n},\n\n'
        SERIES = SERIES + SERIE
    BASE = BASE.replace("ID_GRAFICO", TITULO.replace(' ','_'))
    BASE = BASE.replace("_TITULO_", TITULO)
    BASE = BASE.replace("_EXPLICACAO_", EXPLICACAO)
    BASE = BASE.replace("_EIXO_X_", ROTULO_X)
    BASE = BASE.replace("_EIXO_Y1_", ROTULO_Y1)
    BASE = BASE.replace("_EIXO_Y2_", ROTULO_Y2)
    BASE = BASE.replace("_INTERVALO_X_", str(INTERVALO_X))
    BASE = BASE.replace("_SERIES_", SERIES)
    BASE = BASE.replace("nan", "0")
    BASE = BASE.replace("_AGORA_", ATUAL)
    ESCREVER_ARQUIVO('graf_'+ARQUIVO_SAIDA,BASE)
    MSG('GRÁFICO GERADO: ' + TITULO,'AMARELO')
    MSG(df, 'AMARELO')
    # JS PARA EMBEDAR
    GRAFICO_EMBEDAR_JS = BUSCA_TEXTO_ENTRE_CARACTERES(BASE,'//INICIO_JS_GRAFICO','//FIM_JS_GRAFICO')
    # DIV PARA EMBEDAR
    GRAFICO_EMBEDAR_DIV = BUSCA_TEXTO_ENTRE_CARACTERES(BASE, '<!--INICIO_DIV_EMBEDAR-->', '<!--FINAL_DIV_EMBEDAR-->')
    return GRAFICO_EMBEDAR_JS, GRAFICO_EMBEDAR_DIV


def GRAF_CANVASJS_BUBBLE(ARQUIVO_BASE,df,LEGENDA,X,Y,Z,EIXO,LABEL,COLOR,TIPO,ROTULO_X,ROTULO_Y1,ROTULO_Y2,ARQUIVO_SAIDA,EXPLICACAO,TITULO,SAVE,INTERVALO_X):

    ATUAL = datetime.now().strftime('%d/%m/%Y %H:%M')
    BASE = LER_ARQUIVO(ARQUIVO_BASE,0)
    MSG(df,'AMARELO')
    SERIE = '\n{\nmarkerType: "circle",fillOpacity: .3,\ntype: "_TIPO_",\nshowInLegend: true,\nlegendText: "_LEGENDA_",\ncolor: "_COR_",\nindexLabel: "{name}",\nindexLabelFontSize: 12,\naxisYType: "_EIXO_",\ndataPoints: [\n_DADOS_\n]\n},\n\n'
    SERIES = ''
    for i in range(0, len(Y)):
        LINHA = ''
        for index, row in df.iterrows():
            if X[i] == '':
                Xi = index
            else:
                Xi = row[X[i]]
            if Z[i] == '':
                Zi = 1
            else:
                Zi = row[Z[i]]
            if COLOR[i] == '':
                COLORi = '#ffffff'
            else:
                COLORi = row[COLOR[i]]

            if LABEL == '':
                LABELi = index
            else:
                LABELi = row[LABEL]

            LINHA = LINHA + '   { x: ' + str(Xi) + ', y: ' + str(row[Y[i]]) + ' , z: ' + str(row[Z[i]]) + ' , name: "' + str(LABELi) + '" , color: "' + str(COLORi) + '" },\n'

        NOVA_SERIE = SERIE.replace("_DADOS_", LINHA)
        NOVA_SERIE = NOVA_SERIE.replace("_TIPO_", TIPO[i])
        NOVA_SERIE = NOVA_SERIE.replace("_COR_", COLOR[i])
        NOVA_SERIE = NOVA_SERIE.replace("_LEGENDA_", LEGENDA[i])
        NOVA_SERIE = NOVA_SERIE.replace("_EIXO_", EIXO[i])
        SERIES = SERIES + NOVA_SERIE

    BASE = BASE.replace("_TITULO_", TITULO)
    BASE = BASE.replace("_EXPLICACAO_", EXPLICACAO)
    BASE = BASE.replace("_EIXO_X_", ROTULO_X)
    BASE = BASE.replace("_EIXO_Y1_", ROTULO_Y1)
    BASE = BASE.replace("_EIXO_Y2_", ROTULO_Y2)
    BASE = BASE.replace("_INTERVALO_X_", str(INTERVALO_X))
    BASE = BASE.replace("_SERIES_", SERIES)
    BASE = BASE.replace("nan", "0")
    if SAVE == 1:
        BASE = BASE.replace("_SALVAR_", "chart.exportChart({format: \"png\"});")
    else:
        BASE = BASE.replace("_SALVAR_", "")
    BASE = BASE.replace("_AGORA_", ATUAL)
    ESCREVER_ARQUIVO(ARQUIVO_SAIDA,BASE,'w')
    DELETA_ARQUIVO("C:\\Users\\" + getpass.getuser() + "\\Downloads\\" + TITULO + ".png")
    if SAVE == 1:
        ABRE_PAGINA_WEB(ARQUIVO_SAIDA,'',.25,2)
        SEGURA_APERTA('ctrl','w',.25)
    MSG('GRÁFICO GERADO: ' + TITULO,'AMARELO')
    MSG(df, 'AMARELO')


def ANALISE_MEDIAS_MOVEIS(df,Y,MOSTRAR):
    # Y = 'SOMA_PC'
    # MOSTRAR= 1
    import matplotlib.pyplot as plt
    CRIA_PASTA_AUXILIAR()
    DIRECOES = []
    COMBINACAO = []
    T = len(df[Y])
    def ANALISE_MEDIAS(df,C,L):
        df['CURTA'] = df[Y].rolling(window=C).mean()
        df['LONGA'] = df[Y].rolling(window=L).mean()
        df['HISTOGRAMA'] = df['CURTA']-df['LONGA']
        df['STD_LONGA_S'] = df['LONGA'] + df[Y].rolling(window=L).std()
        df['STD_LONGA_I'] = df['LONGA'] - df[Y].rolling(window=L).std()
        df.loc[df['CURTA'] > df['LONGA'], 'DIRECAO'] = 1
        df.loc[df['CURTA'] < df['LONGA'], 'DIRECAO'] = -1
        df.loc[df['CURTA'] == df['LONGA'], 'DIRECAO'] = 0
        df['ANTES'] = df[Y].shift(1)
        df.loc[df['ANTES'] > df[Y], 'REAL'] = -1
        df.loc[df['ANTES'] < df[Y], 'REAL'] = 1
        df.loc[df['ANTES'] == df[Y], 'REAL'] = 0
        df = ZERO_PARA_VAZIO(df)
        df['FIT'] = 0
        df.loc[df['DIRECAO'] == df['REAL'], 'FIT'] = 1
        ACERTOS = df['FIT'].sum()
        PERCENTUAL = round(df['FIT'].sum() / df['FIT'].count() * 100, 2)
        return df, ACERTOS, PERCENTUAL
    for i in range(2, int(T - 3)): #CURTA
        for j in range(i + 2, T): #LONGA
            N = i*j
            df, ACERTOS, PERCENTUAL = ANALISE_MEDIAS(df,i,j)
            COMBINACAO.append([i,j,ACERTOS,PERCENTUAL])
            DIRECOES.append(df['DIRECAO'].tail(1).values[0])
    FITTED = pd.DataFrame(COMBINACAO, columns=['CURTA','LONGA','ASSERTOS','PERCENTUAL'])
    FITTED = FITTED.sort_values(by=['PERCENTUAL'], ascending=False).reset_index(drop=True)
    CURTA = FITTED['CURTA'][0]
    LONGA = FITTED['LONGA'][0]
    df, ACERTOS, PERCENTUAL = ANALISE_MEDIAS(df,CURTA,LONGA)
    RESULTADO = df.tail(1)['DIRECAO'].values[0]
    if RESULTADO > 0:
        TXR = 'SUBIR'
    else:
        TXR = 'CAIR'
    UP = sum(1 for item in DIRECOES if item == (1))
    DOWN = sum(1 for item in DIRECOES if item == (-1))
    UP = round(UP / len(DIRECOES), 2)
    DOWN = round(DOWN / len(DIRECOES), 2)
    import numpy as np
    df.replace(0, np.nan, inplace=True)
    dfg = df[df['LONGA'].notna()].reset_index(drop=True)
    # GRAFICO ----------------------------------------------------------------------
    fig = plt.figure(facecolor='black')
    fig.suptitle('CRUZAMENTO DE MÉDIAS MÓVEIS ' + Y, color='#ffffff', fontsize=10)
    gs = fig.add_gridspec(2, hspace=0.1, height_ratios=[2,1])
    axs = gs.subplots(sharex=True, sharey=False)
    fig.set_figwidth(10)
    fig.set_figheight(6)
    plt.xticks(fontsize=10, rotation=90)
    axs[0].plot(dfg.index, dfg['CURTA'], ':', color='r', label='Média Curta ['+str(CURTA)+']')
    axs[0].plot(dfg.index, dfg['LONGA'], ':', color='b', label='Média Longa ['+str(LONGA)+']')
    axs[0].plot(dfg.index, dfg[Y], color='white', label=Y + ' ['+str(TXR)+' '+str(PERCENTUAL)+'%]')
    axs[0].plot(dfg.index, dfg['STD_LONGA_I'], '', color='g')
    axs[0].plot(dfg.index, dfg['STD_LONGA_S'], '', color='g')
    axs[0].fill_between(dfg.index, dfg['STD_LONGA_S'], dfg['STD_LONGA_I'], color='g', alpha=0.3)
    axs[0].legend(loc='upper left', fontsize=7.5)
    axs[1].bar(dfg.index, dfg['HISTOGRAMA'], color=(dfg['HISTOGRAMA'] > 0).map({True: 'b', False: 'r'}))
    for i in range(2):
        axs[i].grid(color='#696969', linestyle=':', linewidth=0.7)
        axs[i].set_facecolor('black')
    plt.gcf().savefig("ARQUIVOS_AUXILIARES/ANALISE_MEDIAS.png")
    if MOSTRAR == 0:
        plt.close()
    return int(CURTA), int(LONGA), float(UP),float(DOWN), float(RESULTADO), float(ACERTOS), float(PERCENTUAL), df

def ANALISE_INDICADOR_FINANCEIRO(DIAS,MOSTRAR,URL):
    import pandas as pd
    from datetime import datetime, timedelta
    # DIAS = 90
    # MOSTRAR = 1
    # URL ='https://br.investing.com/commodities/us-soybeans-historical-data?cid=964523' # SOJA
    # URL ='https://br.investing.com/commodities/live-cattle-historical-data?cid=964528' # BOI GORDO
    # URL ='https://br.investing.com/commodities/us-corn-historical-data?cid=964522'  # MILHO
    # URL ='https://br.investing.com/indices/bm-fbovespa-real-estate-ifix-historical-data'  # IFIX
    DRIVER = SL_ABRIR_URL(URL)
    DRIVER.find_element_by_id('onetrust-accept-btn-handler').click()
    DORME(10)
    #R.SL_ROLA_TODA_PAGINA(DRIVER)
    try:
        DRIVER.find_element_by_class_name('largeBannerCloser').click()
    except:
        None
    SL_INTERACAO(DRIVER,10,'ID','widgetFieldDateRange','')
    DRIVER.find_element_by_id('startDate').clear()
    INICIO = (HOJE()- timedelta(days=DIAS)).strftime('%d/%m/%Y')
    SL_INTERACAO(DRIVER,5,'ID','startDate',INICIO)
    SL_INTERACAO(DRIVER, 5, 'ID', 'applyBtn', '')
    DORME(10)
    TABELA = DRIVER.find_element_by_class_name('historicalTbl')
    TAB = pd.read_html(TABELA.get_attribute('outerHTML'))[0]
    df = TAB
    #df = df.head(PERIODOS).reset_index(drop=True)
    df = df.sort_index(ascending=False).reset_index(drop=True)
    df['Último'] = (df['Último']/100).astype(float)
    df['Abertura'] = (df['Abertura'] / 100).astype(float)
    df['Máxima'] = (df['Máxima'] / 100).astype(float)
    df['Mínima'] = (df['Mínima'] / 100).astype(float)
    CURTA, LONGA, UP,DOWN, RESULTADO, ACERTOS, PERCENTUAL, df = ANALISE_MEDIAS_MOVEIS(df,'Último',MOSTRAR)
    SL_FECHAR(DRIVER)
    return CURTA, LONGA, UP,DOWN, RESULTADO, ACERTOS, PERCENTUAL, df

def ENVIA_GRAFICO_POST(URL,NOME_ARQUIVO):
    # COMO NOME DO ARQUIVO ENVIAR O CAMINHO COMPLETO NO COMPUTADOR
    CONTEUDO = LER_ARQUIVO(NOME_ARQUIVO, 0)
    NOME = NOME_ARQUIVO.split('\\')
    myobj = {'NomeArquivo': NOME[-1],'Conteudo': CONTEUDO}
    x = requests.post(URL, data=myobj)
    MSG(x.text,'VERDE')

def ATUALIZA_ALEXA_POST_DASH(NOME_ARQUIVO_SERVIDOR,CONTEUDO, URL):
    # NÃO COLOCAR .txt NO FINAL DO NOME, ESCREVER APENAS O NOME
    # https://developer.amazon.com/alexa/console/ask
    # inhausmensagens@gmail.com
    # Inh@us2021
    CONTEUDO = CONTEUDO.replace('\n','')
    CONTEUDO = CONTEUDO.replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ')
    myobj = {'ArquivoAlexaServidor': NOME_ARQUIVO_SERVIDOR,'Conteudo': CONTEUDO.rstrip(), 'ALEXA': 1}
    x = requests.post(URL, data=myobj)
    MSG(CONTEUDO, 'VERDE')
    MSG(x.text,'VERDE')

def VERIFICA_ACAO_ANTERIOR(PERIODO,TEXTO):

    def MARCA(PERIODO):
        Q = AGORA()
        if PERIODO == "MINUTO":
            return '{}_{}_{}_{}_{}: '.format(Q.year, Q.month, Q.day, Q.hour,Q.minute)
        elif PERIODO == "HORA":
            return '{}_{}_{}_{}: '.format(Q.year, Q.month, Q.day,Q.hour)
        elif PERIODO == "DIA":
            return '{}_{}_{}: '.format(Q.year, Q.month,Q.day)
        elif PERIODO == "MES":
            return '{}_{}: '.format(Q.year, Q.month)
        elif PERIODO == "SEMANA":
            return '{}_{}: '.format(Q.year, Q.isocalendar()[1])
        elif PERIODO == "ANO":
            return '{}: '.format(Q.year)
        else:
            return ""
    TEXTO = MARCA(PERIODO)+TEXTO

    CRIA_PASTA_AUXILIAR()

    try:
        ARQUIVO = LER_ARQUIVO('ARQUIVOS_AUXILIARES/REGISTRO_ACAO.txt', 0)
    except:
        print('ARQUIVO REGISTRO_ACAO.txt NÃO EXISTE E SERÁ CRIADO')
        open('ARQUIVOS_AUXILIARES/REGISTRO_ACAO.txt', 'w+')
        ARQUIVO = LER_ARQUIVO('ARQUIVOS_AUXILIARES/REGISTRO_ACAO.txt', 0)

    EXISTE = ARQUIVO.find(TEXTO)
    if EXISTE < 0:
        ARQUIVO = open('ARQUIVOS_AUXILIARES/REGISTRO_ACAO.txt', 'a+').write('\n' + TEXTO)
    return EXISTE

#################################################################################################################################################
'''
CONJUNTO DE FUNÇÃO PARA APLICAÇÃO COM A BIBLIOTECA SELENIUM - NAVEGAÇÃO WEB USANDO GOOGLE CHROME
IMPORTANTE TER O ARQUIVO [RAFAEL\WEBDRIVE\chromedriver.exe] PRESENTE
https://chromedriver.chromium.org/downloads

http://pythonclub.com.br/selenium-parte-4.html
https://selenium-python.readthedocs.io/waits.html
'''

def SL_ABRIR_URL(URL):
    '''
        ESTÁ FUNÇÃO IRÁ RETORNAR O DRIVER QUE DEVERÁ SER USADA NO RESTANTE DO CÓDIGO OU SEJA, ELA DEVE SER CHAMADA ASSIM:
        DRIVER = SL_ABRIR_URL(URL)
    '''
    browser = webdriver.Chrome(executable_path=r"RAFAEL\WEBDRIVE\chromedriver.exe", options = webdriver.ChromeOptions())
    browser.maximize_window()
    browser.get(URL)
    MSG(URL + " ABERTA", "VERDE")
    time.sleep(5)
    return browser

def SL_INTERACAO(DRIVER,TEMPO,BUSCA_POR,REFERENCIA,TEXTO):
    '''
        DRIVER: DEVE CONTER O RETORNO DA FUNÇÃO SL_ABRIR_URL(URL)
        BUSCA POR: ID,CLASS_NAME,XPATH,NAME,TAG_NAME
        EXEMPLOS
        PARA BUSCAR BUTTON COM TEXTO DEFINIDO: R.SL_INTERACAO(DRIVER,10,'XPATH','//button[text()="Pessoas"]','')

        IDENTIFICA SPAN COM TEXTO
        DRIVER.find_element_by_xpath('//span[text()="Publicar"]').click()
    '''
    try:
        if TEXTO != '':
            if BUSCA_POR == 'ID':
                WebDriverWait(DRIVER, TEMPO).until(EC.element_to_be_clickable((By.ID, REFERENCIA))).send_keys(TEXTO)
            if BUSCA_POR == 'CLASS_NAME':
                WebDriverWait(DRIVER, TEMPO).until(EC.element_to_be_clickable((By.CLASS_NAME, REFERENCIA))).send_keys(TEXTO)
            if BUSCA_POR == 'XPATH':
                WebDriverWait(DRIVER, TEMPO).until(EC.element_to_be_clickable((By.XPATH, REFERENCIA))).send_keys(TEXTO)
            MSG('ESCRITO >>> ' + TEXTO + ' EM [' + BUSCA_POR + '] [' + REFERENCIA + ']','VERDE')

        if TEXTO == '':
            if BUSCA_POR == 'XPATH':
                WebDriverWait(DRIVER, TEMPO).until(EC.element_to_be_clickable((By.XPATH, REFERENCIA))).click()
            if BUSCA_POR == 'ID':
                WebDriverWait(DRIVER, TEMPO).until(EC.element_to_be_clickable((By.ID, REFERENCIA))).click()
            if BUSCA_POR == 'CLASS_NAME':
                WebDriverWait(DRIVER, TEMPO).until(EC.element_to_be_clickable((By.CLASS_NAME, REFERENCIA))).click()
            MSG('CLICADO EM [' + BUSCA_POR + '] [' + REFERENCIA + ']', 'VERDE')
        return 1
    except:
        MSG('ERRO AO INTERAGIR COM [' + BUSCA_POR + '] [' + REFERENCIA + ']', 'VERMELHO')
        return 0
    time.sleep(.25)

def SL_RIGHTCLICK(DRIVER,BUSCA_POR,REFERENCIA):
    if BUSCA_POR == 'XPATH':
        ELEMENTO = WebDriverWait(DRIVER, 50).until(EC.element_to_be_clickable((By.XPATH, REFERENCIA)))
    if BUSCA_POR == 'ID':
        ELEMENTO = WebDriverWait(DRIVER, 50).until(EC.element_to_be_clickable((By.ID, REFERENCIA)))
    if BUSCA_POR == 'CLASS_NAME':
        ELEMENTO = WebDriverWait(DRIVER, 50).until(EC.element_to_be_clickable((By.CLASS_NAME, REFERENCIA)))
    rightClick = ActionChains(DRIVER)
    rightClick.context_click(ELEMENTO).perform()
    time.sleep(.5)
    MSG('CLICK DIREITO EM [' + BUSCA_POR + '] [' + REFERENCIA + ']', 'VERDE')

def SL_NOVA_GUIA(DRIVER,BUSCA_POR,REFERENCIA):
    if BUSCA_POR == 'XPATH':
        ELEMENTO = WebDriverWait(DRIVER, 50).until(EC.element_to_be_clickable((By.XPATH, REFERENCIA)))
    if BUSCA_POR == 'ID':
        ELEMENTO = WebDriverWait(DRIVER, 50).until(EC.element_to_be_clickable((By.ID, REFERENCIA)))
    if BUSCA_POR == 'CLASS_NAME':
        ELEMENTO = WebDriverWait(DRIVER, 50).until(EC.element_to_be_clickable((By.CLASS_NAME, REFERENCIA)))
    ActionChains(DRIVER).key_down(Keys.CONTROL).click(ELEMENTO).key_up(Keys.CONTROL).perform()

def SL_CLICAR_EM_PALAVRA(DRIVER,PALAVRA):
    try:
        DRIVER.find_elements_by_xpath('//span[text()="'+PALAVRA+'"]')[0].click()
        DORME(2)
        return 1
    except:
        return 0

def SL_ROLA_TODA_PAGINA(DRIVER):
    for X in range(5):
        DRIVER.execute_script("window.scrollTo(0,1000000000000000)")
        DORME(.35)
    for X in range(10):
        DRIVER.execute_script("window.scrollTo(0,document.body.scrollHeight*(1/" + str(X) + "))")
        DORME(.35)
    DRIVER.execute_script("window.scrollTo(0,0)")

def SL_FECHAR(DRIVER):
    try:
        DRIVER.close()
        DRIVER.quit()
        MSG('CONEXÃO SELENIUM FECHADA', 'VERDE')
    except:
        return 0

# FIM BIBLIOTECAS SELENIUM
#################################################################################################################################################

#################################################################################################################################################
'''
CONJUNTO DE FUNÇÃO PARA APLICAÇÃO COM A BIBLIOTECA PANDAS PARA TRATAMENTO E ANÁLISE DE DADOS
'''

def ABRE_PKL_DF(URL):
    #https://towardsdatascience.com/the-best-format-to-save-pandas-data-414dca023e0d
    df = pd.read_pickle(URL)
    df = df.dropna(how='all')
    df = df.dropna(how='all', axis=1)
    MSG2(df, 'ABERTO ARQUIVO\n' + URL)
    return df

def ABRE_EXCEL_DF(ARQUIVO,PLANILHA):
    '''
        ABRE UMA PLANILHA EXCEL EM UM DATAFRAME
    '''
    print('>>> ABRINDO EXCEL')
    if PLANILHA != '':
        XLS = pd.read_excel(ARQUIVO, sheet_name=PLANILHA)
    else:
        XLS = pd.read_excel(ARQUIVO)
    df = pd.DataFrame(XLS)
    MSG2(df,'ABERTO ARQUIVO\n' + ARQUIVO + ' ' + PLANILHA)
    return df

def ABRE_CSV_DF(ARQUIVO,LINHAS):
    '''
        LINHAS = 0 > CARREGA TODAS AS LINHAS
        ABRE UM ARQUIVO CSV UM DATAFRAME
        ARGUMENTOS:
            nrows=10 > SELECIONA AS 'X' PRIMEIRAS LINHAS
            skiprows=5 > PULA AS 'X' PRIMEIRAS LINHAS PODE SER UMA MATRIZ
    '''
    print('>>> LENDO CSV ' + ARQUIVO)
    if ARQUIVO.find('.csv') != -1:
        SEPARADOR = ';'
    if ARQUIVO.find('.txt') != -1:
        SEPARADOR = ';'
    if LINHAS == 0:
        df = pd.read_csv(ARQUIVO,sep=SEPARADOR, encoding = 'utf-8', engine='python')
    else:
        df = pd.read_csv(ARQUIVO, nrows=LINHAS,sep=SEPARADOR, encoding = 'utf-8', engine='python')
    MSG2(df,'ARQUIVO CSV ABERTO '+ARQUIVO+'.....')
    return df


def SQLITE(df,QUERY):
    '''
        EXECUTA UMA CONSULTA SQL NO DATAFRAME
        NO SCRIPT SQL, SEMPRE APÓS [FROM] DEVE VIR [df], POIS É O NOME DA VARIÁVEL DA FUNÇÃO
    '''
    df = ps.sqldf(QUERY, locals())
    df = df.reset_index(drop=True)
    df_COR = df.corr(method='pearson')
    MSG2(df, QUERY + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< SQLITE')
    STAT = df.describe()
    MSG2(STAT, 'ESTATÍSTICA DESCRITIVA')
    MSG2(df_COR, 'CORRELAÇÕES')
    df.info()
    #df = df.fillna(0)
    return df

def FORMATA_DATA_HORA_DF(df,CAMPO):
    # FORMATA A DATA E ADICIONA UMA COLUNA PERIODO COM AAAA-MM
    # FORMATO = "%Y-%m-%d %H:%M"
    #df[CAMPO] = df[CAMPO].dt.strftime(FORMATO)
    df = df.reset_index(drop = True)
    NOVA_COLUNA = (CAMPO+'_2').replace(' ','_')
    df[NOVA_COLUNA] = pd.to_datetime(df[CAMPO], dayfirst=True)

    df['PERIODO'] = pd.to_datetime(df[NOVA_COLUNA],format='%m%Y', errors='coerce').dt.to_period('m')
    df['DIA_SEMANA'] = df[NOVA_COLUNA].dt.day_name()
    df['SEMANA_DO_ANO'] = df[NOVA_COLUNA].dt.strftime('%Y-%U')
    df['DIA_DO_MES'] = df[NOVA_COLUNA].dt.day
    df['MES_E_DIA'] = df[NOVA_COLUNA].dt.strftime('%m/%d')
    df['HORA'] = df[NOVA_COLUNA].dt.strftime('%H')
    df.sort_values(by=['PERIODO', 'MES_E_DIA','HORA'])
    df = df.reset_index(drop=True)
    MSG2(df, 'CAMPO DE DATA AJUSTADO ' + CAMPO)
    return df

def AGRUPA_POR_PERIODO_DE_UMA_DATA(df,CAMPO_DATA):
    #FORMATA A DATA E JÁ AGRUPA COM A SOMA DE PERIODO [ANO_MES] DE UMA COLUNA DATA INFORMADA

    df1 = FORMATA_DATA_HORA_DF(df,CAMPO_DATA)
    df1S = SOMA_DF_GROUP(df1, ['PERIODO'])
    df1C = CONTA_DF_GROUP(df1, ['PERIODO'])
    df1C = df1C[['PERIODO','CONTA_DIA_MES']]
    df3 = MERGE_COMBINAR_DFS(df1C,df1S,['PERIODO'],['PERIODO'],'outer')

    MSG2(df3,'CAMPO '+CAMPO_DATA+' AGRUPADO EM PERIODO')
    return(df3)

def INTERVALO_EM_SEGUNDOS(df,COLUNA_DATA_HORA):
    # INSERE UMA COLUNA COM O INTERVALO EM SEGUNDOS COM BASE EM UMA COLUNA DATAHORA EXISTENTE ATÉ AGORA
    df = FORMATA_DATA_HORA_DF(df, COLUNA_DATA_HORA, '%Y-%m-%d %H:%M:%S')
    df['AGORA'] = AGORA()
    df['MINUTOS'] = df['AGORA'] - df[COLUNA_DATA_HORA]
    df['MINUTOS'] = df['MINUTOS'].dt.seconds / 60
    MSG(df,'CYAN')
    return df

def UNIAO_DFS(LISTA_DFS):
    df = pd.concat(LISTA_DFS)
    MSG(df, 'AZUL')
    df.info()
    return df

def UNIAO_ARQUIVOS_EM_UM_MESMO_DF(PASTA,ARQUIVO_SAIDA,GUIA_EXCEL):
    # OS ARQUIVOS PRECISAM ESTAR SOZINHOS NA MESMA PASTA
    df = pd.DataFrame()
    dfq = pd.DataFrame()
    AQVS = ''
    n = 1
    print('>>> ABRINDO OS ARQUIVOS DA PASTA ' + PASTA)
    for diretorio, subpastas, arquivos in os.walk(PASTA):
        for arquivo in arquivos:
            ARQ = os.path.join(diretorio, arquivo)
            k = str(n).zfill(3)
            if ARQ.find('.xlsx') != -1 or ARQ.find('.xls') != -1:
                LINHAS = pd.read_excel(ARQ)
            if ARQ.find('.csv') != -1 or ARQ.find('.txt') != -1:
                LINHAS = ABRE_CSV_DF(ARQ,0)
            LINHAS = LINHAS.dropna(how='all')

            #ARQUIVO DE QUALIFICACAO
            NOME = ARQ.replace(diretorio,'').replace('\\','')
            N_LINHAS = len(LINHAS.index)
            TAMANHO = os.path.getsize(ARQ)/1024
            print('>>> ('+ k +') ' +NOME, N_LINHAS, round(TAMANHO,0))
            dfq = dfq.append([[NOME,N_LINHAS,round(TAMANHO,0)]])
            LINHAS['ARQUIVO_ORIGEM'] = NOME
            LINHAS = LINHAS.rename(columns=lambda x: x.strip())
            df = pd.concat([df,LINHAS],ignore_index=True)
            n = n + 1
    df = df.dropna(how='all')
    df = df.reset_index(drop=True)
    dfq = dfq.rename(columns={0: 'ARQUIVO', 1: 'LINHAS', 2: 'TAMANHO'})
    if GUIA_EXCEL != '':
        print('>>> SALVANDO DADOS NO ARQUIVO XLS > ' + ARQUIVO_SAIDA)
        SALVA_DF_EXCEL(df, ARQUIVO_SAIDA + '.xlsx', GUIA_EXCEL)
    print('>>> SALVANDO DADOS NO ARQUIVO PKL > ' + ARQUIVO_SAIDA + '.pkl')
    SALVA_DF_EXCEL(dfq, ARQUIVO_SAIDA + '_EXTRATO_', 'ARQUIVOS')#SALVA ARQUIVO DE QUALIFICACAO
    SALVA_DF_FORMATO_PANDAS(df, ARQUIVO_SAIDA)
    print('ARQUIVOS UNIDOS................')
    return df


def JOIN(df1,df2,CAMPO):
    dfR = df1.join(df2.set_index(CAMPO), on=CAMPO)
    dfR = dfR.drop_duplicates()
    MSG('JOIN PELO CAMPO ' + str(CAMPO), 'AZUL')
    MSG(dfR, 'MAGENTA')
    return dfR

def CONCATENAR_DFS(DFS,EIXO):
    # EIXO 0 - LINHA
    # EIXO 1 - COLUNA
    df = pd.concat(DFS, axis = EIXO,ignore_index=True)
    MSG(df, 'MAGENTA')
    return df

def ORDENAR(df,LISTA_COLUNAS,CRESCENTE):
    # CRESCENTE: True / False: (True,False,...)
    df = df.sort_values(by=LISTA_COLUNAS, ascending=CRESCENTE).reset_index(drop=True)
    MSG('ORDENADO PELA COLUNA ' + LISTA_COLUNAS, 'VERDE_CLARO')
    MSG(df.head(),'VERDE_CLARO')
    return df

def TRATA_VAZIOS(df):
    df = df.dropna(how='all')
    df = df.dropna(how='all', axis=1)
    df = df.reset_index(drop=True)
    MSG2(df, 'VAZIOS TRATADOS')
    return df

def FILTRA_LINHA(df,COLUNA,LISTA_CONDICAO):
    df = df[df[COLUNA].isin(LISTA_CONDICAO)]
    MSG(df, 'MAGENTA')
    return df

def FILTRA_COLUNA(df,NOME_COLUNA):
    df = df.filter(like=NOME_COLUNA, axis=1)
    MSG(df,'MAGENTA')
    return df

def VALORES_UNICOS(df,COLUNA):
    U = pd.unique(df[COLUNA])
    MSG(U,'VERMELHO')

def ALGUMAS_COLUNAS_EM_LINHAS(df,LISTA_COLUNAS_MANTER,NOME_NOVA_CATEGORIA,NOME_VALORES):
    df = (df.set_index(LISTA_COLUNAS_MANTER).stack().reset_index(name=NOME_VALORES).rename(columns={'level_2': NOME_NOVA_CATEGORIA}))
    MSG(df, 'CYAN')
    return df

def MERGE_COMBINAR_DFS(df1,df2,LISTA_COLUNAS_DF1,LISTA_COLUNAS_DF2,HOW):
    # AS LISTAS DE COLUNAS SÃO AS COLUNAS QUE SERÃO BUSCADAS PARA FAZER A COMBINAÇÃO
    # FUNCIONA COMO UM PROCV DE VÁRIOS NÍVEIS
    # https://medium.com/data-hackers/pandas-combinando-data-frames-com-merge-e-concat-10e7d07ca5ec
    # HOW : inner - Caso queiramos a interseção exata entre as tabelas
    # HOW : outer - Caso queiramos todas as informações, de ambas tabelas
    # HOW : left - Um merge “left” ou “right” depende de qual tabela vocâ deixa na direita ou esquerda
    # HOW : right -Um merge “left” ou “right” depende de qual tabela vocâ deixa na direita ou esquerda
    new_df = pd.merge(df1, df2, how=HOW, left_on=LISTA_COLUNAS_DF1, right_on=LISTA_COLUNAS_DF2)
    new_df = new_df.reset_index(drop=True)
    MSG('MERGE ------------------------------------------------------------', 'CYAN')
    MSG(new_df, 'CYAN')
    return new_df

def CONCATENA_LINHAS(df,COLUNA,LISTA_COL_FILTROS):
    # CONCATENA E JUNTA CÉLULAS DE UMA COLUNA COM BASE EM FILTROS (COMBINAÇÕES) LISTADOS NAS COLUNAS
    df[COLUNA] = df.groupby(LISTA_COL_FILTROS)[COLUNA].transform(lambda x: ' '.join(x.astype(str))).str.replace('\n','')
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    MSG('CONCATENAÇÃO DE LINHAS ------------------------------------------------------------', 'CYAN')
    MSG(df, 'CYAN')
    return df

def PADRONIZA_TEXTO_COLUNA_COM_VALORES_DIFERENTES(df,CAMPO_CHAVE,CAMPO_A_PADRONIZAR):
    # USAR QUANDO EM UMA MESMA COLUNA EXISTEM DESCRIÇÕES DIFERENTES PARA UM MESMO REGISTRO
    # ESSA FUNÇÃO USA OUTRA COLUNA CHAVE COMO PARAMETRO E RETORNA UMA COLUNA COM APENAS UM DOS REGISTROS DIFERENTES PARA A COLUNA
    df = SQLITE(df,'SELECT *,(SELECT '+CAMPO_A_PADRONIZAR+' FROM df T1 WHERE T1.'+CAMPO_CHAVE+' = T0.'+CAMPO_CHAVE+' LIMIT 1) "CAMPO_TEMPORARIO" FROM df T0')
    del df[CAMPO_A_PADRONIZAR]
    df = RENOMEAR_COLUNA(df,'CAMPO_TEMPORARIO',CAMPO_A_PADRONIZAR)
    MSG2(df,'COLUNA '+CAMPO_A_PADRONIZAR+' PADRINIZADA')
    return df

def VALOR_DA_CELULA(df,NOME_COLUNA,INDICE_LINHA):
    VALOR = df[NOME_COLUNA].values[INDICE_LINHA]
    MSG('VALOR DA CELULA ' + NOME_COLUNA + '\n' + str(VALOR),'CYAN')
    return VALOR

def CONVERTE_PARA_NUMERO(df, COLUNAS):
    for COLUNA in COLUNAS:
        try:
            df[COLUNA] = df[COLUNA].astype(str)
            df[COLUNA] = df[COLUNA].str.strip()
            df[COLUNA] = df[COLUNA].str.replace('R$', '', regex=False)
            df[COLUNA] = df[COLUNA].str.replace('%', '', regex=False)
            df[COLUNA] = df[COLUNA].str.replace(' ', '', regex=False)
            df[COLUNA] = df[COLUNA].str.replace(',', '.', regex=False)
            df[COLUNA] = df[COLUNA].str.replace(r'\.(?=.*?\.)', '', regex=True)
            df[COLUNA] = pd.to_numeric(df[COLUNA], errors='coerce')
        except:
            print('ERRO EM CONVERTER COLUNA ',COLUNA)
            continue
    return df



def MEDIA_DF_GROUP(df,COLUNA):
    df = df.groupby(COLUNA).mean()
    df = df.add_prefix('MEDIA_')
    df = df.reset_index(drop=False)
    MSG(df.head(), 'CYAN')
    return df

def SOMA_DF_GROUP(df,LISTA_COLUNAS):
    df = df.groupby(LISTA_COLUNAS).sum()
    df = df.add_prefix('SOMA_')
    df = df.reset_index(drop=False)
    MSG(df.head(), 'CYAN')
    return df



def SOMA_CULULATIVA_CONDICIONAL(df,COLUNA):
    df2 = df.groupby(COLUNA).cumsum()
    df2 = df2.add_prefix('ACUM_SOMA_')
    df3 = df.join(df2)
    df3 = df3.reset_index(drop=False)
    MSG(df3.head(), 'CYAN')
    return df3

def DESVIO_DF_GROUP(df,COLUNA):
    df = df.groupby(COLUNA).std()
    df = df.add_prefix('DESVIO_')
    df = df.reset_index(drop=False)
    MSG(df.head(), 'CYAN')
    return df

def CONTA_DF_GROUP(df,COLUNA):
    df = df.groupby(COLUNA).count()
    df = df.add_prefix('CONTA_')
    df = df.reset_index(drop=False)
    MSG2(df, 'CONTAGEM ' + COLUNA[0])
    return df


def ESTATISTICA_DESCRITIVA(df,COLUNA):
    dfx = df.groupby(COLUNA).count()
    df1 = dfx.add_prefix('CONTAGEM_')
    dfx = df.groupby(COLUNA).mean()
    df2 = dfx.add_prefix('MEDIA_')
    dfx = df.groupby(COLUNA).median()
    df3 = dfx.add_prefix('MEDIANA_')
    dfx = df.groupby(COLUNA).std()
    df4 = dfx.add_prefix('DESPAD_')
    dfx = df.groupby(COLUNA).sum()
    df5 = dfx.add_prefix('SOMA_')
    df = CONCATENAR_DFS([df1, df2, df3, df4, df5], 1)
    df = df.sort_values(by=[COLUNA])
    df.reset_index(drop=True)
    MSG('ESTATISTICA DESCRITIVA POR ' + str(COLUNA), 'CINZA_CLARO')
    MSG(df, 'CINZA_CLARO')
    MSG(list(df.columns), 'CINZA_CLARO')
    SALVA_DF_EXCEL(df, 'ESTATISTICA_DESCRITIVA_'+COLUNA, 'ESTATISTICA')
    df=SQLITE(df,'SELECT * FROM df')
    df = df.reset_index(drop=False)
    return df


def ESTATISTICA_DESCRITIVA_UNICA(df,COLUNA_CHAVE,COLUNA_NUMERICA):
    ESTAT = df.groupby([COLUNA_CHAVE])[COLUNA_NUMERICA].count()
    ESTAT = ESTAT.reset_index(drop=False)
    ESTAT.columns = [COLUNA_CHAVE, 'CONTA']
    CONT = ESTAT

    ESTAT = df.groupby([COLUNA_CHAVE])[COLUNA_NUMERICA].sum()
    ESTAT = ESTAT.reset_index(drop=False)
    ESTAT.columns = [COLUNA_CHAVE, 'SOMA']
    SOMA = ESTAT

    DESCRITIVA = MERGE_COMBINAR_DFS(CONT, SOMA, [COLUNA_CHAVE], [COLUNA_CHAVE], 'outer')

    ESTAT = df.groupby([COLUNA_CHAVE])[COLUNA_NUMERICA].mean()
    ESTAT = ESTAT.reset_index(drop=False)
    ESTAT.columns = [COLUNA_CHAVE, 'MEDIA']
    MEDIA = ESTAT

    DESCRITIVA = MERGE_COMBINAR_DFS(DESCRITIVA, MEDIA, [COLUNA_CHAVE], [COLUNA_CHAVE], 'outer')

    ESTAT = df.groupby([COLUNA_CHAVE])[COLUNA_NUMERICA].std()
    ESTAT = ESTAT.reset_index(drop=False)
    ESTAT.columns = [COLUNA_CHAVE, 'DESVIO']
    DESVIO = ESTAT

    DESCRITIVA = MERGE_COMBINAR_DFS(DESCRITIVA, DESVIO, [COLUNA_CHAVE], [COLUNA_CHAVE], 'outer')

    ESTAT = df.groupby([COLUNA_CHAVE])[COLUNA_NUMERICA].min()
    ESTAT = ESTAT.reset_index(drop=False)
    ESTAT.columns = [COLUNA_CHAVE, 'MIN']
    MINIMO = ESTAT

    DESCRITIVA = MERGE_COMBINAR_DFS(DESCRITIVA, MINIMO, [COLUNA_CHAVE], [COLUNA_CHAVE], 'outer')

    ESTAT = df.groupby([COLUNA_CHAVE])[COLUNA_NUMERICA].max()
    ESTAT = ESTAT.reset_index(drop=False)
    ESTAT.columns = [COLUNA_CHAVE, 'MAX']
    MAXIMO = ESTAT

    DESCRITIVA = MERGE_COMBINAR_DFS(DESCRITIVA, MAXIMO, [COLUNA_CHAVE], [COLUNA_CHAVE], 'outer')
    DESCRITIVA = ZSCORE(DESCRITIVA, 'CONTA')
    DESCRITIVA = ZSCORE(DESCRITIVA, 'SOMA')
    DESCRITIVA = ZSCORE(DESCRITIVA, 'MEDIA')
    DESCRITIVA = ZSCORE(DESCRITIVA, 'DESVIO')
    DESCRITIVA = ZSCORE(DESCRITIVA, 'MIN')
    DESCRITIVA = ZSCORE(DESCRITIVA, 'MAX')

    #COLUNA COR PARA GRAFICOS
    DESCRITIVA['COR'] = PALETA(0)
    DESCRITIVA.loc[(DESCRITIVA['OUTLIER_CONTA'] == 1),'COR'] = PALETA(4)
    DESCRITIVA.loc[(DESCRITIVA['OUTLIER_SOMA'] == 1),'COR'] = PALETA(4)
    DESCRITIVA.loc[(DESCRITIVA['OUTLIER_MEDIA'] == 1), 'COR'] = PALETA(4)
    DESCRITIVA.loc[(DESCRITIVA['OUTLIER_DESVIO'] == 1), 'COR'] = PALETA(4)
    DESCRITIVA.loc[(DESCRITIVA['OUTLIER_MIN'] == 1), 'COR'] = PALETA(4)
    DESCRITIVA.loc[(DESCRITIVA['OUTLIER_MAX'] == 1), 'COR'] = PALETA(4)



    DESCRITIVA = DESCRITIVA.sort_values(by=['SOMA'], ascending=False).reset_index(drop=True)

    DESCRITIVA = DESCRITIVA.reset_index(drop=True)

    if os.path.isdir(".\\ESTATISTICAS_DESCRITIVAS"):
        print("PASTA ESTATISTICAS_DESCRITIVAS EXISTE")
    else:
        print("PASTA ESTATISTICAS_DESCRITIVAS NÃO EXISTE")
        os.mkdir('.\\ESTATISTICAS_DESCRITIVAS')

    SALVA_DF_EXCEL(DESCRITIVA,'ESTATISTICAS_DESCRITIVAS\\stat_'+COLUNA_CHAVE+'_x_'+COLUNA_NUMERICA,'ESTATISTICA')
    return DESCRITIVA

def HISTORICO_CRIA_E_ATUALIZA(df,ARQUIVO_XLS):
    '''
        ESTA FUNÇÃO SERVE PARA SALVAR UM ARQUIVO LOCAL HISTÓRICO PARA SER USADO POSTERIORMENTE EM ALGUMA ANÁLISE EXCLUSIVA
    '''
    try:
        HISTORICO = ABRE_EXCEL_DF(ARQUIVO_XLS, 'HISTORICO')
        df['QUANDO'] = AGORA()
        HISTORICO = UNIAO_DFS([df,HISTORICO])
    except:
        df['QUANDO'] = AGORA()
        HISTORICO = df
        MSG('NÃO ENCONTROU O ARQUIVO HISTÓRICO','VERMELHO')
    SALVA_DF_EXCEL(HISTORICO, ARQUIVO_XLS, 'HISTORICO')
    MSG('HISTÓRICO SALVO EM ['+ARQUIVO_XLS+']', 'VERDE')
    return HISTORICO


def CORRELACAO(df,COL_INDEX,COLUNAS):
    # FORMA UM MAPA DE CALOR COM VARIÁVEIS NUMÉRICAS OU CATEGÓRICAS
    # QUALITATIVA: TESTE QUI-QUADRADO
    # QUANTITATIVA: PEARSON
    # PREESCHER AS VARIÁVEIS PARA ANÁLISE DE VARIÁVEIS CATEGÓRICAS
    if COL_INDEX is None: #QUANTITATIVA
        df_COR=df.corr(method='pearson')
        plt.figure(figsize=(12, 6))
        sns.set(font_scale=0.75)
        sns.heatmap(df_COR, annot=True, fmt=".1%")
        MSG('CORRELAÇÃO COMPLETA','MAGENTA')
        plt.figure(figsize=(12, 6))
        sns.set(font_scale=0.75)
        sns.heatmap(df_COR, annot=True, fmt=".1%")
        #plt.show()
        plt.gcf().savefig('ANALISE_CORRELACAO_NUMERICA.png')
    else:#QUALITATIVA

        # MULTIPLA
        # CHAMAR ASSIM => R.CORRELACAO(df,[df['NPS'],df['MES']],df['SLA'])
        # https://medium.com/@yangdustin5/quick-guide-to-pandas-pivot-table-crosstab-40798b33e367
        # df_COR = pd.crosstab(df[COL_INDEX], df[COLUNAS])
        df_COR = pd.crosstab(index=COL_INDEX, columns=COLUNAS, margins=True)
        # df_COR = pd.crosstab(df[VAR1], df[VAR1], normalize='index')
        c, p, dof, expected = chi2_contingency(df_COR)
        MSG(df_COR, 'MAGENTA')
        MSG('chi2: The test statistic: '+str(c)+' p: The p-value of the test: '+str(p)+' dof: Degrees of freedom: '+str(dof), 'MAGENTA')
        plt.figure(figsize=(12, 6))
        sns.set(font_scale=0.75)
        sns.heatmap(df_COR, cmap='rocket_r', annot=True, fmt='g')
        plt.gcf().savefig('ANALISE_CORRELACAO_CATEGORICA__.png')
        #plt.show()
    plt.close()


def HEATMAP_HTML(MATRIX_CORRELACAO):
    import plotly.express as px
    import plotly
    #df = px.data.medals_wide(indexed=True)
    fig = px.imshow(MATRIX_CORRELACAO)
    #px.offline.plot(fig, filename='name.html')
    plotly.offline.plot(fig, filename='MAPA_DE_CALOR.html', auto_open=False)
    fig.show()

def TESTA_NUMERO(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def MAPA_CALOR_HTML_CATEGORICO(df,COL1,COL2,COR):
    # MAPA DE CALOR NORMAL SIMILAR A UMA TABELA DINAMICA DO EXEL
    # CONSIDERAR APENAS VARIÁVEIS QUALITATIVAS
    tab_contingencia = pd.crosstab(df[COL1], df[COL2])
    stat, p, dof, expected = chi2_contingency(tab_contingencia)
    TC = tab_contingencia
    DADOS = TC.values.tolist()
    MAIOR = np.max(DADOS)
    MENOR = np.min(DADOS)
    HMP = tab_contingencia.to_html()
    HMP = HMP.splitlines()  # or use .split("\n") to do it manually
    NW_HMP=''
    for linha in HMP:
        VLR = BUSCA_TEXTO_ENTRE_CARACTERES(linha,'<td>','</td>')
        if VLR.isnumeric() == True:
            VLR = float(VLR)
            ALPHA = int(round((VLR - MENOR)*100 / (MAIOR - MENOR),0))
            if ALPHA == 100:
                ALPHA = ''
            linha = linha.replace('<td>','<td style="background-color: '+str(COR)+str(ALPHA)+';">')
        NW_HMP = NW_HMP + linha + '\n'
    NW_HMP = '<div style="text-align: -webkit-center;padding: 20px;">\n' + NW_HMP
    NW_HMP = '<style> 	.dataframe{ 		font-family: arial; 		font-size: 12px; 	} 	.dataframe th{ 		text-align: left; padding: 5px; 	} 	.dataframe td{ 		text-align: center; 	} 	.dataframe thead th{ 		font-size: 9px; 	}		 </style> \n' + NW_HMP
    NW_HMP = NW_HMP + '\n</div>'
    NW_HMP = NW_HMP.replace('border="1"','border="0"')
    NW_HMP = NW_HMP.replace('dataframe', 'ID_'+str(COL1.replace(' ','_'))+'_'+str(COL2.replace(' ','_')))
    ESCREVER_ARQUIVO('hmp.html',NW_HMP)
    return NW_HMP

def ANALISE_DE_CORRESPONDENCIA(df,LISTA_COLUNAS):
    # https://napsterinblue.github.io/notes/stats/techniques/mca/
    # https://pypi.org/project/mca/
    # https://codefying.com/2018/12/21/introduction-to-correspondence-analysis/
    # https://towardsdatascience.com/5-must-know-dimensionality-reduction-techniques-via-prince-e6ffb27e55d1
    # MAPA PERCEPTUAL
    # ANALISE DE CORRESPONDENCIA

    dfo = df
    df = df[LISTA_COLUNAS]
    mca = prince.MCA()
    mca = mca.fit(df)

    mca_COORD = mca.transform(df) #TABELA DE CONTINGÊNCIA
    tab_contingencia = pd.crosstab(df[LISTA_COLUNAS[0]], df[LISTA_COLUNAS[1]])

    MSG('TABELA DE CONTINGÊNCIAS', 'AMARELO')
    MSG(tab_contingencia, 'AMARELO')
    stat, p, dof, expected = chi2_contingency(tab_contingencia)
    print('dof=%d' % dof)
    df_expected = pd.DataFrame(expected)
    df_expected.columns = tab_contingencia.columns
    df_expected.index = tab_contingencia.index
    MATRIX_CORRELACAO = df_expected
    MSG(MATRIX_CORRELACAO, 'AMARELO')
    prob = 0.95
    critical = chi2.ppf(prob, dof)
    print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
    if abs(stat) >= critical:
        print('Dependent (reject H0)')
    else:
        print('Independent (fail to reject H0)')
    # interpret p-value
    alpha = 1.0 - prob
    print('significance=%.3f, p=%.3f' % (alpha, p))
    if p <= alpha:
        print('Dependent (reject H0)')
    else:
        print('Independent (fail to reject H0)')
    #HEATMAP

    ID_HEATMAP = str(random()).replace('0.','ID_')
    MAIOR = np.max(expected)
    MENOR = np.min(expected)
    HMP = MATRIX_CORRELACAO.to_html()
    HMP = HMP.splitlines()  # or use .split("\n") to do it manually
    NW_HMP=''
    for linha in HMP:
        VLR = BUSCA_TEXTO_ENTRE_CARACTERES(linha,'<td>','</td>')
        if TESTA_NUMERO(VLR) == True:
            VLR = float(VLR)
            ALPHA = round((VLR - MENOR) / (MAIOR - MENOR),2)
            linha = linha.replace('<td>','<td style="background-color: rgba(255, 0, 0, '+str(ALPHA)+');">')
        NW_HMP = NW_HMP + linha + '\n'

    NW_HMP = '<div style="text-align: -webkit-center;padding: 20px;">\n' + NW_HMP
    NW_HMP = '<style> 	.dataframe{ 		font-family: arial; 		font-size: 11px; 	} 	.dataframe th{ 		text-align: left; 	} 	.dataframe td{ 		text-align: center; 	} 	.dataframe thead th{ 		font-size: 9px; 	}		 </style> \n' + NW_HMP
    NW_HMP = NW_HMP + '\n</div>'
    NW_HMP = NW_HMP.replace('border="1"','border="0"')
    NW_HMP = NW_HMP.replace('dataframe', ID_HEATMAP)
    ESCREVER_ARQUIVO('hmp.html',NW_HMP)
    HEAT_MAP_HTML = NW_HMP

    # MAPA PERCEPTUAL
    ax = mca.plot_coordinates(df, row_points_alpha=.2, figsize=(10, 10), show_column_labels=True, row_points_size=10, legend_n_cols=1)
    ax.get_figure().savefig('MCA_COORDENADAS.png')

    mca_COORD.columns = ['corresp_x','corresp_y']
    df = dfo.join(mca_COORD)
    MSG(df, 'AMARELO')
    SALVA_DF_EXCEL(df, 'DADOS\\Analise_Correspondencia.xlsx', 'DADOS')

    # MAPA PERCEPUTAL (ERRADO)
    M1 = MEDIA_DF_GROUP(df,LISTA_COLUNAS[0])
    M1 = M1[[LISTA_COLUNAS[0],'MEDIA_corresp_x','MEDIA_corresp_y']]
    M1.columns = ['LABEL','X','Y']
    M1['COR'] = '#0d6efd'
    M1['VAR'] = LISTA_COLUNAS[0]
    M2 = MEDIA_DF_GROUP(df, LISTA_COLUNAS[1])
    M2 = M2[[LISTA_COLUNAS[1], 'MEDIA_corresp_x', 'MEDIA_corresp_y']]
    M2.columns = ['LABEL', 'X', 'Y']
    M2['COR'] = '#ffc107'
    M2['VAR'] = LISTA_COLUNAS[1]
    MAPA_PERCEPTUAL = UNIAO_DFS([M1,M2])
    MSG('MAPA PERCEPTUAL', 'CYAN')
    MSG(MAPA_PERCEPTUAL,'CYAN')
    return MATRIX_CORRELACAO,MAPA_PERCEPTUAL,HEAT_MAP_HTML


def REGRESSAO_LINEAR(df,Y,LISTA_X,FORMULA):
    # https://www.statsmodels.org/stable/examples/notebooks/generated/ols.html
    # https://neylsoncrepalde.github.io/2018-02-25-regressao-linear-python/
    # https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLSResults.f_test.html
    # FORMULA: y~x1+x2+x3...
    import statsmodels.formula.api as sm
    #plt.hist(df['SOMA'], color='red', bins=15)
    #plt.title('Histograma da variável resposta')
    #plt.show()
    for Xs in LISTA_X:
        stat, p = shapiro(df[Xs])
        if p > 0.05:
            print('++++++++++ ' + Xs +' É NORMAL')
        else:
            print('---------- ' + Xs + ' NÃO É NORMAL')
    FORMULA = FORMULA.replace('=','~')
    reg = sm.ols(formula=FORMULA, data=df).fit()
    print(reg.summary())
    print('Parameters: ', reg.params)
    print('R2: ', reg.rsquared)
    print('Standard errors: ', reg.bse)
    print('F: ', reg.fvalue)
    INTERPRETACAO = ''
    INTERPRETACAO = INTERPRETACAO + 'O R2 ajustado nos dá uma medida de porcentagem da variância explicada pelo modelo' + '\n'
    INTERPRETACAO = INTERPRETACAO + 'O R2 não é uma medida de ajuste mas apenas nos diz o quanto de nossos dados esse modelo explica' + '\n'
    INTERPRETACAO = INTERPRETACAO + 'A estatística de teste F e seu p-valor < 0.001 basicamente nos mostram que esse modelo é estatisticamente válido' + '\n'
    INTERPRETACAO = INTERPRETACAO + 'O p-valor para todas os coeficientes estimados é menor que 0.001 o que mostra que eles são estatisticamente significativos' + '\n'
    MSG(INTERPRETACAO,'AZUL')
    # O R2 ajustado nos dá uma medida de porcentagem da variância explicada pelo modelo
    # O R2 não é uma medida de ajuste mas apenas nos diz o quanto de nossos dados esse modelo explica
    # A estatística de teste F e seu p-valor < 0.001 basicamente nos mostram que esse modelo é estatisticamente válido.
    # O p-valor para todas os coeficientes estimados é menor que 0.001 o que mostra que eles são estatisticamente significativos
    y_hat = reg.predict()
    res = df[Y] - y_hat
    stat, p = shapiro(res)  # p> 0.05 é normal então o modelo é válido
    if p > 0.05:
        print('++++++++++' + str(p) + ' > 0.05 =>> RESIDUOS É NORMAL MODELO VÁLIDO')
    else:
        print('----------' + str(p) + ' < 0.05 =>> RESIDUOS NÃO É NORMAL MODELO INVÁLIDO')

def PARTE_DA_DATA_HORA(df,CAMPO_ORIGEM,CAMPO_DESTINO):
    df[CAMPO_ORIGEM] = df[CAMPO_ORIGEM].astype('datetime64[ns]')
    if CAMPO_DESTINO == 'ANO':
        df[CAMPO_DESTINO] = df[CAMPO_ORIGEM].dt.year
    if CAMPO_DESTINO == 'MES':
        df[CAMPO_DESTINO] = df[CAMPO_ORIGEM].dt.month
    if CAMPO_DESTINO == 'DIA':
        df[CAMPO_DESTINO] = df[CAMPO_ORIGEM].dt.day
    if CAMPO_DESTINO == 'HORA':
        df[CAMPO_DESTINO] = df[CAMPO_ORIGEM].dt.hour
    if CAMPO_DESTINO == 'MINUTO':
        df[CAMPO_DESTINO] = df[CAMPO_ORIGEM].dt.minute
    df[CAMPO_DESTINO] = df[CAMPO_DESTINO].astype('str')
    df[CAMPO_DESTINO] = df[CAMPO_DESTINO].str.zfill(2)
    MSG(df,'AMARELO')
    return df

def DUMMY(df,VARIAVEL):
    df_dummies = pd.get_dummies(df[VARIAVEL])
    #del df_dummies[df_dummies.columns[-1]]
    df_new = pd.concat([df, df_dummies], axis=1)
    del df_new[VARIAVEL]
    MSG('NOVO df COM VARIAVEL DUMMY ' + VARIAVEL, 'AMARELO')
    MSG(df_new,'AMARELO')
    df_COR = df_new.corr(method='pearson')
    MSG('CORRELAÇÃO PEARSON', 'AMARELO')
    MSG(df_COR, 'AMARELO')
    return df_new

def DUMMY_COM_VALORES_DE_COLUNA(df,VARIAVEL_DUMMY,VARIAVEL_MUNERICA,COLUNAS_AGRUPADAS):
    # ESTA FUNÇÃO REORGANIZA UMA COLUNA EM VÁRIAS LEVANDO EM CONSIDERAÇÃO UMA CATEGORIA E UMA VARIAVEL NUMERICA
    # VARIAVEL_DUMMY DEVE SER CATEGORICA
    df_dummies = pd.get_dummies(df[VARIAVEL_DUMMY]).mul(df[VARIAVEL_MUNERICA], 0)
    df_new = pd.concat([df, df_dummies], axis=1)
    del df_new[VARIAVEL_DUMMY]
    del df_new[VARIAVEL_MUNERICA]
    if COLUNAS_AGRUPADAS != '':
        df_new = df_new.groupby(COLUNAS_AGRUPADAS).sum()
    df_new = df_new.reset_index(drop=False)
    MSG2(df_new, 'COLUNA DUMMY ' + VARIAVEL_DUMMY + ' COM VALORES EM COLUNAS DE ' + VARIAVEL_MUNERICA)

    return df_new



def FREQUENCIA(df,VARIAVEL,TIPO,QUANTIDADE_CLASSES):
    # TIPO = QUALIDATIVA @
    # TIPO = QUANTITATIVA #
    try:
        if TIPO == '@': #QUALITATIVA
            df_freq_abs = df[VARIAVEL].value_counts()
            df_freq_rel = df[VARIAVEL].value_counts()/len(df[VARIAVEL])*100
            df_freq = pd.concat([df_freq_abs, df_freq_rel], axis=1)
            df_freq.columns = ['ABS', 'REL']
            df_freq['ACUM_ABS'] = df_freq['ABS'].cumsum()
            df_freq['ACUM_REL'] = df_freq['REL'].cumsum()
            df_freq = df_freq.sort_values(['ABS'], ascending=False).reset_index()
            df_freq.columns = [VARIAVEL, 'ABS', 'REL', 'ABS_acum', 'REL_acum']
            MSG(df_freq, 'CYAN')
        if TIPO == '#':  # QUANTITATIVA
            n = len(df.index)
            k = int(round(1 + (10 / 3) * np.log10(n))) #https://maestrovirtuale.com/regra-de-sturges-explicacao-aplicacoes-e-exemplos/
            if QUANTIDADE_CLASSES > 0:
                k = QUANTIDADE_CLASSES
            frequency = pd.value_counts(pd.cut(x=df[VARIAVEL], bins=k, include_lowest=True), sort=False)
            percentage = pd.value_counts(pd.cut(x=df[VARIAVEL], bins=k, include_lowest=True), sort=False, normalize=True) * 100
            df_freq = ({'FREQUENCIA': frequency, 'PERCENTUAL': percentage})
            df_freq = pd.DataFrame(df_freq)
            df_freq['INTERVALO'] = df_freq.index
            df_freq = df_freq.reset_index(drop=True)
            df_freq['INTERVALO'] = df_freq.INTERVALO.astype(str)
            df_freq.INTERVALO = df_freq.INTERVALO.str.replace('(', '').str.replace(']', '')
            df_freq['MINIMO'] = df_freq['INTERVALO'].apply(lambda values: values.split(',')[0]).astype(float)
            df_freq['MAXIMO'] = df_freq['INTERVALO'].apply(lambda values: values.split(',')[1]).astype(float)
            df_freq['MIN'] = df[VARIAVEL].min()
            df_freq['MAX'] = df[VARIAVEL].max()
            df_freq['MINIMO'] = np.where(df_freq['MINIMO'] < df_freq['MIN'], df_freq['MIN'], df_freq['MINIMO'])
            df_freq['MAXIMO'] = np.where(df_freq['MAXIMO'] > df_freq['MAX'], df_freq['MAX'], df_freq['MAXIMO'])
            df_freq['INTERVALO'] = 'DE ' + df_freq['MINIMO'].astype(str) + ' ATÉ ' + df_freq['MAXIMO'].astype(str)
            df_freq['PERCENTUAL'] = df_freq.PERCENTUAL.round(1)
            df_freq=df_freq[['INTERVALO','FREQUENCIA','PERCENTUAL']]
            df_freq.info()
            MSG(df_freq, 'CYAN')
        return df_freq
    except:
        pass



def CLUSTERIZAR(df,COLUNAS,MOSTRAR):
    from sklearn.preprocessing import StandardScaler
    # AGRUPAR AS LINHAS/OBSERVAÇÕES
    #https://towardsdatascience.com/visualizing-clusters-with-pythons-matplolib-35ae03d87489
    #https://www.kaggle.com/eriveltonguedes/7-clusteriza-o-k-means-erivelton
    from sklearn.cluster import KMeans
    XX = COLUNAS[0]
    YY = COLUNAS[1]

    df = df.fillna(0)
    dfo = df
    df[COLUNAS] = df[COLUNAS].astype(float)
    # dfx = StandardScaler().fit_transform(df[COLUNAS])  # PADRONIZAÇÃO
    kmeans = KMeans(n_clusters=5, random_state=0)
    df['CLUSTER'] = kmeans.fit_predict(df[COLUNAS])
    centroids = kmeans.cluster_centers_
    cen_x = [i[0] for i in centroids]
    cen_y = [i[1] for i in centroids]
    df['cen_x'] = df.CLUSTER.map({0: cen_x[0], 1: cen_x[1], 2: cen_x[2], 3: cen_x[3], 4: cen_x[4]})
    df['cen_y'] = df.CLUSTER.map({0: cen_y[0], 1: cen_y[1], 2: cen_y[2], 3: cen_y[3], 4: cen_y[4]})
    # VERIFICAR O NÚMERO DE GRUPOS COM ELBOW
    colors = ['#FF0000', '#1C1C1C', '#0000FF', '#FFFF00','#00FF00']
    df['COR'] = df.CLUSTER.map({0: colors[0], 1: colors[1], 2: colors[2], 3: colors[3], 4: colors[4]})
    #dfn = dfo.join(df)
    COLUNAS.insert(0, 'CLUSTER')
    COLUNAS.insert(0, 'cen_y')
    COLUNAS.insert(0, 'cen_x')
    df = df.sort_values(COLUNAS)

    U_CLUSTER = list(df['CLUSTER'].unique())
    df['CLUSTER'] = df['CLUSTER'].replace(U_CLUSTER,[0,1,2,3,4])
    df['COR'] = df['CLUSTER'].replace([0, 1, 2, 3, 4], colors)

    MSG('CLUSTERIZAÇÃO ' + str(COLUNAS), 'CINZA_CLARO')
    df = SQLITE(df,'SELECT * FROM df')
    # FAZER A ANÁLISE DESCRITIVA POR GRUPO (MÉDIA / DESVIO / QUARTIL...)
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, max_iter=300, n_init=10, random_state=0)
        kmeans.fit(dfo[COLUNAS])
        wcss.append(kmeans.inertia_)


    # Mostra o Gráfico
    plt.plot(range(1, 11), wcss)
    plt.title('Curva de Cotovelo')
    plt.xlabel('Numero de Clusters')
    plt.ylabel('WCSS')  # within cluster sum of squares
    plt.gcf().savefig('CLUSTER-ELBOW.png')
    if(MOSTRAR == 1):
        plt.show()
    SALVA_DF_EXCEL(df, 'DADOS\\CLUSTERS-KMEANS.xlsx', 'KMEANS')
    plt.close()

    plt.clf()


    color_dict = dict({'0': 'red', '1': 'orange', '2': 'yellow', '3': 'brown', '4': 'green'})
    sns.set(style="darkgrid")
    sns.scatterplot(x=df[XX], y=df[YY], palette=color_dict, alpha=1, s=50, hue=df['CLUSTER'].astype(str))
    sns.scatterplot(x=df.cen_x, y=df.cen_y, palette=color_dict, alpha=0.5, s=300, hue=df['CLUSTER'].astype(str), legend=False, marker="+")
    sns.color_palette("rocket")
    plt.gcf().set_size_inches(12, 7.5)
    plt.title('CLUSTERS '+XX+' X '+YY)
    plt.xlabel(XX)
    plt.ylabel(YY)
    plt.gcf().savefig('CLUSTERS_' + XX + '_x_' + YY + '_.png')
    #plt.show()
    plt.close()


    return df


def ANALISE_FATORIAL(df):
    # ANALISE FATORIAL
    # AGRUPAR AS COLUNAS/VARIÁVEIS
    # TECNICA NÃO SUPERVISIONADA - NÃO HÁ CAPACIDADE DE INFERÊNCIA/PREDIÇÃO SOMENTE DIAGNÓSTICO E EXPLORATÓRIO
    # DEVE APAGAR AS COLUNAS NÃO NECESSÁRIAS (QUALITATIVAS OU CATEGÓRICAS)
    # https://ichi.pro/pt/introducao-a-analise-fatorial-em-python-116625965253739
    # https://www.phylos.net/2020-11-02/analise-fatorial-usando-python/

    from factor_analyzer import FactorAnalyzer

    # REMOVE COLUNAS CATEGÓRICAS E COM VALORES VAZIOS
    for column in df:
        TIPO = df[column].dtypes
        if TIPO == 'object':
            print('DELETANDO ' + df[column].name)
            df.drop([column], axis=1, inplace=True)
    df.dropna(inplace=True)
    itens = df.columns
    MSG(df,'CYAN')


    # FATORABILIDADE Teste da esfericidade de Bartlett
    from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
    chi_square_value, p_value = calculate_bartlett_sphericity(df)
    #o teste de Bartlett resulta em p-value = 0, o que indica que os dados podem ser fatorados e a matriz de correlação observada não é a identidade

    if int(p_value) == 0:
        MSG('Teste da Esfericidade de Bartlett (PODE SER FATORADO): chi² = %d,  p_value = %d' % (chi_square_value, p_value),'VERDE')
    else:
        MSG('Teste da Esfericidade de Bartlett (NÃO PODE SER FATORADO): chi² = %d,  p_value = %d' % (chi_square_value, p_value), 'VERMELHO')


    # FATORABILIDADE TESTE Kaiser-Meyer-Olkin (KMO)
    from factor_analyzer.factor_analyzer import calculate_kmo
    kmo_all, kmo_model = calculate_kmo(df)
    if kmo_model > 0.6:
        MSG('KMO = ' + str(kmo_model) + ' FATORAÇÃO POSSIVEL VALOR ADEQUADO','VERDE')
    else:
        MSG('KMO = ' + str(kmo_model) + ' FATORAÇÃO POSSIVEL VALOR INADEQUADO', 'VERMELHO')


    # ESCOLHENDO O NÚMERO DE FATORES
    fa = FactorAnalyzer(rotation=None)
    fa.fit(df)
    # Check Eigenvalues
    ev, v = fa.get_eigenvalues()
    for i in ev:
        if i >= 1:
            nev =+ 1
    ev = pd.DataFrame(ev,columns = ['EIGEN_VALUES'])
    MSG('EIGEN VALUES MAIORES QUE UM SUGERE O NÚMERO DE FATORES = ' + str(nev),'VERDE')
    MSG(ev, 'VERDE')
    variancia = pd.DataFrame(fa.get_factor_variance(), index = ['VARIANCIAS', 'VARIANCIAS_PROPORCIONAIS','VARIANCIAS_CUMULARIVAS'])
    MSG(variancia, 'VERDE')

    # EXECUTAR A ANÁLISE FATORIAL

    fa = FactorAnalyzer(nev+1, rotation="varimax")
    fa.fit(df)
    factorLoadings = pd.DataFrame.from_records(fa.loadings_)
    factorLoadings.index = itens
    MSG('CARGAS FATORIAIS', 'VERDE')
    MSG(factorLoadings,'VERDE')
    plt.figure(figsize=(8, 6))
    sns.set(font_scale=.9)
    sns.heatmap(factorLoadings, linewidths=1, linecolor='#ffffff', cmap="YlGnBu", xticklabels=1, yticklabels=1)
    plt.gcf().savefig("CARGAS_FATORIAIS.png")

    # COMUNALIDADES
    COMUNALIDADES = pd.DataFrame(fa.get_communalities(),columns = ['COMUNALIDADES'])
    COMUNALIDADES.index = itens
    COMUNALIDADE_TOTAL = fa.get_communalities().sum()
    MSG('COMUNALIDADE: ' + str(COMUNALIDADE_TOTAL), 'VERDE')
    MSG(COMUNALIDADES,'VERDE')
    # Podemos pensar na comunalidade de uma variável como a proporção de variação nessa variável explicada pelos fatores propostos no modelo.
    # Comunalidades servem para avaliar o desempenho do modelo. Valores mais próximos de um indicam que o modelo explica a maior parte da variação para essas variáveis.
    LINHAS = COMUNALIDADES.count()
    EFICIENCIA_MODELO = int(COMUNALIDADE_TOTAL*100/LINHAS)
    MSG('O MODELO FATORIAL POSSUI UMA EFICIÊNCIA DE ' + str(EFICIENCIA_MODELO) + ' POR CENTO.','CYAN')


    return factorLoadings



def NUVEM_DE_PALAVRAS(df_COLUNA):
    # NUVEM DE PALAVRAS
    # df_COLUNA >> df['nome_da_coluna']
    PALAVRAS = df_COLUNA.to_string(index=False).strip().replace('\n', '')
    from wordcloud import WordCloud, STOPWORDS
    import matplotlib.pyplot as plt
    stopwords = set(STOPWORDS)
    arquivo = LER_ARQUIVO('RAFAEL\\STOPWORDS.txt',1)
    arquivo = arquivo.replace('  ',' ')
    stopwords = arquivo.split(' ')
    MSG(stopwords, 'CYAN')
    plt.figure(figsize=(20, 10))
    wc = WordCloud(min_font_size=10, max_font_size=300, background_color='white', mode="RGB", stopwords=stopwords, width=2000, height=1000, normalize_plurals=True).generate(PALAVRAS)
    plt.title("NÚVEM DE PALAVRAS", fontsize=60, color="red")
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.gcf().savefig("NUVEM_DE_PALAVRAS.png")
    #plt.show()
    plt.close()

def REPLACE_NOMES_COLUNAS(df,ISSO,POR_ISSO):
    df.rename(columns=lambda x: x.replace(ISSO, POR_ISSO), inplace=True)
    MSG(df.head(),'AZUL')
    return df
def RENOMEAR_COLUNA(df,NOME,NOVO_NOME):
    df = df.rename(columns={NOME: NOVO_NOME})
    print('RENOMEADA COLUNA ' + NOME + ' PARA > ' + NOVO_NOME )
    return df

def ZERO_PARA_VAZIO(df):
    import numpy as np
    for COL in df.columns:
        try:
            df[COL] = df[COL].fillna(0)
        except:
            continue
    return df

def CONVERTE_PARA_CATEGORIA(df,LISTA_COLUNAS):
    for C in LISTA_COLUNAS:
        df[C] = df[C].astype('category')
    MSG2(df,'COLUNAS ALTERADAS PARA TIPO CATEGORIA')
    return df

def CONVERTE_PARA_OBJETO(df,LISTA_COLUNAS):
    for C in LISTA_COLUNAS:
        df[C] = df[C].astype(str)
        df[C] = df[C].str.replace('.0','',regex=False)
        print('COLUNAS ALTERADAS PARA TIPO OBJETO: ' + C)
    return df

def EXCLUIR_COLUNAS(df,LISTA_COLUNAS):
    for C in LISTA_COLUNAS:
        try:
            del df[C]
            print('COLUNA DELETADA: ' + C)
        except:
            MSG('ERRO DELETAR COLUNA ' + C, 'VERMELHO')
            pass
    MSG2(df,'COLUNAS EXCLUIDAS')
    return df

def GERAR_EXCEL_DE_PARA(df1,df2):
    # GERA UM ARQUIVO COM AS COLUNAS PARA AUXILIAR A RELACIONAR AS DUAS TABELAS E DEPOIS SER USADA PARA RENOMEAR AS COLUNAS
    cab1 = df1.head().T.reset_index(drop=False).add_prefix('A_').reset_index(drop=False)
    cab2 = df2.head().T.reset_index(drop=False).add_prefix('B_').reset_index(drop=False)
    import pandas as pd
    dp = pd.merge(cab1, cab2, how = 'outer')
    SALVA_DF_EXCEL(dp,'DE_PARA','DE_PARA')
    print(dp)
# FIM BIBLIOTECA PANDAS
#################################################################################################################################################

#################################################################################################################################################
# TESTES ESTATISTICOS

def ZSCORE(df,COLUNA):
    # CRIA UMA COLUNA COM O ZSCORE PARA DEPOIS PODER FILTRAR OS OUTLIERS
    df = CONVERTE_PARA_NUMERO(df, COLUNA)
    df['ZSCORE_'+COLUNA] = (df[COLUNA] - df[COLUNA].mean()) / df[COLUNA].std(ddof=0)
    df['OUTLIER_' + COLUNA] = 0
    df.loc[(np.abs(df['ZSCORE_'+COLUNA]) >= 3),'OUTLIER_' + COLUNA] = 1
    MSG('ZSCORE ADICIONADO PARA A COLUNA ' + COLUNA,'AZUL')
    return df

def TESTE_NORMALIDADE_SHAPIRO_WILK(df,LISTA_COLUNAS):

    for COLUNA in LISTA_COLUNAS:
        stat, p = shapiro(df[COLUNA])
        if p > 0.05:
            print(COLUNA + '\nAMOSTRA GAUSSIANA - FALHA EM REJEITAR H0 - DISTRIBUIÇÃO NORMAL p>0.05: ' + str(p))
        else:
            print(COLUNA + '\nAMOSTRA NÃO GAUSSIANA - REJEITADA H0 - DISTRIBUIÇÃO NÃO NORMAL p<0.05: ' + str(p))

def BOXPLOT(df,COLUNA_ID,COLUNAS_VALORES):
    df_MELT = pd.melt(df.reset_index(), id_vars=[COLUNA_ID], value_vars=COLUNAS_VALORES)
    df_MELT.columns = ['index', 'variable', 'value']
    ax = sns.boxplot(x='variable', y='value', data=df_MELT, color='#99c2a2')
    ax = sns.swarmplot(x="variable", y="value", data=df_MELT, color='#7d0013')
    plt.gcf().savefig("graf_BOXPLOT.png")
    plt.show()

def ANOVA_ONE_WAY(df,COLUNA_ID,COLUNAS_VALORES):
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    # Ordinary Least Squares (OLS) model
    df_MELT = pd.melt(df.reset_index(), id_vars=[COLUNA_ID], value_vars=COLUNAS_VALORES)
    model = ols('value ~ C(variable)', data=df_MELT).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    print('TABELA ANOVA TIPO ONE WAY <<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    print(anova_table)
    pvalue = anova_table["PR(>F)"][0]
    if pvalue < 0.05:
        print('Pvalue: '+str(pvalue)+' < 0.05 - EXISTEM DIFERENÇAS SIGNIFICATIVAS ENTRE OS GRUPOS')
    else:
        print('Pvalue: '+str(pvalue)+' > 0.05 - NÃO EXISTEM DIFERENÇAS SIGNIFICATIVAS ENTRE OS GRUPOS')

# FIM TESTES ESTATISTICOS
#################################################################################################################################################




#################################################################################################################################################
# INICIO GPSP


def NOVA_TAREFA_GPSp(TITULO,DURACAO,ID_LOCAL,ID_CARGO,EVIDENCIA):

    # DURAÇÃO EM MINUTOS
    # TODOS OS PARAMETROS DEVEM SER INSERIDOS ENTRE '', EXCETO DURAÇÃO QUE É INTEIRO
    # EVIDENCIA = true / false
    # ID_CARGO DEVE ENTRAR COMO LISTA, PARA PODER INSERIR MAIS DE UM CARGO

    token = 'SGR4A5L6C7I8S9I10N-HAUS'
    headers = {'Content-type': 'application/json'}
    base_url = 'https://www.cadastrosgpsp.com.br/GPSPPRODAPI/api/'

    INICIO = datetime.isoformat(datetime.now() + dt.timedelta(minutes=1))
    INICIO = INICIO[:19]
    FINAL = datetime.isoformat(datetime.now() + dt.timedelta(minutes=DURACAO))
    FINAL = FINAL[:19]

    #CARGOS
    CARGOS = ''
    for i in ID_CARGO:
        CARGOS = CARGOS + '{"id": ' + i + '}, '
    CARGOS = CARGOS[:-2]


    JSON = '''
        {
            "id": 0,
            "title": "''' + TITULO + '''",
            "single": true,
            "technicalSpecifications": null,
            "endDateTime": "''' + FINAL + '''.000Z",
            "company": {"id": '''+ID_LOCAL+'''},
            "startDateTime": "''' + INICIO + '''.000Z",
            "businessRole": ['''+CARGOS+'''],
            "minimumExperience": {"id": 3},
            "description": "TAREFA CRIADA PELO ROBO PYTHON CRIADO POR RAFAEL GARCIA RODRIGUES",
            "attachment": false,
            "evidence": '''+EVIDENCIA+''',
            "duration": '''+str(DURACAO)+''',
            "stagger": 60,
            "actions": {
                "id": 0,
                "emails": [],
                "idNextTask": 0
            },
            "listCheckList": [
                {
                    "id": 0,
                    "question": "COMENTARIOS",
                    "answers": "(livre)",
                    "order": 2,
                    "variables": null,
                    "kindOfQuestion": {"id": 4}
                }
            ],
            "recurrence": null,
            "allowsMultipleTasks": true,
            "redoTaskCanceled": true,
            "signature": false,
            "qrCode": false,
            "beginRecurrence": 0,
            "autoLink": false
        }
        '''

    try:
        res = requests.post('https://www.cadastrosgpsp.com.br/GPSPPRODAPI/api/task/get?token=SGR4A5L6C7I8S9I10N-HAUS', data=JSON, headers=headers)
        MSG(JSON,'VERDE')
        return print(res)
    except Exception as er:
        return f"Message : {er}"

# FIM GPSP
#################################################################################################################################################

# INICIO RELATÓRIO ON_PAGE
#################################################################################################################################################

def ONE_PAGE_CRIAR_RELATORIO(NOME_RELATORIO):
    HTML = LER_ARQUIVO('RAFAEL\\CANVASJS\\BASE_RELATORIO.html', 0)
    HTML = HTML.replace('*NOME_RELATORIO*', NOME_RELATORIO)
    ESCREVER_ARQUIVO(NOME_RELATORIO + '.html', HTML)


def ONE_PAGE_CRIA_NOVA_LINHA_NO_RELATORIO(NOME_RELATORIO, NOME_DA_LINHA):
    # ANTES O RELATORIO DEVE SER CRIADO NA FUNÇÃO ANTERIOR
    HTML = LER_ARQUIVO(NOME_RELATORIO + '.html', 0)
    ID_LINHA = NOME_DA_LINHA.replace(' ','_')
    NOME_LINHA = NOME_DA_LINHA.replace('_', ' ')
    LINHA = '\n'
    LINHA = LINHA + '<!--LINHA_INSERIDA--> \n'
    LINHA = LINHA + '<div class="row" id="id_linha_'+ID_LINHA+'"> \n'
    LINHA = LINHA + '<h5 style="margin-top: 60px;margin-bottom: 40px;">'+NOME_LINHA+'</h5> \n'
    LINHA = LINHA + '<!--ESPERA_PARA_NOVA_COLUNA_DA_LINHA_ID_'+ID_LINHA+'--> \n'
    LINHA = LINHA + '</div> \n\n'
    LINHA = LINHA + '<!--ESPERA_PARA_NOVA_LINHA--> \n\n'
    LINK = '<a class="nav-link" href="#id_linha_'+ID_LINHA+'">'+NOME_LINHA+'</a>\n<!--ESPERA_NOVO_LINK-->\n\n'
    HTML = HTML.replace('<!--ESPERA_PARA_NOVA_LINHA-->', LINHA)
    HTML = HTML.replace('<!--ESPERA_NOVO_LINK-->', LINK)
    ESCREVER_ARQUIVO(NOME_RELATORIO+'.html', HTML, )
    MSG('LINHA '+NOME_DA_LINHA+' INSERIDA NO RELATORIO '+NOME_RELATORIO, 'VERDE')

def ONE_PAGE_INSERE_CARD_NA_LINHA(NOME_RELATORIO,NOME_DA_LINHA,TEXTO_GR,TEXTO_PQ,TIPO):
    # TIPOS: primary, warning, success, danger
    HTML = LER_ARQUIVO(NOME_RELATORIO + '.html', 0)
    ID_LINHA = NOME_DA_LINHA.replace(' ', '_')
    COLUNA = '\n'
    COLUNA = COLUNA + ' <div class="col-xl-3 col-md-6">\n'
    COLUNA = COLUNA + '     <div class="card bg-'+TIPO+' text-white mb-4"> \n'
    COLUNA = COLUNA + '         <div class="card-body">'+str(TEXTO_GR)+'</div>\n'
    COLUNA = COLUNA + '         <div class="card-footer d-flex align-items-center justify-content-between">\n'
    COLUNA = COLUNA + '             <a class="small text-white stretched-link" href="#">'+str(TEXTO_PQ)+'</a>\n'
    COLUNA = COLUNA + '             <div class="small text-white"><i class="fas fa-angle-right"></i></div>\n'
    COLUNA = COLUNA + '         </div>\n'
    COLUNA = COLUNA + '     </div>\n'
    COLUNA = COLUNA + ' </div>\n'
    COLUNA = COLUNA + ' \n\n'
    COLUNA = COLUNA + '\n\n<!--ESPERA_PARA_NOVA_COLUNA_DA_LINHA_ID_'+ID_LINHA+'--> \n'
    HTML = HTML.replace('<!--ESPERA_PARA_NOVA_COLUNA_DA_LINHA_ID_'+ID_LINHA+'-->', COLUNA)
    ESCREVER_ARQUIVO(NOME_RELATORIO + '.html', HTML, )
    MSG('CARD '+TEXTO_GR+' INSERIDA NO RELATORIO '+NOME_RELATORIO, 'VERDE')


def ONE_PAGE_INSERE_GRAFICO_CANVASJS_NA_LINHA(NOME_RELATORIO,NOME_DA_LINHA,JS_GRAF,DIV_GRAF,TITULO_GRAFICO, GRID):
    HTML = LER_ARQUIVO(NOME_RELATORIO + '.html', 0)
    ID_LINHA = NOME_DA_LINHA.replace(' ', '_')
    HTML = HTML.replace('//ESPERA_NOVO_JS_GRAFICO_CANVAS', JS_GRAF + '\n\n//ESPERA_NOVO_JS_GRAFICO_CANVAS')
    GRAF = '\n'
    GRAF = GRAF + '<div class="col-xl-'+str(GRID)+'">\n'
    GRAF = GRAF + '     <div class="card mb-4">\n'
    GRAF = GRAF + '         <div class="card-header"><i class="fas fa-chart-area me-1"></i>'+TITULO_GRAFICO+'</div>\n'
    GRAF = GRAF + '             <div class="card-body">'
    GRAF = GRAF + '                 '+DIV_GRAF
    GRAF = GRAF + '             </div>\n'
    GRAF = GRAF + '     </div>\n'
    GRAF = GRAF + '</div>\n'
    GRAF = GRAF + '\n\n<!--ESPERA_PARA_NOVA_COLUNA_DA_LINHA_ID_' + ID_LINHA + '-->\n'
    GRAF = GRAF + '\n'
    HTML = HTML.replace('<!--ESPERA_PARA_NOVA_COLUNA_DA_LINHA_ID_' + ID_LINHA + '-->', GRAF)
    ESCREVER_ARQUIVO(NOME_RELATORIO + '.html', HTML, )
    MSG('GRAFICO '+DIV_GRAF+' INSERIDA NO RELATORIO '+NOME_RELATORIO + ' NA LINHA ' + NOME_DA_LINHA, 'VERDE')


def ONE_PAGE_INSERE_TABELA_JS_NA_LINHA(NOME_RELATORIO,NOME_DA_LINHA,JS_TAB,DIV_TAB,TITULO_TABELA, GRID):
    HTML = LER_ARQUIVO(NOME_RELATORIO + '.html', 0)
    ID_LINHA = NOME_DA_LINHA.replace(' ', '_')
    HTML = HTML.replace('//ESPERA_NOVO_JS_TABELA', JS_TAB + '\n//ESPERA_NOVO_JS_TABELA')
    GRAF = '\n'
    GRAF = GRAF + '<!--INICIO DA TABELA '+TITULO_TABELA+' .......................................................................................-->\n'
    GRAF = GRAF + '<div class="col-xl-'+str(GRID)+'">\n'
    GRAF = GRAF + '<div class="card mb-4">\n'
    GRAF = GRAF + '<div class="card-header"><i class="fas fa-chart-area me-1"></i>'+TITULO_TABELA+'</div>\n'
    GRAF = GRAF + '<div class="card-body">\n'
    GRAF = GRAF + DIV_TAB
    GRAF = GRAF + '\n</div>\n'
    GRAF = GRAF + '</div>\n'
    GRAF = GRAF + '</div>\n'
    GRAF = GRAF + '<!--FINAL DA TABELA ' + TITULO_TABELA + ' .......................................................................................-->\n\n'
    GRAF = GRAF + '\n\n<!--ESPERA_PARA_NOVA_COLUNA_DA_LINHA_ID_' + ID_LINHA + '-->\n'
    GRAF = GRAF + '\n'
    HTML = HTML.replace('<!--ESPERA_PARA_NOVA_COLUNA_DA_LINHA_ID_' + ID_LINHA + '-->', GRAF)
    HTML = HTML.replace('&lt;', '<')
    HTML = HTML.replace('&gt;', '>')



    ESCREVER_ARQUIVO(NOME_RELATORIO + '.html', HTML, )
    MSG('TABELA  '+TITULO_TABELA+' INSERIDA NO RELATORIO '+NOME_RELATORIO + ' NA LINHA ' + NOME_DA_LINHA, 'VERDE')

def ONE_PAGE_INSERE_TEXTO_NA_LINHA(NOME_RELATORIO,NOME_DA_LINHA,TEXTO,TITULO, GRID):
    HTML = LER_ARQUIVO(NOME_RELATORIO + '.html', 0)
    ID_LINHA = NOME_DA_LINHA.replace(' ', '_')
    GRAF = '\n'
    GRAF = GRAF + '<!--INICIO DA TABELA '+TITULO+' .......................................................................................-->\n'
    GRAF = GRAF + '<div class="col-xl-'+str(GRID)+'">\n'
    GRAF = GRAF + '<div class="card mb-4">\n'
    GRAF = GRAF + '<div class="card-header"><i class="fas fa-chart-area me-1"></i>'+TITULO+'</div>\n'
    GRAF = GRAF + '<div class="card-body">\n'
    GRAF = GRAF + TEXTO
    GRAF = GRAF + '\n</div>\n'
    GRAF = GRAF + '</div>\n'
    GRAF = GRAF + '</div>\n'
    GRAF = GRAF + '<!--FINAL DA TABELA ' + TITULO + ' .......................................................................................-->\n\n'
    GRAF = GRAF + '\n\n<!--ESPERA_PARA_NOVA_COLUNA_DA_LINHA_ID_' + ID_LINHA + '-->\n'
    GRAF = GRAF + '\n'
    HTML = HTML.replace('<!--ESPERA_PARA_NOVA_COLUNA_DA_LINHA_ID_' + ID_LINHA + '-->', GRAF)
    ESCREVER_ARQUIVO(NOME_RELATORIO + '.html', HTML, )
    MSG('TEXTO  '+TITULO+' INSERIDA NO RELATORIO '+NOME_RELATORIO + ' NA LINHA ' + NOME_DA_LINHA, 'VERDE')

# FINAL RELATÓRIO ON_PAGE
#################################################################################################################################################


# DATA SCIENCE ----------------------------------------------------------------------------------------------------------------------------------
def REGRESSAO_LOGISTICA_PREDICAO(df,y,LISTA_x,TAM_TEST,LISTA_VAR):
    # y: NOME DA COLUNA COM A VARIAVEL Y. PRECISA SEM CATEGÓRICA BINÁRIA
    # LISTA_x: LISTA COM AS COLUNAS X
    # TAM_TEST: 0-1 COM O NÚMERO PERCENTUAL DE DADOS QUE SERÃO USADOS PARA TREINAR O MODELO
    # LISTA_VAR: LISTA CONTENDO OS VALORES NA MESMA ORDEM DE LISTA_x PARA OBTER O VALOR DE Y
    #A seguir, vamos dividir nossos dados em teste e treinamento:
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn import metrics
    from sklearn.metrics import log_loss
    import seaborn as sn
    import matplotlib.pyplot as plt
    y = df[y]
    x = df[LISTA_x]
    X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=TAM_TEST,random_state=0)
    #Agora, está na hora da mágica acontecer, vamos treinar nosso classificador:
    logistic_regression= LogisticRegression()
    logistic_regression.fit(X_train,y_train)
    y_pred=logistic_regression.predict(X_test)
    #Depois de treinado podemos visualizar a matriz de confusão:
    confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['REAIS'], colnames=['PREDITIVOS'])
    sn.heatmap(confusion_matrix, annot=True)
    #Podemos ainda calcular a acurácia do nosso modelo:
    print('ACURÁRIA: ',metrics.accuracy_score(y_test, y_pred))
    print('LOGLOSS: ', metrics.log_loss(y_test,y_pred))
    plt.show()
    #TESTE
    dft = pd.DataFrame([LISTA_VAR], columns=LISTA_x)
    print(dft)
    resultado = logistic_regression.predict(dft)
    print(resultado)
    resultado = resultado[0]
    return resultado
