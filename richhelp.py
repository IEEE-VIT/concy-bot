import discord
from discord.ext import commands
from discord import Color as c

class HelpCommand(commands.DefaultHelpCommand):
    def __init__(self, **options):
        self.paginator = commands.Paginator()
        super().__init__(**options)
        self.paginator.prefix = ""
        self.paginator.suffix = ""
        self.no_category = ""

    def add_indented_commands(self, commands, *, heading, max_size=None):
        if not commands:
            return
        self.paginator.add_line(f"**{heading}**")
        max_size = max_size or self.get_max_size(commands)
        get_width = discord.utils._string_width
        for command in commands:
            name = f"{command.name}"
            width = max_size - (get_width(name) - len(name))
            entry = "{0}{1:<{width}}: *{2}*".format(self.indent * " ",
                                                    name,
                                                    command.short_doc,
                                                    width=width)
            self.paginator.add_line(self.shorten_text(entry))

    def get_ending_note(self):
        command_name = self.invoked_with
        return "Type `{0}{1} <command>` for more info on a command.\n".format(
            self.clean_prefix, command_name)

    def add_command_formatting(self, command):
        if command.description:
            self.paginator.add_line(command.description, empty=True)
        elif command.brief:
            self.paginator.add_line(command.brief, empty=True)
        signature = self.get_command_signature(command)
        self.paginator.add_line(f"`{signature}`" "", empty=True)

        if command.help:
            try:
                self.paginator.add_line(command.help, empty=True)
            except RuntimeError:
                for line in command.help.splitlines():
                    self.paginator.add_line(line)
                self.paginator.add_line()

    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(title="Help",
                          color=discord.Color.blurple(),
                          description="")
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)