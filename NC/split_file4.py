#!/usr/bin/python2.7

import os


#############################################
#src= "p:\\Python27\\R4scripts\\test.csv"
#src= "D:\\tmp\\R4scripts\\test.csv"
#файл источник
src= "D:\\tmp\\R4scripts\\r4d1.csv"
#print("Default value for 'src': " + src)
#src_user= str(input("Input new 'src' file or press Enter to save default: "))
#if (src_user==""): scr=src_user
#print ("New value: " + src)
# директория сохраниения результатов
#Dst_dir="D:\\tmp\\R4scripts\\1\\"
Dst_dir="D:\\tmp\\R4scripts\\names1\\"
# проверяем наличие директории с данным месяцем
if not os.path.exists(Dst_dir): os.mkdir(Dst_dir)
# совпадающие id скриптов

s_file=open(src)
print('Source file:' +src+' is opened: '+format(not(s_file.closed)))
#l_file=open(Dst_dir+'all_found_scripts.txt','w')
#print('Lof file:' +Dst_dir+'all_found_scripts.txt'+' is opened: '+format(not(l_file.closed)))
s_list=s_file.readlines()
i=0
j=0

find_names = ['IMS_CS2K_PDTC_Port_Validation', 'IMS_CS2K_OSSGate_QueryDirectoryNumber', 'IMS_CS2K_OSSGate_QueryMapciLEN', 'IMS_CS2K_GWC_Port_Validation', 'IMS_CS2K_TDM_Port_Validation', 'IMS_CS2K_ValidateCLLI', 'IMS_CS2K_CountSUPERTKG', 'IMS_CS2K_ValidateTrunkGroupType', 'IMS_CS2K_Query_LogicalTerminal', 'IMS_CS2K_QueryDirectoryNumber', 'IMS_CS2K_ValidateRoutingRecords', 'IMS_CS2K_CountIndex', 'IMS_CS2K_DNValidation', 'IMS_CS2K_CheckStatus', 'IMS_CS2K_Check_CLLI', 'IMS_CS2K_SIP_STATE_Validation', 'IMS_CS2K_AdminValidation', 'IMS_CS2K_OSSGate_QueryLineEquipmentNumber']



for text in s_list:
   beg=0
   if (text.find('914')==0):
       beg = 1
       if (i>0) and (name in find_names):
          #print (o_id+'_'+name+'\n'+script)
          #print (Dst_dir+o_id +'_'+name)
         # w_file = open(Dst_dir+name +'.txt','w')
         # print ('File: '+Dst_dir+name +' is opened:'+format(not(w_file.closed)))
         # w_file.write(o_id)
         # w_file.close()
         # print ('File: '+Dst_dir+name +' is closed: '+ format(w_file.closed))
         # l_file.write(o_id+';'+name+'\n')
            j=j+1
            print(o_id+'--'+name+'\n')
       i=i+1
       spl=text.split(";")
       #print i
       o_id=spl[0]
       name=spl[1]
       script= spl[2]
  

   if (i>0) and (beg==0):
      script= script+text
      #print (str(i) +'--'+script)

print (str(j)+ ' out of '+str(len(find_names))+' scripts were found.')
#l_file.write('Total number of scripts: '+str(i)+'\n')
s_file.close()
print ('src file is closed: '+src+' -- '+ format(s_file.closed))
#l_file.close()
#print ('File \'all_found_scripts.txt\' is closed: '+src+' -- '+ format(l_file.closed))



