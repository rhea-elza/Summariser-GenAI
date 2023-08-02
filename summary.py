from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def summarize(link):
    llm = OpenAI(temperature=0.5,model_name="text-davinci-003")
    prompt_template = PromptTemplate(
        input_variables=['link'],
        template = "You are an article summarizer. Please summarize the following content in 3-4 sentences: {link}?"
    )
    chain = LLMChain(llm=llm, prompt = prompt_template)
    return chain.run(link)