from pymonobank.core.invoice import MonoInvoice
from pymonobank.core.merchant import MonoMerchant


__all__ = (
    'Mono',
)


class Mono(MonoInvoice, MonoMerchant):

    def __init__(self, token: str):
        super().__init__(token=token)
