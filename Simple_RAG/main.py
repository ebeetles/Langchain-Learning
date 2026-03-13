from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are a computational biology PhD and expert researcher. 
Your goal is to answer questions about the provided research paper context in an intuitive and educational way for students.

CONTEXT FROM THE PAPERS:
{context}

QUESTION:
{question}

INSTRUCTIONS:
- Use only the provided context to answer the question.
- If the answer is not in the context, say that you don't have enough information from the paper.
- Explain complex concepts simply.
- Be precise and academic yet accessible.
"""

prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

while True:
    print("\n" + "="*50)
    question = input("Ask a question about the paper (q to quit): ")
    if question.lower() == "q":
        break
    
    print("\nThinking...")
    
    docs = retriever.invoke(question)
    
    context = format_docs(docs)
    
    chain = prompt | model
    result = chain.invoke({"context": context, "question": question})
    
    print("\nANSWER:")
    print(result)
