# Discord Command Remover Bot

This Python script is a Discord bot that removes all application commands (slash commands) from a specific guild (server) when it starts. It uses `discord.py` and `aiohttp` to interact with the Discord API asynchronously.

## Features

- Logs in to Discord using a bot token.
- Fetches all registered commands in a specific guild.
- Deletes all commands one by one with a short delay between deletions.
- Provides console feedback for success or failure of each deletion.

## Requirements

- Python 3.10 or higher
- `discord.py` (`pip install discord.py`)
- `aiohttp` (`pip install aiohttp`)
- `python-dotenv` (`pip install python-dotenv`)

## Setup

1. **Create a Discord Bot**

   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application and bot.
   - Copy the **Bot Token**.

2. **Invite the bot to your server**

   - Use the OAuth2 URL Generator in the Developer Portal.
   - Enable `applications.commands` and `bot` scopes.
   - Give it the necessary permissions (at least `Manage Commands`).

3. **Create a `.env` file**
   ```env
   TOKEN=YOUR_BOT_TOKEN
   CLIENT_ID=YOUR_APPLICATION_CLIENT_ID
   GUILD_ID=YOUR_GUILD_ID
   Replace YOUR_BOT_TOKEN YOUR_APPLICATION_CLIENT_ID, and YOUR_GUILD_ID with your bot's token, client ID, and server ID respectively.
   ```

Usage
Clone this repository or download the script.

Install dependencies:

```
pip install -r requirements.txt
```

Run the script:

```
python remove_commands.py
```

The bot will log in and automatically remove all commands from the specified guild. You will see logs in the console indicating which commands were deleted.

Notes
This script only removes guild-specific commands, not global commands.

Deletion is done with a small delay (1 second) between each command to prevent rate-limiting.

Make sure the bot has proper permissions in the target server.
