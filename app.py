import random
import streamlit as st

# ==========================================
# DỮ LIỆU CÂU HỎI PART 1 & PART 2
# ==========================================

PART1_QUESTIONS = [
    # Work / Study
    "Do you work or are you a student?",
    "What subject are you studying or what is your job?",
    "Why did you choose that subject or job?",
    "Do you enjoy your studies or your work?",
    # Hometown
    "Where is your hometown?",
    "What do you like most about your hometown?",
    "Is there anything you dislike about your hometown?",
    "Has your hometown changed much in recent years?",
    # Accommodation
    "Do you live in a house or an apartment?",
    "What is your favorite room in your home?",
    "What would you like to change about your home?",
    "How long have you lived there?",
    # Free time
    "What do you usually do in your spare time?",
    "Do you prefer spending your free time indoors or outdoors?",
    "Did you have any different hobbies when you were a child?",
    "Do you think hobbies should be shared with other people?",
    # Music
    "What kind of music do you like to listen to?",
    "How often do you listen to music?",
    "Did you listen to the same type of music when you were younger?",
    "Have you ever been to a live concert?",
    # Daily Routine
    "What is your daily routine?",
    "Which part of the day do you like best?",
    "Do you usually plan your time every day?",
    "What is the busiest time of the day for you?",
    # Friends
    "Do you prefer to spend time alone or with friends?",
    "What do you usually do with your friends?",
    "How do you keep in touch with your close friends?",
    "Is making new friends easy for you?",
]

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

# ==========================================
# THANH MENU ĐIỀU HƯỚNG (SIDEBAR)
# ==========================================
st.sidebar.title("📌 Menu Luyện Tập")
mode = st.sidebar.radio(
    "Chọn phần luyện tập:", ["Speaking Part 1", "Speaking Part 2"]
)

# ==========================================
# GIAO DIỆN PART 1
# ==========================================
if mode == "Speaking Part 1":
    st.title("🗣️ IELTS Speaking Part 1 Practice")

    if "shuffled_part1" not in st.session_state:
        p1_copy = PART1_QUESTIONS.copy()
        random.shuffle(p1_copy)
        st.session_state.shuffled_part1 = p1_copy
        st.session_state.p1_index = 0

    current_q = st.session_state.shuffled_part1[st.session_state.p1_index]
    st.subheader(
        f"Question {st.session_state.p1_index + 1}/{len(st.session_state.shuffled_part1)}:"
    )
    st.info(current_q)

    if "user_answer_p1" not in st.session_state:
        st.session_state.user_answer_p1 = ""

    answer_p1 = st.text_area(
        "Nói/Nhập câu trả lời Part 1 của bạn:",
        value=st.session_state.user_answer_p1,
        key="ans_p1",
    )

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔍 Check Answer"):
            if answer_p1.strip():
                st.success("Tuyệt vời!")
                st.write(f"**Câu trả lời của bạn:** {answer_p1}")
                st.write(
                    "💡 **Gợi ý:** Áp dụng công thức Answer + Reason + Example."
                )
            else:
                st.warning("Vui lòng nhập/nói câu trả lời trước nhé.")
    with c2:
        if st.button("➡️ Next Question"):
            st.session_state.p1_index = (st.session_state.p1_index + 1) % len(
                st.session_state.shuffled_part1
            )
            st.session_state.user_answer_p1 = ""
            if st.session_state.p1_index == 0:
                random.shuffle(st.session_state.shuffled_part1)
            st.rerun()

# ==========================================
# GIAO DIỆN PART 2
# ==========================================
else:
    st.title("🗣️ IELTS Speaking Part 2 Practice")

    if "shuffled_part2" not in st.session_state:
        p2_copy = PART2_DATA.copy()
        random.shuffle(p2_copy)
        st.session_state.shuffled_part2 = p2_copy
        st.session_state.p2_index = 0

    current_item = st.session_state.shuffled_part2[st.session_state.p2_index]
    st.subheader(
        f"Topic {st.session_state.p2_index + 1}/{len(st.session_state.shuffled_part2)}: {current_item['topic']}"
    )
    st.info(current_item["question"])

    if "user_answer_p2" not in st.session_state:
        st.session_state.user_answer_p2 = ""

    answer_p2 = st.text_area(
        "Nói/Nhập câu trả lời Part 2 của bạn:",
        value=st.session_state.user_answer_p2,
        height=150,
        key="ans_p2",
    )

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔍 Check Answer (Xem Bài Mẫu)"):
            if answer_p2.strip():
                st.success("Cùng đối chiếu nhé!")
                st.write(f"**Bài nói của bạn:**\n{answer_p2}")
                st.markdown("---")
                st.write(
                    f"🌟 **Bài nói mẫu chuẩn:**\n{current_item['ideal_answer']}"
                )
            else:
                st.warning("Vui lòng nhập/nói câu trả lời trước nhé.")
    with c2:
        if st.button("➡️ Next Topic"):
            st.session_state.p2_index = (st.session_state.p2_index + 1) % len(
                st.session_state.shuffled_part2
            )
            st.session_state.user_answer_p2 = ""
            if st.session_state.p2_index == 0:
                random.shuffle(st.session_state.shuffled_part2)
            st.rerun()
