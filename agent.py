from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

#to create agent
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, save_tool, wiki_tool

load_dotenv()

#setup llm



#structuring a output model
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatOpenAI(model="gpt-4.1-mini") #ChatGPT llm
#llm = ChatAnthropic(model="claude-3-5-sonnet-20241022") #Claude model

#seting a output parser
#it takes the output of llm and powers it in the model and we can use it a simple python object
parser = PydanticOutputParser(pydantic_object=ResearchResponse) 

#Setting up prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions()) #it is just the output of the parser as a string frormal instructions
#{format_instructions} will come from parser
#{chat_history} and {agent_scratchpad} will be generated automatically

#tools for agent
tools = [search_tool, save_tool, wiki_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

#creating agent
agent = create_tool_calling_agent(
    llm = llm,
    prompt=prompt,
    tools=[]
)

#it is a way to execute the agent in a proper way
agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)
query = input("How can I help you in Research? ")
raw_response = agent_executor.invoke({"query":query})
#print(raw_response)

try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)
#response = llm.invoke("What is the meaning of life?") #run the llm locally in computer
#print(response)
