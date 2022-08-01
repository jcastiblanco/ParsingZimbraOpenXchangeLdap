# ParsingZimbraOpenXchangeLdap
Scripts en Python para parcear la exportación de cuentas de LDAP de Zimbra 8.0 y OpenExchange

Los scrips de este proyecto fueron construidos en python 3.10.  Permiten parsear el formato de salida de exports de ldaps tanto de zimbra como de openxchange para dejarlo en un formato de filas y columnas y poder analizar la información de una mejor manera.

El formato original de Zimbra es de la siguiente forma

dn: uid=user1,ou=people,dc=xxxtuak,dc=es
zimbraMailQuota: 5368709120
zimbraMailHost: oo2xxx.xxxx.es
zimbraMailTransport: lmtp:oo2xxxx.xxxx.es:7025
objectClass: inetOrgPerson
objectClass: zimbraAccount
objectClass: amavisAccount
zimbraId: b8c4c893-0c59-4c0a-b358-2d4fa9a73xxxx
zimbraCreateTimestamp: 20220720093913Z
zimbraAccountStatus: active
zimbraMailStatus: enabled
zimbraMailDeliveryAddress: user1@xxxtuak.es
mail: user1@xxxtuak.es
cn: user1
sn: user1
uid: user1
zimbraAuthTokenValidityValue: 1
userPassword:: e1NTSEF9Sy9oODYwclowVlkveXdLxxxx=
zimbraPasswordModifiedTime: 20220720102438Z
zimbraLastLogonTimestamp: 20220727074907Z

El formato original de OpenXchange

dn: uid=user1,ou=people,dc=xxx,dc=es
objectClass: TCAccount
OXAccountStatus: enabled
OXId: user1
TCAccountType: standard
TCCustomerId: 1524535
TCSeg: RESIDENCIAL
uid: user1
OXMailDeliveryAddress: user1@xxx.es
OXMailStatus: enabled
OXMailQuota: 2
TCCustomerField01: 1
TCCustomerField02: 2
TCCustomerField03: 3
TCCustomerField04: 4
TCCustomerField05: 5
OXSmarthostStatus: enabled
OXSmarthostCredentials: xxx.es:xxx-SmTp
OXSmarthostHostname: 4559.smtp.xxxx.com:587
structuralObjectClass: TCAccount
entryUUID: 65ab22e2-6233-1036-9aea-59ff2ea71690
creatorsName: uid=user1,cn=services,cn=ox
createTimestamp: 20161229165550Z
OXMailHost: user1.isp.xxx.es
OXMailTransport: lmtp:user1.isp.xxxx.es:9924
userPassword:: e3NoYX1oRVFWRE1kbTBCeEs1WkxxxxxxbktmaTg9
OXLogin: user1@47605
entryCSN: 20170309161514.165069Z#000000#000#000000
modifiersName: uid=user1,cn=services,cn=ox
modifyTimestamp: 20170309161514Z
