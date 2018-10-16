import unittest
import ToDoList

class TestToDoList(unittest.TestCase):

    def setUp(self):
        self.Task = ToDoList.Task()
        self.Task.deleteAllTasks()

    def test_correctSetUp(self):
        self.assertTrue(len(self.Task.tasks) == 0)
    
    def test_addTask(self):
        self.Task.addTask("Test task")
        self.assertTrue(len(self.Task.tasks) == 1)
        
    def test_doTask(self):
        self.Task.addTask("Im getting popped")
        self.Task.doTask("1")
        self.assertTrue(len(self.Task.tasks) == 0)
    
    def test_UniqueKeyAfterDeletion(self):
        self.Task.addTask("key #1")
        self.Task.addTask("This is number two")
        self.Task.addTask("Number 3")
        self.Task.doTask("1")
        self.Task.addTask("This should be number 1")

    def test_deleteAll(self):
        self.Task.addTask("I'm being deleted")
        self.Task.addTask("I'm also being deleted")
        self.Task.addTask("I should have more tests")
        self.Task.deleteAllTasks()
        self.assertTrue(len(self.Task.tasks)== 0)

if __name__ == '__main__':
    unittest.main()