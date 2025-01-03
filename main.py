import tkinter as tk
import requests
import time

def get_public_ip():
    """Retorna o IP público consultando a API do ipify."""
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        # Exemplo de resposta: {"ip":"8.8.8.8"}
        if response.status_code == 200:
            data = response.json()
            return data.get("ip", "Can't find IP")
        else:
            return f"Erro: {response.status_code}"
    except Exception as e:
        return f"Can't find IP: {str(e)}"

def update_ip_label():
    """Função para atualizar o texto do IP."""
    current_ip = get_public_ip()
    ip_label.config(text=current_ip)
    # Agendar para chamar esta mesma função novamente depois de X milissegundos (30 seg = 30000 ms)
    window.after(30000, update_ip_label)

# === Cria a janela principal (Tk root) ===
window = tk.Tk()
window.title("IP")

# Define o tamanho e posição (exemplo: 250x60, canto superior direito)
# Ajuste x/y (1000+10) para posicionar melhor conforme o tamanho da sua tela.
window.geometry("250x60+1000+10")

# Fundo preto
window.configure(bg="black")

# Borda 3D
window.config(bd=2, relief="ridge")

# === Cria um rótulo (label) para exibir o IP ===
ip_label = tk.Label(window, 
                    text="Find IP...",   # texto inicial
                    fg="white",             # cor do texto
                    bg="black",             # cor de fundo
                    font=("Arial", 14, "bold"))  # fonte fácil de ler
ip_label.pack(expand=True, fill="both")

# === Inicializa a primeira atualização do IP ===
update_ip_label()

# Mantém a janela aberta
window.mainloop()
