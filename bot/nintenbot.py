from twitchio.ext import commands
from dotenv import load_dotenv
import keyboard
import os


load_dotenv()

class Playbot(commands.Bot):


  blacklist= ['shit', 'fuck', 'damn', 'etc']

  def __init__(self):
    self.twitchplayactive = False
    super().__init__(token=os.getenv('ACCESSTOKEN'), prefix='!', initial_channels=['seattcpybot'])

  async def event_ready(self):
    print(f'Logged in as | {self.nick}')
    print(f'User id is | {self.user_id}')

  @commands.command()
  async def up(self, ctx: commands.Context):
    keyboard.press_and_release('up')
  @commands.command()
  async def down(self, ctx: commands.Context):
    keyboard.press_and_release('down')
  @commands.command()
  async def left(self, ctx: commands.Context):
    keyboard.press_and_release('left')
  @commands.command()
  async def up(self, ctx: commands.Context):
    keyboard.press_and_release('right')
  @commands.command()
  async def a(self, ctx: commands.Context):
    keyboard.press_and_release('s')
  @commands.command()
  async def b(self, ctx: commands.Context):
    keyboard.press_and_release('a')
  @commands.command()
  async def start(self, ctx: commands.Context):
    keyboard.press_and_release('return')

  @commands.command()
  async def hello(self, ctx: commands.Context):
    await ctx.send(f'Hello {ctx.author.name}!')

  @commands.command()
  async def controls(self, ctx: commands.Context):
        # shouts out the controls
    await ctx.send(f'Hello {ctx.author.name}! controls: !up, !down, !left, !right. !a, !b and !start')

  #Explicit Chat Filter ON/Off    
  @commands.command(name="explicitfilter")
    # Check to see if is moderator to activate
  async def explicit_filter(self, ctx: commands.Context):
        if ctx.author.is_mod or ctx.author.is_broadcaster:
            if self.explicitfilter is False:
                self.explicitfilter = True
                await ctx.send('Kiddie filter on!')
            if self.explicitfilter is True:
                self.explicitfilter = False
                await ctx.send('Kiddie filter off!')
   
    # Check chat for blacklisted words
  async def event_message(self, ctx: commands.Context):
        if ctx.message.echo:
            return
        if self.explicitfilter is False:
            return
        if self.explicitfilter is True:
            if ctx.author.is_broadcaster:
                return
            if any([word in ctx.message.content for word in self.blacklist]):
                self.timeout(ctx = commands.Context, user = ctx.author.name,  duration = 300, reason ='You said a bad word')

  @commands.command()
  async def addblacklist(self, ctx : commands.context, message):
        self.blacklist.append(message)
        await ctx.send(f'{message} has been added to blacklist there are {len(self.blacklist)} words banned from chat')

  @commands.command()
  async def timeout(self, ctx: commands.Context, user, duration : int = 300, *, reason : str = ''):
        await ctx.send(f'/timeout {user} {duration} {reason}')
    

bot = Playbot()
bot.run()

