from typing import Any
from django.forms import CheckboxSelectMultiple


class ServicoCheckbox(CheckboxSelectMultiple):
    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
        )
        if value:
            option["attrs"]["data-preco"] = value.instance.preco
        return option