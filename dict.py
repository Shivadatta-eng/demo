# null_dict ={}
# print(null_dict)

# null_dict["name"] = {"Shivadatta", "Shivam", "Shiva"} 
# print(null_dict)

Student = {
    "Name": "Abc",
    "Rollno": 101,
    "Marks": [90, 85, 92, 46, 77, 74],
    "result": "pass"
}
# print(Student)
# print(Student["result"])
# print(Student.keys()) # to print all the keys in the dictionary
# print(Student.values()) # to print all the values in the dictionary
# print(Student.items()) # to print all the key-value pairs in the dictionary
print(Student.get("result")) # to get the value of a key, if the key is not present it will return None
print(Student.get("age", "16")) # to get the value of a key, if the key is not present it will return "Key not found"
