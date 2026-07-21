def is_obstacle(center_x, frame_width, distance):

    left = frame_width * 0.4
    right = frame_width * 0.6

    if left <= center_x <= right:
        if distance in ["very close", "medium distance"]:
            return True

    return False