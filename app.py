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
