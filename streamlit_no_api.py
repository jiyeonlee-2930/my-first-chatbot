import streamlit as st
import random
import time

st.title("나의 첫 번째 챗봇 🤖")

st.write(
    "Streamlit을 이용하여 만든 간단한 챗봇입니다."
)

st.caption(
    "현재는 실제 LLM과 연결되지 않은 연습용 챗봇입니다."
)

# ----------------------------------
# 1. 대화 기록 초기화
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요! 무엇을 도와드릴까요?"
        }
    ]


# ----------------------------------
# 2. 이전 대화 화면에 출력
# ----------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ----------------------------------
# 3. 사용자 입력
# ----------------------------------

if prompt := st.chat_input("질문을 입력하세요"):

    # 사용자 질문 저장
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # 사용자 질문 출력
    with st.chat_message("user"):
        st.markdown(prompt)


    # ----------------------------------
    # 4. 챗봇 답변
    # ----------------------------------

    with st.chat_message("assistant"):

        message_placeholder = st.empty()

        full_response = ""

        assistant_response = random.choice(
            [
                "안녕하세요! 무엇을 도와드릴까요?",
                "반갑습니다. 궁금한 것을 질문해 주세요.",
                "네, 제가 도와드리겠습니다."
            ]
        )


        # 타이핑 효과
        for chunk in assistant_response.split():

            full_response += chunk + " "

            time.sleep(0.05)

            message_placeholder.markdown(
                full_response + "▌"
            )

        message_placeholder.markdown(full_response)


    # ----------------------------------
    # 5. AI 답변 저장
    # ----------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )