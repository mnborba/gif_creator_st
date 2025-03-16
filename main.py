import streamlit as st
import imageio.v3 as iio
import os
import tempfile
from PIL import Image
import io

def main():
    st.title("AnimaGIF - Criador de GIFs")
    st.write("Upload de imagens PNG para criar um GIF animado")
    
    # Upload de múltiplas imagens
    uploaded_files = st.file_uploader("Escolha as imagens PNG", 
                                      type=["png", "jpg", "jpeg"], 
                                      accept_multiple_files=True)
    
    if uploaded_files:
        # Mostrar as imagens carregadas
        st.write(f"**{len(uploaded_files)} imagens carregadas:**")
        cols = st.columns(min(len(uploaded_files), 4))
        for i, img_file in enumerate(uploaded_files):
            cols[i % 4].image(img_file, width=150, caption=f"Imagem {i+1}")
        
        # Parâmetros de configuração do GIF
        st.write("### Configurações do GIF")
        duration = st.slider("Duração de cada frame (ms)", 
                             min_value=100, 
                             max_value=2000, 
                             value=500, 
                             step=100)
        
        loop_options = {
            "Infinito": 0,
            "1 vez": 1,
            "3 vezes": 3,
            "5 vezes": 5
        }
        loop = st.selectbox("Número de repetições", 
                            options=list(loop_options.keys()))
        
        output_filename = st.text_input("Nome do arquivo GIF", "animacao.gif")
        if not output_filename.endswith('.gif'):
            output_filename += '.gif'
        
        # Botão para criar o GIF
        if st.button("Criar GIF"):
            with st.spinner("Criando o GIF..."):
                # Processar as imagens
                images = []
                for file in uploaded_files:
                    # Ler a imagem com imageio
                    img_data = file.getvalue()
                    img = iio.imread(img_data)
                    images.append(img)
                
                # Criar um arquivo temporário para o GIF
                with tempfile.NamedTemporaryFile(delete=False, suffix='.gif') as tmpfile:
                    temp_filename = tmpfile.name
                    # Criar o GIF
                    iio.imwrite(
                        temp_filename, 
                        images, 
                        duration=duration, 
                        loop=loop_options[loop]
                    )
                
                # Ler o arquivo GIF para exibir no Streamlit
                with open(temp_filename, 'rb') as f:
                    gif_data = f.read()
                
                # Exibir o GIF
                st.success("GIF criado com sucesso!")
                st.write("### Visualização do GIF:")
                st.image(gif_data)
                
                # Opção para download
                st.download_button(
                    label="Download do GIF",
                    data=gif_data,
                    file_name=output_filename,
                    mime="image/gif"
                )
                
                # Remover o arquivo temporário
                os.unlink(temp_filename)
    else:
        st.info("Por favor, faça upload de pelo menos duas imagens para criar um GIF.")
        
        # Mostrar exemplo
        st.write("### Exemplo:")
        st.write("""
        1. Clique em 'Browse files' para selecionar suas imagens
        2. Ajuste a duração dos frames e número de loops
        3. Dê um nome para seu arquivo GIF
        4. Clique em 'Criar GIF' para gerar a animação
        5. Visualize e faça o download do seu GIF
        """)

if __name__ == "__main__":
    main()