
begin_block = [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": ":santa: Secret Santa :santa:",
				"emoji": true
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
					"emoji": true
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
					"emoji": true
				},
				"action_id": "multi_users_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Choose some users to start!",
				"emoji": true
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
					"emoji": true
				},
				"action_id": "users_select-action"
			}
		}
	]