# FootballLens

**FootballLens** is an intelligent football analysis app designed to provide accurate, insightful, and engaging content about football leagues worldwide. With a focus on research and storytelling, FootballLens ensures users receive well-organized data and captivating stories about their favorite leagues, players, and matches.

---

## Features

- **In-depth Research:** Leverages AI tools to gather accurate match results, player performances, key events, and league standings.
- **Engaging Content Creation:** Transforms research into concise and compelling articles suitable for sports enthusiasts.
- **Customizable Creativity:** Allows users to adjust the creativity of content to match their preferences.
- **Data-Driven Insights:** Provides fact-based summaries with proper source references to ensure reliability.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/footballlens.git
   ```

2. Navigate to the project directory:
   ```bash
   cd footballlens
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add the following environment variables:
   ```
   SERPER_API_KEY=your_serper_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Run the application:
   ```bash
   python football_app.py
   ```

---

## Usage

### Running the Flask Application

1. Run the Flask application:
   ```bash
   python football_app.py
   ```

2. Use the `/generate_blog` endpoint to generate a blog post by sending a POST request with the following JSON payload:
   ```json
   {
     "topic": "Gameweek highlights",
     "sector": "Indian Super League",
     "creativity_limit": 0.5
   }
   ```

### Running the Streamlit Application

1. Run the Streamlit application:
   ```bash
   streamlit run football_page.py
   ```

2. Follow the instructions on the web interface to generate your football blog post.

---

## How It Works

FootballLens uses two primary AI agents:

1. **Research Analyst:**
   - Gathers data on match results, player performances, key events, and standings.
   - Ensures accuracy by sourcing information from credible and reliable sources.

2. **Content Writer:**
   - Converts research into an engaging article with sections like Introduction, Match Highlights, Player Performances, and Key Events.
   - Maintains clarity, structure, and reader engagement.

---

## Technology Stack

- **Programming Language:** Python
- **AI Models:** OpenAI GPT-4o-mini
- **Tools:**
  - [SerperDevTool](https://serper.dev/) for web search and data retrieval.
  - [Dotenv](https://pypi.org/project/python-dotenv/) for environment variable management.
  - [Streamlit](https://streamlit.io/) for the web interface.
  - [Flask](https://flask.palletsprojects.com/) for the backend API.

---

## Contributing

We welcome contributions to enhance FootballLens! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push the changes to your fork:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request and describe your changes.

---

## License

This project is licensed under the [MIT License](./LICENSE).

---

## Contact

For queries or suggestions, please reach out to us:

- **Linkedin:** [Arnab Bera](https://www.linkedin.com/in/arnabbera-tech/)
- **GitHub:** [arnabberawork/footballlens](https://github.com/arnabberawork/Football-Lens-Research-App)

---

**Experience football like never before with FootballLens! ⚽**
