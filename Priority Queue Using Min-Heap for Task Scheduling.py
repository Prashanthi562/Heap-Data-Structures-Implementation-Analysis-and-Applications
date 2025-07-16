## Description:The program offers an implementation of a priority queue that can be executed using a min-heap that allows the application of tasks based on their respective priority. The main operations include insertion, removal of the task with the highest-priority, priority modification, and displaying the queue itself.

import heapq

# Creating a Task class to store task details
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        # Storing the task identifier
        self.task_id = task_id
        # Storing the priority number where a smaller number means higher priority
        self.priority = priority
        # Storing the time the task arrives
        self.arrival_time = arrival_time
        # Storing the time by which the task should be completed
        self.deadline = deadline

    # Allowing comparison of tasks based on priority for the heap
    def __lt__(self, other):
        return self.priority < other.priority

    # Creating a readable format when printing task objects
    def __repr__(self):
        return f"(ID: {self.task_id}, Priority: {self.priority})"

# Creating a priority queue class using a min-heap
class PriorityQueue:
    def __init__(self):
        # Initializing an empty list to store the heap
        self.heap = []

    # Inserting a new task into the priority queue
    def insert(self, task):
        # Adding the task to the heap while keeping the heap order correct
        heapq.heappush(self.heap, task)

    # Removing and returning the task with the highest priority
    def extract_min(self):
        # Checking if the heap is empty before removing
        if self.is_empty():
            return None
        # Removing the task with the smallest priority value
        return heapq.heappop(self.heap)

    # Changing the priority of a task to a lower value
    def decrease_key(self, task_id, new_priority):
        # Going through the heap to find the task by its identifier
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                # Updating the task's priority
                self.heap[i].priority = new_priority
                # Fixing the heap structure after the change
                heapq.heapify(self.heap)
                return True  # Showing that the update worked
        return False  # Showing that the task was not found

    # Checking if the priority queue is empty
    def is_empty(self):
        return len(self.heap) == 0

    # Showing all tasks currently in the queue
    def display(self):
        print("Current Priority Queue:")
        for task in self.heap:
            print(task)

# Running sample actions to test the priority queue
if __name__ == "__main__":
    # Creating a new priority queue
    pq = PriorityQueue()

    # Creating tasks with id, priority, arrival time, and deadline
    task1 = Task("T1", 4, "09:00", "10:00")
    task2 = Task("T2", 2, "09:05", "09:55")
    task3 = Task("T3", 5, "09:10", "10:10")
    task4 = Task("T4", 1, "09:15", "09:45")

    # Inserting tasks into the priority queue
    pq.insert(task1)
    pq.insert(task2)
    pq.insert(task3)
    pq.insert(task4)

    # Showing all tasks in the queue
    pq.display()

    # Removing and showing the task with the highest priority
    print("\nExtracted Task:", pq.extract_min())

    # Showing the queue after removal
    pq.display()

    # Changing the priority of a task to a higher level
    print("\nDecreasing priority of task T3 to 0...")
    pq.decrease_key("T3", 0)

    # Showing the queue after the priority change
    pq.display()

    # Checking if the queue is now empty
    print("\nIs the queue empty?", pq.is_empty())
