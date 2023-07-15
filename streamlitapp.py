import streamlit as st
import openai
import config

# Use the OpenAI API key from the config file
openai.api_key = config.openai_api_key

def get_response(message):
    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []
    chat_log = st.session_state.chat_log
    chat_log.append({"role": "user", "content": message})
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=chat_log
    )
    
    chat_log.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    return response['choices'][0]['message']['content']

def main():
    st.markdown("<h1 style='text-align: right; dir:rtl;'>روبوت الدردشة باللغة العربية</h1>", unsafe_allow_html=True)
    st.markdown("""
                <p style='text-align: right; dir:rtl;'>
                هذا روبوت الدردشة مدعوم من GPT-4 من OpenAI، وهو نموذج لغة (LM). روبوت الدردشة هو تطبيق برنامج يُستخدم لإجراء محادثة دردشة عبر الإنترنت عبر النص أو النص إلى الكلام، بدلاً من تقديم اتصال مباشر مع وكيل بشري حي. نموذج اللغة هو نوع من نماذج الذكاء الاصطناعي التي تنشئ نصًا يشبه الإنسان بناءً على الإدخال المعطى لها. مفهوم "القطع" يشير إلى النقطة التي تم تدريب النموذج عليها حتى البيانات. على سبيل المثال، تشمل بيانات التدريب الخاصة بي التي تم تضمينها معلومات حتى سبتمبر 2021، مما يعني أنني لا أعلم عن الأحداث في العالم بعد تلك التاريخ.
                </p>
                """, unsafe_allow_html=True)

    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
    st.session_state.user_input = st.text_area("اكتب رسالتك هنا...", st.session_state.user_input)
    
    if st.button("إرسال"):
        response = get_response(st.session_state.user_input)
        st.markdown(f"<p style='text-align: right; dir:rtl;'>روبوت الدردشة: {response}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
