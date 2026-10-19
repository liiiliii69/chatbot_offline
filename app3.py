import streamlit as st
import app

st.title('OFFLINE CHATBOT')

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {'role': 'ai', 'content': 'how can i help you?'}
    ]

if 'stop' not in st.session_state:
    st.session_state['stop'] = False

if st.button('Clear History'):
    st.session_state['messages'] = [
        {'role': 'ai', 'content': 'how can i help you?'}
    ]
    st.rerun()

if st.button('Stop Model'):
    st.session_state['stop'] = True

for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])

model = 'gemma3:1b'
prompt = st.chat_input('ask your question')

if prompt and not st.session_state['stop']:

    st.session_state['messages'].append(
        {'role': 'user', 'content': prompt}
    )

    st.chat_message('user').write(prompt)

    with st.spinner('Generating Answer...'):
        response = app.call_ollama_model(prompt, model)

    if not st.session_state['stop']:
        st.chat_message('ai').write(response)

        st.session_state['messages'].append(
            {'role': 'ai', 'content': response}
        )

    st.session_state['stop'] = False