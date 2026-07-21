import easyocr

reader = easyocr.Reader(
    ['en'],
    gpu=False
)


def read_text(frame):

    results = reader.readtext(
        frame,
        detail=0,
        paragraph=False
    )

    return results