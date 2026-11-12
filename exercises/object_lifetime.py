from dataclasses import dataclass
import weakref 

@dataclass
class Note:
    text: str


first = Note("Learning memory management")

second = first

observer = weakref.ref(first)

print(observer() is not None)

del first

print(observer() is not None)

del second

print(observer() is  None)
