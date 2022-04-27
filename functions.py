
'''
def cria_cabecalho():
    f = open('exportDID.csv','w', encoding='UTF8',newline='')
    cabecalho = ['PRIORITY','NAME','TYPE','MASK','PORTS','INOFFICE_DEST_TYPE','INOFFICE_DEST_NUMBER','SAME_DEST_AS_INOFFICE','SPECIFIC_HOURS','SPECIFIC_HOURS_TIME','INCLUDE_HOLIDAYS','OUTOFOFFICE_DEST_TYPE','OUTOFOFFICE_DEST_NUMBER','PLAY_HOLIDAY_PROMPT']
    writer = csv.writer(f)
    writer.writerow(cabecalho)
    return(cabecalho)
'''