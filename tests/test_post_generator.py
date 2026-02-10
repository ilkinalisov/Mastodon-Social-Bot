#test_post_generator.py

import pytest
from ai_trend_bot.post_generator import generate_post
# The source file is src/ai_trend_bot/post_generator.py
# The target to mock is the function on the *instance* of the client:
MOCK_TARGET = "ai_trend_bot.post_generator._client.chat.completions.create" 


class DummyMessage:
    def __init__(self, text): 
        self.content = text

class DummyChoice:
    def __init__(self, text): 
        self.message = DummyMessage(text)

class DummyResponse:
    def __init__(self, text): 
        self.choices = [DummyChoice(text)]

def test_generate_post(monkeypatch):
    # Mock the actual method on the client instance
    # The lambda function must match the call signature (no args needed for mock)
    def mock_create(**kwargs):
        return DummyResponse('Hello world')
        
    monkeypatch.setattr(MOCK_TARGET, mock_create)
    
    # Test a function call
    out = generate_post('#Test') 
    assert out == 'Hello world'
