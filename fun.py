import asyncio
import random
import helper
import access

async def hug(discord, kizuna, huger, *hugee):
    if len(hugee) > 0: # Check if hugee has any arguements
        member = helper.getUsers(discord, huger.message.server.members, hugee) # Grab user data on all users in the arguement
        users = helper.duplicateCleaner([i.mention for i in member]) # Convert the data into strings and remove all duplicates
        
        image = access.randomImage("hug")
        chosen = random.choice(image)
               
        if len(users) == 1: # Check if array only has one object
            if huger.message.author in member: # Check if the huger is in the array and display a special message for them hugging themselves
                fancy = discord.Embed(description = huger.message.author.display_name + " hugs themselves. What a fucking loser", color = 0xDEADBF)
                fancy.set_image(url = chosen)
                await kizuna.say(embed = fancy)
            else: # if the huger is not in the array then just do a normal hug
                fancy = discord.Embed(description = huger.message.author.display_name + " hugs " + " ".join(users), color = 0x0DEADBF) 
                fancy.set_image(url = chosen)
                await kizuna.say(embed = fancy)
        elif len(users) > 1: # Check if there is more then 1 object in the array
            if huger.message.author in member: # Check if the huger is in the array and remove them from the array
                users.remove(huger.message.author.mention)
            else: 
                False
            fancy = discord.Embed(description = huger.message.author.display_name + " groups hugs " + " ".join(users), color = 0xDEADBF) # Join the array together into a string for the group hug
            fancy.set_image(url = chosen)
            await kizuna.say(embed = fancy)
        else: # Display a special message if the array is empty
            await kizuna.say("Enter a valid username you dumbass")
    else: # Display a special message of hugee has no arguements
        await kizuna.say("You hugged no one dumbass")

async def ai(discord,kizuna):
    image = access.randomImage("ai")
    chosen = random.choice(image)

    fancy = discord.Embed()
    fancy.set_image(url = chosen)
    await kizuna.say(embed = fancy)
