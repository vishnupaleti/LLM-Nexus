# LLM Nexus - Enterprise LLM Comparison Platform

LLM Nexus is an enterprise-grade web application built with Streamlit that enables users to compare multiple Large Language Models (LLMs) in real-time.

## Features

- **Multi-Model Comparison**: Compare responses from ChatGPT, Gemini, and LLaMA simultaneously
- **User Authentication**: Secure login and registration system with SHA-256 password hashing
- **Cost Analysis**: Calculate and track API costs across different models
- **Performance Metrics**: Track latency, response quality, and cost efficiency
- **Report Generation**: Export comparison results as CSV reports
- **Parallel Processing**: Execute multiple model queries simultaneously for faster results
- **Rate Limiting**: Prevent API overuse and manage request throttling
- **Intelligent Routing**: Task-based model recommendations

## Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python with async/parallel processing
- **APIs**: OpenAI (ChatGPT), Google (Gemini), Open source (LLaMA)
- **Data Storage**: CSV-based file system
- **Authentication**: SHA-256 password hashing

## Project Structure

```
LLM/
├── app.py                  # Main Streamlit application
├── auth.py                 # Authentication module
├── config.py               # Configuration and constants
├── models/                 # LLM model implementations
│   ├── chatgpt_model.py   # ChatGPT integration
│   ├── gemini_model.py    # Google Gemini integration
│   └── llama_model.py     # Open-source LLaMA integration
├── utils/                  # Utility functions
│   ├── router.py          # Model selection logic
│   ├── parallel.py        # Parallel execution
│   ├── rate_limiter.py    # API rate limiting
│   ├── cost_tracker.py    # Cost calculation
│   ├── metrics.py         # Performance metrics logging
│   ├── report.py          # Report generation
│   └── fallback.py        # Fallback mechanisms
├── data/                   # Data storage directory
│   ├── users.csv          # User credentials (hashed)
│   ├── metrics/           # Performance metrics
│   └── comparison_reports/# Generated comparison reports
└── reports/                # Final reports directory
```

## Supported Models

| Model | Cost (per 1000 tokens) | Speed | Best For |
|-------|------------------------|-------|----------|
| ChatGPT (GPT-4o-mini) | $0.002 | Medium | General tasks, coding |
| Gemini | $0.0005 | Fast | Fast responses, cost savings |
| LLaMA | $0.00 | Slow | Local deployment, free usage |

## Installation

1. Clone the repository
2. Install dependencies:
```
bash
pip install -r requirements.txt
```

3. Set up environment variables:
```
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
```

4. Run the application:
```
bash
streamlit run app.py
```

## Usage

1. **Register/Login**: Create an account or login with existing credentials
2. **Select Models**: Choose which LLM models to compare
3. **Enter Prompt**: Input your question or task
4. **View Results**: Compare responses side-by-side
5. **Export**: Download comparison reports as CSV

## Configuration

The application uses `config.py` for centralized configuration of all LLM models and their properties.

## Dependencies

- streamlit
- pandas
- openai
- google-cloud-generativeai
- python-dotenv
- requests

## License

MIT License
