import random 
import os 
import discord
from dotenv import load_dotenv 

load_dotenv() 
  
client = discord.Client(intents=discord.Intents.all())
token = os.getenv('TOKEN')

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    
@client.event 
async def on_message(message): 
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.name) 
    user_message = str(message.content) 
  
    print(f'Message {user_message} by {username} on {channel}') 
  
    if message.author == client.user: 
        return
  
    if channel == "general": 
        if user_message.lower() == "hello" or user_message.lower() == "hi": 
            await message.channel.send(f'Hello {username}') 
            return
        elif user_message.lower() == "bye": 
            await message.channel.send(f'Bye {username}') 
        elif user_message.lower() == "tell me a joke": 
            jokes = ["Can someone please shed more light on how my lamp got stolen?",
                     "Why is she called llene? She stands on equal legs.",
                     "What do you call a gazelle in a lions territory? Denzel."]
            await message.channel.send(random.choice(jokes))
            
client.run(token)