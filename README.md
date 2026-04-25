# Omnitrainer-Multimodal-Customer-Service-Trainer-Project

This is an AI-powered content moderation system for customer service interactions at a fictional company called ACME Enterprise.

What it does:

- Moderates text, images, videos, and audio before they're sent to customers  
- Detects issues like: PII (personally identifiable information), unprofessional tone, unfriendly content, disturbing images/videos, and low-quality media
- Blocks harmful content and provides detailed explanations for why content was flagged

# Execution
Follow the following steps in order:
  
## 1. Moderation result
Here we setup the Pydantic models for our moderation agents. These are the output schemas for the text, audio, image and video moderation agents we'll work on later.
  
Edit the `types/moderation_result.py` file and replace the # TODO sections with your code
Run the test to get feedback on your work. From the root of the starter run: `uv run tests/test_moderation_result.py -vv`. If you get an error, read it carefully as it will give you information on what to fix. DO NOT continue unless the test passes.
## 2. Text agent
Here we will complete the setup of the moderation agent for text.
  
Edit the text agent (`agents/text_agent.py`) and replace the # TODO sections
Run the test to get feedback on your work. From the root of the starter run: `uv run tests/test_text_agent.py -vv`. If you get an error, read it carefully as it will give you information on what to fix. DO NOT continue unless the test passes.
  
## 3. Image agent
Here we will complete the setup of the moderation agent for images, similarly to what we just did for text. Since this is a multimodal agent, we will use the multimodal capabilities of Pydantic AI and Gemini.

Edit the image agent (`agents/image_agent.py`) and replace the # TODO sections
Run the test to get feedback on your work. From the root of the starter run: `uv run tests/test_image_agent.py -vv`. If you get an error, read it carefully as it will give you information on what to fix. DO NOT continue unless the test passes.
  
## 4. Video and Audio agents
The audio and video agents are already completed. You will just test them to make sure they work.

The Video and Audio agents are already complete. You can test them with `uv run tests/test_video_agent.py` and `uv run tests/test_audio_agent.py`.

## 5. Gradio App
Here we put everything together into a Gradio app, which constitutes the front-end of our solution.

Edit the gradio app (`gradio_app.py`) and replace all # TODO sections. There are quite a few, going from the top to the bottom. Before moving on, make sure you did not left any by searching TODO in the file (Crtl+F or Command+F).
Run the test to get feedback on your work. From the root of the starter run: `uv run tests/test_gradio_app.py -vv`. If you get an error, read it carefully as it will give you information on what to fix. DO NOT continue unless the test passes.

## 6. Run all tests
It is now time to verify your work. Run all tests at once with:

```
uv run pytest tests/ -vv
```
All tests should pass. If they don't, fix them before submitting your project.

## 7. Evals
Now that our system is complete, we need to run evaluations to understand and measure how it behaves.

Edit the `evals/text/test_cases.py` and replace all # TODO sections. Same for `evals/image/test_cases.py`.
Once you are done, run `uv run evals/text/test_cases.py` to see the results of the evals on text. NOTE: your score will NOT always be 100%! that is not a bug. The text agent is not perfect!
Run the evals for the other media (`uv run evals/image/test_cases.py`, `uv run evals/audio/test_cases.py` and `uv run evals/video/test_cases.py`)

## Play with the app  
## Conversation
Now that you are done, the app should work. You can run it by executing in the terminal:

uv run multimodal-moderation
and then going with your browser to `http://localhost:7860/` to interact with the app. You are free to play with it, however, if you need inspiration, this is how a conversation could go:

```YOU> Welcome to ACME Customer Service. How can I help?
CUSTOMER-LLM> ... [will complain about the product not working]  
YOU> I am sorry to hear that. Is this the product you are talking about? [attach evals/test_data/professional_image.jpg]  
CUSTOMER-LLM> ... [will say something about wanting a refund]  
YOU> I am sorry but I absolutely cannot offer a refund  
------> message will be flagged as rude  
YOU> I am going to help you solving your issue. I am authorized to offer you a replacement. Would you be willing to accept it?  
CUSTOMER-LLM> ... [probably won't accept]  
[you can now close the conversation by clicking on the End Conversation button]  
See your traces  
After a conversation like the one suggested above, you can go to the Phoenix UI at http://localhost:6006/projects, click on the default project, and see your traces and spans. Explore the different metadata and different reports.
```

See your backend APIs
Go to `http://0.0.0.0:8000/docs` to see a nice documentation of your moderation APIs. If you wanna test them out from here, click on Authorize on the upper right and insert your USER_API_KEY (the one you have set in your .env file). Then click on an endpoint (say, `/api/v1/moderate-text`) and click on Try it out (in the upper right). You will see a JSON like:

```
{
  "text": "string"
}
```
Just change string to a message and click Execute, your message will be moderated. Scroll down a bit to see the results.
