import openai
import streamlit as st

# Set up OpenAI API credentials
openai.api_key = "INSERT_YOUR_API_KEY_HERE"

# Define the scene template
scene_template = """
Prompt: This prompt is for creating a TV or movie screenplay in traditional screenplay format. Please fill out the following scene template with the necessary information:

Location: [Insert location]

Time of Day: [Insert time of day]

Characters: [Insert character names and brief descriptions]

Objective: [Insert the main objective of the scene]

Conflict: [Insert the main conflict or obstacle that the characters face in achieving their objective]

Dialogue: [Insert any key dialogue that needs to be included in the scene]

Action: [Insert any key actions that need to be included in the scene]

Emotion: [Insert the primary emotion or tone of the scene]

Notes: [Insert any additional notes or details that are important for the scene]
"""

# Define the Streamlit app
def app():
    # Set up the input fields with help text
    st.write("Enter the following information for your scene:")
    location_help = scene_template.split("\n")[2][10:-1]
    location = st.text_input("Location", help=location_help)
    time_of_day_help = scene_template.split("\n")[3][14:-1]
    time_of_day = st.text_input("Time of Day", help=time_of_day_help)
    characters_help = scene_template.split("\n")[4][13:-1]
    character_names = st.text_input("Character Names and Descriptions", help=characters_help)
    objective_help = scene_template.split("\n")[5][11:-1]
    objective = st.text_input("Objective", help=objective_help)
    conflict_help = scene_template.split("\n")[6][11:-1]
    conflict = st.text_input("Conflict", help=conflict_help)
    dialogue_help = scene_template.split("\n")[7][11:-1]
    dialogue = st.text_input("Dialogue", help=dialogue_help)
    action_help = scene_template.split("\n")[8][9:-1]
    action = st.text_input("Action", help=action_help)
    emotion_help = scene_template.split("\n")[9][9:-1]
    emotion = st.text_input("Emotion", help=emotion_help)
    notes_help = scene_template.split("\n")[10][8:-1]
    notes = st.text_area("Notes", help=notes_help)

    # Set up the optional input fields for OpenAI API parameters
    st.write("Optionally adjust the following parameters for the OpenAI API:")
    temperature_help = "Controls the randomness of the generated text. Lower values are more deterministic, higher values are more creative."
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, step=0.01, value=0.7, help=temperature_help)
    p_help = "Controls the 'diversity' of the generated text. Lower values result in more repetitive text, higher values result in more diverse text."
    p = st.slider("P-Value", min_value=0.0, max_value=1.0, step=0.01, value=0.9, help=p_help)

    # Generate the scene template with the user's input values
    scene = scene_template.format(
        location=location,
        time_of_day=time_of_day,
        characters=character_names,
        objective=objective,
        conflict=conflict,
        dialogue=dialogue,
        action=action,
        emotion=emotion,
        notes=notes
    )

    # Generate the screenplay text using the OpenAI API
    if st.button("Generate Screenplay"):
        screenplay = openai.Completion.create(
            engine="davinci",
            prompt=scene,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=temperature,
            p=p,
        )

        # Display the generated screenplay text
        st.write(screenplay.choices[0].text)

    # Display explanations of the OpenAI API parameters
    st.write("Explanation of Parameters:")
    st.write(f"Temperature ({temperature}): {temperature_help}")
    st.write(f"P-Value ({p}): {p_help}")

if __name__ == "__main__":
    # Set up the Streamlit app on a webpage
    st.set_page_config(page_title="Screenplay Generator", page_icon=":clapper:", layout="wide")
    st.title("Screenplay Generator")
    st.write("Use this app to generate a screenplay based on a scene template!")
    app()
