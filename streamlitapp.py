import streamlit as st
import openai

# Use the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

@st.cache(allow_output_mutation=True)
def get_chat_models():
    return openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
            {"role": "system", "content": "أنت مساعد مفيد."},
            {"role": "user", "content": "مرحبا، من أنت؟"},
        ]
    )

def get_response(message):
    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
            {"role": "system", "content": "أنت مساعد مفيد يتحدث العربية."},
            {"role": "user", "content": message},
        ]
    )
    return response['choices'][0]['message']['content']

def main():
    st.markdown("<h1 style='text-align: right; dir:rtl;'>روبوت الدردشة باللغة العربية</h1>", unsafe_allow_html=True)
    st.markdown("""
                <p style='text-align: right; dir:rtl;'>
                هذا روبوت الدردشة مدعوم من GPT-4 من OpenAI، وهو نموذج لغة (LM). روبوت الدردشة هو تطبيق برنامج يُستخدم لإجراء محادثة دردشة عبر الإنترنت عبر النص أو النص إلى الكلام، بدلاً من تقديم اتصال مباشر مع وكيل بشري حي. نموذج اللغة هو نوع من نماذج الذكاء الاصطناعي التي تنشئ نصًا يشبه الإنسان بناءً على الإدخال المعطى لها. مفهوم "القطع" يشير إلى النقطة التي تم تدريب النموذج عليها حتى البيانات. على سبيل المثال، تشمل بيانات التدريب الخاصة بي التي تم تضمينها معلومات حتى سبتمبر 2021، مما يعني أنني لا أعلم عن الأحداث في العالم بعد تلك التاريخ.
                </p>
                """, unsafe_allow_html=True)

    user_input = st.text_input("اكتب رسالتك هنا...")
    if st.button("إرسال"):
        response = get_response(user_input)
        st.markdown(f"<p style='text-align: right; dir:rtl;'>روبوت الدردشة: {response}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
