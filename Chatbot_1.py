import json
import os


"""
future plans:

    - adding all of the popular geometric formulas for questioning
    - solving the simple geometric problems by merging a calculator in this way:
        1. showing the formula
        2. step-by-step solving the problem and finally showing the answer
        3. (maybe) adding shapes for visualization
"""


def file_check() -> bool:
    """makes sure the .json file exists | returns True anyway"""

    try:
        if os.path.exists("knowledge_base.json"):
            return True
        else:

            # here's the template content
            content = {
                            "questions": {
                                "hi": "Hi there! How can I assist you today?",
                                "hello": "Hello! What brings you here?",
                                "how are you": "I'm doing well, thank you!",
                                "what is your name": "I'm a chatbot. My creator hasn't decided on it yet :/.",
                                "where are you from": "I exist in the digital realm, here to assist you.",
                                "what can you do": "I can learn from you can have a conversation that way.",
                                "help me with math": "Will do, but in future updates."
                            }
                        }

            # writing the json content in json format in the empty_file
            with open("knowledge_base.json", 'w') as empty_file:
                json.dump(content, empty_file, indent=4)

            return True
    except Exception as e:
        print(f"looks like you've got a {e.__class__.__name__}")


def get_answer(question):
    try:
        # opening json file in read mode
        with open("knowledge_base.json", "r") as f:
            data = json.load(f)

        # asking for an answer for the question
        print("You can enter \"skip\" to pass")
        given_answer: str = input("Bot: I don't know the answer."
                                  " you can teach it to me by typing the answer: ").strip()

        # making a space in the output terminal to look better
        print("")

        if given_answer == "skip":
            # going back to process() because the user wanted so
            return
        else:
            # creating the new key-value pair
            data["questions"][question] = given_answer

            # opening the json file in write mode to add the new key-value pair
            with open("knowledge_base.json", 'w') as file:
                json.dump(data, file, indent=4)

                # now the program ends and will be started again by the main()

    # catching exceptions
    except FileNotFoundError:
        print("Couldn't find the file")
    except json.JSONDecodeError:
        print("Unable to read this JSON file")
    except KeyError:
        print("couldn't find the Key (in other words your specific question with it's answer)")
    except IOError:
        print("there was something wrong with input/output stuff (even I dont know what's happening)")


def process() -> None:
    """
    1. checks if the json file exists via file_check()
    2. loads up the json file to get started
    3. asks for an input to be searched among json file keys (key-value pair)
    4. adds new question-answer to the data set via get_answer()
    """
    try:
        # checking if the json file exists
        if file_check():

            # opening the json file in read mode
            with open("knowledge_base.json", 'r') as f:
                data_set = json.load(f)

                # getting user's question to answer
                user_input: str = input("You: ").strip()

                #
                proper_data_path = data_set["questions"]

                # searching the "keys" in "questions" in the json file for similarity
                # redirecting to get_answer() if no matching word is being found
                for question, answer in proper_data_path.items():

                    if question in user_input:
                        print(f"Bot: {answer}\n")

                        return

                # redirecting to get_answer() to add the new question and its answer to the data set
                get_answer(user_input)

    # handling exceptions
    except ValueError:
        print("wrong input format, too fancy? just enter words ok?")
    except FileNotFoundError:
        print("File not founds")
    except KeyboardInterrupt:
        print("Keyboard interrupted (it hates you)")
    except KeyError:
        print("mapping key not found")


def main() -> None:
    print("Welcome to my Chatbot!\n"
          "Start the chat by asking or saying something like \"hi\" or \"hello\"\n")
    while True:
        process()


if __name__ == '__main__':
    main()
