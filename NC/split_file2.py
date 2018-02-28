#!/usr/bin/python2.7

import os


#############################################
#src= "p:\\Python27\\R4scripts\\test.csv"
#src= "D:\\tmp\\R4scripts\\test.csv"
#файл источник
src= "D:\\tmp\\R4scripts\\r4d2.csv"
#print("Default value for 'src': " + src)
#src_user= str(input("Input new 'src' file or press Enter to save default: "))
#if (src_user==""): scr=src_user
#print ("New value: " + src)
# директория сохраниения результатов
#Dst_dir="D:\\tmp\\R4scripts\\1\\"
Dst_dir="D:\\tmp\\R4scripts\\check2\\"
# проверяем наличие директории с данным месяцем
if not os.path.exists(Dst_dir): os.mkdir(Dst_dir)
# совпадающие id скриптов
wrName_id= ['9144898056313136335',
'9144898056313136407',
'9144898056313136422',
'9144898056313136427',
'9144905731613295118',
'9145009790413418400',
'9145304372313565525',
'9145365619813717308',
'9145433357713651293',
'9145440653013660508',
'9145441818513663039',
'9145561582513822647',
'9145561593513822692',
'9145606549213885400',
'9145606642713885702',
'9145606778113886012',
'9145614375413897455',
'9145693131413012077',
'9145693237513012206',
'9145693237513012243',
'9145700188213022726',
'9145700376013023368',
'9145727437613066197',
'9146030343913902371',
'9146055915613019855',
'9146091015513171197',
'9146339876213581497',
'9146565075013118572',
'9147385366513336542',
'9144966969513540287',
'9145813701713268553',
'9145978318813675590',
'9145978375613675841',
'9146039446313944617',
'9146054321413012164',
'9146054704713013943',
'9146054920013015022',
'9146055006513015403',
'9146055803013019330',
'9146056320513021923',
'9146056353013022129',
'9146090150013167406',
'9146090704013169809',
'9146235648513181425',
'9146338946713202249',
'9146443353813659509']
s_file=open(src)
l_file=open(Dst_dir+'all_found_scripts.txt','w')
print('Source file:' +src+' is opened: '+format(not(s_file.closed)))
print('Lof file:' +Dst_dir+'all_found_scripts.txt'+' is opened: '+format(not(l_file.closed)))
s_list=s_file.readlines()
i=0
j=0
for text in s_list:
   beg=0
   if (text.find('914')==0):
       beg = 1
       if (i>0) and (o_id in wrName_id):
          #print (o_id+'_'+name+'\n'+script)
          #print (Dst_dir+o_id +'_'+name)
          w_file = open(Dst_dir+o_id +'.txt','w')
          print ('File: '+Dst_dir+o_id +' is opened:'+format(not(w_file.closed)))
          w_file.write(script)
          w_file.close()
          print ('File: '+Dst_dir+o_id +' is closed: '+ format(w_file.closed))
          l_file.write(o_id+';'+name+'\n')
          j=j+1
       i=i+1
       spl=text.split(";")
       #print i
       o_id=spl[0]
       name=spl[1]
       script= spl[2]
  

   if (i>0) and(beg==0):
      script= script+text
      #print (str(i) +'--'+script)

print ('Total number of scripts: '+str(j) +' of '+ str(len(wrName_id)))
l_file.write('Total number of scripts: '+str(i)+'\n')
s_file.close()
print ('src file is closed: '+src+' -- '+ format(s_file.closed))
l_file.close()
print ('File \'all_found_scripts.txt\' is closed: '+src+' -- '+ format(l_file.closed))



