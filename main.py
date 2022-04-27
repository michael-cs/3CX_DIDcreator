import csv
r_inicial=1000
r=(r_inicial-1)
ddr_inicial=32045500
ddr_final=32045505
atd_noturno=8002
trunk_id=[10000]
diu_type=2
notu_type=5
f = open('exportDID.csv','w', encoding='UTF8',newline='')
cabecalho = ['PRIORITY','NAME','TYPE','MASK','PORTS','INOFFICE_DEST_TYPE','INOFFICE_DEST_NUMBER','SAME_DEST_AS_INOFFICE','SPECIFIC_HOURS','SPECIFIC_HOURS_TIME','INCLUDE_HOLIDAYS','OUTOFOFFICE_DEST_TYPE','OUTOFOFFICE_DEST_NUMBER','PLAY_HOLIDAY_PROMPT']
writer = csv.writer(f)
writer.writerow(cabecalho)

for i in range(ddr_inicial,ddr_final+1):
    i+1
    r+=1
    data=['','','1',i,trunk_id,diu_type,r,'0','0','','',notu_type,atd_noturno,'0']   
    with open('exportDID.csv', 'a', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)                                                                                          
        writer.writerow(data)
        print(data)
