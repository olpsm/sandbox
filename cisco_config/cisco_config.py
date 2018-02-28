#!/usr/bin/python3.6

import os


#############################################
#src= "p:\\Python27\\R4scripts\\test.csv"
#src= "D:\\tmp\\R4scripts\\test.csv"
src= "D:\\progs\\Python27\\Scripts\\my\\cisco_config\\22rrwip01-10-03-16.log"
#print("Default value for 'src': " + src)
#src_user= str(input("Input new 'src' file or press Enter to save default: "))
#if (src_user==""): scr=src_user
#print ("New value: " + src)

#Dst_dir="D:\\tmp\\R4scripts\\1\\"
Dst_dir="D:\\progs\\Python27\\Scripts\\my\\cisco_config\\"
# проверяем наличие директории с данным месяцем
if not os.path.exists(Dst_dir): os.mkdir(Dst_dir)


s_file=open(src)
l_file=open(Dst_dir+'loopback_with_vrf.txt','w')
l_file2=open(Dst_dir+'loopback_without_vrf.txt','w')
print('Source file:' +src+' is opened: '+format(not(s_file.closed)))
##print('Lof file:' +Dst_dir+'all_found_scripts.txt'+' is opened: '+format(not(l_file.closed)))
s_list=s_file.readlines()
##print(s_list)
beg=0
i=1
loo_vrf_list=[]
loo_novrf_list=[]
tmp_list=[]
for text in s_list:
   i+=1
   if (text.find('interface Loopback')==0):beg = 1;#print(text)

   if text.find('!')==0: beg=0
   if beg==1: tmp_list.append(text)
      
   if beg==0 and len(tmp_list)>0:
##      print (tmp_list)
      for x in tmp_list:
##         print(i,x, x.find('vrf'), end='')
         if x.find('vrf')>0:
##            print('vrf found')
            vrf=True
            break
         else:
##            print('NO vrf found')
            vrf=False
      if vrf:
         loo_vrf_list.append(tmp_list[0])
         for x in tmp_list:  
            l_file.write(x)
      else:      
         loo_novrf_list.append(tmp_list[0])
         for x in tmp_list:  
            l_file2.write(x)
            
      tmp_list=[]
##   if i%100==0 :      print('beg= ',beg,i, ' of ', len(s_list), ' in total')
print ('NO VRF','\n',*loo_novrf_list)
print('VRF','\n',*loo_vrf_list)
##print ('Total number of scripts: '+str(i))
##l_file.write('Total number of scripts: '+str(i)+'\n')
s_file.close()
print ('src file is closed: '+src+' -- '+ format(s_file.closed))
l_file.close()
l_file2.close()


