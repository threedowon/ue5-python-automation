import os.path

import unreal
import uuid

def say_hi():
    unreal.log("Hi! I am a new hello script!")

print("I just god imported");

random_name = str(uuid.uuid4())
path = os.path.join(r"F:\SourceTree\PythonAutomation\Tools\PythonAutomation\editor_scripts", random_name)

with open(path, "w") as f:
    pass

print(f"created {random_name}");