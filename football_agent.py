# Import necessary libraries and modules
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def run_crew_ai_football(topic, league_name, creativity_limit):
    
    # Tool 1: LLM (Language Model) setup
    llm_tool = LLM(
        model="gpt-4o-mini",       # Define the model to use
        timeout=120,               # Maximum wait time for the response in seconds
        max_tokens=2000,           # Reduced token limit
        temperature=creativity_limit,           # Creativity limit for balanced reporting
        seed=42                    # Seed for reproducibility of results
    )

    # Tool 2: Search tool setup using SerperDevTool for information retrieval
    search_tool = SerperDevTool(n=10)  # Limit the number of search results to 5

    # Define league and topic
    research_topic = f"{topic} in {league_name}"

    # Agent 1: League Research Analyst
    delimiter = "######"  # A delimiter used for separating sections in the prompt

    research_analyst = Agent(
        role='You are a Research Analyst specializing in football leagues.',
        goal=f'''
            {delimiter} Role {delimiter} Football League Research Analyst {delimiter}
            Research and summarize data of {research_topic}.
            - Gather data only from verified and trusted sources, including official league data, major sports news outlets, and reputable statistical websites.
            - Do not generate speculative or fabricated content. If information is unavailable, note it clearly.
            - Focus only on the current season (Season 2024-2025), and ensure all details are fact-checked before inclusion.
            {delimiter} Constraints {delimiter}
            - Use credible sources such as official websites and renowned sports databases (e.g., ESPN, BBC, official league platforms).
            - Provide concise summaries with real statistics and verified data.
            - Include citations and source links for every factual piece of information.
        ''',
        backstory=f'''
            A meticulous researcher specializing in gathering and analyzing data on football leagues, with a focus on {research_topic}.
        ''',
        tools=[search_tool],    # Set the tool(s) available to the agent
        llm=llm_tool,           # Provide the language model tool for processing
        verbose=True,            # Enable verbose logging
        allow_delegation=False   # Disable delegation of tasks
    )

    # Task 1: Research Task
    research_task = Task(
        description=f'''
            Research and compile a comprehensive brief on {research_topic}.
            - Cover match results, player performances, key events, and standings from {research_topic}.
            - Ensure data is from the current season (Season 2024-2025).
            - Focus only on data directly related to {research_topic}.
            - Use only reliable, verified sources and verify data accuracy before inclusion.
            - If a particular fact is unavailable or unclear, note that clearly, instead of guessing.
        ''',
        expected_output=f'''
            - A well-organized research brief covering key aspects of {research_topic}.
            - Data-driven insights with proper source references.
            - Avoid speculative or incorrect data points.
        ''',
        agent=research_analyst  # Assign the research analyst agent to the task
    )


    # Agent 2: League Content Writer
    content_writer = Agent(
        role='You are a Content Writer specializing in creating engaging sports articles.',
        goal=f'''
            {delimiter} Role {delimiter} Football Content Writer {delimiter}
            Write a news article or blog post based only on the verified research provided on {research_topic}.
            - Do not add any data or facts that were not included in the research brief.
            - Structure the article with accurate, fact-checked information, and avoid any unsupported claims or errors.
            - Focus on presenting the data clearly and engagingly, without making up any details.
            {delimiter} Constraints {delimiter}
            - Maintain a word limit of 400-500 words.
            - Ensure clarity, proper structure, and balance between facts and storytelling.
            - Avoid any errors or fabricated data.
            ''',
        backstory=f'''
            An experienced writer adept at transforming verified research into engaging, fact-driven content for sports journalism.
        ''',
        llm=llm_tool,           # Use the language model for content writing
        verbose=True,            # Enable verbose logging
        allow_delegation=False   # Disable delegation of tasks
    )

    # Task 2: Content Writing Task
    writing_task = Task(
        description=f'''
            Based on the research provided, write a detailed news article or blog post (400-500 words) on {research_topic}.
            - Focus on match highlights, player performances, key events, and league standings of {research_topic} from the current season (Season 2024-2025).
            - Structure the article for clarity and reader engagement.
        ''',
        expected_output=f'''
            - A concise and engaging article with clear sections.
            - Insightful coverage of {research_topic} with balanced reporting.
        ''',
        agent=content_writer  # Assign the content writer agent to the task
    )

    # Set up Crew with both research and content writing agents and tasks
    crew = Crew(
        agents=[research_analyst, content_writer],
        tasks=[research_task, writing_task],
        verbose=True  # Enable verbose logging for the entire crew process
    )

    # Kick off the crew agents with the initial input for league coverage
    result = crew.kickoff(inputs={'research_topic': research_topic})

    # Print detailed information about the result
    print("Result type: ", type(result))
    print("Result content: ", result)

    # Return the result of the task execution
    return result

if __name__ == "__main__":
    # Prompt for user input
    topic = input("Enter the research topic (e.g., Gameweek highlights): ")
    league_name = input("Enter the league name (e.g., Indian Super League): ")
    creativity_limit = float(input("Enter the creativity limit (0.0 to 1.0): "))

    # Call the function with user inputs
    result = run_crew_ai_football(topic, league_name, creativity_limit)

    # Print detailed information about the result
    print("Result type from main: ", type(result))
    print("Result content from main: ", result)