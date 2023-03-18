# Screenplay Generator

The Screenplay Generator is a web application that allows users to generate a TV or movie screenplay based on a scene template. The application uses OpenAI's natural language generation capabilities to generate the screenplay text based on the user's inputs and specified parameters. The output is in traditional screenplay format and can be copied and pasted into screenwriting software.

## Usage

To use the Screenplay Generator, follow these steps:

1. Enter the necessary information for your scene, including the location, time of day, character names and descriptions, objective, conflict, dialogue, action, emotion, and any additional notes.
2. Optionally adjust the parameters for the OpenAI API, including the temperature and p-value.
3. Click the "Generate Screenplay" button to generate the screenplay text.
4. Copy and paste the generated screenplay text into screenwriting software.

## Installation

To install and run the Screenplay Generator, follow these steps:

1. Clone or download the repository to your local machine.
2. Install the necessary Python packages by running `pip install -r requirements.txt` in your terminal or command prompt.
3. Set your OpenAI API key as an environment variable by running `export OPENAI_API_KEY=YOUR_API_KEY` (replacing `YOUR_API_KEY` with your actual API key) in your terminal or command prompt.
4. Run the app by running `streamlit run app.py` in your terminal or command prompt.
5. Open your web browser and navigate to the URL displayed in the terminal or command prompt (usually http://localhost:8501).

## Requirements

The Screenplay Generator requires the following:

- Python 3.6 or higher
- OpenAI API key
- Streamlit
- OpenAI Python package

## Contributing

Contributions to the Screenplay Generator are welcome! Please see `CONTRIBUTING.md` for more information.

## License

The Screenplay Generator is licensed under the MIT License. See `LICENSE` for more information.
