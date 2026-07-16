priority = {
    "person": 1,
    "car": 2,
    "bus": 3,
    "truck": 4,
    "motorcycle": 5,
    "bicycle": 6,
    "dog": 7,
    "chair": 8,
    "bottle": 9,
    "laptop": 10
}


def get_priority(object_name):
    return priority.get(object_name, 999)
