import discord
from fighters import fighters2ids, ids2fighters


class Profile(discord.Embed):
    def __init__(self, member, **kwargs):
        super().__init__(**kwargs)
        self.member = member
        self.switchCode = '-'
        self.mains = []
        self.secondaries = []
        self.add_field(name='Name', value=self.member.name)
        self.add_field(name='Switch Code', value=self.switchCode)
        self.add_field(name='Mains', value='-')
        self.add_field(name='Secondaries', value='-')

    def setSwitchCode(self, switchCode):
        self.switchCode = switchCode
        self.set_field_at(1, name='Switch Code', value=self.switchCode)

    def setMains(self, fighters):
        fighters.replace(' ', '')
        names = fighters.lower().split(',')
        if len(names) < 1:
            self.mains = []
        else:
            self.mains = list(map(lambda x: fighters2ids.get(x), names))
        names = str(list(map(lambda x: ids2fighters.get(x), self.mains)))
        self.set_field_at(2, name='Mains', value=names[1:-1])

    def setSecondaries(self, fighters):
        fighters.replace(' ', '')
        names = fighters.lower().split(',')
        if len(names) < 1:
            self.secondaries = []
        else:
            self.secondaries = list(map(lambda x: fighters2ids.get(x), names))
        names = str(list(map(lambda x: ids2fighters.get(x), self.secondaries)))
        self.set_field_at(3, name='Secondaries', value=names[1:-1])
