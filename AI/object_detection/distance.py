def get_distance(area):
    if area > 100000:
        return "very close"
    elif area > 40000:
        return "medium distance"
    else:
        return "far"