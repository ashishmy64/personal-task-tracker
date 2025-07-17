import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Personal Task Tracker", page_icon="✅")

# Title of your app
st.title("✅ Personal Task Tracker")
st.write("Stay organized and productive!")

# Initialize session state for tasks if it doesn't exist
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Function to add a new task
def add_task(task):
    st.session_state.tasks.append({"task": task, "completed": False})

# Function to toggle task completion
def toggle_task(index):
    st.session_state.tasks[index]["completed"] = not st.session_state.tasks[index]["completed"]

# Input section
st.header("Add New Task")
new_task = st.text_input("Enter a new task:")
if st.button("Add Task"):
    if new_task:
        add_task(new_task)
        st.success(f"Task '{new_task}' added!")
        st.rerun()  # Refresh the app to show the new task
    else:
        st.warning("Please enter a task!")

# Display tasks
st.header("Your Tasks")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            if task["completed"]:
                st.write(f"~~{task['task']}~~")  # Strikethrough for completed tasks
            else:
                st.write(task["task"])
        
        with col2:
            if st.button("✓" if not task["completed"] else "↻", key=f"toggle_{i}"):
                toggle_task(i)
                st.rerun()
    
    # Show progress
    completed_tasks = sum(1 for task in st.session_state.tasks if task["completed"])
    total_tasks = len(st.session_state.tasks)
    st.progress(completed_tasks / total_tasks)
    st.write(f"Progress: {completed_tasks}/{total_tasks} tasks completed")
    
    # Clear completed tasks button
    if st.button("Clear Completed Tasks"):
        st.session_state.tasks = [task for task in st.session_state.tasks if not task["completed"]]
        st.rerun()
else:
    st.write("No tasks yet! Add one above to get started.")

# Footer
st.markdown("---")
st.write("Built with ❤️ By Ashish M ")