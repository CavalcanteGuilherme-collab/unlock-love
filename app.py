import streamlit as st
from datetime import datetime

# Texto do presente
texto_presente = """
Oiie meu amor, tudo bem?

Eu fiquei pensando no que te escrever hoje… e a verdade é que, mesmo sem saber usar as palavras mais bonitas, eu sei exatamente o que sinto: eu te amo.

Quero passar muitos e muitos dias ao seu lado, criando momentos com você, vivendo tudo isso juntos. E também queria te pedir desculpas por não fazer nada grandioso hoje, nem conseguir te dar um presente. Mas, de coração, tudo isso que estou fazendo é sincero, é verdadeiro… é meu.

Como eu prometi, estou escrevendo o que vem na minha mente, e o que mais vem é gratidão. Obrigado por esses 3 meses na minha vida, por me deixar fazer parte da sua também.

Eu te amo muito, meu amor. E pode ter certeza: esse é só o começo. Ainda vamos comemorar muitos meses, anos e muitas conquistas juntos.

E pode deixar… eu ainda vou melhorar esse “app” aqui, viu? ❤️
"""

# Estado da aplicação
if "etapa" not in st.session_state:
    st.session_state.etapa = "login"

st.title("💖 Um presente pra você")

# ETAPA 1 - LOGIN
if st.session_state.etapa == "login":
    st.subheader("🔐 Acesso especial")

    login = st.text_input("Login")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if login == "a" and senha == "a":
            st.session_state.etapa = "data"
            st.rerun()
        else:
            st.error("Login ou senha incorretos 😢")

# ETAPA 2 - DATA
elif st.session_state.etapa == "data":
    st.subheader("📅 Primeira pergunta")

    data = st.text_input("Qual é o dia mais importante para nós? (dd/mm/aaaa)")

    if st.button("Confirmar"):
        try:
            data_usuario = datetime.strptime(data, "%d/%m/%Y").date()
            data_correta = datetime.strptime("03/01/2026", "%d/%m/%Y").date()

            if data_usuario == data_correta:
                st.session_state.etapa = "comida"
                st.rerun()
            else:
                st.error("Data incorreta 😢")
        except:
            st.error("Formato inválido! Use dd/mm/aaaa")

# ETAPA 3 - COMIDA
elif st.session_state.etapa == "comida":
    st.subheader("🍣 Segunda pergunta")

    comida = st.text_input("O que amamos comer juntos?")

    if st.button("Confirmar"):
        if comida.lower() == "sushi":
            st.session_state.etapa = "lugar"
            st.rerun()
        else:
            st.error("Resposta incorreta 😢")

# ETAPA 4 - LUGAR
elif st.session_state.etapa == "lugar":
    st.subheader("🌳 Última pergunta")

    lugar = st.text_input("Qual é o lugar que mais importou para mim esse ano?")

    if st.button("Confirmar"):
        if lugar.lower() == "parque":
            st.session_state.etapa = "presente"
            st.rerun()
        else:
            st.error("Resposta incorreta 😢")

# ETAPA FINAL - PRESENTE
elif st.session_state.etapa == "presente":
    st.success("💖 Você acertou tudo!")

    if st.button("🎁 Abrir presente"):
        st.markdown(texto_presente)