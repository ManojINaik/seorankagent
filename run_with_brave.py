#!/usr/bin/env python3
"""
Simple runner script for the advanced browsing agent with Brave browser
"""
import asyncio
import os
import sys
from dotenv import load_dotenv

# Add the parent directory to the Python path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../browser-use')))

# Load environment variables
load_dotenv()

# Check for API key
gemini_api_key = os.getenv('GEMINI_API_KEY')
if not gemini_api_key:
    print("ERROR: GEMINI_API_KEY is not set in your environment or .env file.")
    print("Please create a .env file with your API key or set it as an environment variable.")
    print("Example .env file content: GEMINI_API_KEY=your_api_key_here")
    sys.exit(1)

# Default Brave browser path
DEFAULT_BRAVE_PATH = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

# Default target site
DEFAULT_TARGET_SITE = "rooms.murudeshwar.co.in"

# List of search queries
SEARCH_QUERIES = [
    "best hotels in murudeshwar",
    "murudeshwar accommodation",
    "places to stay in murudeshwar",
    "murudeshwar beach resorts",
    "luxury hotels in murudeshwar",
    "murudeshwar rooms",
    "murudeshwar resort booking",
    "murudeshwar temple stay",
    "budget hotels in murudeshwar",
    "beach view hotels murudeshwar"
]

from pydantic import SecretStr
from browser_use import Agent, Browser, BrowserConfig, BrowserContextConfig, SystemPrompt
from langchain_google_genai import ChatGoogleGenerativeAI
from user_agents import DESKTOP_USER_AGENTS, MOBILE_USER_AGENTS

import random
import json
import time
import datetime

# Configure Gemini model
def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=SecretStr(gemini_api_key),
        temperature=0.7,
        top_p=0.95,
        max_output_tokens=2048,
    )

class AdvancedBrowsingAgent:
    def __init__(self, browser_path=None, headless=False):
        self.browser_path = browser_path
        self.headless = headless
        self.session_data = {
            "start_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "searches": [],
            "total_interactions": 0,
            "website_visits": 0,
            "session_duration": 0
        }
        
    async def run(self, search_queries=None, target_website=None):
        if search_queries is None:
            search_queries = SEARCH_QUERIES[:3]  # Use a subset by default
        
        if target_website is None:
            target_website = DEFAULT_TARGET_SITE
            
        print(f"Starting advanced browsing session targeting: {target_website}")
        print(f"Using browser at: {self.browser_path}")
        print(f"Will search for {len(search_queries)} keywords")
        
        # Configure the browser with executable path
        browser_config = BrowserConfig(
            headless=self.headless,
            browser_executable_path=self.browser_path
        )
        
        # Get a random device type for this session
        is_mobile = random.choice([True, False])
        device_type = "mobile" if is_mobile else "desktop"
        print(f"Using device type: {device_type}")
        
        # Select an appropriate user agent
        user_agent = random.choice(MOBILE_USER_AGENTS if is_mobile else DESKTOP_USER_AGENTS)
        
        # Configure browser context with the selected user agent and viewport
        if is_mobile:
            context_config = BrowserContextConfig(
                user_agent=user_agent,
                viewport_width=390,
                viewport_height=844,
                is_mobile=True,
                device_scale_factor=2.0
            )
        else:
            context_config = BrowserContextConfig(
                user_agent=user_agent,
                viewport_width=1920,
                viewport_height=1080,
                is_mobile=False
            )
        
        # Prepare system prompt with Gemini model
        system_prompt = SystemPrompt(
            llm=get_llm(),
            max_actions_per_step=6,
            max_steps=15,
        )
        
        # Import the main agent implementation module
        from advanced_interaction_agent import AdvancedBrowsingAgent
        
        # Create and run an instance of the advanced browsing agent
        agent = AdvancedBrowsingAgent(browser_path=self.browser_path, headless=self.headless)
        await agent.run(search_queries=search_queries, target_website=target_website)

async def main():
    # Check if Brave browser executable exists
    if not os.path.exists(DEFAULT_BRAVE_PATH):
        print(f"WARNING: Brave browser executable not found at {DEFAULT_BRAVE_PATH}")
        print("Please edit this script to provide the correct path to your Brave browser.")
        brave_path = None  # Will use default browser
    else:
        brave_path = DEFAULT_BRAVE_PATH
    
    # Create and run the advanced browsing agent with Brave browser
    agent = AdvancedBrowsingAgent(
        browser_path=brave_path, 
        headless=False  # Set to True for headless mode
    )
    
    # Run with a subset of queries to test
    await agent.run(search_queries=SEARCH_QUERIES[:3])

if __name__ == "__main__":
    asyncio.run(main()) 