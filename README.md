# LangChain Agent Executor Project

Welcome to the LangChain Agent Executor Project repository! This project demonstrates the integration of various LangChain functionalities, including the use of external APIs such as the Google Search API, to create an agent executor that performs searches based on user interests and summarizes relevant content found. The goal is to provide a solution for automated content curation, leveraging LangChain's text comprehension and generation capabilities.

## Objectives

- Facilitate the research and curation of relevant content on the internet.
- Demonstrate the integration of LangChain with external APIs and the creation of intelligent agents.
- Provide a foundation for the development of more complex applications focused on the automation of search tasks and information synthesis.

## Prerequisites

- Python 3.8 or higher.
- Internet access for package installation and to perform searches using the Google API.

## Installation

To set up the environment and install the necessary dependencies, execute the following command:

```bash
pip install -r requeriments.txt
```
## Usage
Configure the environment variables with your Google and OpenAI API keys:
python
Copy code
```
import os

os.environ["GOOGLE_CSE_ID"] = "<your_google_cse_id>"
os.environ["GOOGLE_API_KEY"] = "<your_google_api_key>"
os.environ["OPENAI_API_KEY"] = "<your_openai_api_key>"
Initialize and use the agent executor to perform searches and content curation:
python
Copy code
# Google Search API Initialization
search = GoogleSearchAPIWrapper()

# Create and configure a Tool for Google Search
google_search_tool = Tool(
    name="google_search",
    func=search.run,  # Adapt the function to return relevant content links
    description="Finds relevant content based on user interest."
)

# Execute the content curation function for a specific topic
topic = "latest news on langchain in 2024 in English"
content_summaries = curate_content(topic)
print("Summaries of Found Content:")
for summary in content_summaries:
    print(summary)
```
## Features
Integration with the Google Search API: Allows searching for internet content based on specific user interests.
Automated Content Curation: Summarizes the contents found, providing a quick and efficient overview.
Conversation Memory: Stores the interaction history, improving the contextualization of responses and user experience.
