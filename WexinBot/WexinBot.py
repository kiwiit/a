import werobot

robot = werobot.WeRoBot(token="schedule")

@robot.text
def hello_world():
    return 'Hello World!'

robot.run()