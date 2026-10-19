import streamlit as st

st.set_page_config(page_title="Luyện thi Speaking - Part 1", layout="centered")

st.title("🎯 Luyện thi Speaking English - Part 1")
st.caption("Gõ câu trả lời của bạn và bấm Check Answer để kiểm tra lỗi.")

# Danh sách 30 câu hỏi
questions = [
    {
        "id": 1,
        "question": "Where are you from? Can you tell me something about your hometown? How often do you visit your grandparents?",
        "corrections": "• **vitsit** ➔ **visit** (Lỗi chính tả)\n• **moth** ➔ **month** (Lỗi chính tả: 'moth' nghĩa là con bướm đêm)\n• **It is** ➔ **it is** (Chữ 'I' không cần viết hoa sau dấu phẩy)",
        "ideal_ans": "I come from Da Nang. It is a nice city with many clean beaches. I visit my grandparents once a month because they live far away."
    },
    {
        "id": 2,
        "question": "What is your favorite outdoor activity? Where do you play it and with whom?",
        "corrections": "• **at park** ➔ **at the park** (Thiếu mạo từ 'the')",
        "ideal_ans": "I like playing football. I usually play it at the park near my house with my friends."
    },
    {
        "id": 3,
        "question": "Do you play sports? How often do you play? What are the benefits of playing sports?",
        "corrections": "• **Yes,.** ➔ **Yes,** (Thừa dấu chấm)\n• **two time** ➔ **two times** (Danh từ số nhiều)\n• **It help** ➔ **It helps** (Chia động từ số ít)",
        "ideal_ans": "Yes, I play sports two times a week. It helps me stay healthy and feel relaxed after school."
    },
    {
        "id": 4,
        "question": "What do you usually wear to class? Why?",
        "corrections": "• **Tốt!** Không có lỗi ngữ pháp nghiêm trọng.",
        "ideal_ans": "I usually wear a T-shirt and jeans to class. I wear them because they are simple and comfortable."
    },
    {
        "id": 5,
        "question": "What do you usually do in your free time?",
        "corrections": "• **tivi** ➔ **TV** hoặc **television** (Từ chuẩn tiếng Anh)\n• **learn Japanese** ➔ **study Japanese** (Tự nhiên hơn)",
        "ideal_ans": "In my free time, I often watch TV or study Japanese."
    },
    {
        "id": 6,
        "question": "What do you usually do on weekends? What did you do last weekend?",
        "corrections": "• **learn more** ➔ **study**\n• **Last week** ➔ **Last weekend**",
        "ideal_ans": "On weekends, I usually study English or Japanese. Last weekend, I went to the beach with my friends."
    },
    {
        "id": 7,
        "question": "How many seasons are there in a year? What do you usually do in spring?",
        "corrections": "• **Tốt!** Câu trả lời chính xác.",
        "ideal_ans": "There are four seasons in my country. In spring, I usually clean the house to celebrate Tet."
    },
    {
        "id": 8,
        "question": "Are there any festivals in your country? What do you usually do then?",
        "corrections": "• **holiday, When** ➔ **holiday. When**\n• **it come** ➔ **it comes**\n• **wish Tet** ➔ **give Tet wishes to my relatives**",
        "ideal_ans": "Yes, we have Tet holiday. When it comes, I often visit my relatives to give Tet wishes and go to temples."
    },
    {
        "id": 9,
        "question": "What do you usually do during summer vacation? What did you do last summer?",
        "corrections": "• **park-time** ➔ **part-time** (Lỗi chính tả)",
        "ideal_ans": "In summer, I often work part-time and help my family. Last summer, I went to the beach with my friends."
    },
    {
        "id": 10,
        "question": "Do you like watching movies? What type of movie do you like? What is your favorite film and what is it about?",
        "corrections": "• **like movie** ➔ **like movies** (Số nhiều)\n• **very fun** ➔ **very funny**",
        "ideal_ans": "Yes, I like movies. My favorite type is comedy. My favorite film is \"Làm giàu với ma\" because it is very funny. It tells about the journey of bringing Na's soul home."
    },
    {
        "id": 11,
        "question": "Is science and technology necessary for your life? Can you tell me the advantages and disadvantages of technology in our lives?",
        "corrections": "• **it necessary** ➔ **it is necessary** (Thiếu tobe 'is')",
        "ideal_ans": "Yes, it is necessary for my life. It makes our lives easier, but it also makes us lazy."
    },
    {
        "id": 12,
        "question": "Where do you study? What is your major? Why did you choose it?",
        "corrections": "• **I choose** ➔ **I chose** (Quá khứ)\n• **I good at** ➔ **I am good at** (Thiếu tobe 'am')",
        "ideal_ans": "I study at university. My major is Chemical engineering. I chose it because I am good at chemistry and theory."
    },
    {
        "id": 13,
        "question": "What was your favorite subject in high school? Why?",
        "corrections": "• **I like it** ➔ **I liked it** (Thì quá khứ)",
        "ideal_ans": "My favorite subject in high school was chemistry. I liked it because it was fun and very interesting."
    },
    {
        "id": 14,
        "question": "Where do you live? How far is it from school? How do you get to school? Do you take public transport?",
        "corrections": "• **because i'm** ➔ **because I'm** (Viết hoa chữ 'I')",
        "ideal_ans": "I live at K144/60 Nguyen Luong Bang Street. It's about 1km from my school. I walk to school and I don't usually take the bus because I live close by."
    },
    {
        "id": 15,
        "question": "Who are you closest to in your family? Why? Do you spend much time with them?",
        "corrections": "• **she talk** ➔ **she talks** (Chia động từ số ít)",
        "ideal_ans": "I'm closest to my mother because she talks to me the most and is very caring. Yes, I spend a lot of time with my mom and help her with household chores every day."
    },
    {
        "id": 16,
        "question": "Which room in your house do you like best? Why?",
        "corrections": "• **Tốt!** Chuẩn cấu trúc.",
        "ideal_ans": "My favorite room is my bedroom because it is quiet and I can rest well there."
    },
    {
        "id": 17,
        "question": "When is your birthday? What do you usually do on your birthday?",
        "corrections": "• **is December 11th** ➔ **is on December 11th** (Thiếu 'on')",
        "ideal_ans": "My birthday is on December 11th. I usually eat cake with my friends and get gifts and birthday wishes."
    },
    {
        "id": 18,
        "question": "Do you often use a computer? What are the advantages and disadvantages of using a computer?",
        "corrections": "• **Tốt!** Tự nhiên và chính xác.",
        "ideal_ans": "Yes, I use a computer every day. It is good for finding information, but bad because it makes my eyes tired."
    },
    {
        "id": 19,
        "question": "What do you usually do in the evening? Should we spend evenings with family?",
        "corrections": "• **listen music** ➔ **listen to music**\n• **Yes, We** ➔ **Yes, we**\n• **because to talk** ➔ **to talk**",
        "ideal_ans": "In the evening, I do homework and listen to music. Yes, we should spend evenings with our family to talk and relax together."
    },
    {
        "id": 20,
        "question": "Do you often keep in touch with your best friend? How? What do you do together?",
        "corrections": "• **i rarely** ➔ **I rarely** (Viết hoa 'I')\n• **messenger** ➔ **Messenger**",
        "ideal_ans": "No, I rarely contact my friends. When I do, I contact them via Messenger and we often go out."
    },
    {
        "id": 21,
        "question": "Who usually cooks in your family? Do you cook? Why?",
        "corrections": "• **Tốt!** Đúng cấu trúc.",
        "ideal_ans": "My mother cooks in my family. I also cook sometimes because I want to help my mother."
    },
    {
        "id": 22,
        "question": "What is your favorite dish? How is it made?",
        "corrections": "• **salad** ➔ **vegetables**",
        "ideal_ans": "My favorite dish is fried rice. It is made with rice, eggs, vegetables, and meat."
    },
    {
        "id": 23,
        "question": "What is your hobby? How much time do you spend on it?",
        "corrections": "• **Tốt!** Đúng trọng tâm.",
        "ideal_ans": "My hobby is playing games. I spend about one hour a day on my hobby."
    },
    {
        "id": 24,
        "question": "Do you live in a house or an apartment? Which do you prefer? What would you like to change in your home?",
        "corrections": "• **wanna** ➔ **want to**",
        "ideal_ans": "I live in an apartment, but I like a house more because it is bigger. I want to add more plants to my home."
    },
    {
        "id": 25,
        "question": "Do you often ride a bicycle? At what age did you learn? Do many people ride bikes in your country? Why is cycling encouraged?",
        "corrections": "• **7 year old** ➔ **7 years old**\n• **clean for the air** ➔ **good for the environment**",
        "ideal_ans": "I do not ride a bike now, but I learned when I was 7 years old. In my country, many people ride bicycles because it is convenient. Cycling is recommended because it is healthy and good for the environment."
    },
    {
        "id": 26,
        "question": "Do you like traveling? When was the last time you traveled? Where did you go and what did you do?",
        "corrections": "• **moths** ➔ **months** (Lỗi chính tả)",
        "ideal_ans": "Yes, I love traveling. The last time I traveled was 4 months ago. I went to the Imperial City of Hue and visited historical monuments."
    },
    {
        "id": 27,
        "question": "How many languages can you speak? Do you like learning a new language? Why?",
        "corrections": "• **two language** ➔ **two languages** (Số nhiều)",
        "ideal_ans": "I can speak two languages: English and Japanese. I like learning a new language, but only if it is work-related."
    },
    {
        "id": 28,
        "question": "When did you start learning a foreign language? How can someone learn a foreign language well?",
        "corrections": "• **expose it daily** ➔ **practice it daily**",
        "ideal_ans": "I started learning English in primary school. To learn well, you should practice it daily."
    },
    {
        "id": 29,
        "question": "What is your favorite type of music? How much time do you spend listening to music? Who is your favorite singer?",
        "corrections": "• **two hour** ➔ **two hours**\n• **listen for** ➔ **listen to music for**",
        "ideal_ans": "I like pop music. I listen to music for two hours every day when I study. My favorite singer is MCK."
    },
    {
        "id": 30,
        "question": "Do you often go shopping? Who usually buys groceries in your home? Do you prefer online or in-store shopping?",
        "corrections": "• **pefer** ➔ **prefer** (Lỗi chính tả)",
        "ideal_ans": "I don't often go shopping. My mom usually buys groceries. I prefer online shopping because it is cheaper and more convenient."
    }
]

# Quản lý trạng thái câu hỏi hiện tại
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

current_q = questions[st.session_state.q_index]

# Thanh tiến trình
progress = (st.session_state.q_index + 1) / len(questions)
st.progress(progress)
st.write(f"**Câu hỏi {st.session_state.q_index + 1} / {len(questions)}**")

# Hiển thị câu hỏi
st.subheader(f"Question {current_q['id']}:")
st.info(current_q["question"])

# Tạo khóa riêng biệt cho mỗi ô nhập để xóa sạch văn bản cũ
input_key = f"user_ans_{st.session_state.q_index}"

user_input = st.text_area("Nhập câu trả lời của bạn vào đây:", value="", height=120, key=input_key)

col1, col2 = st.columns(2)

# Nút kiểm tra
if col1.button("🔍 Check Answer (Kiểm tra)", type="primary"):
    if not user_input.strip():
        st.warning("⚠️ Hãy nhập câu trả lời của bạn vào ô trên trước khi kiểm tra nhé!")
    else:
        st.markdown("---")
        st.write("### ✍️ Câu bạn vừa nhập:")
        st.write(f"> *{user_input}*")
        
        st.write("### 🛠️ Phân tích & Gợi ý sửa lỗi:")
        st.error(f"**Các lỗi cần tránh:**\n\n{current_q['corrections']}")
        st.success(f"**Gợi ý đáp án chuẩn (Ideal Answer):**\n\n{current_q['ideal_ans']}")

# Nút sang câu tiếp theo
if col2.button("➡️ Next Question (Câu tiếp)"):
    if st.session_state.q_index < len(questions) - 1:
        st.session_state.q_index += 1
        st.rerun()
    else:
        st.balloons()
        st.success("🎉 Bạn đã hoàn thành tất cả 30 câu hỏi Part 1!")
        import random
import streamlit as st
# Danh sách câu hỏi IELTS Speaking Part 1
QUESTIONS = [
    "What is your name?",
    "Where are you from?",
    "Do you work or are you a student?",
    "What do you like about your hometown?",
    "What do you usually do in your free time?",
    "Do you prefer spending time alone or with friends?",
    "How often do you use social media?",
    "What kind of music do you like listening to?",
]

# Khởi tạo danh sách câu hỏi đã xáo trộn trong session_state
if "shuffled_questions" not in st.session_state:
    questions_copy = QUESTIONS.copy()
    random.shuffle(questions_copy)
    st.session_state.shuffled_questions = questions_copy
    st.session_state.current_index = 0

st.title("🗣️ IELTS Speaking Part 1 Practice")

# Lấy câu hỏi hiện tại
current_question = st.session_state.shuffled_questions[
    st.session_state.current_index
]
st.subheader(
    f"Question {st.session_state.current_index + 1}/{len(st.session_state.shuffled_questions)}:"
)
st.info(current_question)

# Khởi tạo giá trị ô nhập liệu
if "user_answer" not in st.session_state:
    st.session_state.user_answer = ""

# Ô nhập câu trả lời
answer_input = st.text_area(
    "Your Answer (Use voice/keyboard):",
    value=st.session_state.user_answer,
    key="answer_box",
)

col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Check Answer"):
        if answer_input.strip():
            st.success("Great job! Here is your feedback:")
            st.write(f"**Your response:** {answer_input}")
            # Thêm gợi ý trả lời mẫu (Ideal Answer)
            st.write(
                "💡 **Ideal Answer Hint:** Try to extend your answer with reasons and examples."
            )
        else:
            st.warning("Please enter or speak your answer first.")

with col2:
    if st.button("➡️ Next Question"):
        # Chuyển sang câu tiếp theo
        st.session_state.current_index = (
            st.session_state.current_index + 1
        ) % len(st.session_state.shuffled_questions)

        # Xóa nội dung ô nhập câu trả lời
        st.session_state.user_answer = ""

        # Xáo trộn lại danh sách khi đã trả lời hết lượt
        if st.session_state.current_index == 0:
            random.shuffle(st.session_state.shuffled_questions)

        st.rerun()
