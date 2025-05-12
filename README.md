# SEO Automation Agent

An advanced SEO optimization tool that uses browser-use and Google's Gemini model to automate SEO tasks and analysis.

## Features

- **Comprehensive SEO Analysis**: Analyze your website and top competitors for a target keyword
- **Competitor Analysis**: Compare your website against top-ranking competitors
- **Keyword Research**: Find related keywords and content opportunities
- **Automated Browser Interaction**: Watch the agent interact with search engines and websites
- **Detailed Reports**: Generate markdown reports with actionable insights

## Setup

### Prerequisites

- Python 3.8+
- Playwright
- Google Generative AI API key

### Installation

1. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the required packages:
   ```
   pip install browser-use langchain-google-genai python-dotenv
   ```

3. Install Playwright browsers:
   ```
   playwright install
   ```

4. Create a `.env` file in the project root with your API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Usage

Run the basic SEO agent:

```
python seo_agent.py
```

Or run the advanced SEO agent with more features:

```
python advanced_seo_agent.py
```

You'll be prompted to enter:
- Your target keyword
- Your website URL
- Optional competitor URLs

## Available Tasks

1. **Comprehensive SEO Analysis**
   - Analyzes on-page and off-page factors
   - Provides actionable recommendations

2. **Competitor Analysis**
   - Compares your site with top-ranking competitors
   - Identifies competitive advantages and gaps

3. **Keyword Research**
   - Discovers related keywords
   - Analyzes search intent
   - Creates content strategy recommendations

## How It Works

The SEO agent uses browser-use to control a web browser and perform the following actions:

1. Search for your target keyword on Google
2. Analyze the top-ranking pages
3. Visit your website and analyze its content and structure
4. Compare your site with competitors
5. Generate detailed reports with actionable recommendations

All reports are saved in the `seo_results` directory in markdown format.

## Customization

You can customize the agent's behavior by modifying:

- Browser settings (headless mode, viewport size, etc.)
- Agent settings (max iterations, thinking depth, etc.)
- Specific SEO tasks and analysis parameters

## Notes

- The agent requires internet access to perform its tasks
- Some websites may block automated browser access
- For best results, run in non-headless mode to watch the agent's progress
- The quality of the analysis depends on the Gemini model's capabilities 