import secrets
import time

session_storage = {}
def create_session(user_id: int, lifetime_seconds: int = 60) -> str:
    token = secrets.token_urlsafe(32)
    session_storage[token] = {
        "user_id" : user_id,
        "expires_at" : time.time() + lifetime_seconds,
    }

    return token

def get_user(session_id: str) -> int | None:
   
    user_info = session_storage.get(session_id)

    if user_info is None:
        return None

    if time.time() >= user_info["expires_at"]:
        logout(session_id)
        return None

    return user_info["user_id"]

def logout(session_id: str) -> None:

        del session_storage[session_id]


active = create_session(7, lifetime_seconds=60)
print(get_user(active))  # 7

expired = create_session(8, lifetime_seconds=0)
print(get_user(expired))  # None

logout(active)
print(get_user(active))  # None