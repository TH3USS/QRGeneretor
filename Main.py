import qrcode
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox

# Função para gerar QR Code
def gerar_qr_code():
    conteudo = entrada_texto.get().strip()

    if not conteudo:
        messagebox.showwarning("Aviso", "Por favor, insira um texto ou URL.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(conteudo)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    caminho_arquivo = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        title="Salvar QR Code"
    )

    if caminho_arquivo:
        img.save(caminho_arquivo)
        messagebox.showinfo("Sucesso", f"QR Code salvo em {caminho_arquivo}")

# Configurar interface gráfica
janela = Tk()
janela.title("Gerador de QR Code")
janela.geometry("400x200")

# Elementos da interface
titulo = Label(janela, text="Gerador de QR Code", font=("Arial", 16))
titulo.pack(pady=10)

instrucao = Label(janela, text="Digite o texto ou URL para gerar o QR Code:")
instrucao.pack(pady=5)

entrada_texto = Entry(janela, width=50)
entrada_texto.pack(pady=5)

botao_gerar = Button(janela, text="Gerar QR Code", command=gerar_qr_code)
botao_gerar.pack(pady=10)

# Iniciar a interface
janela.mainloop()
