#!/usr/bin/env python3
import asyncio
import os
import random
import time
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, BrowserSettings, AgentSettings

# Load environment variables
load_dotenv()

class HumanInteractionAgent:
    """
    Agent that simulates human-like browsing behavior to interact with
    a specific website through Google searches
    """
    
    def __init__(self, target_site="rooms.murudeshwar.co.in", headless=False, verbose=True):
        """Initialize the agent with configuration settings"""
        self.target_site = target_site
        self.headless = headless
        self.verbose = verbose
        self.results_dir = "browsing_logs"
        os.makedirs(self.results_dir, exist_ok=True)
        
    async def setup_agent(self, task):
        """Set up the browser-use agent with Gemini model"""
        # Configure browser settings - simulating human-like interactions
        browser_settings = BrowserSettings(
            headless=self.headless,
            viewport_size={"width": 1366, "height": 768},  # Common laptop resolution
            default_timeout=60000,  # 60 seconds
            slow_mo=random.randint(50, 200),  # Random slowdown to appear more human-like
        )
        
        # Configure agent settings for more human-like behavior
        agent_settings = AgentSettings(
            max_iterations=40,
            max_thinking_depth=3,
            max_thinking_length=2000,
            verbose=self.verbose,
        )
        
        # Initialize the agent with Gemini model
        agent = Agent(
            task=task,
            llm=ChatGoogleGenerativeAI(
                model="gemini-1.5-flash",
                temperature=0.7,  # Higher temperature for more varied, human-like behavior
                convert_system_message_to_human=True,
            ),
            browser_settings=browser_settings,
            agent_settings=agent_settings,
        )
        
        return agent
    
    async def browse_for_keyword(self, keyword):
        """
        Perform human-like browsing for a keyword:
        1. Search Google for the keyword
        2. Scroll to find the target site
        3. Click on the site
        4. Interact with it randomly
        5. Return to Google
        """
        # Create a detailed browsing task with instructions for human-like behavior
        browse_task = f"""
        Act as a human browsing the internet with natural behavior. Follow these steps:
        
        1. Go to Google and search for "{keyword}"
        
        2. Scroll down slowly, spending a few seconds looking at each result until you find 
           {self.target_site} in the search results
           
        3. If you don't find it on the first page, check the second page
        
        4. Once you find {self.target_site}, click on it to visit the site
        
        5. On the website, interact naturally for about 1-2 minutes:
           - Scroll up and down at varying speeds (sometimes fast, sometimes slow)
           - Pause occasionally as if reading content (3-10 seconds)
           - Click on 2-3 different internal links that look interesting
           - Spend some time (20-30 seconds) on each page you visit
           - If there are images, look at them for a few seconds
           - If there's a booking form, click on it but DON'T submit any forms
           
        6. After exploring the site naturally, return to Google by clicking the back button
           multiple times until you reach the search results
           
        7. Report what you found on the site and how the interaction went
        """
        
        # Set up and run the agent
        agent = await self.setup_agent(browse_task)
        result = await agent.run()
        
        # Log the results
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        log_filename = f"{self.results_dir}/browse_{keyword.replace(' ', '_')}_{timestamp}.txt"
        
        log_data = {
            "keyword": keyword,
            "target_site": self.target_site,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "result": result
        }
        
        with open(log_filename, "w", encoding="utf-8") as f:
            f.write(f"Browsing Log for '{keyword}' targeting {self.target_site}\n")
            f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Results:\n{result}\n")
        
        return {
            "keyword": keyword,
            "result": result,
            "log_file": log_filename
        }
    
    async def run_batch(self, keywords):
        """Run through a batch of keywords with random delays between searches"""
        results = []
        
        print(f"Starting human-like browsing for {len(keywords)} keywords...")
        print(f"Target site: {self.target_site}")
        
        for i, keyword in enumerate(keywords):
            print(f"\n[{i+1}/{len(keywords)}] Browsing for: '{keyword}'")
            
            # Perform the browsing
            result = await self.browse_for_keyword(keyword)
            results.append(result)
            
            # Log completion
            print(f"Completed browsing for '{keyword}'")
            print(f"Log saved to: {result['log_file']}")
            
            # Random delay between searches to appear more human-like
            if i < len(keywords) - 1:
                delay = random.randint(30, 120)  # 30-120 seconds delay
                print(f"Waiting {delay} seconds before next search...")
                await asyncio.sleep(delay)
        
        print("\nAll keywords processed successfully!")
        return results

async def main():
    """Main function to run the human interaction agent"""
    print("=" * 60)
    print("Human-like Web Browsing Agent")
    print("=" * 60)
    
    # Get target site (default or custom)
    target_site = input("Enter your target website (default: rooms.murudeshwar.co.in): ").strip()
    if not target_site:
        target_site = "rooms.murudeshwar.co.in"
    
    # Create agent
    agent = HumanInteractionAgent(
        target_site=target_site,
        headless=False,  # Show browser for monitoring
        verbose=True
    )
    
    # Get keywords
    while True:
        keywords_input = input("\nEnter keywords (comma-separated) or path to keywords file: ").strip()
        
        if keywords_input.endswith('.txt'):
            # Load keywords from file
            try:
                with open(keywords_input, 'r', encoding='utf-8') as f:
                    keywords = [line.strip() for line in f.readlines() if line.strip()]
                break
            except FileNotFoundError:
                print(f"File not found: {keywords_input}")
        else:
            # Parse comma-separated keywords
            keywords = [k.strip() for k in keywords_input.split(',') if k.strip()]
            if keywords:
                break
            else:
                print("Please enter at least one keyword")
    
    print(f"\nProcessing {len(keywords)} keywords: {', '.join(keywords[:5])}" + 
          (f"... and {len(keywords)-5} more" if len(keywords) > 5 else ""))
    
    # Run the agent with all keywords
    await agent.run_batch(keywords)

if __name__ == "__main__":
    asyncio.run(main()) 