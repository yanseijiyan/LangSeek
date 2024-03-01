import os
# Importing necessary modules from langchain_community and langchain
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain.llms import OpenAI
from langchain.agents import AgentExecutor, ZeroShotAgent
from langchain.memory import ConversationBufferMemory

# Setting up environment variables for API keys with placeholders for security
os.environ["GOOGLE_CSE_ID"] = "your_google_cse_id_here"
os.environ["GOOGLE_API_KEY"] = "your_google_api_key_here"
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"

# Initialize the Google Search API Wrapper
search = GoogleSearchAPIWrapper()

# Configure the Google Search Tool
google_search_tool = Tool(
    name="google_search",
    func=search.run,  # The function should be adapted to return relevant content links
    description="Finds relevant content based on user's interest."
)

# Setting up conversation buffer memory for chat history
memory = ConversationBufferMemory(memory_key="chat_history")

# Function to curate content based on a given topic
def curate_content(topic):
    # Fetching top 5 search results for the topic
    search_results = google_search_tool.func(topic)[:5]
    summaries = []

    # Summarizing each search result
    for result in search_results:
        summary = agent_executor.run(input=f"Summarize this text: {result}")
        summaries.append(summary)

    return summaries

# Function to display the memory in a user-friendly way
def print_formatted_memory(memory):
    chat_history = memory.load_memory_variables({}).get('chat_history', '')
    if isinstance(chat_history, list):
        for message in chat_history:
            print(f"{message.sender}: {message.content}")
    else:
        print(chat_history)

# Example of using the content curation function
topic = "latest news on langchain in 2024 in English"
content_summaries = curate_content(topic)
print("Content Summaries Found:")
for summary in content_summaries:
    print(summary)

# Displaying formatted chat history
print("\nFormatted Chat History:")
print_formatted_memory(memory)
