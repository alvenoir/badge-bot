    import os
    import discord
    from discord.ext import commands

    # Get the bot token from environment variables (like Render's secrets).
    # Make sure you set a variable named DISCORD_BOT_TOKEN on Render.
    DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

    # Define intents: we only need 'guilds' for basic slash commands
    intents = discord.Intents.default()
    intents.guilds = True

    # Create the bot instance.
    # command_prefix is required by discord.py, even if not used for text commands.
    bot = commands.Bot(command_prefix="!", intents=intents)

    # Event: Bot is ready
    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user.name} ({bot.user.id})")
        print("Attempting to sync slash commands...")
        try:
            # Sync the slash commands globally.
            # This is important so Discord knows about your /ping command.
            synced_commands = await bot.tree.sync()
            print(f"Successfully synced {len(synced_commands)} global slash command(s).")
            print("Your bot is ready and online. Try typing /ping in Discord!")
        except Exception as e:
            print(f"Error syncing commands: {e}")
            print("Please ensure your bot has the 'applications.commands' scope in its invite URL from Discord Developer Portal.")

    # Slash Command: /ping
    # This defines the actual /ping command and its response.
    @bot.tree.command(name="ping", description="Responds with Pong!")
    async def ping(interaction: discord.Interaction):
        # This sends "Pong!" back in Discord when someone uses /ping.
        await interaction.response.send_message("Pong!")

    # Run the bot with the token
    if __name__ == "__main__":
        if not DISCORD_BOT_TOKEN:
            print("ERROR: DISCORD_BOT_TOKEN environment variable not found.")
            print("Please ensure you have set the 'DISCORD_BOT_TOKEN' secret on your hosting platform (like Render).")
        else:
            bot.run(DISCORD_BOT_TOKEN)
