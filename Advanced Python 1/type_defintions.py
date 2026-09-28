from typing import List, Tuple, Dict, Union, Any, Optional, Set, FrozenSet, Iterable, Callable, TypeVar, Generic, Type, Protocol, runtime_checkable

# List
numbers: List[int] = [1,2,3,4,5]

# Tuple
person: Tuple[str, int, float] = ("Zarish", 21, 5.11)

#dict
person: Dict[str, Union[str, int]] = {"name": "Zarish", "age": 21}

#union
identifier: Union[int, str] = "ID123"

#Any
identifier: Any = "ID123"
#Optional
age: Optional[int] = None


n : int = 5

name: str = "Zarish"


def sum(a: int,b:int) -> int:
    return a+b

sum(2,4)