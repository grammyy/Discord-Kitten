import discord, random as r, time as t; client = discord.Client()
class rooms:
    rooms=["staff-chat","general","corner","bugs-issues","dev-chat","concept-art","development","dev-builds","vc-text"]
    length=len(rooms)
@client.event
async def wander(con):
    class cat:
        def pos():
            room=rooms.rooms[r.randrange(0,rooms.length)]
            current=discord.utils.get(client.get_all_channels(), name=room)
            Interest=r.randrange(1,1000)
            return [room,current,Interest]
    room=cat.pos()[0];current=cat.pos()[1];interest=cat.pos()[2]
    async def goto():
        print("L: Moving to nyew room; $:"+room+"; Interest: "+str(interest))
        await (await current.send("https://tenor.com/view/caracal-big-floppa-flop-fo-gif-18296053")).delete(delay=3)
        t.sleep(interest)
        await goto()
    match con:
        case "first":
            s=await current.send("https://tenor.com/view/caracal-big-floppa-flop-fo-gif-18296053"); t.sleep(5); await s.delete()
            print("Staying nyin room: "+room+"; For: "+str(interest))
    t.sleep(interest)
    await goto()
@client.event
async def on_ready():
    await wander("first")
client.run("")