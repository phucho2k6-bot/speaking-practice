import random
import streamlit as st

# ==========================================
# DỮ LIỆU CÂU HỎI & ĐÁP ÁN PART 1 (GIỮ NGUYÊN 100% ĐÁP ÁN CỦA BẠN)
# ==========================================
PART1_DATA = [
    {
        "question": "Where are you from? Can you tell me something about your hometown? How often do you visit your grandparents?",
        "ideal_answer": "I come from Da Nang, It is a nice city with many clean beaches. I vitsit my grandparents once a moth because they live far away.",
    },
    {
        "question": "What are your favorite outdoor activities? Where and with whom do you play them?",
        "ideal_answer": "I like playing football. I usually play it at the park near my house with my friends.",
    },
    {
        "question": "Do you play sports? How often do you exercise? Can you tell me the benefits of exercising?",
        "ideal_answer": "Yes,. I play sports two time a week. It help me stay healthy and feel relaxed after school",
    },
    {
        "question": "What do you usually wear to class? Why?",
        "ideal_answer": "I usually wear a T-shirt and jeans to class. I wear them because they are simple and comfortable",
    },
    {
        "question": "What do you usually do in your free time?",
        "ideal_answer": "In my free time, I often watch tivi or learn Japanese",
    },
    {
        "question": "What do you usually do at weekends? What did you do last weekend?",
        "ideal_answer": "On weekends, I usually learn more English or Japanese. Last week, I went to the beach with my friends",
    },
    {
        "question": "How many seasons are there in a year? What do you usually do in spring?",
        "ideal_answer": "There are four seasons in my country. In spring, I usually clean the house to celebrate Tet",
    },
    {
        "question": "Are there any festivals in your country? What do you usually do during them?",
        "ideal_answer": "Yes, we have Tet holiday, When it come, I often go to wish Tet and visit temples",
    },
    {
        "question": "What do you usually do during the summer holidays? What did you do last summer?",
        "ideal_answer": "In summer, I often work park-time and help my family. Last summer, I went to the beach with my friends",
    },
    {
        "question": "Do you like watching films? What genres do you like? What is your favorite film and what is it about?",
        "ideal_answer": 'Yes, I like movie. My favorite type is comedy. My favorite film is "Làm giàu với ma" because it is very fun. It tells the journey of bringing Na\'s soul home',
    },
    {
        "question": "Is technology necessary for your life? Can you tell me the advantages and disadvantages of technology in our life?",
        "ideal_answer": "Yes, it necessary for my life. It makes our lives easier but it also makes us lazy",
    },
    {
        "question": "Where do you study? What is your major? Why did you choose it?",
        "ideal_answer": "I study at university. My major is Chemical engineering. I choose it because I good at chemistry and theory",
    },
    {
        "question": "What was your favorite subject in high school? Why?",
        "ideal_answer": "My favorite subject in high school was chemistry. I like it because it brings a lot of fun and is very interesting.",
    },
    {
        "question": "Where do you live? How far is your home from school? How do you usually get to school? Do you use public transport to get to school? Why?",
        "ideal_answer": "I live in K144/60 Nguyen Luong Bang. I'm about 1km from the school. I walk to school. I don't usually take the bus because i'm close to the school",
    },
    {
        "question": "Who is the person you are closest to in your family? Why? Do you spend much time with them? What do you usually do together?",
        "ideal_answer": "I'm closest to my mother because she talk to me the most and is very caring. Yes, I spend a lot of time with my mom. I usually help her with household chores every day",
    },
    {
        "question": "Which room in your house is your favorite? Why?",
        "ideal_answer": "My favorite room is my bedroom because it is quiet and I can rest well there",
    },
    {
        "question": "When is your birthday? What do you usually do on your birthday? What gifts do you usually receive?",
        "ideal_answer": "My birthday is December 11th. I usually eat cake with my friends. I'm often given gifts and wishes",
    },
    {
        "question": "Do you often use a computer? What are the advantages and disadvantages of computers?",
        "ideal_answer": "Yes, I use a computer every day. It is good for finding information but bad because it makes my eyes tired",
    },
    {
        "question": "What do you usually do in the evening? Should we spend the evening with family?",
        "ideal_answer": "In the evening, I do homework  and listen music. Yes, We should spend evenings with my family because to talk and relax together",
    },
    {
        "question": "Do you often keep in touch with your best friend? How do you contact each other? What do you usually do together?",
        "ideal_answer": "No, i rarely contact my friends. I contact my friends via messenger. We often go out",
    },
    {
        "question": "Who usually does the cooking in your family? Do you often cook? Why?",
        "ideal_answer": "My mother cooks in my family. I also cook sometimes because I want to help my mother",
    },
    {
        "question": "What is your favorite dish? How is it made?",
        "ideal_answer": "My favorite food is fried rice. It is made with rice, eggs, salad and meat",
    },
    {
        "question": "What are your hobbies? How much time do you spend on your hobbies?",
        "ideal_answer": "My hobby is playing games. I spend about one hour a day on my hobby",
    },
    {
        "question": "Do you live in a house or an apartment? Would you prefer to live in a house or an apartment? Why? What would you like to change about your home?",
        "ideal_answer": "I live in an apartment but I like a house more because it is bigger. I wanna add more plants to my house",
    },
    {
        "question": "Do you often ride a bicycle? How old were you when you learned to ride a bike? Is cycling encouraged in your country? Why?",
        "ideal_answer": "I do not ride a bike now but I learned it when I was 7 year old. In my country there are a lot of people who ride bicycles because it is very convenient to move. Cycling is highly recommended because it is healthy and clean for the air",
    },
    {
        "question": "Do you like traveling? When was your last trip and where did you go? What did you do there?",
        "ideal_answer": "Yes, I love travelling. The last time I traveled was 4 moths ago. I went to Dai Noi Hue and visited the monuments",
    },
    {
        "question": "How many languages can you speak? Would you like to learn a new language? Why?",
        "ideal_answer": "I can speak two language. English and Japanese. I like to learn a new language but only if it is work-related",
    },
    {
        "question": "When did you start learning a foreign language? How can someone learn a foreign language well?",
        "ideal_answer": "I started learning English in primary school. To learn well, you should expose it daily",
    },
    {
        "question": "What kind of music do you like? How much time do you spend listening to music and when do you usually listen? Who is your favorite singer?",
        "ideal_answer": "I like pop music. I listen for two hour every day when I study. My favorite singer is MCK.",
    },
    {
        "question": "Do you often go shopping? Who usually buys food for your family? Do you prefer shopping online or at physical shops? Why?",
        "ideal_answer": "I don't often go shopping. My mom usually goes shopping the most. I prefer online shopping because it is cheaper and more convenient",
    },
]

# ==========================================
# DỮ LIỆU CÂU HỎI & ĐÁP ÁN PART 2 (GIỮ NGUYÊN 100% ĐÁP ÁN CỦA BẠN)
# ==========================================
PART2_DATA = [
    {
        "topic": "1. A sports match you watched",
        "question": """Describe a live sports match you watched.
You should say:
• What match it was
• Where and when you watched it
• What happened during the match
And explain how you felt after watching it.""",
        "ideal_answer": "I watched a live football match between Vienam and Thailand last year at a stadium. The atmosphere was very exciting because many fans cheered louly. I liked the most when Vietnam scored a goal in the last few minutes. everyone was happy and shouted with joy. After watching the match, I felt excited and proud of my country. It was an unforgettable experience for me.",
    },
    {
        "topic": "2. Your favorite sport",
        "question": """Describe your favorite sport.
You should say:
• What sport it is
• How often and with whom you play it
• What equipment is needed
And explain why this is your favorite sport.""",
        "ideal_answer": "My favorite sport is football. I usually plat it with my friends twice a week and watch football matches on TV at weekends. To play football, we need a ball, sports shoes and comfortable clothes. I love this sport because it is fun and helps me stay healthy. It also teahes me teamwork and helps me make more fiends. That is why football is my favorite sport.",
    },
    {
        "topic": "3. A healthy lifestyle you know",
        "question": """Describe a healthy lifestyle you know about.
You should say:
• What kind of lifestyle it is
• How you learned about it
• What activities are involved
And explain why you think this lifestyle is healthy.""",
        "ideal_answer": "A healthy lifestyle I know is doing exercise regularly. I learned abouot it from my parents, teaches and the internet. I usually exercise in the morning or play sports with my friends in the afternoon. I think this lifestyle is healthy because it helps me become stronges and feel happier. It also helps me reduce stress and sleep better. I believe everyone should exercise regularly to stay healthy.",
    },
    {
        "topic": "4. A time you were sick",
        "question": """Describe a time when you were sick.
You should say:
• What illness you had and when it was
• Why you got sick
• What you did to recover
And explain how this experience affected you.""",
        "ideal_answer": "last year, I had a bad cold. I got sick because I stayed up late and did not get enough rest. I had a headache and a runny nose, so I felt very tired. To get better, I took medicine, drank warm water and slept more. After a few day, I felt much better. This experience taught me to take better care of my healthy.",
    },
    {
        "topic": "5. Your favorite method of transport",
        "question": """Describe your favorite mode of transport.
You should say:
• What mode of transport it is
• How often you use it
• Why it is popular in your country
And explain why you prefer this mode of transport.""",
        "ideal_answer": "My favorite method of transport is the motorbike. I use it almost every day to gonna university and visit my friends. It is very popular in Vietnam because it is fast and convenient. I enjoy riding a motorbike because I can travel easily and save time. However, I always wear a helmet to keep myself safr.",
    },
    {
        "topic": "6. A time you were stuck in a traffic jam",
        "question": """Describe a time you were stuck in a traffic jam.
You should say:
• When and where it happened
• How long you waited
• What you did while waiting
And explain how you felt about this experience.""",
        "ideal_answer": "Last Monday morning, I was stuck in a big traffic jam when I was going to school. The street was full of cars and motorbikes. I had to wait for about 40 minutes under the sun. I felt very tired, worried and stressed necause I thought I would be late for my class. It was a really bed experience for me.",
    },
    {
        "topic": "7. A difficult challenge you faced",
        "question": """Describe a difficult challenge you faced.
You should say:
• What the challenge was
• When you faced it
• How you handled/overcame it
And explain how you felt after overcoming it.""",
        "ideal_answer": "One difficult challenge I faced was preparing fo an information exam last year when I was in high school. I had many subject to study, so I felt tired anf worried about my results. To overcome this challenge, I made a study plan and tied my best every day. In the end, I passed the exam and felt very happy and proud of myself.",
    },
    {
        "topic": "8. An important achievement you made",
        "question": """Describe an important achievement you have made.
You should say:
• What the achievement was
• When and where you achieved it
• How you achieved it
And explain why this achievement was important to you.""",
        "ideal_answer": "One important achievement I have made was passing my university entrance exam. I achieved this two years ago in Vietnam. To get good result, I studied hard every day, did many exercises and review my lesson carefully. I felt very happy and proud when I received my results. This achievement was important to me because I could enter my dream university and make my family proud",
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
        p1_copy = PART1_DATA.copy()
        random.shuffle(p1_copy)
        st.session_state.shuffled_part1 = p1_copy
        st.session_state.p1_index = 0

    current_item_p1 = st.session_state.shuffled_part1[st.session_state.p1_index]
    st.subheader(
        f"Question {st.session_state.p1_index + 1}/{len(st.session_state.shuffled_part1)}:"
    )
    st.info(current_item_p1["question"])

    if "user_answer_p1" not in st.session_state:
        st.session_state.user_answer_p1 = ""

    answer_p1 = st.text_area(
        "Nói/Nhập câu trả lời Part 1 của bạn:",
        value=st.session_state.user_answer_p1,
        key="ans_p1",
    )

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔍 Check Answer (Xem Đáp Án Mẫu)"):
            if answer_p1.strip():
                st.success("Cùng đối chiếu nhé!")
                st.write(f"**Câu trả lời của bạn:**\n{answer_p1}")
                st.markdown("---")
                st.write(
                    f"🌟 **Đáp án mẫu chuẩn:**\n{current_item_p1['ideal_answer']}"
                )
            else:
                st.warning("Vui lòng bật Micro nói hoặc gõ câu trả lời trước nhé!")
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

    current_item_p2 = st.session_state.shuffled_part2[st.session_state.p2_index]
    st.subheader(
        f"Topic {st.session_state.p2_index + 1}/{len(st.session_state.shuffled_part2)}: {current_item_p2['topic']}"
    )
    st.info(current_item_p2["question"])

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
                    f"🌟 **Bài nói mẫu chuẩn:**\n{current_item_p2['ideal_answer']}"
                )
            else:
                st.warning("Vui lòng bật Micro nói hoặc gõ câu trả lời trước nhé!")
    with c2:
        if st.button("➡️ Next Topic"):
            st.session_state.p2_index = (st.session_state.p2_index + 1) % len(
                st.session_state.shuffled_part2
            )
            st.session_state.user_answer_p2 = ""
            if st.session_state.p2_index == 0:
                random.shuffle(st.session_state.shuffled_part2)
            st.rerun()
