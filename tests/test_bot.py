from src import discord_bot
from src import vtes


def test_bot(monkeypatch):
    VTES = vtes._VTES()
    VTES.load_from_vekn(save=False)
    VTES.configure(fuzzy_threshold=12, safe_variants=False)
    monkeypatch.setattr(vtes, "VTES", VTES, raising=True)
    # match REMAP values (it may contain easter eggs)
    response = discord_bot.handle_message("krcg")
    assert not response.get("content")
    assert response["embed"]
    assert response["embed"].to_dict() == {
        "color": 3498574,
        "fields": [
            {"inline": True, "name": "Type", "value": "Master"},
            {"inline": True, "name": "Cost", "value": "2 Pool"},
            {
                "inline": False,
                "name": "Card Text",
                "value": "Unique location.\n"
                "Lock to give a minion you control +1 intercept. Lock "
                "and burn 1 pool to give a minion controlled by another "
                "Methuselah +1 intercept.",
            },
        ],
        "footer": {"text": ""},
        "image": {
            "url": "http://www.codex-of-the-damned.org/card-images/krcgnewsradio.jpg"
        },
        "title": "KRCG News Radio",
        "type": "rich",
        "url": (
            "http://www.codex-of-the-damned.org/card-search/index.html"
            "?card=KRCG+News+Radio"
        ),
    }
    # matching isn't easy
    response = discord_bot.handle_message("monastery")
    assert not response.get("content")
    assert response["embed"]
    assert response["embed"].to_dict() == {
        "color": 3498574,
        "fields": [
            {"inline": True, "name": "Type", "value": "Master"},
            {"inline": True, "name": "Cost", "value": "3 Pool"},
            {
                "inline": False,
                "name": "Card Text",
                "value": "Unique location.\n"
                "+1 hand size. Lock to give a vampire with capacity 8 or "
                "more +1 stealth.",
            },
        ],
        "footer": {"text": ""},
        "image": {
            "url": (
                "http://www.codex-of-the-damned.org/card-images/"
                "monasteryofshadows.jpg"
            )
        },
        "title": "Monastery of Shadows",
        "type": "rich",
        "url": (
            "http://www.codex-of-the-damned.org/card-search/index.html"
            "?card=Monastery+of+Shadows"
        ),
    }
    # multiple possibilities gives you a choice
    response = discord_bot.handle_message("isabel")
    assert not response.get("content")
    assert response["embed"]
    assert response["embed"].to_dict() == {
        "color": 16777215,
        "description": "1: Isabel Giovanni\n" "2: Isabel de Leon",
        "footer": {"text": 'Click a number or answer with one (eg. "krcg 1")'},
        "title": "What card did you mean ?",
        "type": "rich",
    }
    # too many possibilities (> 10) gives you an error
    response = discord_bot.handle_message("the")
    assert response["content"] == "Too many candidates, try a more complete card name."
    assert not response.get("embed")
    # vampire with advanced version
    response = discord_bot.handle_message("kemintiri")
    assert response["embed"]
    assert response["embed"].to_dict() == {
        "color": 16777215,
        "description": "1: Kemintiri\n" "2: Kemintiri (ADV)",
        "footer": {"text": 'Click a number or answer with one (eg. "krcg 1")'},
        "title": "What card did you mean ?",
        "type": "rich",
    }
    # vampire with comma in the name
    response = discord_bot.handle_message("tariq")
    assert response["embed"]
    assert response["embed"].to_dict() == {
        "color": 16777215,
        "description": "1: Tariq, The Silent\n" "2: Tariq, The Silent (ADV)",
        "footer": {"text": 'Click a number or answer with one (eg. "krcg 1")'},
        "title": "What card did you mean ?",
        "type": "rich",
    }
    # card with column in the name
    response = discord_bot.handle_message("condemnation")
    assert response["embed"]
    assert response["embed"].to_dict() == {
        "color": 16777215,
        "description": "1: Condemnation: Betrayed\n"
        "2: Condemnation: Doomed\n"
        "3: Condemnation: Languid\n"
        "4: Condemnation: Mute\n"
        "5: Consanguineous Condemnation",
        "footer": {"text": 'Click a number or answer with one (eg. "krcg 1")'},
        "title": "What card did you mean ?",
        "type": "rich",
    }
    # short easter egg
    response = discord_bot.handle_message("no")
    assert response["embed"]
    assert response["embed"].title == "Direct Intervention"
