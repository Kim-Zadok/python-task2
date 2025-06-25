 **Functions Used**
- **`display_menu()`**: Shows a user-friendly menu of actions.
- **`view_tasks(tasks)`**: Lists all current tasks with their status (Completed or Pending).
- **`add_task(tasks, description)`**: Appends a new task to the list with a default "Pending" status.
- **`update_task(tasks, index, description, completed)`**: Updates task details like description or status.
- **`delete_task(tasks, index)`**: Removes a task from the list.
- **`main()`**: The central loop that handles user interaction and calls the above functions based on choices.

---

 **Core Logic**
- Maintains a list of tasks (each as a dictionary with `description` and `completed` keys).
- Prompts users through a numbered menu system.
- Uses conditionals and nested inputs to interpret choices and manage tasks.
- Handles input errors like invalid indexes and empty descriptions with `try-except` blocks and checks.

---

 **Challenges & Common Pitfalls**
1. **Input Validation**:
   - Ensuring descriptions aren’t empty.
   - Preventing invalid status entries or task numbers.
2. **List Indexing**:
   - Requires careful adjustment between 1-based user input and 0-based Python lists.
3. **Data Persistence**:
   - Tasks don’t persist between sessions. For real-world use, you'd need file I/O or database integration.
4. **Scalability**:
   - Adding features like due dates, priority, or search would require expanding the task structure.
