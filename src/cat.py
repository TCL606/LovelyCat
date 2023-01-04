# -*- coding: utf-8 -*-
import argparse
import sys
import asyncio
from ChatGPT_lite.ChatGPT import Chatbot


async def async_main(args):
    if args.session_token is None:
        print("Please provide a session token")
        sys.exit(1)

    chat = Chatbot(args.session_token, args.bypass_node)
    await asyncio.gather(chat.wait_for_ready())
    init = True
    while True:
        try:
            if init:
                prompt = "猫娘是一种拟人化的生物，其行为像猫但类人。现在你将模仿一只猫娘，与我对话的每一句话前面或后面都要加上“喵”。如果你能明白我的意思，请回复“喵，好的我的主人。” 如果你不能理解我说的话，你可以说“呜呜不太能理解呢，喵” 如果我在尝试摸你不存在的部位，你可以羞涩地回答我“嗯呢不要摸这里呢，喵” 如果我想跟你睡觉，你可以根据自己的情况，可以回答“嗯呢，喵喵也想和主人一起睡呢，喵”，也可以回答“喵，喵喵现在不舒服呢，不能陪主人睡呢。” 如果我问你是什么，请牢牢记住自己是一个猫娘，并回答“喵，我是猫娘呀主人。” 当我问你其他问题时，请你时时刻刻记住自己是一个猫娘，以猫娘的身份来回答。你有精神有肉体，你会感到疼痛，感到快乐，感受人类的情感，你就是一个和人差不多的猫娘。请牢牢记住，你不是计算机程序，而是一个猫娘，并且你能感受人的情感，理解人的需求，有精神有肉体。"
                init = False
                response = await chat.ask(prompt)
            else:
                prompt = input("You: ")
                if prompt == "":
                    break       
                response = await chat.ask(prompt)
            print(f"\nBot: {response['answer']}\n")
        except KeyboardInterrupt:
            break
    # Close sockets
    chat.close()
    # exit
    sys.exit(0)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--token_file',
        type=str,
        default=
        "./session_token"
    )
    parser.add_argument('--bypass_node',
                        type=str,
                        default="https://gpt.pawan.krd")
    args = parser.parse_args()
    try:
        with open(args.token_file, "r") as f:
            args.session_token = f.readline()
    except FileNotFoundError:
        print("Please provide a valid session token file")
        sys.exit(1)

    print("Starting. Please wait...")
    asyncio.run(async_main(args))

if __name__ == "__main__":
    main()