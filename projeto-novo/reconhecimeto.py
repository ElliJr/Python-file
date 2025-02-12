import os
from dotenv import load_dotenv
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# Carrega variáveis de ambiente
load_dotenv()

# Obtém chave da API do OpenAI a partir das variáveis de ambiente
api_key = os.getenv("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")
if not api_key:
    raise ValueError("Chave da API do OpenAI não encontrada. Certifique-se de configurar o arquivo .env corretamente.")

# Configura o modelo da OpenAI
llm = OpenAI(temperature=0.7, openai_api_key=api_key)

# Define o template de prompt
template = "Usuário: {user_input}\nAssistente:"  # Simples estrutura de prompt
prompt = PromptTemplate(input_variables=["user_input"], template=template)

# Cria uma cadeia de LLM
dialog_chain = LLMChain(llm=llm, prompt=prompt)

def chatbot():
    print("Chatbot iniciado! Digite 'sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Encerrando chatbot. Até logo!")
            break
        try:
            response = dialog_chain.run(user_input)
            print(f"Bot: {response.strip()}")
        except Exception as e:
            print("Ocorreu um erro ao gerar a resposta:", e)

if __name__ == "__main__":
    chatbot()
