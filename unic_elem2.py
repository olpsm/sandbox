Elements=['IMS_CS2K_PDTC_Port_Validation',
'IMS_CS2K_OSSGate_QueryDirectoryNumber',
'IMS_CS2K_OSSGate_QueryMapciLEN',
'IMS_CS2K_GWC_Port_Validation',
'IMS_CS2K_TDM_Port_Validation',
'IMS_CS2K_GWC_Port_Validation',
'IMS_CS2K_ValidateCLLI',
'IMS_CS2K_CountSUPERTKG',
'IMS_CS2K_ValidateCLLI',
'IMS_CS2K_ValidateTrunkGroupType',
'IMS_CS2K_Query_LogicalTerminal',
'IMS_CS2K_QueryDirectoryNumber',
'IMS_CS2K_ValidateRoutingRecords',
'IMS_CS2K_CountIndex',
'IMS_CS2K_Query_LogicalTerminal',
'IMS_CS2K_QueryDirectoryNumber',
'IMS_CS2K_CountIndex',
'IMS_CS2K_DNValidation',
'IMS_CS2K_CheckStatus',
'IMS_CS2K_QueryDirectoryNumber',
'IMS_CS2K_QueryDirectoryNumber',
'IMS_CS2K_Check_CLLI',
'IMS_CS2K_SIP_STATE_Validation',
'IMS_CS2K_AdminValidation',
'IMS_CS2K_SIP_STATE_Validation',
'IMS_CS2K_SIP_STATE_Validation',
'IMS_CS2K_OSSGate_QueryLineEquipmentNumber',
'IMS_CS2K_OSSGate_QueryDirectoryNumber']
UnicElem=[]
NoUnicElem=[]
a=0
for i in Elements:
       if i not in UnicElem: UnicElem.append(i); a+=1
       else:
         if i not in NoUnicElem: NoUnicElem.append(i)
print ('list of unic elems: ', UnicElem)
print ('original ammount =',len(Elements))
print ('unic ammount =',a)
print ('list of repeated elems: ', NoUnicElem)


      
    
