import json
from typing import Any


class InvalidInstagramDataError(ValueError):
    """Raised when uploaded JSON files do not match expected structure."""


def _extract_followers(data: Any) -> set[str]:
    if not isinstance(data, list):
        raise InvalidInstagramDataError("followers_1.json no tiene el formato esperado.")

    followers: set[str] = set()
    for user in data:
        try:
            followers.add(user["string_list_data"][0]["value"])
        except (KeyError, IndexError, TypeError):
            continue
    return followers


def _extract_following(data: Any) -> set[str]:
    if not isinstance(data, dict):
        raise InvalidInstagramDataError("following.json no tiene el formato esperado.")

    following: set[str] = set()
    for user in data.get("relationships_following", []):
        try:
            following.add(user["title"])
        except KeyError:
            continue
    return following


def calculate_non_followers(followers_bytes: bytes, following_bytes: bytes) -> dict[str, Any]:
    try:
        followers_data = json.loads(followers_bytes.decode("utf-8"))
        following_data = json.loads(following_bytes.decode("utf-8"))
    except UnicodeDecodeError as exc:
        raise InvalidInstagramDataError("Los archivos deben estar codificados en UTF-8.") from exc
    except json.JSONDecodeError as exc:
        raise InvalidInstagramDataError("Uno de los archivos no es JSON valido.") from exc

    followers = _extract_followers(followers_data)
    following = _extract_following(following_data)
    non_followers = sorted(following - followers)

    return {
        "followers_count": len(followers),
        "following_count": len(following),
        "non_followers_count": len(non_followers),
        "non_followers": non_followers,
    }
