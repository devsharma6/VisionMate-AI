# Higher number = Higher priority

PRIORITY = {
    "person": 100,
    "bicycle": 90,
    "motorcycle": 85,
    "car": 80,
    "bus": 75,
    "truck": 70,
    "dog": 65,
    "cat": 60,
    "chair": 40,
    "table": 35,
    "bottle": 20,
    "cup": 15,
    "laptop": 10,
}


def get_priority(object_name):
    return PRIORITY.get(object_name, 0)