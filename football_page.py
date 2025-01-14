import streamlit as st
import requests  # For backend API calls

# Page configuration
st.set_page_config(page_title="Football Blog Generator", page_icon="⚽", layout="wide")

# Custom CSS for gradient background and styling
st.markdown("""
    <style>
        /* Gradient background */
        body {
            background: linear-gradient(135deg, #ffffff, #c1e1ec); /* Light gradient from white to light blue */
            color: #333; /* Dark text for contrast */
            font-family: "Verdana", sans-serif;
        }

        /* Button styling */
        .stButton>button {
            background-color: #1e88e5; /* Blue color */
            color: white;
            border-radius: 12px;
            font-size: 16px;
            padding: 10px 25px;
        }

        /* Input field styling */
        .stTextInput>div>input {
            background-color: #f9f9f9;
            color: #333;
            border: 2px solid #ccc;
            border-radius: 5px;
        }

        /* Slider styling */
        .stSlider {
            max-width: 250px;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .stSlider>div>div>span {
            color: #333;
        }

        /* Title and spacing adjustments */
        .stTitle {
            margin-bottom: 50px;
            text-align: center;
            color: #1e88e5; /* Blue color for the title */
        }
        .stTextInput {
            margin-bottom: 30px;
        }

        /* Footer styling */
        footer {
            text-align: center;
            color: #555;
            margin-top: 30px;
            font-size: 14px;
        }
        footer span {
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar with updated instructions
st.sidebar.title("⚽ How to Use")
st.sidebar.markdown("""
    1. **Describe your topic**: Enter a football-related topic such as **Match Recap**, **Player Profile**, or **League Statistics** 🏆⚽.
    2. **Specify the League or Tournament**: Enter the league name or tournament name (e.g., Premier League, FA Cup, or Champions League) 🎯.
    3. **Adjust Creativity**: Use the slider to set creativity (0 = Minimal, 1 = High) 🎨.
    4. **Generate Blog**: Click the button to generate your football blog post 📝.
    5. **Review the Result**: Read, copy, or download your generated blog ✨.
    
    🔹 **Note**: Blogs are created using **web-based research** and football news 📄.
""")

# Header with emojis and proper spacing
st.title("Football Blog Generator ⚽")

# Input area for blog topic
topic_input = st.text_input(
    "🌟 Enter your football blog topic (e.g., Gameweek 2 recap):",
    "Premier League Match Recap - Gameweek 2"
)

# Create two columns for sector input and creativity slider
col1, col2 = st.columns(2)

# Input area for sector in the first column
with col1:
    sector_input = st.text_input(
        "🎯 Enter the League/Tournament name (e.g., Premier League, FA Cup):",
        "Premier League"
    )

# Slider for creativity level in the second column
with col2:
    creativity_limit = st.slider(
        "🎨 Set Creativity Level (0 to 1):", 
        min_value=0.0, 
        max_value=1.0, 
        value=0.5, 
        step=0.1
    )

# Generate Blog Button
if st.button("Generate Blog Post 📝"):
    with st.spinner("Generating your football blog... 🤖"):
        # Call the backend (replace with your endpoint URL)
        response = requests.post("http://localhost:5000/generate_blog", json={
            "topic": topic_input,
            "sector": sector_input,
            "creativity_limit": creativity_limit
        })
        
        if response.status_code == 200:
            blog_post = response.json().get('blog_post', 'No blog content returned.')
            st.markdown(f"### Generated Blog Post 📝\n\n{blog_post}")

            # Create a download button for the generated blog post
            st.download_button(
                label="Download Blog as Text File 📥",
                data=blog_post,
                file_name="football_blog_post.txt",
                mime="text/plain"
            )
        else:
            st.error("⚠️ Error generating blog post. Please try again.")

# Footer mentioning Crew, OpenAI, and SerperAI
st.markdown("""
    <footer>
        <p>Powered by <b>Crew</b>, <b>OpenAI</b>, and <b>SerperAI</b> ⚽✨ | Innovate. Inspire. Create.</p>
    </footer>
""", unsafe_allow_html=True)
