from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class PedidoApp(BoxLayout):
    def tipo_pagamento(self, tipo_p):
        if tipo_p == 'À vista (espécie)':
            self.ids.mensagem.text = "Pagamento a vista"
        elif tipo_p == 'À vista (pix)':
            self.ids.mensagem.text = "Pagamento por pix"
        elif tipo_p == 'À vista (cartão de crédito)':
            self.ids.mensagem.text = "Pagamento por cartão de crédito"
        elif tipo_p == 'Parcelado 2x no cartão de crédito':
            self.ids.mensagem.text = "Pagamento parcelado 2x no cartão de crédito"
        
    def sair(self, instance):
        # Função para sair da aplicação
        App.get_running_app().stop()

        #Dicionário para associar funções aos botões
    funcoes_botoes = {
        'sair': sair
    }
    
    def limpar_campos(self):
        self.ids.nome_usuario.text = ''
        self.ids.q1.text = ''
        self.ids.q2.text = ''
        self.ids.q3.text = ''
        self.ids.q4.text = ''
        self.ids.q5.text = ''
        self.ids.q6.text = ''
        self.ids.sp1.text = 'Escolha o tipo de pagamento'
        self.ids.tmnho.text = 'Esolha o tamanho'
        self.ids.q_queijo.active = False
        self.ids.Mus.active = False
        self.ids.clabrsa.active = False
        self.ids.portu.active = False
        self.ids.cat.active = False
        self.ids.cro.active = False
        self.ids.mensagem.text=''

    def calcular_total(self):
        valor_total = 0

        sabores_quantidades = {
            'Quatro queijos': self.ids.q1.text,
            'Mussarela': self.ids.q2.text,
            'Calabresa': self.ids.q3.text,
            'Portuguesa': self.ids.q4.text,
            'Frango c/ Catupiry': self.ids.q5.text,
            'Crocante': self.ids.q6.text
        }

        valores_sabores = {
            'Quatro queijos': 25,
            'Mussarela': 20,
            'Calabresa': 22,
            'Portuguesa': 23,
            'Frango c/ Catupiry': 24,
            'Crocante': 30
        }

        for sabor, quantidade_str in sabores_quantidades.items():
            # Se a quantidade for uma string vazia, consideramos como 0
            if not quantidade_str:
                quantidade = 0
            else:
                try:
                    quantidade = int(quantidade_str)
                except ValueError:
                    self.ids.mensagem.text = f'Quantidade inválida para {sabor}, tente novamente!'
                    return

                # Adiciona o valor do sabor ao valor total
                valor_total += quantidade * valores_sabores[sabor]

        tamanho_selecionado = self.ids.tmnho.text

        # Chame o método para calcular o valor da pizza com base nos sabores selecionados
        valor_pizza = self.calcular_valor_pizza()

        # Adicione o valor do tamanho da pizza ao valor total
        if tamanho_selecionado == 'Pequena':
            valor_total *= 1.0  # Multiplicação pelo tamanho
        elif tamanho_selecionado == 'Média':
            valor_total *= 1.2
        elif tamanho_selecionado == 'Grande':
            valor_total *= 1.5
        elif tamanho_selecionado == 'Gigante':
            valor_total *= 2.0

        # Multiplique pelo número de pizzas
        quantidade_total = sum(1 for quantidade_str in sabores_quantidades.values() if quantidade_str.strip())
        valor_total *= quantidade_total

        nome_usuario = self.ids.nome_usuario.text
        self.ids.mensagem.text = f'O valor da compra de {nome_usuario} totalizou R$ {valor_total:.2f}'

    def calcular_valor_pizza(self):
        valor_pizza = 0

        # Valores fictícios para cada sabor
        valores_sabores = {
            'Quatro queijos': 25,
            'Mussarela': 20,
            'Calabresa': 22,
            'Portuguesa': 23,
            'Frango c/ Catupiry': 24,
            'Crocante': 30
        }

        # Verifique quais checkboxes estão marcados e some os valores dos sabores selecionados
        if self.ids.q_queijo.active:
            valor_pizza += valores_sabores['Quatro queijos']
        if self.ids.Mus.active:
            valor_pizza += valores_sabores['Mussarela']
        if self.ids.clabrsa.active:
            valor_pizza += valores_sabores['Calabresa']
        if self.ids.portu.active:
            valor_pizza += valores_sabores['Portuguesa']
        if self.ids.cat.active:
            valor_pizza += valores_sabores['Frango c/ Catupiry']
        if self.ids.cro.active:
            valor_pizza += valores_sabores['Crocante']

        return valor_pizza


                
class MainApp(App):
    def build(self):
        
        return PedidoApp()
    
if __name__ == '__main__':
    MainApp().run()
