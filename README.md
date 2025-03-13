**📚 Passo a Passo para Usar o Buscador de Livros no Android**  

---

### **Pré-requisitos**  
1. **Termux instalado** (baixe [aqui](https://f-droid.org/repo/com.termux_118.apk)).  
2. Conexão com internet.  
3. Permissão para acessar armazenamento (ativa no Termux).  

---

### **Instalação**  
Siga os comandos abaixo no Termux (copie e cole):  

1. **Atualize os pacotes:**  
   ```bash
   pkg update && pkg upgrade -y
   ```  

2. **Instale o Python e ferramentas:**  
   ```bash
   pkg install python git -y
   ```  

3. **Instale as dependências do script:**  
   ```bash
   pip install requests beautifulsoup4 googlesearch-python
   ```  

4. **Baixe o script do GitHub:**  
   ```bash
   git clone https://github.com/JonJonesBR/Buscador-de-livros.git
   ```  

5. **Acesse a pasta do projeto:**  
   ```bash
   cd Buscador-de-livros
   ```  

---

### **Execução**  
1. **Inicie o script:**  
   ```bash
   python buscador_livros_google.py
   ```  

2. **Permita acesso ao armazenamento:**  
   - Se aparecer uma mensagem de permissão, digite:  
     ```bash
     termux-setup-storage
     ```  
   - Toque em **"Permitir"** quando solicitado.  

---

### **Como Usar**  
1. **Busca de livros:**  
   - Digite o **título, autor ou palavras-chave** do livro (ex: *Dom Casmurro Machado de Assis*).  
   - Escolha se quer livros em **Português do Brasil** (s/n).  
   - Selecione o **tipo de arquivo** (PDF, EPUB, etc.) ou digite *todos*.  

   > 💡 Exemplo de uso:  
   > ```  
   > Título: Dom Casmurro  
   > Idioma: s  
   > Tipo de arquivo: pdf  
   > ```  

2. **Resultados:**  
   - O script mostrará **5 links por vez**.  
   - Digite **`s`** para mais links ou **`n`** para parar.  

3. **Download:**  
   - Digite o **número do link** para baixar (ex: *1*).  
   - O arquivo será salvo em: **`Arquivos > Download`** do seu celular.  

4. **Comandos especiais:**  
   - **`menu`**: Volta ao início para nova pesquisa.  
   - **`sair`**: Encerra o programa.  

---

### **Dicas Importantes**  
- Verifique se o **Termux** tem permissão para acessar arquivos.  
- Se houver erro de instalação, repita os passos ou consulte o [repositório oficial](https://github.com/JonJonesBR/Buscador-de-livros).  
- Links inválidos? Tente refazer a pesquisa com termos diferentes.  

---

**✅ Pronto! Agora você pode buscar e baixar livros diretamente do Termux!**  

🔗 **Repositório do Projeto:** [Buscador-de-livros](https://github.com/JonJonesBR/Buscador-de-livros)