import streamlit as st
import app

st.title('OFFLINE CHATBOT')

#prompt = st.chat_input('Enter Your Question')
#msg = st.chat_message('user').write('who is messi')
#msg = st.chat_message('ai').write('messi is best player')

count = 0

st.write(st.session_state)
if 'count'not in st.session_state:
     st.session_state['count']=0
if st.button('add'):
    st.session_state['count']+=1
    st.write(f'count:{st.session_state['count']}')  

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role': 'ai',
    'content':'how can i help you?'}] 
   
for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])    

model = 'gemma3:1b'
prompt = st. chat_input('ask your question') 
if prompt:
    
    st.chat_message('user').write(prompt)
    st.session_state['messages'].append({'role': 'user','content': prompt})
    

    with st.spinner('Generatintg Awnser...'):
        response = app.call_ollama_model(prompt, model)
    
    st.chat_message('ai').write(response)
    st.session_state['messages'].append({'role':'ai', 'content':response})
    