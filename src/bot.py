import discord

class ArticleBot(discord.Client):
    async def on_ready(self):
        print('I\'m ready!!1')

    async def on_message(self, message):
        if "meme" in message.channel.name and message.attachments.count() > 0:
            message.channel.send('The content you are trying to post has been banned by Article 17 (previously Article 13)'+
                                 'of the European Union Directive on Copyright in the Digital Single Market.\n' +
                                 'Please only post content of which you can 100 percent confirm that you have both made it and ' +
                                 'own the rights to it.')
            message.delete()

client = ArticleBot()
client.run('NTYxNTU1NjA0ODE3MzEzODEz.XJ97ng.SEpkH9826_JIf_n58aFXMGxXoKI')
