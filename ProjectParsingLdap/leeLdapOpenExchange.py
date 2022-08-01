##Import librerias
import pandas as pd

## Declaración de variables
dn=""
OXId=""
OXMailDeliveryAddress=""
ModifyTimestamp=""
#inserta información en variable
listaContador=list()
listaDn=list()
listaOXId=list()
listaOXMailDeliveryAddress=list()
listaModifyTimestamp=list()
#Crea contador de usuarios
contador=1
## lee archivo
fhand = open('K:\My Drive\Ibermatica\masmovil\Fase2\cuentasT_OX.csv') 
#print(fhand)
##funciones
def AsignaValorValirable(stripped_line,contador):
    if (stripped_line.startswith('dn:')):
            global dn
            dn=stripped_line[4:]
    if (stripped_line.startswith('OXId:')):
            global OXId
            OXId=stripped_line[6:]
    if (stripped_line.startswith('OXMailDeliveryAddress:')):
            global OXMailDeliveryAddress
            OXMailDeliveryAddress=stripped_line[23:]
    if (stripped_line.startswith('modifyTimestamp: ')):
            global ModifyTimestamp
            ModifyTimestamp=stripped_line[17:]
def AlmacenaValorLista(dn,mail,uid,zimbraLastLogonTimestamp,contador):
    listaDn.insert(contador,dn)
    listaOXId.insert(contador,mail)
    listaOXMailDeliveryAddress.insert(contador,uid)
    listaModifyTimestamp.insert(contador,zimbraLastLogonTimestamp)
    listaContador.insert(contador,contador)
## Genera Loop para recorrer el archivo
for line in fhand:
    stripped_line=line.strip()
    # print(stripped_line)
    if len(stripped_line) == 0:
        #insert almacena valores
        AlmacenaValorLista(dn,OXId,OXMailDeliveryAddress,ModifyTimestamp,contador)
        #aumenta contador usario
        contador=contador+1
        #cree una nueva fila en el arreglo e inicialice las variables
        dn=""
        OXId=""
        OXMailDeliveryAddress=""
        ModifyTimestamp=""
    else:
        #agregue el valor de la linea al arreglo
        AsignaValorValirable(stripped_line,contador)

dict={
    'Contador':listaContador,
    'dn':listaDn,
    'OXId':listaOXId,   
    'OXMailDeliveryAddress':listaOXMailDeliveryAddress,
    'ModifyTimestamp':listaModifyTimestamp}
df=pd.DataFrame(dict)
listColumnas=list(df.columns)
#print(df)
df.to_csv(r'K:\My Drive\Ibermatica\masmovil\Fase2\JIRA 393\usuariosOpenXchange.csv', 
          header=listColumnas)
