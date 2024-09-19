from abc import abstractclassmethod
from mailbox import Message


class User:
    def __init__(self, name: str, contact_info: str, conversation: list["Conversation"]):
        self.name = name
        self.contact_info = contact_info
        self.conversation = conversation

    def creat_conversation(self, user: "User") -> "Conversaton":
        self.user = user

    def send_message(self, message: "Message", conversation: "Conversation") -> None:
        self.message = message
        self.conversation = conversation

    def receive_message(self, message: "Message") -> None:
        self.message = mesasge

    def manage_settings(self) -> None:
        print("Hi baby")

    def get_conversation(self) -> list["Conversation"]:
        print("How are you baby")

class Conversation:
    def __init__(self, participants: list["User"], message_history: list["Message"]):
        self._participants = participants
        slef._message_history = message_history

    def add_message(self, message: ["Message"]) -> None:
        self._message.append(message)

    def add_user(self, user: "User") -> None:
        self._user.append(user)

    def get_messages(self) -> list["Message"]:
        print("Have a questions?")

class Message(ABC):
    def __init__(self, sender: "User", conversation: "Conversation", timestamp: datetime):
        self._sender = sender
        self._conversation = conversation
        self._timestamp = timestamp

    def displey_content(self) -> None:
        ...

    def get_message_type(self) -> str:
        ...

class TextMessage(Message):
    def __init__(self, sender: "User", conversation: "Conversation", timestamp: datetime, content: str):
        super().__init__(sneder, conversation, timestamp)
        self._content = content

    def displey_content(self) -> None:
        print("What are you doing")

    def get_message_type(self) -> str:
        return "Text"

class MultimediaMessages(Message):
    def __init__(self, sender: "User", conversation: "Conversation", timestamp: datetime, file_path: str, media_type: str):
        super().__init__(sender, conversation, timestamp)
        self._file_path = file_path
        self._media_type = media_type

    def displey_content(self) -> None:
        ...

    def get_message_type(self) -> str:
        ...

class MessagingManager:

    def send_message(self, message: 'Message') -> None:
        ...

    def receive_message(self, message: 'Message') -> None:
        ...

    def view_conversation_history(self, conversation: 'Conversation') -> List['Message']:
        ...








New_User = User("Jorj", "lav", [])
New_User.manage_settings()
New_User.get_conversation()