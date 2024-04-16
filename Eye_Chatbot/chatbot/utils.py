#chatbot/utils.py

# import openai

# # Set your OpenAI API key here
# #OPENAI_API_KEY = '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'

# from django.conf import settings

# openai.api_key = settings.OPENAI_API_KEY

# # def text_to_speech(input_text):
# #     response = openai.Completion.create(
# #         engine="text-davinci-002",
# #         prompt=input_text,
# #         max_tokens=100,
# #         temperature=0.5,
# #         top_p=1.0,
# #         frequency_penalty=0.0,
# #         presence_penalty=0.0,
# #         stop=['\n']
# #     )
# #     audio_file_path = response.choices[0].audio
# #     return audio_file_path


# # def speech_to_text(audio_data):
# #     with open(audio_data, "rb") as audio_file:
# #         transcript = openai.audio.transcriptions.create(
# #             model="whisper-1",
# #             response_format="text",
# #             file=audio_file
# #         )
# #     return transcript



# def get_answer(messages):
#     system_message = [{"role": "system", "content": "You are an helpful AI chatbot, that answers questions asked by User."}]
#     messages = system_message + [messages]
#     response = openai.chat.completions.create(
#         model="gpt-3.5-turbo-1106",
#         messages=messages,
#         temperature=0.7,
#         max_tokens=150
#     )
#     return response.choices[0].message.content
