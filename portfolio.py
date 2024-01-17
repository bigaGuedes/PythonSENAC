import streamlit as st

# Site Config
st.set_page_config(page_title='Portfolio - Lucas Guedes', page_icon='🦈', layout='wide')

# Header e Subheader
st.markdown("<h1 style='text-align: center;'>Olá, eu sou Lucas!👋</h1>", unsafe_allow_html=True)
subTitulo = 'Um designer em transição para uma carreira de desenvolvedor.'
st.markdown(f"<h6 style='text-align: center;'>{subTitulo}</h6>", unsafe_allow_html=True)
st.divider()

# Sidebar
with st.sidebar:
    st.image('profile.jpg', width=150)
    st.header('Lucas Guedes')
    st.markdown('*Recife/PE*')

    st.divider()
    st.write('Contato')
    st.write('✉️ [lgt.guedes@gmail.com](mailto:lgt.guedes@gmail.com)')
    st.write('🤙 (81) 9 9975 9851')

    st.divider()
    st.write('Links Úteis')
    st.write('🌐 [LinkedIn](https://br.linkedin.com/in/lucas-guedes-181b37210)')
    st.write('🐈‍⬛ [GitHub](https://github.com/bigaguedes)')

# Colunas
row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(border=True)
    tile.write('teste')