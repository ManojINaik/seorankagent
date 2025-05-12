#!/usr/bin/env python3
"""
Custom SEO tasks for use with the SEO agent
"""

class SEOTasks:
    """Collection of SEO tasks that can be used with the SEO agent"""
    
    @staticmethod
    def analyze_serp_features(keyword):
        """Task to analyze SERP features for a keyword"""
        return f"""
        Analyze the SERP features for the keyword "{keyword}":
        
        1. Search Google for "{keyword}"
        2. Identify all SERP features present in the results:
           - Featured snippets
           - People also ask boxes
           - Knowledge panels
           - Image carousels
           - Video results
           - Top stories
           - Local packs
           - Shopping results
           - Twitter/social media results
        
        3. For each SERP feature, analyze:
           - Content type and format
           - Source websites
           - Structure and presentation
        
        4. Determine which SERP features might be achievable for a website
        5. Provide recommendations for optimizing content to capture these features
        6. Save the analysis in an organized format with screenshots if possible
        """
    
    @staticmethod
    def content_gap_analysis(website_url, keyword):
        """Task to perform content gap analysis"""
        return f"""
        Perform a content gap analysis for {website_url} related to "{keyword}":
        
        1. Search Google for "{keyword}" and analyze the top 10 results
        2. Visit {website_url} and identify its current content related to "{keyword}"
        3. For each top-ranking page, identify:
           - Main topics covered
           - Subtopics and related concepts
           - Content formats (text, images, videos, tools, etc.)
           - Content depth and comprehensiveness
        
        4. Create a list of topics/subtopics covered by competitors but missing from {website_url}
        5. Identify unique content opportunities not currently addressed by competitors
        6. Develop a content plan to fill these gaps with:
           - Topic suggestions
           - Content formats
           - Suggested word counts
           - Key points to cover
        
        7. Prioritize content opportunities based on potential impact and difficulty
        8. Save the analysis and content plan to a file
        """
    
    @staticmethod
    def technical_seo_audit(website_url):
        """Task to perform a technical SEO audit"""
        return f"""
        Perform a technical SEO audit of {website_url}:
        
        1. Visit {website_url} and analyze:
           - Page load speed (observe loading time)
           - Mobile responsiveness (resize browser window)
           - URL structure and navigation
           - Internal linking
           - Robots.txt (visit {website_url}/robots.txt)
           - Sitemap (look for sitemap.xml link in robots.txt or footer)
        
        2. Check basic on-page SEO elements:
           - Title tags
           - Meta descriptions
           - Heading structure
           - Image alt attributes
           - Schema markup (check page source)
        
        3. Test key user experience factors:
           - Navigation usability
           - Mobile usability
           - Page layout and content organization
           - Form functionality (if applicable)
           - Overall site structure
        
        4. Identify technical issues such as:
           - Broken links
           - Duplicate content
           - Canonicalization issues
           - JavaScript rendering problems
           - Console errors
        
        5. Provide actionable recommendations for fixing technical issues
        6. Create a prioritized list of technical improvements
        
        7. Save the audit results and recommendations to a file
        """
    
    @staticmethod
    def backlink_analysis(website_url, keyword):
        """Task to analyze backlink profile"""
        return f"""
        Analyze the backlink profile for {website_url} and top competitors for "{keyword}":
        
        1. Search Google for "{keyword}" and identify the top 5 competitors
        2. Visit backlink analysis tools like Ahrefs, SEMrush, Moz, or similar (if accessible)
        3. For {website_url} and each competitor, analyze:
           - Domain authority/domain rating
           - Total number of backlinks
           - Number of referring domains
           - Link quality metrics
           - Anchor text distribution
           - Top linking pages
        
        4. Identify backlink opportunities by finding:
           - Sites linking to multiple competitors but not to {website_url}
           - Industry sites and directories
           - Resource pages in the niche
           - Guest posting opportunities
        
        5. Develop a backlink acquisition strategy with:
           - Target websites
           - Outreach approaches
           - Content creation recommendations
           - Relationship building opportunities
        
        6. Save the analysis and strategy to a file
        """
    
    @staticmethod
    def local_seo_optimization(business_name, location, keyword):
        """Task to optimize for local SEO"""
        return f"""
        Optimize local SEO for {business_name} in {location} targeting "{keyword}":
        
        1. Search Google for "{keyword} in {location}" and analyze:
           - Local pack/map results
           - Organic results
           - Featured snippets
           - People also ask questions
        
        2. Check Google Business Profile (if available):
           - Search for "{business_name} {location}"
           - Analyze business listing completeness
           - Review profile information
           - Check photos and posts
           - Analyze reviews and ratings
        
        3. Analyze local competitors:
           - Business profile completeness
           - Review quality and quantity
           - Website local optimization
           - Local backlink profile
        
        4. Develop local SEO recommendations:
           - Google Business Profile optimization
           - Local content creation strategy
           - Local citation opportunities
           - Review management approach
           - Local schema markup
           - NAP (Name, Address, Phone) consistency
        
        5. Create an action plan for local SEO improvements
        6. Save the analysis and plan to a file
        """ 