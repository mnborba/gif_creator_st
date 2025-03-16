# AnimaGIF - Criador de GIFs

Uma aplicação web simples construída com Streamlit para criar GIFs animados a partir de imagens PNG, JPG ou JPEG.

![AnimaGIF Demo](https://via.placeholder.com/800x450)

## 📋 Descrição

AnimaGIF permite que você carregue múltiplas imagens e as converta em um GIF animado personalizado. Você pode ajustar a duração de cada quadro, definir o número de repetições do GIF e fazer o download do resultado final.

## ✨ Recursos

- Upload de múltiplas imagens (PNG, JPG, JPEG)
- Visualização prévia das imagens carregadas
- Personalização da duração dos quadros
- Ajuste do número de repetições do GIF
- Download do GIF gerado

## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

### Passo 1: Clone o repositório

```bash
git clone https://github.com/seu-usuario/animagif.git
cd animagif
```

### Passo 2: Crie um ambiente virtual (recomendado)

```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instale as dependências

```bash
pip install streamlit imageio Pillow
```

### Passo 4: Execute a aplicação

```bash
streamlit run app.py
```

Após executar o comando acima, o Streamlit abrirá automaticamente a aplicação no seu navegador padrão. Se isso não acontecer, você pode acessar a aplicação em [http://localhost:8501](http://localhost:8501).

## 🎮 Como usar

1. Clique em "Browse files" para selecionar múltiplas imagens (PNG, JPG ou JPEG)
2. Visualize as imagens carregadas
3. Ajuste a duração de cada quadro usando o controle deslizante
4. Selecione o número de repetições do GIF
5. Digite um nome para o arquivo GIF (opcional)
6. Clique em "Criar GIF"
7. Visualize o resultado final
8. Clique em "Download do GIF" para salvar o arquivo

## 🧪 Exemplo de código

O código principal da aplicação está disponível no arquivo `app.py`:

```python
import streamlit as st
import imageio.v3 as iio
import os
import tempfile
from PIL import Image
import io

def main():
    # Código da aplicação aqui...

if __name__ == "__main__":
    main()
```

## 📦 Dependências

- [Streamlit](https://streamlit.io/) - Framework para criação rápida de aplicações web
- [ImageIO](https://imageio.readthedocs.io/) - Biblioteca para leitura e escrita de imagens
- [Pillow](https://python-pillow.org/) - Biblioteca para processamento de imagens

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias.

1. Faça um fork do projeto
2. Crie sua feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request