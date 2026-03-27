import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from langchain-course!")
    
    information = """
    Elon Musk is a business magnate and investor. He is the founder, CEO and chief engineer of SpaceX; angel investor, CEO and product architect of Tesla, Inc.; owner and CEO of Twitter, Inc.; owner and CEO of xAI; president of the philanthropic Musk Foundation; owner of the private jet company JetSmarter; co-founder of Neuralink and OpenAI; president of the philanthropic Future of Life Institute; and president of the philanthropic Donors Trust. He was elected a Fellow of the Royal Society (FRS) in 2018.
    He was born in Pretoria, South Africa, on June 28, 1971. He emigrated to the United States in the mid-1990s and attended the University of Pennsylvania, where he earned degrees in physics and economics. He moved to California to attend Stanford University but dropped out after two days to pursue a career in business and technology.
    In 1995, Musk co-founded Zip2, a web software company, with his brother Kimbal. The company was acquired by Compaq for nearly $300 million in 1999
    In 2002, Musk founded SpaceX, an aerospace manufacturer and space transport services company. SpaceX has launched numerous satellites, resupply missions to the International Space Station, and has developed the Starship spacecraft for interplanetary travel.
    In 2004, Musk joined Tesla Motors, Inc. (now Tesla, Inc.), an electric vehicle and clean energy company, as chairman of the board and product architect. He became
    CEO in 2008. Under his leadership, Tesla has become a major player in the electric vehicle market and has expanded into energy storage and solar energy products.
    He has also been involved in various other ventures, including the development of the Hyperloop transportation concept, the founding of The Boring Company to build underground transportation tunnels, and the creation of Neuralink to develop brain-computer interfaces.
    In addition to his business ventures, Musk has made significant contributions to the field of renewable energy and space exploration. He has been a vocal advocate for sustainable energy and has pledged to use his wealth to help combat climate change.
    He has also been recognized for his philanthropic efforts, including his donations to education, healthcare, and scientific research. In 2020, he signed the Giving Pledge, committing to give away the majority of his wealth to charitable causes.
    In summary, Elon Musk is a highly influential entrepreneur and innovator who has made significant contributions to the fields of technology, space exploration, and renewable energy. His work has had a profound impact on the world and continues to shape the future of various industries.

    Politically, Musk has been known for his outspoken and sometimes controversial statements on social media. He has expressed support for various political candidates and causes, and has been involved in debates on topics such as free speech, government regulation, and the future of artificial intelligence. Despite his polarizing nature, Musk's influence on technology and business is undeniable, and he continues to be a prominent figure in the global landscape.
    There is no doubt that Elon Musk's impact on the world will be felt for years to come, as his ventures and innovations continue to shape the future of technology and society.
    """

    summary_template = """
    Summarize the following information about Elon Musk in 3 sentences:\n\n{information}
    Give the summary in a concise and clear manner, highlighting the key points about his life, career, and impact on the world.
    Output the summary in a single paragraph, ensuring that it captures the essence of Elon Musk's contributions and influence in a way that is easy to understand for a general audience.
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)
    #llm = ChatOllama(model="phi3:latest", temperature=0)
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    
    print("\n--- SUMMARY ---")
    print(response.content)


    #print(os.getenv("GOOGLE_API_KEY"))


if __name__ == "__main__":
    main()
