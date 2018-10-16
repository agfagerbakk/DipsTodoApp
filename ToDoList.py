#!/usr/bin/env python3.6
import json

class Task:

	def __init__(self):
		self.tasks = {}

	def updateFile(self):
		""" Update dictionary from disk """
		update = json.dumps(self.tasks)

		with open("todoList.txt", 'w+') as f:
			f.write(update)

	def addTask(self, command):
		""" Add a task to the Todo list """
		command = command.strip('"')

		if len(command) == 0:
			print("Task description is empty")
			return

		key = 1
		while(True):
			if str(key) not in self.tasks:
				self.tasks[str(key)] = command
				break
			key += 1

		self.updateFile()

		print('Added task number #{0} with task: {1}'.format(key, command))

	def doTask(self, number):
		""" Complete and remove your task from the Todo list """
		number = number.strip('# ')

		if not number  in self.tasks:
			print("Task does not exist")
			return

		tasks = self.tasks.pop(number)

		self.updateFile()

		print('Completed/Removed task number #{0} with task: {1}'.format(number, tasks))

	def deleteAllTasks(self):
		""" Delete all task entries """
		if len(self.tasks) == 0:
			print(' There are currently no tasks to delete')
			return

		with open("todoList.txt", 'w') as out:
			out.close()

		self.tasks.clear()

		print("All tasks were deleted")

	def printTasks(self):
		""" Print all task in the list """

		if len(self.tasks) == 0:
			print(' There are currently no registered tasks, use command "add" + "task", to add a task')
			return

		for key, tasks in self.tasks.items():
			print("#{0} {1}".format(key, tasks))

def todoLoop():
	""" Input and console loop"""
	todo = Task()
	welcome_messages()
	print('Welcome to the TodoApp!')
	print('To add a task use the	 command "add" followed by a task you need to complete...')
	print('To mark your task completed and bask in your achievement use command "do + # of task, i.e do 1".')
	print('To print all of your tasks use command "print".\n')

	with open("todoList.txt", 'r') as f:
		backup = f.read()

	todo.tasks = json.loads(backup)

	while(1):
		user_input = input("> ")
		command = user_input.split(' ', 1)
		command[0].lower()

		if (command[0] == "add"):
			todo.addTask(command[1])
		elif (command[0] == "do"):
			todo.doTask(command[1])
		elif (command[0] == "print"):
			todo.printTasks()
		elif(command[0] == "delete" and command[1] == "all"):
			todo.deleteAllTasks()
		elif (command[0] == "quit"):
			break

if __name__ == '__main__':
	todoLoop()
