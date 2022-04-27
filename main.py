import csv
from graphical_interface import index_trunk,n_ddr_inicial,n_ddr_final,destino_unico_diu,pri_destino_diu,tipo_diu_ramal,tipo_diu_ura,destino_unico_not,pri_destino_not,tipo_not_ramal,tipo_not_ura

dest_diu=(int(pri_destino_diu)-1)
ddr_inicial=int(n_ddr_inicial)
ddr_final=int(n_ddr_final)
dest_not=(int(pri_destino_not)-1)
trunk_id=[int(index_trunk)]
diu_type=''
notu_type=''

f = open('exportDID.csv','w', encoding='UTF8',newline='')
cabecalho = ['PRIORITY','NAME','TYPE','MASK','PORTS','INOFFICE_DEST_TYPE','INOFFICE_DEST_NUMBER','SAME_DEST_AS_INOFFICE','SPECIFIC_HOURS','SPECIFIC_HOURS_TIME','INCLUDE_HOLIDAYS','OUTOFOFFICE_DEST_TYPE','OUTOFOFFICE_DEST_NUMBER','PLAY_HOLIDAY_PROMPT']
writer = csv.writer(f)
writer.writerow(cabecalho)

for ddr in range(ddr_inicial,ddr_final+1):
    ddr+1
    #VALIDAÇÃO DE CHEKBOXES DE DESTINO UNICO
    if destino_unico_diu == True:
        dest_diu=pri_destino_diu
    else:
        dest_diu+=1
    if destino_unico_not == True:
        dest_not=pri_destino_not
    else:
        dest_not+=1
    #VALIDAÇÃO DE CHECKBOXES DE TIPOS DE DESTINO
    if tipo_diu_ramal == True:
        diu_type=2
    elif tipo_diu_ura == True:
        diu_type=5
    elif tipo_diu_ramal == tipo_diu_ura:
        diu_type=2
    if tipo_not_ramal == True:
        notu_type=2
    elif tipo_not_ura == True:
        notu_type=5
    elif tipo_not_ramal == tipo_not_ura:
        notu_type=2       
    data=['','','1',ddr,trunk_id,diu_type,dest_diu,'0','0','','',notu_type,dest_not,'0']   
    with open('exportDID.csv', 'a', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)                                                                                          
        writer.writerow(data)
        print(data)
