import os
import time
import twitchio
from twitchio.ext import commands
from dotenv import load_dotenv
import pyautogui

load_dotenv()


class Bot(commands.Bot):
    def __init__(self):
        self.twitchplayactive = False
        self.explicitfilter = False
        self.blacklist = []
        super().__init__(
            token=os.getenv("ACCESSTOKEN"), prefix="!", initial_channels=["bkhanal4351"]
        )

    async def event_ready(self):
        """
        Verifies the login of bot
        """
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")

    # Check chat for blacklisted words
    # Check if mod
    '''
    key,value = 'mod', '1'
    if value == message.tags[key]
    return boolean true/false
    '''

    async def event_message(self, message: twitchio.Message):
        if message.echo:
            return
        try:
            return await self.profanity_check(message)
        finally:
            await self.handle_commands(message)

    async def profanity_check(self, message: twitchio.Message):
        if not self.explicitfilter:
            return
        if message.author.is_mod or message.author.is_broadcaster:
            return
        for word in message.content.lower().split(' '):
            if word in self.blacklist:
                await message.channel.send(f"/timeout {message.author.name} 30 You Said a Bad Word")
                print(f"/timeout {message.tags['display-name']} 30 You Said a Bad Word")

    # Start Twitch Plays Commands

    @commands.command()
    async def up(self, ctx: commands.Context):
        pyautogui.press("up")

    @commands.command()
    async def down(self, ctx: commands.Context):
        pyautogui.press("down")

    @commands.command()
    async def left(self, ctx: commands.Context):
        pyautogui.press("left")

    @commands.command()
    async def right(self, ctx: commands.Context):
        pyautogui.press("right")

    @commands.command()
    async def w(self, ctx: commands.Context):
        pyautogui.press("w")

    @commands.command()
    async def s(self, ctx: commands.Context):
        pyautogui.press("s")

    @commands.command()
    async def d(self, ctx: commands.Context):
        pyautogui.press("d")

    @commands.command()
    async def a(self, ctx: commands.Context):
        pyautogui.press("a")

    @commands.command(name="b")
    async def push_b(self, ctx: commands.Context):
        pyautogui.press("b")

    @commands.command()
    async def start(self, ctx: commands.Context):
        pyautogui.press("return")

    @commands.command()
    async def enter(self, ctx: commands.Context):
        pyautogui.press("return")

    @commands.command(name='1')
    async def one(self, ctx: commands.Context):
        pyautogui.press("1")

    @commands.command(name='2')
    async def two(self, ctx: commands.Context):
        pyautogui.press("2")

    @commands.command(name='3')
    async def three(self, ctx: commands.Context):
        pyautogui.press("3")

    @commands.command(name='4')
    async def four(self, ctx: commands.Context):
        pyautogui.press("4")

    @commands.command(name='5')
    async def five(self, ctx: commands.Context):
        pyautogui.press("5")

    @commands.command(name='tab')
    async def tab(self, ctx: commands.Context):
        pyautogui.press("tab")

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def controls(self, ctx: commands.Context):
        # shouts out the controls
        await ctx.send(f'Hello {ctx.author.name}! controls for the game are: !up, !down, !left, !right, !w, !s, !a, !d, !b, !tab, !enter, !1, !2, !3, !4, !5 and !start')


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
        time.sleep(2)
        if blkmsg in self.blacklist:
            await ctx.send(f"{blkmsg} is already in the blacklist")
            return
        self.blacklist.append(blkmsg)
        await ctx.send(f"{blkmsg} has been added to the blacklist")


bot = Bot()
bot.run()
