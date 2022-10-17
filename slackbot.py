import os
import requests
import datetime 
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
load_dotenv()

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
user = os.environ.get("SLACK_USER_TOKEN")

@app.command("/begin")
def secretSanta_begin(ack, respond, payload):
  blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":santa: Secret Santa :santa:",
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
                    "text": "Pick a deadline to signup by:"
                },
                "accessory": {
                    "type": "datepicker",
                    "initial_date": f'{datetime.date.today()}',
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select a date",
                        "emoji": True
                    },
                    "action_id": "datepicker-action"
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
                    "action_id": "multi_users_select-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "Choose some users to start!",
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
                    "action_id": "users_select-action"
                }
            }
        ]
  ack()
  respond(text="Secret Santa Begin Message", blocks=blocks)


# Listen for a button invocation with action_id `coffee` 
@app.action("coffee")
def open_coffee(ack, body, client):
    # Acknowledge the command request
    ack()
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
                "text": {
                  "type": "mrkdwn",
                  "text": "I heard you say the magic word, so enjoy this image!"
                }
              },
              {
                "type": "image",
                "title": {
                  "type": "plain_text",
                  "text": ":coffee:",
                  "emoji": True
                },
                "image_url": requests.get('https://coffee.alexflipnote.dev/random.json').json()['file'],
                "alt_text": "some coffee"
              }
            ]
        }
    )

# Listen for a shortcut invocation
@app.shortcut("begin")
def open_modal(ack, body, client):
    # Acknowledge the command request
    print(body.keys())
    print(client.keys())
    ack()
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={
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
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": ":santa: Secret Santa :santa:",
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
                        "text": "Pick a deadline to signup by:"
                    },
                    "accessory": {
                        "type": "datepicker",
                        "initial_date": "1990-04-28",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select a date",
                            "emoji": True
                        },
                        "action_id": "datepicker-action"
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
                        "action_id": "multi_users_select-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Choose some users to start!",
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
                        "action_id": "users_select-action"
                    }
                }
            ]
        }
    )

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
    print(body['trigger_id'])
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={
            "type": "modal",
            "callback_id": "user_secret_santa_submission",
            "title": {
                "type": "plain_text",
                "text": "My App",
                "emoji": True
            },
            "submit": {
                "type": "plain_text",
                "text": "Submit",
                "emoji": True,
            },
            "close": {
                "type": "plain_text",
                "text": "Close",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "This is the page to edit your profile for Secret Santa."
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "List your interests here",
                        "emoji": True
                    }
                }
            ]
        }
    )

@app.view("user_secret_santa_submission")
def handle_secret_santa_submission(ack, body, logger, payload):
    ack()
    print(body.keys())
    print(body['user'], body['team'])
    print(payload)
    logger.info(body)

#Event loggers that record events that happen
#This leads to less errors in the terminal as well
@app.event("message")
def handle_message_events(body, logger):
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
