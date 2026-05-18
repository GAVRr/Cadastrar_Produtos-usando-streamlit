import streamlit as st

st.title('Cadastro de produtos')

produto = st.text_input('Produto:')

preco_produto = st.number_input('Preço do produto:')

desconto = st.slider('Porcentagem  de desconto:')

if st.button('Cadastrar Produto'):
    if not produto:
        st.warning('Produto não cadastrado!')
    elif not preco_produto:
        st.warning('Preço não cadastrado!')

    else:
        valor_desconto = preco_produto * (desconto/100)
        preco_com_desconto = preco_produto - valor_desconto
        with open('produtos.txt','a',encoding='utf-8') as adicionar_produto:
            adicionar_produto.write(f'{produto};{preco_produto:.2f};{desconto};{preco_com_desconto}\n')
        st.success(f'Produto: {produto} adicionado com sucesso!')

st.divider()

if st.button('Verificar lista de produtos'):
    st.subheader('Histórico de produtos')
    lista_produtos = []

    try:
        with open('produtos.txt' , 'r',encoding='utf-8') as leitura_produtos:
            for linha in leitura_produtos:
                if linha.strip():
                    dados_produtos = linha.strip().split(';')

                    if len(dados_produtos) == 4:
                        lista_produtos.append({
                            'Produto': dados_produtos[0],
                            'Preço original': dados_produtos[1],
                            'Desconto': f"{dados_produtos[2]}%",
                            'Preço final': f"{dados_produtos[3]}"
                        })

    except FileNotFoundError:
        st.info("Nenhum produto cadastrdado ainda.")

    if lista_produtos:
        st.dataframe(lista_produtos)