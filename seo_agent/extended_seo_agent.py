#!/usr/bin/env python3
import asyncio
import os
from dotenv import load_dotenv
from custom_seo_tasks import SEOTasks
from advanced_seo_agent import SEOAgent

# Load environment variables
load_dotenv()

class ExtendedSEOAgent(SEOAgent):
    """Extended SEO Agent with additional specialized tasks"""
    
    async def run_serp_features_analysis(self, keyword):
        """Analyze SERP features for a keyword"""
        task = SEOTasks.analyze_serp_features(keyword)
        agent = await self.setup_agent(task)
        result = await agent.run()
        
        # Save results
        filename = f"{self.results_dir}/serp_features_{keyword.replace(' ', '_')}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# SERP Features Analysis for '{keyword}'\n\n")
            f.write(result)
        
        return {
            "result": result,
            "filename": filename
        }
    
    async def run_content_gap_analysis(self, keyword, website_url):
        """Run content gap analysis"""
        task = SEOTasks.content_gap_analysis(website_url, keyword)
        agent = await self.setup_agent(task)
        result = await agent.run()
        
        # Save results
        filename = f"{self.results_dir}/content_gap_{keyword.replace(' ', '_')}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Content Gap Analysis for '{keyword}' on {website_url}\n\n")
            f.write(result)
        
        return {
            "result": result,
            "filename": filename
        }
    
    async def run_technical_seo_audit(self, website_url):
        """Run technical SEO audit"""
        task = SEOTasks.technical_seo_audit(website_url)
        agent = await self.setup_agent(task)
        result = await agent.run()
        
        # Save results
        filename = f"{self.results_dir}/technical_audit_{website_url.replace('https://', '').replace('http://', '').replace('/', '_')}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Technical SEO Audit for {website_url}\n\n")
            f.write(result)
        
        return {
            "result": result,
            "filename": filename
        }
    
    async def run_backlink_analysis(self, keyword, website_url):
        """Run backlink analysis"""
        task = SEOTasks.backlink_analysis(website_url, keyword)
        agent = await self.setup_agent(task)
        result = await agent.run()
        
        # Save results
        filename = f"{self.results_dir}/backlink_analysis_{website_url.replace('https://', '').replace('http://', '').replace('/', '_')}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Backlink Analysis for {website_url}\n\n")
            f.write(result)
        
        return {
            "result": result,
            "filename": filename
        }
    
    async def run_local_seo_optimization(self, business_name, location, keyword):
        """Run local SEO optimization"""
        task = SEOTasks.local_seo_optimization(business_name, location, keyword)
        agent = await self.setup_agent(task)
        result = await agent.run()
        
        # Save results
        filename = f"{self.results_dir}/local_seo_{location.replace(' ', '_')}_{keyword.replace(' ', '_')}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Local SEO Optimization for {business_name} in {location}\n\n")
            f.write(result)
        
        return {
            "result": result,
            "filename": filename
        }

async def main():
    """Main function to run the extended SEO agent"""
    print("=" * 60)
    print("Extended SEO Agent with Specialized Tasks")
    print("=" * 60)
    
    # Get user inputs
    main_keyword = input("Enter the main target keyword: ")
    website_url = input("Enter your website URL: ")
    
    # Create the extended SEO agent
    seo_agent = ExtendedSEOAgent(headless=False, verbose=True)
    
    # Extended menu for selecting tasks
    while True:
        print("\nSEO Tasks Menu:")
        print("=" * 30)
        print("Basic Tasks:")
        print("1. Run comprehensive SEO analysis")
        print("2. Run competitor analysis")
        print("3. Run keyword research")
        print("\nAdvanced Tasks:")
        print("4. Analyze SERP features")
        print("5. Perform content gap analysis")
        print("6. Run technical SEO audit")
        print("7. Analyze backlink profile")
        print("8. Optimize for local SEO")
        print("9. Exit")
        
        choice = input("\nSelect a task (1-9): ")
        
        if choice == "1":
            print(f"\nRunning comprehensive SEO analysis for '{main_keyword}' on {website_url}...")
            result = await seo_agent.run_seo_analysis(main_keyword, website_url)
            print(f"\nAnalysis complete! Results saved to: {result['filename']}")
            
        elif choice == "2":
            competitors_input = input("Enter competitor URLs (comma-separated) or press Enter to skip: ")
            competitors = [url.strip() for url in competitors_input.split(",")] if competitors_input.strip() else None
            print(f"\nRunning competitor analysis for '{main_keyword}'...")
            result = await seo_agent.run_competitor_analysis(main_keyword, website_url, competitors)
            print(f"\nCompetitor analysis complete! Results saved to: {result['filename']}")
            
        elif choice == "3":
            print(f"\nRunning keyword research for '{main_keyword}'...")
            result = await seo_agent.run_keyword_research(main_keyword, website_url)
            print(f"\nKeyword research complete! Results saved to: {result['filename']}")
        
        elif choice == "4":
            print(f"\nAnalyzing SERP features for '{main_keyword}'...")
            result = await seo_agent.run_serp_features_analysis(main_keyword)
            print(f"\nSERP features analysis complete! Results saved to: {result['filename']}")
            
        elif choice == "5":
            print(f"\nPerforming content gap analysis for '{main_keyword}' on {website_url}...")
            result = await seo_agent.run_content_gap_analysis(main_keyword, website_url)
            print(f"\nContent gap analysis complete! Results saved to: {result['filename']}")
            
        elif choice == "6":
            print(f"\nRunning technical SEO audit for {website_url}...")
            result = await seo_agent.run_technical_seo_audit(website_url)
            print(f"\nTechnical SEO audit complete! Results saved to: {result['filename']}")
            
        elif choice == "7":
            print(f"\nAnalyzing backlink profile for {website_url}...")
            result = await seo_agent.run_backlink_analysis(main_keyword, website_url)
            print(f"\nBacklink analysis complete! Results saved to: {result['filename']}")
            
        elif choice == "8":
            business_name = input("Enter business name: ")
            location = input("Enter location (city, region): ")
            print(f"\nOptimizing local SEO for {business_name} in {location}...")
            result = await seo_agent.run_local_seo_optimization(business_name, location, main_keyword)
            print(f"\nLocal SEO optimization complete! Results saved to: {result['filename']}")
            
        elif choice == "9":
            print("\nExiting SEO Agent. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please select a number between 1-9.")

if __name__ == "__main__":
    asyncio.run(main()) 