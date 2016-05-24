#coding:utf-8
import re

foldercount = {0:'FM_scf',1:'stripe_AFM_scf',2:'scf'} 
list = open ('G:\\replace_work\\energy.dat','w') 

for name in range(1,37):        
    currentE=''                 
    for count in range(3):      
        workdir = 'G:\\replace_work\\%04d'%name+'\\'+foldercount[count]+'\\OSZICAR' 
        fo =  open (workdir,'r')
        txt = fo.readlines()            
        fo.close()
        a = txt[len(txt)-1]             
        reg =r'E0=.*?  '
        E = re.findall(reg,a)           
        E[0]=re.sub('E0= ','',E[0])     
        currentE+=E[0]                  
        print currentE
    currentE+='\n'                   
    list.writelines(currentE)          

list.close()
