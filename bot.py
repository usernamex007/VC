from pyrogram import Client, raw
from pyrogram.raw.types import UpdateGroupCallParticipants

# Yahan apne credentials daal dijiye
API_ID = 28795512  # Replace with your actual API ID
API_HASH = "c17e4eb6d994c9892b8a8b6bfea4042a"  # Replace with your actual API Hash
BOT_TOKEN = "7589052839:AAHB5ui50RkR-gTX1ZTJm93XJGND1ehzsXA"  # Replace with your actual bot token

# Initialize Pyrogram Client
app = Client("video_chat_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_raw_update(UpdateGroupCallParticipants)
async def handle_video_chat_participants(client, update, users, chats):
    try:
        if chats:
            chat_id = list(chats.values())[0].id  
        else:
            print("No chat information available in the update.")
            return

        for participant in update.participants:
            try:
                user = await client.get_users(participant.user_id)
                user_mention = user.mention
            except:
                user_mention = "Unknown User"

            if hasattr(participant, "just_joined") and participant.just_joined:
                text = (
                    f"🎉 #JoinVideoChat 🎉\n\n"
                    f"Name: {user_mention}\n"
                    f"Action: Joined\n\n"
                )
                await client.send_message(chat_id, text)

            elif hasattr(participant, "left") and participant.left:
                text = (
                    f"😕 #LeftVideoChat 😕\n\n"
                    f"Name: {user_mention}\n"
                    f"Action: Left\n\n"
                )
                await client.send_message(chat_id, text)

    except Exception as e:
        print(f"Error handling participants: {e}")

# Start the bot
app.run()
