#!/usr/bin/env python3
import asyncio
import os
import sys
import random
import time
import json
import datetime
from dotenv import load_dotenv
from pydantic import SecretStr

# Add paths to make imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../browser-use')))

# Import browser_use after adding to path
from browser_use import Agent, Browser, BrowserConfig, BrowserContextConfig, SystemPrompt
from user_agents import DESKTOP_USER_AGENTS, MOBILE_USER_AGENTS

# Load environment variables
load_dotenv()

# Get Gemini API key from environment variables
gemini_api_key = os.getenv('GEMINI_API_KEY')
if not gemini_api_key:
    raise ValueError('GEMINI_API_KEY is not set. Please add it to your .env file.')

# Import the ChatGoogleGenerativeAI directly here to avoid errors if not installed
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    raise ImportError(
        "The langchain_google_genai package is not installed. "
        "Please install it with: pip install langchain-google-genai"
    )

# Create a user agents file if it doesn't exist
if not os.path.exists('user_agents.py'):
    with open('user_agents.py', 'w') as f:
        f.write("""
# Desktop and mobile user agents for randomization
DESKTOP_USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
]

MOBILE_USER_AGENTS = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Android 14; Mobile; rv:109.0) Gecko/113.0 Firefox/113.0",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
]
""")

# Define target website
TARGET_WEBSITE = "rooms.murudeshwar.co.in"

# Read search queries from the keywords.txt file
def load_keywords():
    keywords_file = os.path.join(os.path.dirname(__file__), 'keywords.txt')
    if os.path.exists(keywords_file):
        with open(keywords_file, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    else:
        print(f"Warning: Keywords file not found at {keywords_file}.")
        return [
            "best hotels in murudeshwar",
            "murudeshwar accommodation",
            "places to stay in murudeshwar"
        ]

# Load keywords
SEARCH_QUERIES = load_keywords()

# Configure Gemini model
def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=SecretStr(gemini_api_key),
        temperature=0.7,
        top_p=0.95,
        max_output_tokens=2048,
    )

# Create a browser instance with the Brave browser
def create_browser(headless=False, browser_path=None, context_config=None):
    if browser_path is None:
        browser_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    
    browser_config = BrowserConfig(
        headless=headless,
        browser_binary_path=browser_path,
        keep_alive=True,
        disable_security=False,
        new_context_config=context_config  # Pass context config to the browser
    )
    
    return Browser(config=browser_config)  # Use 'config=' parameter

# Advanced human-like browsing behavior
class AdvancedBrowsingAgent:
    def __init__(self, browser_path=None, headless=False):
        self.browser_path = browser_path or "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
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
            target_website = TARGET_WEBSITE
            
        print(f"Starting advanced browsing session targeting: {target_website}")
        print(f"Will search for {len(search_queries)} keywords")
        print(f"Using Brave browser: {self.browser_path}")
        
        # Session start timer
        session_start = time.time()
        
        # Create a single browser instance that will be used for all queries
        browser = None
        try:
            for i, query in enumerate(search_queries):
                search_start = time.time()
                print(f"\n[{i+1}/{len(search_queries)}] Processing query: '{query}'")
                
                search_data = {
                    "query": query,
                    "start_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "found_target": False,
                    "completed": False,
                    "result": None,
                    "duration": 0
                }
                
                # Get a random device type for this session
                is_mobile = random.choice([True, False])
                device_type = "mobile" if is_mobile else "desktop"
                
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

                # Create/recreate the browser for each query with the specific context
                if browser:
                    await browser.close()
                browser = create_browser(
                    headless=self.headless, 
                    browser_path=self.browser_path,
                    context_config=context_config
                )

                # Define a randomized interaction time
                interaction_time = random.randint(30, 90)
                    
                # Create a task description for human-like browsing behavior
                task = (
                    f"Follow these steps in order, behaving like a human user:\n"
                    f"1. Go to Google.com\n"
                    f"2. Search for '{query}'\n"
                    f"3. Scroll through the search results naturally with pauses as if reading\n"
                    f"4. Look for the website '{target_website}' in the results\n"
                    f" 4.1. if not found, scroll down on google and click on next page button\n"
                    f" 4.2. repeat until you find the website\n"
                    f"5. If you find '{target_website}', click on it and report the position it was found at\n"
                    f"6. After clicking, interact with the website for approximately {interaction_time} seconds:\n"
                    f"   - Scroll down slowly, with occasional pauses\n"
                    f"   - Sometimes scroll back up a bit\n"
                    f"   - Click on 1-2 interesting elements like navigation links or buttons\n"
                    f"   - Spend some time on each page\n"
                    f"7. Report whether you successfully visited the target website and what actions you took."
                )
                
                try:
                    # Create an Agent with task, llm, and browser only (no browser_context_config)
                    agent = Agent(
                        task=task,
                        llm=get_llm(),
                        browser=browser
                    )
                    
                    # Execute the task
                    print(f"Executing search and browse task...")
                    result = await agent.run()
                    
                    # Record result
                    search_data["completed"] = True
                    search_data["result"] = str(result)
                    
                    # Attempt to determine if target was found based on result text
                    if target_website.lower() in result.lower() and any(term in result.lower() for term in ["clicked", "visited", "found"]):
                        search_data["found_target"] = True
                        self.session_data["website_visits"] += 1
                        print(f"✓ Found and visited target website")
                    else:
                        print(f"✗ Target website not found or not visited")
                    
                    # Increment interaction count (approximate)
                    self.session_data["total_interactions"] += 1
                    
                except Exception as e:
                    print(f"Error during task: {str(e)}")
                    search_data["result"] = f"Error: {str(e)}"
                
                # Calculate search duration
                search_duration = time.time() - search_start
                search_data["duration"] = round(search_duration, 2)
                
                # Add search data to session
                self.session_data["searches"].append(search_data)
                
                # Wait between searches with variable time
                if i < len(search_queries) - 1:
                    wait_time = random.uniform(10, 30)
                    print(f"Waiting {wait_time:.1f} seconds before next search...")
                    await asyncio.sleep(wait_time)
        
        finally:
            # Ensure browser is closed
            if browser:
                print("\nClosing browser...")
                await browser.close()
                print("Browser closed.")
        
        # Calculate total session duration
        self.session_data["session_duration"] = round(time.time() - session_start, 2)
        
        # Save session report
        self._save_session_report()
        
        print(f"\nSession completed in {self.session_data['session_duration']} seconds")
        print(f"Visited target website {self.session_data['website_visits']} times")
        print(f"Total interactions: {self.session_data['total_interactions']}")
    
    def _save_session_report(self):
        """Save session data to a JSON file"""
        reports_dir = "reports"
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
            
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{reports_dir}/browsing_session_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(self.session_data, f, indent=2)
            
        print(f"Session report saved to {filename}")

async def main():
    # Use Brave browser
    agent = AdvancedBrowsingAgent(
        browser_path="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
        headless=False
    )
    
    # Run with a subset of queries from keywords file (use 3 random keywords)
    keywords = SEARCH_QUERIES
    if len(keywords) > 3:
        keywords = random.sample(keywords, 3)
    
    await agent.run(search_queries=keywords)

if __name__ == "__main__":
    asyncio.run(main()) 