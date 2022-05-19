import os
from twitchio.ext import commands
from twitchio import chatter
from dotenv import load_dotenv
import keyboard

load_dotenv()


class Bot(commands.Bot):
    def __init__(self):
        self.twitchplayactive = False
        self.explicitfilter = False
        self.blacklist = []
        super().__init__(
            token=os.getenv("ACCESSTOKEN"), prefix="!", initial_channels=["seattcpybot"]
        )

    
    async def event_ready(self):
        """
        Verifies the login of bot
        """
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")

    # Check chat for blacklisted words
    
    async def event_message(self, message):
        if message.echo:
            return
        try:
            print(f'{message.tags}: {message.author}: {message.content}')
            print(chatter.badges)
            await self.check_message(message)
        finally:
            await self.handle_commands(message)
        


    async def check_message(self, message):
        print(f'original message: {message.content}')
        if self.explicitfilter is False:
            print('filter is off')
            return message
        if self.explicitfilter is True:
            print('checking message')
            if not message.author['is_broadcaster'] or message.author.is_moderator:
                for word in message.content:
                    word = word.lower()
                    if word in self.blacklist:
                        message_id = message.tags['id']
                        await message.channel.send(f'/delete {message_id}')
                        await self.timeout(
                            user=message.tags['display-name'], duration=30, reason="You said a bad word"
                            )
                    else:
                        return

    @commands.command()
    async def up(self, ctx: commands.Context):
        keyboard.press_and_release("up")

    @commands.command()
    async def down(self,ctx: commands.Context):
        keyboard.press_and_release("down")

    @commands.command()
    async def left(self, ctx: commands.Context):
        keyboard.press_and_release("left")

    @commands.command()
    async def right(self, ctx: commands.Context):
        keyboard.press_and_release("right")

    @commands.command(name="a")
    async def push_a(self, ctx: commands.Context):
        keyboard.press_and_release("s")

    @commands.command(name="b")
    async def push_b(self, ctx: commands.Context):
        keyboard.press_and_release("a")

    @commands.command()
    async def start(self, ctx: commands.Context):
        keyboard.press_and_release("return")

    # Explicit Chat Filter ON/Off
    @commands.command(name="filter")
    # Check to see if is moderator to activate
    async def explicit_filter(self, ctx: commands.Context):
        # if ctx.author.is_mod or ctx.author.is_broadcaster:
        if self.explicitfilter is False:
            self.explicitfilter = True
            await ctx.send("Kiddie filter on!")
        elif self.explicitfilter is True:
            self.explicitfilter = False
            await ctx.send("Kiddie filter off!")

    @commands.command(name="banword")
    async def add_to_blacklist(self, ctx: commands.Context):
        blkmsg = ctx.message.content.replace("!banword ", "").lower()
        await ctx.send(f"Attempting to add {blkmsg} to blacklist")
        if blkmsg in self.blacklist:
            await ctx.send(f"{blkmsg} is already in the blacklist")
            return
        self.blacklist.append(blkmsg)
        await ctx.send(f"{blkmsg} has been added to the blacklist")

    async def timeout(self, user, duration: int = 300, *, reason: str = ""):
        ctx = commands.Context
        await ctx.send('someone said a bad word')
        


bot = Bot()
bot.run()
