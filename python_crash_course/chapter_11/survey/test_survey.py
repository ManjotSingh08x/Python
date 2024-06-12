from c11_survey_class import AnonymousSurvey
import pytest

@pytest.fixture
def language_survey():
    """A survy available to every test function"""
    question = "what language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey
    

def test_store_single_response(language_survey):
    """Test that a sinlge response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_response(language_survey):
    """Test that three responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses