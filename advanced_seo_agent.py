#!/usr/bin/env python3
import asyncio
import os
import json
import datetime
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, BrowserSettings, AgentSettings, OutputFormat

# Load environment variables
load_dotenv()

class SEOAgent:
    """Advanced SEO Agent using browser-use with Gemini model"""
    
    def __init__(self, headless=False, verbose=True):
        """Initialize the SEO Agent with configuration settings"""
        self.headless = headless
        self.verbose = verbose
        self.results_dir = "seo_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
    async def setup_agent(self, task):
        """Set up the browser-use agent with Gemini model"""
        # Configure browser settings
        browser_settings = BrowserSettings(
            headless=self.headless,
            viewport_size={"width": 1280, "height": 800},
            default_timeout=60000,  # 60 seconds
            slow_mo=100,  # Slow down actions by 100ms for better visibility
            record_video=True,  # Record video of the browser session
        )
        
        # Configure agent settings
        agent_settings = AgentSettings(
            max_iterations=40,  # Increase max iterations for complex SEO tasks
            max_thinking_depth=5,
            max_thinking_length=4000,
            verbose=self.verbose,
        )
        
        # Initialize the agent with Gemini model
        agent = Agent(
            task=task,
            llm=ChatGoogleGenerativeAI(
                model="gemini-1.5-flash",  # Using Gemini 1.5 Flash
                temperature=0.2,
                convert_system_message_to_human=True,
            ),
            browser_settings=browser_settings,
            agent_settings=agent_settings,
            output_format=OutputFormat.MARKDOWN,  # Use markdown for better readability
        )
        
        return agent
    
    async def run_seo_analysis(self, keyword, website_url):
        """Run comprehensive SEO analysis for the given keyword and website"""
        seo_task = f"""
        Perform a comprehensive SEO analysis for the keyword "{keyword}" on the website {website_url}:
        
        1. Search Google for "{keyword}" and analyze the top 5 search results
        2. For each top result, identify:
           - Title structure and keyword usage
           - Meta description patterns
           - Content structure (headings, paragraphs, lists)
           - Content length and keyword density
           - Media usage (images, videos)
           - Internal and external link patterns
        
        3. Visit the target website at {website_url} and analyze:
           - Current title and meta description
           - Heading structure (H1, H2, H3)
           - Content quality and relevance to keyword
           - Internal linking structure
           - Page speed (observe loading time)
           - Mobile responsiveness (resize browser window)
           - Schema markup (check page source)
        
        4. Provide specific recommendations to optimize {website_url} for "{keyword}":
           - Title and meta description improvements
           - Content structure suggestions
           - Keyword placement recommendations
           - Internal linking strategy
           - Technical SEO improvements
        
        5. Save the analysis and recommendations to a file in a clear, organized format.
        6. Create a summarized action plan with priority tasks for immediate implementation.
        """
        
        agent = await self.setup_agent(seo_task)
        result = await agent.run()
        
        # Save the results
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.results_dir}/seo_analysis_{keyword.replace(' ', '_')}_{timestamp}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# SEO Analysis for '{keyword}' on {website_url}\n\n")
            f.write(f"Analysis Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(result)
        
        return {
            "result": result,
            "filename": filename
        }
    
    async def run_competitor_analysis(self, keyword, website_url, competitors=None):
        """Run competitor analysis for the given keyword"""
        competitors_str = ""
        if competitors:
            competitors_str = "Also visit and analyze these specific competitors:\n"
            for i, comp in enumerate(competitors, 1):
                competitors_str += f"{i}. {comp}\n"
        
        task = f"""
        Perform a detailed competitor analysis for the keyword "{keyword}" comparing with {website_url}:
        
        1. Search Google for "{keyword}" and identify the top 5 ranking websites
        2. For each competitor (including those in Google results and the specified list), analyze:
           - Domain authority and backlink profile (check for displayed metrics)
           - Content quality, length, and structure
           - Keyword usage and density
           - User experience and site navigation
           - Unique selling points and differentiators
        
        3. {competitors_str}
        
        4. Compare {website_url} against these competitors on the same factors
        
        5. Identify specific competitive advantages of top-ranking sites
        
        6. Provide actionable recommendations for {website_url} to outperform competitors
        
        7. Save the analysis with a clear competitive positioning map and strategy recommendations
        """
        
        agent = await self.setup_agent(task)
        result = await agent.run()
        
        # Save the results
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.results_dir}/competitor_analysis_{keyword.replace(' ', '_')}_{timestamp}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Competitor Analysis for '{keyword}' vs {website_url}\n\n")
            f.write(f"Analysis Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(result)
        
        return {
            "result": result,
            "filename": filename
        }
    
    async def run_keyword_research(self, main_keyword, website_url):
        """Run keyword research to find related keywords"""
        task = f"""
        Perform comprehensive keyword research starting with "{main_keyword}" for {website_url}:
        
        1. Search Google for "{main_keyword}" and analyze:
           - Related searches at the bottom of search results
           - "People also ask" questions
           - Autocomplete suggestions (type the keyword slowly and note suggestions)
        
        2. Visit at least one keyword research tool (like Ahrefs, SEMrush, Ubersuggest, or similar) if possible
        
        3. For each identified related keyword:
           - Check search volume if available
           - Analyze keyword difficulty if available
           - Check the search results to understand search intent
        
        4. Group keywords by search intent (informational, navigational, transactional)
        
        5. Identify low-competition, high-opportunity keywords
        
        6. Create a content strategy plan using the identified keywords for {website_url}
        
        7. Save the keyword research results and strategy in an organized format
        """
        
        agent = await self.setup_agent(task)
        result = await agent.run()
        
        # Save the results
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.results_dir}/keyword_research_{main_keyword.replace(' ', '_')}_{timestamp}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Keyword Research for '{main_keyword}' - {website_url}\n\n")
            f.write(f"Research Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(result)
        
        return {
            "result": result,
            "filename": filename
        }

async def main():
    """Main function to run the SEO agent"""
    print("=" * 50)
    print("Advanced SEO Agent using Browser-Use with Gemini")
    print("=" * 50)
    
    # Get user inputs
    main_keyword = input("Enter the main target keyword: ")
    website_url = input("Enter your website URL: ")
    
    # Optional competitor URLs
    competitors_input = input("Enter competitor URLs (comma-separated) or press Enter to skip: ")
    competitors = [url.strip() for url in competitors_input.split(",")] if competitors_input.strip() else None
    
    # Create the SEO agent
    seo_agent = SEOAgent(headless=False, verbose=True)
    
    # Menu for selecting tasks
    while True:
        print("\nSEO Tasks Menu:")
        print("1. Run comprehensive SEO analysis")
        print("2. Run competitor analysis")
        print("3. Run keyword research")
        print("4. Run all tasks")
        print("5. Exit")
        
        choice = input("\nSelect a task (1-5): ")
        
        if choice == "1":
            print(f"\nRunning comprehensive SEO analysis for '{main_keyword}' on {website_url}...")
            result = await seo_agent.run_seo_analysis(main_keyword, website_url)
            print(f"\nAnalysis complete! Results saved to: {result['filename']}")
            
        elif choice == "2":
            print(f"\nRunning competitor analysis for '{main_keyword}'...")
            result = await seo_agent.run_competitor_analysis(main_keyword, website_url, competitors)
            print(f"\nCompetitor analysis complete! Results saved to: {result['filename']}")
            
        elif choice == "3":
            print(f"\nRunning keyword research for '{main_keyword}'...")
            result = await seo_agent.run_keyword_research(main_keyword, website_url)
            print(f"\nKeyword research complete! Results saved to: {result['filename']}")
            
        elif choice == "4":
            print(f"\nRunning all SEO tasks for '{main_keyword}' on {website_url}...")
            
            print("\n1. Running comprehensive SEO analysis...")
            seo_result = await seo_agent.run_seo_analysis(main_keyword, website_url)
            print(f"SEO analysis saved to: {seo_result['filename']}")
            
            print("\n2. Running competitor analysis...")
            comp_result = await seo_agent.run_competitor_analysis(main_keyword, website_url, competitors)
            print(f"Competitor analysis saved to: {comp_result['filename']}")
            
            print("\n3. Running keyword research...")
            kw_result = await seo_agent.run_keyword_research(main_keyword, website_url)
            print(f"Keyword research saved to: {kw_result['filename']}")
            
            print("\nAll tasks completed successfully!")
            
        elif choice == "5":
            print("\nExiting SEO Agent. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please select a number between 1-5.")

if __name__ == "__main__":
    asyncio.run(main()) 