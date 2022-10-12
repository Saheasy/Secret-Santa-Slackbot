import os
import random
import requests
import re
import blocks
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
load_dotenv()


# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
user = os.environ.get("SLACK_USER_TOKEN")


# My Dadjoke Slash Command
# Send a dadjoke via "icanhazdadjoke.com"'s api
@app.command("/dadjoke")
def dadjoke(ack, respond, payload):
  message = requests.get("https://icanhazdadjoke.com/",
                         headers={"Accept": "text/plain"}).text
  ack()
  respond(message)

@app.command("/begin")
def secretSanta_begin(ack, respond, payload):
  blocks =  blocks.begin_block
  ack()
  respond(text="Secret Santa Begin Message", blocks=blocks)


# Listen for a button invocation with action_id `coffee` 
@app.action("coffee")
def open_modal(ack, body, client):
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

# Listen for a button invocation with action_id `button_abc` (assume it's inside of a modal)
@app.action("button_abc")
def update_modal(ack, body, client):
    # Acknowledge the button request
    ack()
    # Call views_update with the built-in client
    client.views_update(
        # Pass the view_id
        view_id=body["view"]["id"],
        # String that represents view state to protect against race conditions
        hash=body["view"]["hash"],
        # View payload with updated blocks
        view={
            "type": "modal",
            # View identifier
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": "Updated modal"},
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "plain_text", "text": "You updated the modal!"}
                },
                {
                    "type": "image",
                    "image_url": "https://media.giphy.com/media/SVZGEcYt7brkFUyU90/giphy.gif",
                    "alt_text": "Yay! The modal was updated"
                }
            ]
        }
    )


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
