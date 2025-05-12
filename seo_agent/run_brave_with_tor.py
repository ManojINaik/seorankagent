#!/usr/bin/env python3
"""
Script to run Brave browser with Tor network enabled
"""
import asyncio
import os
import sys
import subprocess
from dotenv import load_dotenv

# Add paths to make imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../browser-use')))

# Load environment variables
load_dotenv()

# Default Brave browser path
BRAVE_PATH = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

# Function to directly launch Brave with subprocess
def launch_brave_with_tor():
    """Launch Brave browser with Tor directly using subprocess"""
    if not os.path.exists(BRAVE_PATH):
        print(f"ERROR: Brave browser not found at {BRAVE_PATH}")
        print("Please make sure Brave is installed or update the path in this script.")
        return False
    
    try:
        print(f"Directly launching Brave with Tor using subprocess...")
        subprocess.Popen([BRAVE_PATH, "--tor"])
        print("Browser launched with Tor flag. Check for the Tor icon in the browser.")
        return True
    except Exception as e:
        print(f"Error launching Brave: {str(e)}")
        return False

# Modified main function to use the browser_use library or direct subprocess launch
async def main():
    # First try direct launch with subprocess
    if launch_brave_with_tor():
        print("Brave launched successfully with subprocess.")
        return
    
    print("Direct launch failed. Trying with browser_use library...")
    
    # If direct launch fails, try with the browser_use library
    try:
        from advanced_interaction_agent import AdvancedBrowsingAgent
        
        # Create the browsing agent with Brave
        agent = AdvancedBrowsingAgent(
            browser_path=BRAVE_PATH,
            headless=False
        )
        
        # Run the agent
        await agent.run()
        
    except Exception as e:
        print(f"Error using browser_use library: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Try both methods
    print("=== Running Brave Browser with Tor Network ===")
    
    # For simple non-async use, just call the direct launch function
    launch_brave_with_tor()
    
    # No need to run the async part if direct launch works
    # asyncio.run(main()) 