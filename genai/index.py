import google.generativeai as genai

# Substitua pelo seu projeto e modelo
genai.configure(project="890323175549", api_key="AIzaSyBKbrT2tI08ljmzzcZaJV6UwG5OrkOPCFo")


def gerar_texto(prompt):
    try:
        response = genai.generate_text(prompt=prompt, model="models/gemini-pro") # ou outro modelo disponível
        return response.text
    except Exception as e:
        return f"Erro: {e}"


def traduzir(texto, idioma_destino):
    try:
        response = genai.generate_text(prompt=f"Traduza para {idioma_destino}: {texto}", model="models/gemini-pro")
        return response.text
    except Exception as e:
        return f"Erro: {e}"


# Exemplos de uso:

prompt = "Escreva um pequeno poema sobre a natureza."
poema = gerar_texto(prompt)
print(f"Poema:\n{poema}\n")

texto_ingles = "Hello, how are you?"
traducao = traduzir(texto_ingles, "português")
print(f"Tradução:\n{traducao}\n")

# Lembre-se de substituir "models/gemini-pro" pelo nome do modelo que você quer usar.  Verifique a documentação do Gemini para ver os modelos disponíveis.