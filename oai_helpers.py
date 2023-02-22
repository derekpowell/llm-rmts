# import numpy as np
# import pandas as pd
# import openai
# import configparser
# import re 
# import time
# from  scipy.special import expit, logit


# # 

def get_gpt_text(response):

    choices = response["choices"]
  
    if type(choices)==list:
        out = [x['text'] for x in choices]
    else: 
        out = choices['text']
    
    return(out)


def make_prompt(query, base_prompt, suffix=""):
    if type(query)==list:
        output = [base_prompt + q + suffix for q in query]
    else:
        output = base_prompt + query + suffix

    return(output)


# def batch_function(x, func, batch_size=20):
    
#     batches = [x[i:i+batch_size] for i in range(0, len(x), batch_size)] # batch into lists of 20
#     # print(batches)
#     out = list()

#     for b in batches:
#         val = func(b)
#         out.append(val)

#     return(out)


def gpt_complete_batch(questions, prompt, suffix = "", sleep=0, **kwargs): #  , max_tokens=12, stop=None
  
  # need to add batching into groups of 20 prompts

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= make_prompt(questions, prompt, suffix),
        # temperature=0,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0,
        **kwargs
        # max_tokens=max_tokens,
        # stop = stop
    )

    full_text = get_gpt_text(response)

    out = [s.strip() for s in full_text]

    # sleep for sleep seconds (default = 0)
    time.sleep(sleep)

    return(out)    


def gpt_complete(questions, prompt="", suffix = "", sleep=0, **kwargs):

    if type(questions)==list:
  
        questions_list = [questions[i:i+20] for i in range(0, len(questions), 20)] # batch into lists of 20
        # should make this a for loop and sleep a bit in between batches
        response_list = [gpt_complete_batch(q, prompt, suffix, **kwargs) for q in questions_list] 
        
        out = list()

        for sub_list in response_list:
            out = out + sub_list

    else:
        out = gpt_complete_batch(questions, prompt, suffix, **kwargs)

    return(out)


### things for token probs

def get_gpt_logprobs(response):
    x = [r["logprobs"]["token_logprobs"] for r in response["choices"]]
    return(x)


def gpt_token_probs_batch(questions, prompt, suffix = "", sleep=0, **kwargs):
  
  # need to add batching into groups of 20 prompts

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= make_prompt(questions, prompt, suffix),
        logprobs=1,
        echo=True,
        max_tokens=0,
        **kwargs
        # stop = stop
    )

    # full_text = get_gpt_text(response)

    out = get_gpt_logprobs(response)
    # sleep for sleep seconds (default = 0)
    time.sleep(sleep)

    return(out)    


def gpt_token_probs(questions, prompt="", suffix = "", sleep=0, **kwargs):

    if type(questions)==list:
  
        questions_list = [questions[i:i+20] for i in range(0, len(questions), 20)] # batch into lists of 20
        # should make this a for loop and sleep a bit in between batches
        response_list = [gpt_token_probs_batch(q, prompt, suffix, **kwargs) for q in questions_list] 
        
        out = list()

        for sub_list in response_list:
            out = out + sub_list

    else:
        out = gpt_token_probs_batch(questions, prompt, suffix, **kwargs)

    return(out)