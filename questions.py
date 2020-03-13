"""
Create a list of JSON objects to store the questions for the Think About Testing tool
json object format should be {"type":"open-question","question":"","example-apps":[]}

"""

questions = [
    {
        "type":"open-question",
        "question":"How do you test the emoticons compatibility across different platforms?",
        "example-apps": ["Skype", "Slack", "MS Teams"]
    } ,
    {
        "type":"open-question",
        "question":"How do I test recording?",
        "example-apps": ["GoogleHangouts","MS Team"]
    },
    {
        "type":"open-question",
        "question":"How do you test 'block user' functionality in a chat app?",
        "example-apps": ["Skype", "Slack"]
    },
    {
        "type":"open-question",
        "question":"Does the recording pick up the background noise from one of the participant?",
        "example-apps": ["GoogleHangouts","MS Team"]
    },
    {
        "type":"open-question",
        "question":"How do you test a video call application temporarily disables video for someone who has high latency?",
        "example-apps": ["GoogleHangouts","MS Team"]
    },
    {
        "type":"open-question",
        "question":"How does a word processing application hande mulitple people editing the same line at the same time?",
        "example-apps": ["Google Docs", "MS Office"]
    },
    {
        "type":"open-question",
        "question":"How does a CI/CD tool handle a queue of events that trigger a test?",
        "example-apps": ["Jenkins","Circle CI"]
    },
    {
        "type":"open-question",
        "question":"How do you check the plugin's compatibility for a platform that changes frequently?",
        "example-apps": ["Chrome","Firefox","Jenkins"]
    },
    {
        "type":"open-question",
        "question":"How do you test if the search returns the right results on chat platforms?",
        "example-apps": ["Skype", "Slack", "MS Teams"]
    },
    {
        "type":"open-question",
        "question":"How does the video chat application knows there is latency in a connection?",
        "example-apps": ["Skype", "Slack", "MS Teams"]
    },
    {
        "type":"open-question",
        "question":"How are the messages ordered in a group chat? messages first sent to the application server are listed first? messages recieved at the server are listed first?",
        "example-apps": ["Skype", "Slack", "MS Teams"]
    },
    {
        "type":"open-question",
        "question":"How do you test calendar events sent to people across different time zones?",
        "example-apps": ["Google", "Outlook"]
    },
    {
        "type":"open-question",
        "question":"How do you decide the test coverage with regards to verifying the languages an IDE supports?",
        "example-apps": ["VS Code","Notepad","SublimeText"]
    }
]

