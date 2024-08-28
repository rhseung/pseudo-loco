import time
import send


def main():
    send.init()
    message = send.TextMessage()
    room = "방"
    message.text("Hello World!").mention("류현승").text("ㅁㄴㅇㄹ")
    send.send_message(room, message)
    send.send_file(room, "D:\\Repo\\pseudo-loco\\timetable.png")
    send.send_message(room, send.TextMessage().text("테스트2").lw())
    send.send_message(room, send.TextMessage().text("테스트3"))
    send.send_file(room, "D:\\Repo\\pseudo-loco\\requirements.txt")


if __name__ == '__main__':
    main()
