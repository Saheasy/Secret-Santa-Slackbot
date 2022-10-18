import os
import requests
from SecretSantaClasses import SecretSanta
import datetime
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
load_dotenv()

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
user = os.environ.get("SLACK_USER_TOKEN")
secret_santa_app = SecretSanta('test.json')

# Listen for a button invocation with action_id `coffee` 
@app.view("secret_santa_begin_callback")
def secret_santa_begin_callback(ack, body, client, payload):
    # Acknowledge the command request
    ack()
    secret_santa_app.set_begin(
        payload['state']['values'][payload['blocks'][3]['block_id']]['datepicker-begin-date']['selected_date'],
        payload['state']['values'][payload['blocks'][4]['block_id']]['datepicker-start-date']['selected_date'],
        body['user']['id'],
        payload['state']['values'][payload['blocks'][6]['block_id']]['channels-select-begin']['selected_channel']
        )
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={
            "type": "modal",
            # View identifier
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": "My App"},
            "blocks": [
                {
                "type": "section",
                "text": {
                  "type": "mrkdwn",
                  "text": "Your response has been submitted!"
                }
              }
            ]
        }
    )

# Listen for a shortcut invocation
@app.shortcut("secret_santa_begin")
def secret_santa_begin_modal(ack, body, client):
    # Acknowledge the command request
    ack()
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={
            "callback_id": "secret_santa_begin_callback",
            "type": "modal",
            "title": {
                "type": "plain_text",
                "text": "Secret Santa",
                "emoji": True
            },
            "submit": {
                "type": "plain_text",
                "text": "Submit",
                "emoji": True
            },
            "close": {
                "type": "plain_text",
                "text": "Cancel",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": ":santa: Begin your Secret Santa event! :santa:",
                        "emoji": True
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*You want to begin the process of having a Secret Santa this year!*\nPlease fill out the following information..."
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Pick a time to start the Secret Santa Signup:"
                    },
                    "accessory": {
                        "type": "datepicker", #datetime.today()
                        "initial_date": str(datetime.date.today()),
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select a date",
                            "emoji": True
                        },
                        "action_id": "datepicker-begin-date"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Pick a time to start the Secret Santa Event:"
                    },
                    "accessory": {
                        "type": "datepicker", #datetime.today()
                        "initial_date": str(datetime.date.today()),
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select a date",
                            "emoji": True
                        },
                        "action_id": "datepicker-start-date"
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "multi_users_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select users",
                            "emoji": True
                        },
                        "action_id": "multi-users-begin"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Choose some users to inform of the Secret Santa Event!",
                        "emoji": True
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Select a channel for Secret Santa to post in*"
                    },
                    "accessory": {
                        "type": "channels_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select a channel",
                            "emoji": True
                        },
                        "action_id": "channels-select-begin"
                    }
                }
            ]
        }
    )

@app.action('datepicker-begin-date')
def datepicker_begin_date(body, logger, ack):
    ack()
    logger.info(body)

@app.action('datepicker-start-date')
def datepicker_start_date(body, logger, ack):
    ack()
    logger.info(body)

@app.action('multi-users-begin')
def multi_users_begin(body, logger, ack):
    ack()
    logger.info(body)

@app.action('channels-select-begin')
def channels_select_begin(body, logger, ack):
    ack()
    logger.info(body)

# Listen for a shortcut invocation
@app.shortcut("example_modal")
def open_modal(ack, body, client):
    # Acknowledge the command request
    ack()
    print(body['trigger_id'])
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={
            "type": "modal",
            # View identifier
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": "My App"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "Welcome to a modal with _blocks_"},
                    "accessory": {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Click me!"},
                        "action_id": "button_abc"
                    }
                },
                {
                    "type": "input",
                    "block_id": "input_c",
                    "label": {"type": "plain_text", "text": "What are your hopes and dreams?"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "dreamy_input",
                        "multiline": True
                    }
                }
            ]
        }
    )

# Listen for a shortcut invocation
@app.shortcut("user_secret_santa")
def user_secret_santa(ack, body, client):
    # Acknowledge the command request
    ack()
    #print(body['trigger_id'])
    # Call views_open with the built-in client
    if secret_santa_app.isUserInDatabase(body['user']['id']):
        blocks = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Please enter your user information here to help your Secret Santa out!"
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "initial_value": secret_santa_app.data['users'][body['user']['id']]['interests'],
                        "action_id": "plain_text_input_user_submission"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Insert your interests here",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "multi_static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select group/s",
                            "emoji": True
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Pathfinders Leadership",
                                    "emoji": True
                                },
                                "value": "Pathfinders Leadership"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Pathfinders Archean",
                                    "emoji": True
                                },
                                "value": "Pathfinders Archean"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Pathfinders Protozoic",
                                    "emoji": True
                                },
                                "value": "Pathfinders Protozoic"
                            }
                        ],
                        "initial_options": secret_santa_app.data['users'][body['user']['id']]['groups_slack'],
                        "action_id": "multi_static_select_user_submission"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Select your group/s that you belong to",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select an item",
                            "emoji": True
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Iowa City, IA",
                                    "emoji": True
                                },
                                "value": "Iowa City, IA"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "San Antonio, TX",
                                    "emoji": True
                                },
                                "value": "San Antonio, TX"
                            }
                        ],
                        "initial_option": secret_santa_app.data['users'][body['user']['id']]['location_slack'],
                        "action_id": "static_select_user_submission"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Select your location",
                        "emoji": True
                    }
                }
            ]
    else:
        blocks = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Please enter your user information here to help your Secret Santa out!"
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plain_text_input_user_submission"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Insert your interests here",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "multi_static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select group/s",
                            "emoji": True
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Pathfinders Leadership",
                                    "emoji": True
                                },
                                "value": "Pathfinders Leadership"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Pathfinders Archean",
                                    "emoji": True
                                },
                                "value": "Pathfinders Archean"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Pathfinders Protozoic",
                                    "emoji": True
                                },
                                "value": "Pathfinders Protozoic"
                            }
                        ],
                        "action_id": "multi_static_select_user_submission"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Select your group/s that you belong to",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select an item",
                            "emoji": True
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Iowa City, IA",
                                    "emoji": True
                                },
                                "value": "Iowa City, IA"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "San Antonio, TX",
                                    "emoji": True
                                },
                                "value": "San Antonio, TX"
                            }
                        ],
                        "action_id": "static_select_user_submission"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Select your location",
                        "emoji": True
                    }
                }
            ]
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        view={
            "callback_id": "secret_santa_user_submission",
            "type": "modal",
            "title": {
                "type": "plain_text",
                "text": "My App",
                "emoji": True
            },
            "submit": {
                "type": "plain_text",
                "text": "Submit",
                "emoji": True
            },
            "close": {
                "type": "plain_text",
                "text": "Cancel",
                "emoji": True
            },
            "blocks": blocks
        }
    )

@app.view("secret_santa_user_submission")
def handle_secret_santa_submission(ack, body, client, logger, payload):
    ack()
    #print(payload['blocks'])
    secret_santa_app.set_user(
        body['user']['id'],
        body['user']['name'],
        body['user']['username'],
        payload['state']['values'][payload['blocks'][1]['block_id']]['plain_text_input_user_submission']['value'],
        [ values['value'] for values in payload['state']['values'][payload['blocks'][2]['block_id']]['multi_static_select_user_submission']['selected_options'] ],
        payload['state']['values'][payload['blocks'][2]['block_id']]['multi_static_select_user_submission']['selected_options'],
        payload['state']['values'][payload['blocks'][3]['block_id']]['static_select_user_submission']['selected_option']['value'],
        payload['state']['values'][payload['blocks'][3]['block_id']]['static_select_user_submission']['selected_option']
        )

    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={
            "type": "modal",
            # View identifier
            "callback_id": "secret_santa_user_submission_callback",
            "title": {"type": "plain_text", "text": "My App"},
            "blocks": [
                {
                "type": "section",
                "text": {
                  "type": "mrkdwn",
                  "text": "Your response has been submitted!"
                }
              }
            ]
        }
    )


#Event loggers that record events that happen
#This leads to less errors in the terminal as well
@app.event("message")
def handle_message_events(body, logger, payload):
    logger.info(body)

@app.event("pin_added")
def handle_pin_added_events(body, logger):
    logger.info(body)

@app.event("app_mention")
def handle_app_mention_events(body, logger):
  logger.info(body)

@app.event("link_shared")
def handle_link_shared_events(body, logger):
    logger.info(body)

@app.event("team_join")
def member_join(event):
  print("test")
  print(event.keys())
  
@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    try:
        # Call views.publish with the built-in client
        client.views_publish(
            # Use the user ID associated with the event
            user_id=event["user"],
            # Home tabs must be enabled in your app configuration
            view={
                "type": "home",
                "blocks": [
                {
                  "type": "image",
                  "image_url": "https://picsum.photos/400/100",
                  "alt_text": "inspiration"
                },
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Welcome to my Bot homepage, <@" + event['user'] + ">!*\nYou can access it's code at <https://bitbucket.pearson.com/users/usahusp/repos/spencer-sahu-slackbot/browse?at=refs%2Fheads%2Fdev | my BitBucket Repository>"
                  }
                },
                {
                  "type": "actions",
                  "elements": [
                    {
                      "type": "button",
                      "text": {
                        "type": "plain_text",
                        "text": "I do nothing",
                        "emoji": True
                      },
                      "value": "Nothing",
                      "action_id": "button_abc"
                    },
                    {
                      "type": "button",
                      "text": {
                        "type": "plain_text",
                        "text": "Open Modal",
                        "emoji": True
                      },
                      "value": "click_me_123",
                      "action_id": "Open_Modal"
                    }
                  ]
                }
              ]
            }
        )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")

# Start your app
if __name__ == "__main__":
  SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
