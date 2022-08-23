# -*- coding: utf-8 -*-
#python 3.x

import csv
import sys

#convert a "comma separated values" file to vcf contact cards. I used this to convert a list of student
#names and phone numbers into a vcf and save the trouble of adding one by one through phone

#USAGE:
#CSV_to_Vcards.py CSV_filename


def convert(somefile):
    #assuming file format : lastname,firstname,phonenumber,mail
    with open( somefile, 'r' ) as source:
        reader = csv.reader( source ) 
        #contador,dateofbirth,piphone1,piphone2,piphone3,piphone4,piphone5,piphone1type
        # ,piphone2type,piphone3type,piphone4type,piphone5type,piAdditionalPhone
        # ,piemail1,piemail2,piemail3,piemail1type,piemail2type,piemail3type
        # ,sn,givenName,nickname,displayname,company,jobTitle,dn1,cuenta,dn3
        # ['lastname', 'firstname', 'phonenumber', 'mail']
        i = 0
        for row in reader:
            vcffilename= row[26] + '.vcf'
            #vcffilename='G:\ldfEKTMail\'  + vcffilename
            allvcf = open(vcffilename, 'a') 
            #write in the "ALL.vcf" file.
            allvcf.write( 'BEGIN:VCARD' + "\n")
            allvcf.write( 'VERSION:2.1' + "\n")
            allvcf.write( 'N:' + row[20] + ';'  "\n")
            allvcf.write( 'FN:' + row[19] + ' ' + row[20] + "\n") #rembemer that lastname first
            allvcf.write( 'ORG:' + row[23] + "\n")
            if(row[2]!=''):
                allvcf.write( 'TEL;TYPE='+row[7]+':' +   row[2] + "\n")# posee telefono 1
            if(row[3]!=''):
                allvcf.write( 'TEL;TYPE='+row[8]+':' +   row[3] + "\n")# posee telefono 2
            if(row[4]!=''):
                allvcf.write( 'TEL;TYPE='+row[9]+':' +   row[4] + "\n")# posee telefono 3
            if(row[5]!=''):
                allvcf.write( 'TEL;TYPE='+row[10]+':' +   row[5] + "\n")# posee telefono 3
            if(row[6]!=''):
                allvcf.write( 'TEL;TYPE='+row[11]+':' +   row[6] + "\n")# posee telefono 3
            if(row[13]!=''):
                allvcf.write( 'EMAIL;TYPE='+row[16]+':' + row[13] + "\n") #EMAIL;TYPE=INTERNET:ganguly@acm.org
            if(row[14]!=''):
                allvcf.write( 'EMAIL;TYPE='+row[17]+':' + row[14] + "\n") #EMAIL;TYPE=INTERNET:ganguly@acm.org
            if(row[15]!=''):
                allvcf.write( 'EMAIL;TYPE='+row[18]+':' + row[15] + "\n") #EMAIL;TYPE=INTERNET:ganguly@acm.org
            allvcf.write( 'END:VCARD' + "\n")
            allvcf.write( "\n")
            i += 1#counts
            allvcf.close()

        
        print (str(i) + " vcf cards generated")


somefile="G:\ldfEKTMail\PreviewContactosEKTMail20220816v2.csv"
convert(somefile)

