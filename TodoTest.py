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
        self.Task.addTask("Im getting key #1")
        self.Task.addTask("This is number two")
        self.Task.addTask("Number 3")
        self.Task.doTask("1")
        self.Task.addTask("This should be number 1")
        print(self.Task.tasks[0])
        self.assertEqual(self.Task.tasks[0], 1)

    def test_deleteAll(self):
        self.Task.addTask("Im going to be deleted, hopefully...")
        self.Task.addTask("Im also going to be deleted")
        self.Task.addTask("See you on the other side")
        self.Task.deleteAllTasks()
        self.assertTrue(len(self.Task.tasks)== 0)

if __name__ == '__main__':
    unittest.main()