import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBlue15')

        layout = [
        [sg.Text('Indice do tronco(Máscara utilzada pelo sistema 3CX.Ex:10000,10001...):'), sg.Input(key='indicetronco',size=10)],
        [sg.Text('DDR Inicial:'), sg.Input(key='DDR inicial',size=12), sg.Text('DDR Final'), sg.Input(key='DDR final',size=12)],
        [sg.Text('__________________________________________Diurno_______________________________________')],
        [sg.Checkbox('Enviar todos os DIDs para o mesmo destino.', default=False, key='checkdestinodiu')],               
        [sg.Text('Primeiro Destino:'), sg.Input(key='primeirodestinodia',size=10), sg.Text('Tipo de destino:'), sg.Checkbox('Ramal',default=False, key='checktiporamaldiu'), sg.Checkbox('URA',default=False,key='checktipouradiu')],
        [sg.Text('_________________________________________Noturno_______________________________________')],
        [sg.Checkbox('Enviar todos os DIDs para o mesmo destino.', default=False, key='checkdestinonot')],               
        [sg.Text('Primeiro Destino:'), sg.Input(key='primeirodestinonot',size=10), sg.Text('Tipo de destino:'), sg.Checkbox('Ramal',default=False, key='checktiporamalnot'), sg.Checkbox('URA',default=False,key='checktipouranot')],
        
        ]
        
        window = sg.Window('3CX DID Rules Creator - By Michatec').layout(layout)
        self.event,self.values = window.read()
    
    def Iniciar(self):
        global index_trunk
        global n_ddr_inicial
        global n_ddr_final

        global destino_unico_diu
        global pri_destino_diu
        global tipo_diu_ramal
        global tipo_diu_ura

        global destino_unico_not
        global pri_destino_not
        global tipo_not_ramal
        global tipo_not_ura

        index_trunk=self.values['indicetronco']
        n_ddr_inicial=self.values['DDR inicial']
        n_ddr_final=self.values['DDR final']

        destino_unico_diu=self.values['checkdestinodiu']
        pri_destino_diu=self.values['primeirodestinodiu']
        tipo_diu_ramal=self.values['checktiporamaldiu']
        tipo_diu_ura=self.values['checktipouradiu']

        destino_unico_not=self.values['checkdestinonot']
        pri_destino_not=self.values['primeirodestinodnot']
        tipo_not_ramal=self.values['checktiporamalnot']
        tipo_not_ura=self.values['checktipouranot']

tela = TelaPython()
tela.Iniciar()
