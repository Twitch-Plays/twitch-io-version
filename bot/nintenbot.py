from twitchio.ext import commands
from dotenv import load_dotenv
import keyboard
import os

load_dotenv()

class Playbot(commands.Bot):

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

bot = Playbot()
bot.run()

