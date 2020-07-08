from typing import Iterable, Callable, Union, Coroutine, Type, Dict

from coc.client import Client
from coc.players import Player, ClanMember
from coc.clans import Clan
from coc.wars import ClanWar
from coc.war_attack import WarAttack

_ClanType = Type[Clan]
_PlayerType = Type[Player]
_CustomClassType = Union[Type[Clan], Type[Player], Type[ClanWar]]
_EventPredicateClasses = Union[Clan, Player, ClanWar, ClanMember, WarAttack]
_EventCallbackType = Callable[[_EventPredicateClasses, _EventPredicateClasses], Coroutine]
_EventCallbackCustomArgumentsType = Callable[..., Coroutine]
_EventPredicateType = Callable[[_EventPredicateClasses, _EventPredicateClasses], bool]
_EventWrappedPredicateType = Callable[
    [_EventPredicateClasses, _EventPredicateClasses, _EventCallbackType], Coroutine[None]
]
_EventDecoratorReturn = Callable[[_EventCallbackType], _EventCallbackType]

class ClanEvents:
    event_type: str
    @classmethod
    def name(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def badge(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def level(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def points(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def versus_points(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def member_count(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def location(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def type(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def required_trophies(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def war_frequency(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def war_win_streak(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def war_wins(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def war_ties(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def war_losses(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def public_war_log(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def description(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def war_league(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def labels(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def member_join(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def member_leave(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def member_name(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def member_role(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def member_exp_level(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def member_league(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def member_trophies(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def member_clan_rank(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def member_clan_previous_rank(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def member_donations(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def member_received(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def member_versus_trophies(cls, tags: Iterable = None, custom_class: _ClanType = Clan, retry_interval: int = None) -> _EventDecoratorReturn: ...

class PlayerEvents:
    event_type: str
    @classmethod
    def achievement_change(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def name(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def exp_level(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def trophies(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def versus_trophies(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def clan_rank(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def clan_previous_rank(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def donations(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def received(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def league(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def role(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def best_trophies(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def war_stars(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def town_hall(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def town_hall_weapon(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def builder_hall(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def best_versus_trophies(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def versus_attack_wins(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def legend_statistics(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def labels(cls, tags: Iterable = None, custom_class: _PlayerType = Player, retry_interval: int = None) -> _EventDecoratorReturn: ...

class WarEvents:
    event_type: str
    @classmethod
    def war_attack(cls, tags: Iterable = None, custom_class: Type[ClanWar] = ClanWar, retry_interval: int = None) -> _EventDecoratorReturn: ...
    @classmethod
    def state(cls, tags: Iterable = None, custom_class: Type[ClanWar] = ClanWar, retry_interval: int = None) -> _EventDecoratorReturn: ...

class ClientEvents:
    @classmethod
    def maintenance_start(cls): ...
    @classmethod
    def maintenance_completion(cls): ...
    @classmethod
    def keys_reset(cls): ...
    @classmethod
    def event_error(cls): ...
    @classmethod
    def clan_loop_start(cls): ...
    @classmethod
    def clan_loop_finish(cls): ...
    @classmethod
    def player_loop_start(cls): ...
    @classmethod
    def player_loop_finish(cls): ...
    @classmethod
    def war_loop_start(cls): ...
    @classmethod
    def war_loop_finish(cls): ...

class EventsClient(Client):
    clan_retry_interval: int
    player_retry_interval: int
    war_retry_interval: int

    clan_cls: Type[Clan]
    player_cls: Type[Player]
    war_cls: Type[ClanWar]

    _player_updates: set
    _clan_updates: set
    _war_updates: set

    _listeners: Dict


    is_cwl_active: bool

    def add_clan_updates(self, value: Union[Iterable, str]) -> None: ...
    def add_player_updates(self, value: Union[Iterable, str]) -> None: ...
    def add_war_updates(self, value: Union[Iterable, str]) -> None: ...
    def event(self, event: Callable) -> Callable: ...
    def add_events(self, *events: Callable) -> None: ...
    def remove_events(self, *events: Callable) -> None: ...
    def run_forever(self) -> None: ...
    def close(self) -> None: ...
    async def event_error(self, exception, *args, **kwargs) -> None: ...