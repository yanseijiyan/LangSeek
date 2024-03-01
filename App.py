import os
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain.llms import OpenAI
from langchain.agents import AgentExecutor, Tool, ZeroShotAgent
from langchain.memory import ConversationBufferMemory

# Set up environment variables for API keys
os.environ["GOOGLE_CSE_ID"] = "your_google_cse_id"
os.environ["GOOGLE_API_KEY"] = "your_google_api_key"
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

# Google Search API Initialization
search = GoogleSearchAPIWrapper()

# Configure the Tool for Google Search
google_search_tool = Tool(
    name="google_search",
    func=search.run,  # The function should be adapted to return relevant content links
    description="Finds relevant content based on user's interest."
)

# Memory Configuration
memory = ConversationBufferMemory(memory_key="chat_history")

# Function to curate content from search results
def curate_content(topic):
    # Retrieve search results for the given topic
    search_results = google_search_tool.func(topic)[:5]  # Limit to top 5 results
    summaries = []

    # Generate summaries for each search result
    for result in search_results:
        # Use the agent executor to summarize the content
        summary = agent_executor.run(input=f"Summarize this text: {result}")
        summaries.append(summary)

    return summaries


# Function to print memory in a user-friendly format
def print_formatted_memory(memory):
    chat_history = memory.load_memory_variables({}).get('chat_history', '')
    if isinstance(chat_history, list):
        for message in chat_history:
            print(f"{message.sender}: {message.content}")
    else:
        print(chat_history)


# Agent Executor Configuration
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=[google_search_tool], verbose=True, memory=memory
)

# Example of using the content curation function
topic = "latest news about langchain in 2024"
content_summaries = curate_content(topic)
print("Content Summaries:")
for summary in content_summaries:
    print(summary)

# Displaying the formatted memory
print("\nFormatted Chat History:")
print_formatted_memory(memory)
