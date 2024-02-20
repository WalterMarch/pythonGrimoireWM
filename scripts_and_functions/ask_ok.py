def ask_ok(prompt, retries=5, reminder='Please try again!'):
    """Check response to prompt against yes/no and variants. 
    Loop some number of times if invalid answer.
    https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
    """
    while True:
        ok = input(prompt).lower()
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries <= 0:
            print('invalid user response')
            return None
        print(reminder)
        
prompt_response = ask_ok("Does this work? ")

if prompt_response is None:
    print("Didn't get a yes/no response that fits our guesses. Ending.")
elif prompt_response:
    print("Thank you! I'm glad it works.")
else:
    print("But... you got this response... I feel like that means it worked...")