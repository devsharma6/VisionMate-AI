def get_direction(center_x, frame_width):
    """
    Returns the direction of the detected object
    based on its position in the frame.
    """

    left_boundary = frame_width / 3
    right_boundary = 2 * frame_width / 3

    if center_x < left_boundary:
        return "Left"

    elif center_x < right_boundary:
        return "Center"

    else:
        return "Right"