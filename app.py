import streamlit as st
import random
import time

def voting_system():
    st.markdown(
        """
        <style>
        .title {
            color: #FF5733; 
            font-size: 40px;
        }
        .header {
            color: #FFC300;
            font-size: 30px;
        }
        .results {
            font-size: 24px;
            color: #30336b;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown("<div class='title'>🗳️ Voting System</div>", unsafe_allow_html=True)
    st.markdown("<div class='header'>Welcome to the voting system!😍</div>", unsafe_allow_html=True)

    if 'votes' not in st.session_state:
        st.session_state.votes = [0, 0, 0, 0]
    if 'candidates' not in st.session_state:
        st.session_state.candidates = ["Tabish 👨‍💼", "Nabeeha👩‍💼", "Zain 👨‍🔧", "Kiran 👩‍🔬"]

    selected_candidate = st.selectbox("Select a candidate to vote for:", st.session_state.candidates)

    if st.button("Vote"):
        candidate_index = st.session_state.candidates.index(selected_candidate)
        st.session_state.votes[candidate_index] += 1
        st.success(f"🎉 Your vote for {selected_candidate} has been counted! ✅")

    if st.button("Exit"):
        st.write("### 🏆 Final Results:")
        for i, candidate in enumerate(st.session_state.candidates):
            st.markdown(f"<div class='results'>{candidate}: {st.session_state.votes[i]} votes</div>", unsafe_allow_html=True)
        
        # Determine the winner
        max_votes = max(st.session_state.votes)
        winners = [candidate for i, candidate in enumerate(st.session_state.candidates) if st.session_state.votes[i] == max_votes]

        # Celebrating the winner(s)
        st.balloons()
        time.sleep(1)
        for _ in range(5):
            st.snow()
            time.sleep(0.5)

        if len(winners) == 1:
            st.success(f"🎉 Congratulations to {winners[0]} for winning the election with {max_votes} votes! 🏆")
        else:
            st.success(f"🎉 It's a tie between {', '.join(winners)} with {max_votes} votes each! 🏆")

        st.write("🙏 Thank you for voting!")
        st.stop()

# Call the function directly
voting_system()
