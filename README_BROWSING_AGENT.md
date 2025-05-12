# Human-like Web Browsing Agent

A browser automation tool that simulates natural human browsing behavior to interact with your website through Google searches. This agent is designed to:

1. Search for keywords on Google
2. Find and click on your website in the search results
3. Interact with your site in a human-like manner
4. Return to Google and repeat with the next keyword

## Features

- **Natural Browsing Behavior**: Simulates realistic human interactions including variable scroll speeds, pauses, and mouse movements
- **Multi-device Simulation**: Randomly switches between desktop and mobile browsing patterns
- **Randomized Timing**: Uses variable delays between actions and searches to appear more human-like
- **Detailed Logging**: Records all browsing sessions with timestamps and actions taken
- **Session Reports**: Generates summary reports of browsing sessions
- **Anti-Bot Detection**: Implements natural browsing patterns to avoid bot detection algorithms
- **Real Browser Support**: Can use your existing Brave browser instance for more authentic interactions
- **Gemini AI Model**: Powered by Google's Gemini 2.0 Flash model for intelligent browsing behavior

## Setup

### Prerequisites

- Python 3.8+
- Playwright
- Gemini API key (from Google AI Studio)
- Brave Browser (recommended) or other Chrome-based browser

### Installation

1. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Install Playwright browsers:
   ```
   playwright install
   ```

4. Create a `.env` file in the project root with your API key:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   You can obtain a Gemini API key from [Google AI Studio](https://ai.google.dev/).

## Usage

### Using Your Real Brave Browser (Recommended)

For the most authentic browsing experience, use your existing Brave browser:

```
python run_with_brave.py
```

This script will:
1. Detect your Brave browser installation
2. Open a new window in your existing browser
3. Perform all browsing activities in your real browser
4. Provide a more natural and authenticated browsing experience

### Standard Agent Options

There are also two versions of the agent using standard browser automation:

#### Basic Human Interaction Agent

For simple human-like browsing:

```
python human_interaction_agent.py
```

#### Advanced Interaction Agent

For more sophisticated browsing patterns with device simulation:

```
python advanced_interaction_agent.py
```

You'll be prompted to:
1. Enter your target website (default is rooms.murudeshwar.co.in)
2. Enter keywords (comma-separated) or the path to a keywords file
3. Choose whether to randomize the keyword order

## Keyword Files

You can create a text file with one keyword per line, for example:
```
murudeshwar beach rooms
hotels in murudeshwar
murudeshwar accommodation
```

A sample keyword file is included: `sample_keywords.txt`

## How It Works

The agent:

1. Takes a list of keywords to search for
2. For each keyword:
   - Creates a random browser profile (desktop or mobile)
   - Opens Google and searches for the keyword
   - Scrolls naturally through results looking for your website
   - When found, clicks on your site and explores it naturally:
     - Scrolls at variable speeds
     - Pauses on interesting content
     - Clicks on internal links
     - Explores various pages
   - Returns to Google for the next keyword

3. Generates a session report with statistics

## Using Real Browser vs Standard Browser

### Real Browser (Brave) Advantages:
- Uses your existing browser profile with cookies and history
- More authentic browsing experience for Google and websites
- May bypass some bot detection mechanisms
- Allows for authenticated browsing if you're already logged in

### Standard Browser Advantages:
- More control over browser parameters
- Can simulate different device types more easily
- Better for automated testing environments

## Customization

You can customize the agent by modifying:
- Target website
- Browsing patterns and interaction styles
- Device profiles and user agents
- Timing parameters and randomization
- Browser path (for real browser mode)

## Notes

- When using real browser mode, make sure your browser is not already running, or close it first
- For best results, use a diverse set of keywords related to your website
- Allow the agent to run without interference to maintain natural browsing patterns
- All logs and reports are saved in the `browsing_logs` directory 