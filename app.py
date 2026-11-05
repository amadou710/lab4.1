import streamlit as st

# TODO 1: Key-value pairs for the fictional club details
club_info = {
    "name": "The Pixel & Guild Gaming Society",
    "day": "Every Thursday",
    "time": "6:00 PM - 8:30 PM",
    "location": "Student Union, Room 204",
    "dues": "Free for all students",
}

# TODO 2: List of relevant activities (includes added item per change check)
activities = [
    "Weekly retro arcade and casual multiplayer tournaments",
    "Indie game development showcase and playtesting sessions",
    "Co-op board game nights and tabletop roleplaying campaigns",
    "End-of-semester speedrunning marathon for charity",  # New item added
]

st.title(club_info["name"])
st.caption(
    "A fictional CIS 211 course project. These are not real campus arrangements."
)

st.header("About this club or service")
# TODO 3: Introduction with bold and italic formatting using triple-quoted string
st.markdown(
    """
    Welcome to the **Pixel & Guild Gaming Society**, the ultimate campus hub for digital and tabletop enthusiasts! 
    Our mission is to create an *inclusive environment* where players of all skill levels can connect, compete, and collaborate. 
    Whether you are a casual gamer or an aspiring game developer, there is **always a seat** at our table.
"""
)

st.header("Activities or services")
# TODO 4: Loop displaying each item in the activities list dynamically
for activity in activities:
    st.write(f"• {activity}")

st.header("Details")
# TODO 5: Displaying key-value dictionary entries with descriptive labels
st.write(f"**Meeting Day:** {club_info['day']}")
st.write(f"**Meeting Time:** {club_info['time']}")
st.write(f"**Location:** {club_info['location']}")
st.write(f"**Membership Dues:** {club_info['dues']}")

st.header("Prepare for a visit")
# TODO 6: Markdown list containing a functional external link
st.markdown(
    """
* Bring your student ID card for building entry.
* Feel free to bring your own controller or handheld console.
* Check out our official [Discord Community](https://discord.com) to get real-time announcements.
"""
)