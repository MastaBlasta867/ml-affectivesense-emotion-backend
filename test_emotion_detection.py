from emotion_detection import emotion_detector

def test_joy():
    result = emotion_detector("I am so happy and joyful today!")
    assert result is not None
    assert result.get("joy", 0) > result.get("sadness", 0)

def test_sadness():
    result = emotion_detector("I feel so sad and depressed.")
    assert result is not None
    assert result.get("sadness", 0) > result.get("joy", 0)

def test_anger():
    result = emotion_detector("I am furious and angry right now!")
    assert result is not None
    assert result.get("anger", 0) > result.get("joy", 0)

def test_fear():
    result = emotion_detector("I am scared and fearful.")
    assert result is not None
    assert result.get("fear", 0) > result.get("joy", 0)

def test_disgust():
    result = emotion_detector("That is disgusting and gross.")
    assert result is not None
    assert result.get("disgust", 0) > result.get("joy", 0)
