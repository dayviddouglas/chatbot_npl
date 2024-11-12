import customtkinter as ctk
import requests
from bs4 import BeautifulSoup


class Chatbot:
    def __init__(self, master):
        self.master = master
        master.title("Artemis")
        master.geometry("600x500")

        # Configuração da janela
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=0)
        master.grid_rowconfigure(2, weight=0)

        ctk.set_appearance_mode("dark")  # "light" ou "dark"
        ctk.set_default_color_theme("dark-blue")  # Temas disponíveis: "blue", "green", "dark-blue"

        # Área de texto
        self.text_area = ctk.CTkTextbox(master, width=500, height=300, wrap="word")
        self.text_area.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.text_area.insert(ctk.END, "Olá! Eu sou a Artemis, sua assistente virtual. Como posso te ajudar hoje?\n")
        self.text_area.configure(state="disabled")  # Apenas leitura na área de texto

        # Campo de entrada
        self.entry = ctk.CTkEntry(master, width=400, placeholder_text="Digite o nome do aluno...")
        self.entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.entry.bind("<Return>", self.process_input)

        # Botão de envio
        self.send_button = ctk.CTkButton(master, text="Enviar", fg_color="blue", command=self.process_input)
        self.send_button.grid(row=2, column=0, padx=20, pady=10)

    def process_input(self, event=None):
        user_input = self.entry.get()
        if not user_input:
            return

        self.text_area.configure(state="normal")
        self.text_area.insert(ctk.END, "Você: " + user_input + "\n")
        self.text_area.configure(state="disabled")

        # Processar a entrada do usuário
        response = self.get_response(user_input)

        self.text_area.configure(state="normal")
        self.text_area.insert(ctk.END, "Artemis: " + response + "\n")
        self.text_area.configure(state="disabled")
        self.entry.delete(0, ctk.END)
########################################################################
    def get_response(self, user_input):
        # Consultar a tabela do Google Sheets
        try:
            response =  requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vRrTxRg3S35qTykQKHLfnncdbcNriOynuxA33H3D9jOHyj4kjtHKBdtJ1v8EnD-civ8ovU7sFCRJ2Rj/pubhtml")
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                rows = soup.find_all('tr')
#########################################################################
                # Procurar o nome do aluno na tabela
                for row in rows[1:]:  # Pular o cabeçalho
                    cells = row.find_all('td')
                    nome_livro = cells[1].get_text().strip()
                    if nome_livro.lower() == user_input.lower():
                        nome_livro = cells[1].get_text().strip()
                        autor = cells[2].get_text().strip()
                        genero= cells[4].get_text().strip()
                        
                        return f" Nome: {nome_livro}, autor: {autor}, genero:{genero}"
                return "Aluno não encontrado. Por favor, verifique o nome e tente novamente."
            else:
                return "Desculpe, não consegui acessar a tabela no momento."
        except requests.exceptions.RequestException as e:
            return f"Erro ao conectar com a tabela: {e}"
##########################################################
if __name__ == "__main__":
    root = ctk.CTk()
    chatbot = Chatbot(root)
    root.mainloop()