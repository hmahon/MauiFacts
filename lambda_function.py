"""
This is a Python template for Alexa to get you building skills (conversations) quickly.
"""

from __future__ import print_function
import random 

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "Maui Facts",
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------
def get_fact_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "Straight facts homie"
    fact_list = ["The Hawaiian alphabet includes just 13 letters.", 
    "The road to Hana is 45 miles long, featuring no less than 59 bridges and more than 600 hairpin turns. Its lush jungles and countless cascading waterfalls have dazzled many a photographer",
	"Anywhere between 4,000 and 10,000 humpback whales migrate to Hawaii from Alaska each year. The 6,000-mile journey is one of the longest of any mammal. Hawaii is one of the best whale watching destinations in the world.",
	"Lahaina was the original capital of Hawaii until 1850 when it changed to Honolulu.",
	"While Lahaina and Ka’anapali get around 10 inches of rain each year, Pu’u Kukui nearby in the West Maui Mountains gets around 365 inches per year.",
	"Haleakala is the world’s largest dormant volcano, standing at 10,023 feet from sea level. The Crater at the summit is 21 miles across, making it almost the size of Manhattan.",
	"The Banyan Tree in Lahaina Town is 60 feet tall and spans an entire city block. Its sprawling canopy provides shade for the many gatherings that take place beneath it.",
	"Maui has sixteen golf courses, some of which host professional tournaments.",
	"Honokohau Falls plunges a total of 1,100 feet, making it one of the highest waterfalls in the world.",
	"The tiny crescent island of Molokini off Maui’s South Shore is home to around 250 marine species.",
	"Hawaii is the only U.S. state with two official languages. English and Hawaiian. Some locals like to think of Pidgin as an official language, but it’s not. It certainly can sound foreign, and it is spoken a lot here, but Pidgin is not an official language.",
	"People in Maui wear white pants after Labor Day.",
	"You can mail a coconut from Maui.",
	"Surfing was invented in Hawaii.",
	"People from Maui greet with a hug, not a handshake.",
	"You might see signs here with words misspelled, missing the d. Examples include Shave Ice, Smoke Fish, Open Saturday, Close Sunday. In Hawaii, that missing d is just understood. It has origins from the Pidgin language which is prevalent on the islands.",
	"There is no smog, but they do have vog. Island skies are unpolluted for the most part–we have no smog. But they get vog, the volcanic haze from the Kilauea volcano that has been actively erupting since 1983 on the Big Island (aka Island of Hawaii).",
	"Maui has been dubbed the Valley Isle due to its unique formation with Central Maui lying in a massive valley between Mount Haleakala to the east and the West Maui mountain range.",
	"The Hawaiian word Aloha serves as both “hello” and “goodbye.” You pretty much can’t go wrong with a flexible greeting like that.",
	"Hawaii still honors its ali’i (royalty) from the past. They celebrate Kamehameha Day on June 11 (honoring King Kamehameha the Great) and Prince Kuhio Day on March 26 (honoring Prince Jonah Kuhio Kalanianaole). Both dates are Hawaii state holidays and are marked with festivals and parades.",
	"The Hawaiian islands were previously ruled under a monarchy, with kings and queens and princes and princesses.",
	"By law, no one can own a beach on Maui or has the right to keep people off of it, including “exclusive” beach resorts.",
	"Maui has no billboards. Other than traffic and safety signs, you have free view of the natural landscape around you. Hawaii is one of only four states to ban billboards, in addition to Vermont, Maine and Alaska.",
	"The Maui Gold Brand of pineapple possesses three times the amount of vitamin C as other brands of pineapple. It is specially grown and takes approximately 18 months to reach ripeness.",
	"Founded in 1831, Maui’s Lahainaluna High School is the oldest school west of the Rocky Mountains and owned the first printing press in the western United States.",
	"There are 81 accessible beaches on Maui, including ones with white, gold, black, and red sand. It has 120 miles of accessible beach, more than any other Hawaiian island.",
	"Charles Lindbergh, famous aviator, explorer and social activist, was buried on Maui in 1974. His grave sits underneath a plum tree at the Palapala Ho’omau Church along the Road to Hana.",
	"The Haleakala High Altitude Observatory is considered one of the best astronomical and space surveillance sites in the world, noted for its tremendous seeing conditions and clear skies. It is not open to the public, but occasional public events and talks are open for visitors.",
	"In Hawaii and Guam, more spam is eaten per person than anywhere else in the world.",
	"Hawaii has the highest life expectancy in the United States at 81.5 years.",
	"A popular legend concerning the island involves a story about a demigod named Maui. Legend says the island is shaped to resemble Maui’s head and body. The legend also says Maui pulled the Hawaiian islands from the sea and lassoed the sun on Haleakala, a volcano to the east of the island.",
	"Maui is the second-largest Hawaiian island, with a population of less than 200,000.",
	"In Maui, you will find three different sand colors: black, white and red. Black sand is created by the island’s pulverized lava rock that makes up most of its composition. Coral and shells help create white sand, and many Maui beaches feature the classic color. Red sand also comes from lava, however its coloration is due to iron-rich content.",
	"The Banyan tree is located in Lahaina on the island of Maui. A popular attraction, the tree stands more than 60 feet tall. It was originally 8 feet tall when it was first brought to the island from India. Today, the tree is the size of a full city block, and visitors can walk nearly an acre under its shade. The Banyan also serves as a spot for special events and arts activities."
	]

    speech_output = random.choice(fact_list)
    reprompt_text = "I have a lot more facts. Ask me for another. Or else say quit"
    
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Get ready to learn about Maui! Say.. 'tell me a fact'.. and prepare to be amazed"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I don't know if you heard me, let's learn about Maui!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for listening to me ramble about Maui Facts. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific 
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass

    

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "GetNewFactIntent":
        return get_fact_response()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("Incoming request...")

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
