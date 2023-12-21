

import streamlit as st
from model import GoogleGenerativeAIBot, MessageItem

st.set_page_config(page_title="Code Guru", page_icon="🤪")

st.title('Code Guru')
st.write("Code Guru is provide full support for your coding journey.")

if "bot" not in st.session_state:
    st.session_state.bot = GoogleGenerativeAIBot("Math Tutor",
        instructions="You are a Software Engineer Provide Users Complete fledge code in the providing language.")  # Use GoogleGenerativeAIBot instead

# Create a list to store chat history
chat_history = []

for m in st.session_state.bot.get_messages():
    if isinstance(m, MessageItem):  # Check if m is an instance of MessageItem
        chat_history.append((m.role, m.content))

# Display chat history
for role, content in chat_history:
    with st.chat_message(role):
        st.markdown(content.text)

if prompt := st.chat_input("Please Ask a Question"):
    st.session_state.bot.send_message(prompt)
    with st.chat_message("user"):
        st.markdown(prompt)

    response = st.session_state.bot.generate_response(prompt)

    if isinstance(response, MessageItem):  # Check if response is an instance of MessageItem
        with st.chat_message("bot"):
            st.code(f"bot: {response.content.text}")
            # Append the bot's response to chat history
            chat_history.append(("bot", response.content.text))
