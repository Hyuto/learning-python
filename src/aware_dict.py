from typing import Any, Dict, Optional


class AwareDict(Dict[Any, Any]):
    """Dictionary with awareness of change

    Example:
        Logging change

        >>> dict_ = AwareDict({"a": 2})
        >>> dict_["b"] = 3
        {'a': 2, 'b': 3}
    """

    def __init__(self, initialDict: Dict[Any, Any], _main: Optional[Dict[Any, Any]] = None) -> None:
        for k, v in initialDict.items():
            if isinstance(v, Dict):
                initialDict[k] = AwareDict(v, _main=self)
        super().__init__(initialDict)

        if _main is not None:
            self._main = _main
        else:
            self._main = self

    def __setitem__(self, item: Any, value: Any) -> None:
        if isinstance(value, Dict):
            _value = AwareDict(value, _main=self)
        else:
            _value = value
        super().__setitem__(item, _value)
        print(self._main)
