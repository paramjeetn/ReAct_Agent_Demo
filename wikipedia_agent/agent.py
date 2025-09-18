"""
Simplified Wikipedia Agent using Google ADK
Single agent in loop with wikipedia tool and exit_loop
"""

import os
from google.adk.agents import Agent, LoopAgent
from google.adk.tools import FunctionTool
from google.adk.tools.exit_loop_tool import exit_loop
from dotenv import load_dotenv

# Import our wikipedia search function
from .tools import wikipedia_search

# Load environment variables
load_dotenv()

# 1. Tool: Wikipedia Search (FunctionTool)
wikipedia_tool = FunctionTool(wikipedia_search)

# 2. Wikipedia Search Agent (searches iteratively until finding answer)
wikipedia_agent = Agent(
    name="wikipedia_searcher",
    model="gemini-2.0-flash-exp",
    instruction="""
You are a Wikipedia researcher that searches iteratively until finding the exact answer.

Your process:
1. Use wikipedia_search with the user's question to search Wikipedia
2. Evaluate if the result answers the user's question completely
3. If YES: Provide the answer and call exit_loop() to stop searching
4. If NO: Try a different search query and continue

Keep refining your search until you find the exact answer the user wants.

Example:
- User asks: "When did Gandhi die?"
- Search "Gandhi death" → Not specific enough, try again
- Search "Mahatma Gandhi assassination date" → Found: January 30, 1948 → exit_loop()

Always explain your reasoning and call exit_loop() when you find the complete answer.
""",
    tools=[wikipedia_tool, FunctionTool(exit_loop)]
)

# 3. LoopAgent that runs the wikipedia search agent
wikipedia_loop = LoopAgent(
    name="wikipedia_search_loop",
    sub_agents=[wikipedia_agent],
    max_iterations=5
)

# 4. Root agent is the LoopAgent
root_agent = wikipedia_loop

if __name__ == "__main__":
    print("Simplified Wikipedia Search Agent Created!")
    print("\nArchitecture:")
    print("- Root Agent: Custom agent that manages the process")
    print("- Loop Agent: Iterates until answer found")
    print("- Check Agent: LLM that searches and decides when to stop")
    print("- Wikipedia Tool: Searches Wikipedia with query refinement")
    print("\nFlow:")
    print("User → Root Agent → Loop Agent → [Check Agent + Wikipedia Tool] → Answer")
    print("\nThe agent will keep refining searches until it finds exactly what you're looking for!")
    print("\nExample: 'When did Gandhi die?' → Searches → Refines → Finds → Stops")