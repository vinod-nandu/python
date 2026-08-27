import streamlit as st

# ---------- Page config ----------
st.set_page_config(
    page_title="Grade Scale Calculator",
    page_icon="🎓",
    layout="centered",
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #f5f7fa 0%, #e8ecf1 100%);
}
.title-box {
    text-align: center;
    padding: 1.2rem 0 0.4rem 0;
}
.title-box h1 {
    font-size: 2.4rem;
    margin-bottom: 0;
    background: linear-gradient(90deg, #4f46e5, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.title-box p {
    color: #6b7280;
    font-size: 1.05rem;
    margin-top: 0.2rem;
}
.scale-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0 1.5rem 0;
    font-size: 0.95rem;
}
.scale-table th {
    background: #4f46e5;
    color: white;
    padding: 0.5rem;
    text-align: center;
}
.scale-table td {
    padding: 0.45rem;
    text-align: center;
    border-bottom: 1px solid #e5e7eb;
}
.scale-table tr:last-child td {
    border-bottom: none;
}
div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #4f46e5, #06b6d4);
    color: white;
    font-weight: 600;
    font-size: 1.05rem;
    padding: 0.6rem 0;
    border-radius: 10px;
    border: none;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(79, 70, 229, 0.35);
    color: white;
}
.result-card {
    margin-top: 1.5rem;
    padding: 1.6rem;
    border-radius: 16px;
    text-align: center;
    animation: fadeIn 0.4s ease-in;
}
.result-grade {
    font-size: 3.2rem;
    font-weight: 800;
    margin: 0;
}
.result-mark {
    font-size: 1.1rem;
    color: #4b5563;
    margin-top: -0.3rem;
}
.result-message {
    font-size: 1.05rem;
    margin-top: 0.6rem;
    font-weight: 500;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("""
<div class="title-box">
    <h1>🎓 Grade Scale Calculator</h1>
    <p>Enter your mark below to see your grade and feedback</p>
</div>
""", unsafe_allow_html=True)

# ---------- Grade scale reference table ----------
st.markdown("""
<table class="scale-table">
    <tr><th>Mark</th><th>Grade</th></tr>
    <tr><td>90 - 100</td><td>A</td></tr>
    <tr><td>80 - 89</td><td>B</td></tr>
    <tr><td>70 - 79</td><td>C</td></tr>
    <tr><td>60 - 69</td><td>D</td></tr>
    <tr><td>Below 60</td><td>E</td></tr>
</table>
""", unsafe_allow_html=True)

# ---------- Grade logic ----------
def get_grade_info(mark: float):
    """Return (grade, color, background, message) for a given mark."""
    if mark > 100 or mark < 0:
        return None, None, None, None

    if mark >= 90:
        return "A", "#065f46", "#d1fae5", "Outstanding work! Keep it up. 🌟"
    elif mark >= 80:
        return "B", "#1e40af", "#dbeafe", "Great job! You're doing really well. 👏"
    elif mark >= 70:
        return "C", "#92400e", "#fef3c7", "Good effort — a bit more polish and you'll be at the top. 📘"
    elif mark >= 60:
        return "D", "#9a3412", "#ffedd5", "You passed, but there's real room to improve. Keep pushing. 💪"
    else:
        return "E", "#991b1b", "#fee2e2", "This isn't a pass — focus on the fundamentals and try again. 📚"

# ---------- Input ----------
mark = st.number_input(
    "Enter your mark (0 - 100)",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=1.0,
    format="%.1f",
)

calculate = st.button("Calculate My Grade")

# ---------- Result ----------
if calculate:
    grade, color, bg, message = get_grade_info(mark)

    if grade is None:
        st.error("⚠️ Please enter a valid mark between 0 and 100.")
    else:
        st.markdown(f"""
        <div class="result-card" style="background:{bg};">
            <p class="result-grade" style="color:{color};">{grade}</p>
            <p class="result-mark">Mark entered: <strong>{mark:.1f}</strong></p>
            <p class="result-message" style="color:{color};">{message}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown(
    "<p style='text-align:center; color:#9ca3af; margin-top:2rem; font-size:0.85rem;'>"
    "Built with Streamlit</p>",
    unsafe_allow_html=True,
)
