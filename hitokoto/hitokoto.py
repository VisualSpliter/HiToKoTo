import requests
import json
from mcdreforged.api.decorator import *
from mcdreforged.api.types import PluginServerInterface,CommandSource,Info
from mcdreforged.api.rtext import *
from mcdreforged.api.command import Literal
import re

#death event listener
#re.fullmatch pre compile
death1 = re.compile(".*? was shot.*?")
death2 = re.compile(".*?lost connection: Killed")
death3 = re.compile(".*? was pummeled.*?")
death4 = re.compile(".*? was pricked to death")
death5 = re.compile(".*? walked into a cactus whilst trying to escape .*?")
death6 = re.compile(".*? drowned")
death7 = re.compile(".*? drowned.*?")
death8 = re.compile(".*? experienced kinetic.*?")
death9 = re.compile(".*? blew up")
death10 = re.compile(".*? was blown up by .*?")
death11 = re.compile(".*? was killed by [Intentional Game Design]")
death12 = re.compile(".*? hit the ground too hard.*?")
death13 = re.compile(".*? fell.*?")
death14 = re.compile(".*? was impaled on a.*?")
death15 = re.compile(".*? went up in flames")
death16 = re.compile(".*? walked into fire whilst fighting .*?")
death17 = re.compile(".*? burned to death")
death18 = re.compile(".*? was burnt to a crisp whilst fighting .*?")
death19 = re.compile(".*? went off with a bang.*?")
death20 = re.compile(".*? tried to swim in lava.*?")
death21 = re.compile(".*? was struck by lightning.*?")
death22 = re.compile(".*? discovered the floor was lava")
death23 = re.compile(".*? walked into danger zone due to .*?")
death24 = re.compile(".*? was killed by.*?")
death25 = re.compile(".*? froze to death")
death26 = re.compile(".*? was frozen to death by .*?")
death27 = re.compile(".*? was slain by.*?")
death28 = re.compile(".*? was fireballed by .*?")
death29 = re.compile(".*? was stung to death")
death30 = re.compile(".*? was shot by a skull from .*?")
death31 = re.compile(".*? starved to.*?")
death32 = re.compile(".*? suffocated.*?")
death33 = re.compile(".*? was squished.*?")
death34 = re.compile(".*? was poked to death by a sweet berry bush")
death35 = re.compile(".*? was killed.*?")
death36 = re.compile(".*? was impaled by .*? with .*?")
death37 = re.compile(".*? fell out of the world")
death38 = re.compile(".*? didn't want to live in the same world as .*?")
death39 = re.compile(".*? withered.*?")
#All moved into death_listener_api



#每个人的生命都弥足珍贵
elm_title = RText("每个人的生命都弥足珍贵",color=RColor.red,styles=RStyle.bold)
elm_subtitle = RText("————XiaohongSVB",color=RColor.gray)


#一言URL
hitokoto_url = "https://v1.hitokoto.cn"


def death_detect(server_message):
    if death1.fullmatch(server_message) or death2.fullmatch(server_message) or death3.fullmatch(server_message) or death4.fullmatch(server_message) or death5.fullmatch(server_message) or death6.fullmatch(server_message) or death7.fullmatch(server_message) or death8.fullmatch(server_message) or death9.fullmatch(server_message) or death10.fullmatch(server_message) or death11.fullmatch(server_message) or death12.fullmatch(server_message) or death13.fullmatch(server_message) or death14.fullmatch(server_message) or death15.fullmatch(server_message) or death16.fullmatch(server_message) or death17.fullmatch(server_message) or death18.fullmatch(server_message) or death19.fullmatch(server_message) or death20.fullmatch(server_message) or death21.fullmatch(server_message) or death22.fullmatch(server_message) or death23.fullmatch(server_message) or death24.fullmatch(server_message) or death25.fullmatch(server_message) or death26.fullmatch(server_message) or death27.fullmatch(server_message) or death28.fullmatch(server_message) or death29.fullmatch(server_message) or death30.fullmatch(server_message) or death31.fullmatch(server_message) or death32.fullmatch(server_message) or death33.fullmatch(server_message) or death34.fullmatch(server_message) or death35.fullmatch(server_message) or death36.fullmatch(server_message) or death37.fullmatch(server_message) or death38.fullmatch(server_message) or death39.fullmatch(server_message):
        return True
# def death_detect(server_message):
#     if death1.fullmatch(server_message) != None:
#         return True
#     elif death2.fullmatch(server_message) != None:
#         return True
#     elif death3.fullmatch(server_message) != None:
#         return True
#     elif death4.fullmatch(server_message) != None:
#         return True
#     elif death5.fullmatch(server_message) != None:
#         return True
#     elif death6.fullmatch(server_message) != None:
#         return True
#     elif death7.fullmatch(server_message) != None:
#         return True
#     elif death8.fullmatch(server_message) != None:
#         return True
#     elif death9.fullmatch(server_message) != None:
#         return True
#     elif death10.fullmatch(server_message) != None:
#         return True
#     elif death11.fullmatch(server_message) != None:
#         return True
#     elif death12.fullmatch(server_message) != None:
#         return True
#     elif death13.fullmatch(server_message) != None:
#         return True
#     elif death14.fullmatch(server_message) != None:
#         return True
#     elif death15.fullmatch(server_message) != None:
#         return True
#     elif death16.fullmatch(server_message) != None:
#         return True
#     elif death17.fullmatch(server_message) != None:
#         return True
#     elif death18.fullmatch(server_message) != None:
#         return True
#     elif death19.fullmatch(server_message) != None:
#         return True
#     elif death20.fullmatch(server_message) != None:
#         return True
#     elif death21.fullmatch(server_message) != None:
#         return True
#     elif death22.fullmatch(server_message) != None:
#         return True
#     elif death23.fullmatch(server_message) != None:
#         return True
#     elif death24.fullmatch(server_message) != None:
#         return True
#     elif death25.fullmatch(server_message) != None:
#         return True
#     elif death26.fullmatch(server_message) != None:
#         return True
#     elif death27.fullmatch(server_message) != None:
#         return True
#     elif death28.fullmatch(server_message) != None:
#         return True
#     elif death29.fullmatch(server_message) != None:
#         return True
#     elif death30.fullmatch(server_message) != None:
#         return True
#     elif death31.fullmatch(server_message) != None:
#         return True
#     elif death32.fullmatch(server_message) != None:
#         return True
#     elif death33.fullmatch(server_message) != None:
#         return True
#     elif death34.fullmatch(server_message) != None:
#         return True
#     elif death35.fullmatch(server_message) != None:
#         return True
#     elif death36.fullmatch(server_message) != None:
#         return True
#     elif death37.fullmatch(server_message) != None:
#         return True
#     elif death38.fullmatch(server_message) != None:
#         return True
#     elif death39.fullmatch(server_message) != None:
#         return True


def say_hitokoto(src:CommandSource):
    hitokoto_sentence = requests.get(hitokoto_url).text
    hitokoto_sentence = json.loads(hitokoto_sentence)
    hitokoto_sentence = hitokoto_sentence["hitokoto"]
    src.reply(RText("今日一言：",color=RColor.gold)+hitokoto_sentence)


def help_message(src: CommandSource):
    src.reply(RText("!!hitokoto 显示一言",color=RColor.green))
    src.reply(RText("!!hitokoto help 显示帮助信息",color=RColor.green))


def title_set(server:PluginServerInterface):
    server.execute("/title @a times 15 30 15")


@new_thread("HiToKoTo - ELM")
def everybodys_live_matters(server: PluginServerInterface):
    title_set(server)
    server.execute("/title @a subtitle {}".format(RText.to_json_str(elm_subtitle)))
    server.execute("/title @a title {}".format(RText.to_json_str(elm_title)))


def register_command(server:PluginServerInterface):
    server.register_command(
            Literal('!!hitokoto').runs(lambda src:say_hitokoto(src))
                .then(
                Literal({"help"})
                    .runs(lambda src:help_message(src))
            )
                .then(
                Literal({"elm"})
                    .runs(lambda :everybodys_live_matters(server))
            )
    )





def on_load(server: PluginServerInterface,old):
    title_set(server)
    register_command(server)


def on_player_joined(server: PluginServerInterface, player: str, info: Info):
    hitokoto_sentence = requests.get(hitokoto_url).text
    hitokoto_sentence = json.loads(hitokoto_sentence)
    hitokoto_sentence = hitokoto_sentence["hitokoto"]
    server.tell(player=player,text=RText("今日一言：",color=RColor.gold)+hitokoto_sentence)


#fullmatch all death events
@new_thread("HiToKoTo - ReMatch")
def on_info(server: PluginServerInterface,info:Info):
    if info.is_from_server:
        if death_detect(info.content):
            everybodys_live_matters(server)
            server.logger.info("每个人的生命都弥足珍贵")