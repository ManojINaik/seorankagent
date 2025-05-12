#!/usr/bin/env python3
import asyncio
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, BrowserSettings

# Load environment variables
load_dotenv()

# Define custom functions for SEO optimization
async def seo_agent(task, headless=False, verbose=True):
    """
    Create and run a browser automation agent for SEO tasks
    
    Args:
        task (str): The SEO task description
        headless (bool): Whether to run the browser in headless mode
        verbose (bool): Whether to display verbose output
    
    Returns:
        str: The result of the agent's task
    """
    # Configure browser settings
    browser_settings = BrowserSettings(
        headless=headless,
        viewport_size={"width": 1280, "height": 800},
        default_timeout=60000,  # 60 seconds
        slow_mo=100,  # Slow down actions by 100ms for better visibility
    )
    
    # Initialize the agent with Gemini model
    agent = Agent(
        task=task,
        llm=ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",  # Using Gemini 1.5 Flash (adjust as needed)
            temperature=0.2,
            convert_system_message_to_human=True,
        ),
        browser_settings=browser_settings,
        verbose=verbose,
    )
    
    # Run the agent
    result = await agent.run()
    return result

async def main():
    # Define your SEO tasks here
    seo_task = """
    Perform the following SEO optimization tasks:
    1. Search Google for "{keyword}"
    2. Analyze the top 5 search results to understand ranking factors
    3. Visit my website at {website_url}
    4. Provide recommendations for optimizing the site to rank higher for "{keyword}"
    5. Save the analysis and recommendations to a file
    """
    
    # Replace with your actual keyword and website
    keyword = input("Enter the target keyword: ")
    website_url = input("Enter your website URL: ")
    
    # Format the task with the provided information
    formatted_task = seo_task.format(keyword=keyword, website_url=website_url)
    
    print(f"Starting SEO optimization for keyword '{keyword}' on {website_url}")
    result = await seo_agent(formatted_task, headless=False, verbose=True)
    
    print("\nSEO Agent Results:")
    print("=" * 50)
    print(result)

if __name__ == "__main__":
    asyncio.run(main()) 