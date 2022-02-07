from JsonFlattener import JsonFlattener
import unittest
import json

#Arrange
f = open('TestFiles/Input1.json', 'r')
data=f.read()
f.close()
data=json.loads(data)

f = open('TestFiles/Output1.json', 'r')
Output=f.read()
f.close()

f = open('TestFiles/Input2.json', 'r')
Input2=f.read()
f.close()
Input2=json.loads(Input2)

f = open('TestFiles/Output2.json', 'r')
Output2=f.read()
f.close()

f = open('TestFiles/Input3.json', 'r')
Input3=f.read()
f.close()
Input3=json.loads(Input3)

f = open('TestFiles/Output3.json', 'r')
Output3=f.read()
f.close()

#Act
JsonFlattener=JsonFlattener()

data=JsonFlattener.flatten(data)
JsonFlattener.flush()

Input2=JsonFlattener.flatten(Input2)
JsonFlattener.flush()

Input3=JsonFlattener.flatten(Input3)

#Assert
class IOValidation(unittest.TestCase):
    def test_input_one(self):
        self.assertEqual(data,Output)

    def test_input_two(self):
        self.assertEqual(Input2,Output2)

    def test_input_three(self):
        self.assertEqual(Input3,Output3)
