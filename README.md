# LangChain Agent Executor Project

## This project demonstrates the integration of various LangChain functionalities, including the use of external APIs such as the Google Search API, to create an agent executor that conducts searches based on user interests and summarizes relevant content found. The goal is to provide a solution for automated content curation, leveraging LangChain's capabilities for understanding and generating text.

# Objectives
1. Facilitate the search and curation of relevant content on the internet.
2. Demonstrate the integration of LangChain with external APIs and the creation of intelligent agents.
3. Provide a foundation for the development of more complex applications focused on automating search and information synthesis tasks.

   
# Prerequisites
1. Python 3.8 or higher.
2. Internet access for package installation and to conduct searches using the Google API.

   
# Installation
1. To set up the environment and install the necessary dependencies, execute:

bash
## Copy code
pip install -r requeriments

## Usage
Configure the environment variables with your Google and OpenAI API keys:

python
## Copy code
os.environ["GOOGLE_CSE_ID"] = "<your_google_cse_id>"
os.environ["GOOGLE_API_KEY"] = "<your_google_api_key>"
os.environ["OPENAI_API_KEY"] = "<your_openai_api_key>"

## Initialize and use the agent executor to conduct searches and content curation:

python
## Copy code
# Initialization of the Google Search API
search = GoogleSearchAPIWrapper()

# Create and configure a Tool for Google Search
google_search_tool = Tool(
    name="google_search",
    func=search.run,  # Adapt the function to return relevant content links
    description="Finds relevant content based on user interest."
)

# Execute the content curation function for a specific topic
topic = "latest news about langchain in 2024 in English"
content_summaries = curate_content(topic)
print("Summaries of Found Content:")
for summary in content_summaries:
    print(summary)
Features
Integration with the Google Search API: Allows searching for content on the internet based on specific user interests.
Automated Content Curation: Summarizes found content, providing a quick and efficient overview.
Conversational Memory: Stores interaction history, improving response contextualization and user experience.
