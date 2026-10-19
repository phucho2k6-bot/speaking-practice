import random
import streamlit as st

# Bộ dữ liệu 8 câu hỏi Part 2 kèm đáp án chuẩn từ bạn
PART2_DATA = [
    {
        "topic": "1. A sports match you watched",
        "question": """Describe a live sports match you watched.
You should say:
• What match it was
• Where and when you watched it
• What happened during the match
And explain how you felt after watching it.""",
        "ideal_answer": "I watched a live football match between Vietnam and Thailand last year at a stadium. The atmosphere was very exciting because many fans cheered loudly. I liked it the most when Vietnam scored a goal in the last few minutes. Everyone was happy and shouted with joy. After watching the match, I felt excited and proud of my country. It was an unforgettable experience for me.",
    },
    {
        "topic": "2. Your favorite sport",
        "question": """Describe your favorite sport.
You should say:
• What sport it is
• How often and with whom you play it
• What equipment is needed
And explain why this is your favorite sport.""",
        "ideal_answer": "My favorite sport is football. I usually play it with my friends twice a week and watch football matches on TV at weekends. To play football, we need a ball, sports shoes and comfortable clothes. I love this sport because it is fun and helps me stay healthy. It also teaches me teamwork and helps me make more friends. That is why football is my favorite sport.",
    },
    {
        "topic": "3. A healthy lifestyle you know",
        "question": """Describe a healthy lifestyle you know about.
You should say:
• What kind of lifestyle it is
• How you learned about it
• What activities are involved
And explain why you think this lifestyle is healthy.""",
        "ideal_answer": "A healthy lifestyle I know is doing exercise regularly. I learned about it from my parents, teachers and the internet. I usually exercise in the morning or play sports with my friends in the afternoon. I think this lifestyle is healthy because it helps me become stronger and feel happier. It also helps me reduce stress and sleep better. I believe everyone should exercise regularly to stay healthy.",
    },
    {
        "topic": "4. A time you were sick",
        "question": """Describe a time when you were sick.
You should say:
• What illness you had and when it was
• Why you got sick
• What you did to recover
And explain how this experience affected you.""",
        "ideal_answer": "Last year, I had a bad cold. I got sick because I stayed up late and did not get enough rest. I had a headache and a runny nose, so I felt very tired. To get better, I took medicine, drank warm water and slept more. After a few days, I felt much better. This experience taught me to take better care of my health.",
    },
    {
        "topic": "5. Your favorite method of transport",
        "question": """Describe your favorite mode of transport.
You should say:
• What mode of transport it is
• How often you use it
• Why it is popular in your country
And explain why you prefer this mode of transport.""",
        "ideal_answer": "My favorite method of transport is the motorbike. I use it almost every day to go to university and visit my friends. It is very popular in Vietnam because it is fast and convenient. I enjoy riding a motorbike because I can travel easily and save time. However, I always wear a helmet to keep myself safe.",
    },
    {
        "topic": "6. A time you were stuck in a traffic jam",
        "question": """Describe a time you were stuck in a traffic jam.
You should say:
• When and where it happened
• How long you waited
• What you did while waiting
And explain how you felt about this experience.""",
        "ideal_answer": "Last Monday morning, I was stuck in a big traffic jam when I was going to school. The street was full of cars and motorbikes. I had to wait for about 40 minutes under the sun. I felt very tired, worried and stressed because I thought I would be late for my class. It was a really bad experience for me.",
    },
    {
        "topic": "7. A difficult challenge you faced",
        "question": """Describe a difficult challenge you faced.
You should say:
• What the challenge was
• When you faced it
• How you handled/overcame it
And explain how you felt after overcoming it.""",
        "ideal_answer": "One difficult challenge I faced was preparing for an important exam last year when I was in high school. I had many subjects to study, so I felt tired and worried about my results. To overcome this challenge, I made a study plan and tried my best every day. In the end, I passed the exam and felt very happy and proud of myself.",
    },
    {
        "topic": "8. An important achievement you made",
        "question": """Describe an important achievement you have made.
You should say:
• What the achievement was
• When and where you achieved it
• How you achieved it
And explain why this achievement was important to you.""",
        "ideal_answer": "One important achievement I have made was passing my university entrance exam. I achieved this two years ago in Vietnam. To get good results, I studied hard every day, did many exercises and reviewed my lessons carefully. I felt very happy and proud when I received my results. This achievement was important to me because I could enter my dream university and make my family proud.",
    },
]

# Khởi tạo danh sách xáo trộn trong session_state
if "shuffled_part2" not in st.session_state:
    data_copy = PART2_DATA.copy()
    random.shuffle(data_copy)
    st.session_state.shuffled_part2 = data_copy
    st.session_state.current_index = 0

st.title("🗣️ IELTS Speaking Part 2 Practice")

# Lấy đề bài hiện tại
current_item = st.session_state.shuffled_part2[st.session_state.current_index]

st.subheader(
    f"Topic {st.session_state.current_index + 1}/{len(st.session_state.shuffled_part2)}: {current_item['topic']}"
)

# Hiển thị Cue Card (Đề bài Part 2)
st.info(current_item["question"])

# Khởi tạo giá trị ô nhập
if "user_answer" not in st.session_state:
    st.session_state.user_answer = ""

answer_input = st.text_area(
    "Nói/Nhập câu trả lời của bạn vào đây (Sử dụng Micro bàn phím):",
    value=st.session_state.user_answer,
    height=150,
    key="answer_box",
)

col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Check Answer (Xem Đáp Án Mẫu)"):
        if answer_input.strip():
            st.success("Cùng đối chiếu câu trả lời của bạn nhé!")
            st.write(f"**Bài nói của bạn:**\n{answer_input}")
            st.markdown("---")
            st.write(
                f"🌟 **Đáp án mẫu chuẩn (Ideal Answer):**\n{current_item['ideal_answer']}"
            )
        else:
            st.warning("Vui lòng bật Micro nói hoặc gõ câu trả lời trước nhé!")

with col2:
    if st.button("➡️ Next Topic (Chủ đề tiếp)"):
        st.session_state.current_index = (
            st.session_state.current_index + 1
        ) % len(st.session_state.shuffled_part2)
        st.session_state.user_answer = ""

        # Xáo trộn lại khi hết 1 vòng
        if st.session_state.current_index == 0:
            random.shuffle(st.session_state.shuffled_part2)

        st.rerun()
