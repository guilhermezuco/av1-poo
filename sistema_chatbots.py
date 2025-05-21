from abc import ABC, abstractmethod
from datetime import datetime

# Classe base abstrata para todas as mensagens
class Mensagem(ABC):
    def __init__(self, conteudo, data_envio=None):
        self.conteudo = conteudo
        self.data_envio = data_envio if data_envio else datetime.now()
    
    @abstractmethod
    def exibir_informacoes(self):
        pass

# Classes concretas para cada tipo de mensagem
class MensagemTexto(Mensagem):
    def __init__(self, conteudo, data_envio=None):
        super().__init__(conteudo, data_envio)
    
    def exibir_informacoes(self):
        return f"Texto: {self.conteudo} | Enviada em: {self.data_envio.strftime('%d/%m/%Y %H:%M')}"

class MensagemVideo(Mensagem):
    def __init__(self, conteudo, arquivo, formato, duracao, data_envio=None):
        super().__init__(conteudo, data_envio)
        self.arquivo = arquivo
        self.formato = formato
        self.duracao = duracao
    
    def exibir_informacoes(self):
        return (f"Vídeo: {self.conteudo} | Arquivo: {self.arquivo} | "
                f"Formato: {self.formato} | Duração: {self.duracao}s | "
                f"Enviada em: {self.data_envio.strftime('%d/%m/%Y %H:%M')}")

class MensagemFoto(Mensagem):
    def __init__(self, conteudo, arquivo, formato, data_envio=None):
        super().__init__(conteudo, data_envio)
        self.arquivo = arquivo
        self.formato = formato
    
    def exibir_informacoes(self):
        return (f"Foto: {self.conteudo} | Arquivo: {self.arquivo} | "
                f"Formato: {self.formato} | "
                f"Enviada em: {self.data_envio.strftime('%d/%m/%Y %H:%M')}")

class MensagemArquivo(Mensagem):
    def __init__(self, conteudo, arquivo, formato, data_envio=None):
        super().__init__(conteudo, data_envio)
        self.arquivo = arquivo
        self.formato = formato
    
    def exibir_informacoes(self):
        return (f"Arquivo: {self.conteudo} | Arquivo: {self.arquivo} | "
                f"Formato: {self.formato} | "
                f"Enviada em: {self.data_envio.strftime('%d/%m/%Y %H:%M')}")

# Classe base abstrata para os canais
class Canal(ABC):
    def __init__(self, destinatario):
        self.destinatario = destinatario
    
    @abstractmethod
    def enviar_mensagem(self, mensagem):
        pass

# Classes concretas para cada canal
class WhatsApp(Canal):
    def enviar_mensagem(self, mensagem):
        print(f"Enviando para WhatsApp - Número: {self.destinatario}")
        print(mensagem.exibir_informacoes())
        print("--- Mensagem enviada com sucesso! ---\n")

class Telegram(Canal):
    def __init__(self, destinatario, eh_numero=True):
        super().__init__(destinatario)
        self.eh_numero = eh_numero
    
    def enviar_mensagem(self, mensagem):
        tipo_destino = "Número" if self.eh_numero else "Usuário"
        print(f"Enviando para Telegram - {tipo_destino}: {self.destinatario}")
        print(mensagem.exibir_informacoes())
        print("--- Mensagem enviada com sucesso! ---\n")

class Facebook(Canal):
    def enviar_mensagem(self, mensagem):
        print(f"Enviando para Facebook - Usuário: {self.destinatario}")
        print(mensagem.exibir_informacoes())
        print("--- Mensagem enviada com sucesso! ---\n")

class Instagram(Canal):
    def enviar_mensagem(self, mensagem):
        print(f"Enviando para Instagram - Usuário: {self.destinatario}")
        print(mensagem.exibir_informacoes())
        print("--- Mensagem enviada com sucesso! ---\n")

# Função para demonstrar o uso
def demonstrar_envios():
    # Criando mensagens
    msg_texto = MensagemTexto("Olá, tudo bem?")
    msg_video = MensagemVideo("Confira nosso novo produto!", "produto.mp4", "mp4", 120)
    msg_foto = MensagemFoto("Veja esta paisagem", "paisagem.jpg", "jpg")
    msg_arquivo = MensagemArquivo("Documento importante", "contrato.pdf", "pdf")

    # Criando canais
    whatsapp = WhatsApp("+5511999999999")
    telegram_numero = Telegram("+5511888888888")
    telegram_usuario = Telegram("@pedro_silva", False)
    facebook = Facebook("pedro.silva")
    instagram = Instagram("@pedro.silva.photo")

    # Enviando mensagens pelos canais
    whatsapp.enviar_mensagem(msg_texto)
    telegram_numero.enviar_mensagem(msg_video)
    telegram_usuario.enviar_mensagem(msg_foto)
    facebook.enviar_mensagem(msg_arquivo)
    instagram.enviar_mensagem(msg_texto)

if __name__ == "__main__":
    demonstrar_envios()
