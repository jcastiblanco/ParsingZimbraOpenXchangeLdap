##Import librerias
import pandas as pd

## Declaración de variables
dn=""
mail=""
uid=""
zimbraLastLogonTimestamp=""
#inserta información en variable
listaContador=list()
listaDn=list()
listaMail=list()
listaUid=list()
listaZimbraLastLogonTimestamp=list()
#Crea contador de usuarios
contador=1
## lee archivo
fhand = open('K:\My Drive\Ibermatica\masmovil\Fase2\JIRA 393\cuentasOO_2807.csv') 
#print(fhand)
##funciones
def AsignaValorValirable(stripped_line,contador):
    if (stripped_line.startswith('dn:')):
            global dn
            dn=stripped_line[3:]
    if (stripped_line.startswith('mail:')):
            global mail
            mail=stripped_line[5:]
    if (stripped_line.startswith('uid:')):
            global uid
            uid=stripped_line[4:]
    if (stripped_line.startswith('zimbraLastLogonTimestamp:')):
            global zimbraLastLogonTimestamp
            zimbraLastLogonTimestamp=stripped_line[25:]
def AlmacenaValorLista(dn,mail,uid,zimbraLastLogonTimestamp,contador):
    listaDn.insert(contador,dn)
    listaMail.insert(contador,mail)
    listaUid.insert(contador,uid)
    listaZimbraLastLogonTimestamp.insert(contador,zimbraLastLogonTimestamp)
    listaContador.insert(contador,contador)
## Genera Loop para recorrer el archivo
for line in fhand:
    stripped_line=line.strip()
    # print(stripped_line)
    if len(stripped_line) == 0:
        #insert almacena valores
        AlmacenaValorLista(dn,mail,uid,zimbraLastLogonTimestamp,contador)
        #aumenta contador usario
        contador=contador+1
        #cree una nueva fila en el arreglo e inicialice las variables
        zimbraLastLogonTimestamp=""
        uid=""
        mail=""
        dn=""
    else:
        #agregue el valor de la linea al arreglo
        AsignaValorValirable(stripped_line,contador)

dict={
    'Contador':listaContador,
    'dn':listaDn,
    'mail':listaMail,   
    'uid':listaUid,
    'zimbraLastLogonTimestamp':listaZimbraLastLogonTimestamp}
df=pd.DataFrame(dict)
listColumans=list(df.columns)
#print(df)
df.to_csv(r'K:\My Drive\Ibermatica\masmovil\Fase2\JIRA 393\usuariosZimbra.csv', 
          header=listColumans)
