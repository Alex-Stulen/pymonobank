from dataclasses import dataclass

from pymonobank.schemas import BaseDataclass
from pymonobank.utils.currencies import Currencies


__all__ = (
    'InvoiceData',
    'StatusInvoiceData'
)


@dataclass
class InvoiceData(BaseDataclass):
    amount: int | float
    ccy: int = Currencies.UAH  # Currency. Default: UAH
    redirectUrl: str = ''
    webHookUrl: str = ''
    validity: int = 86400  # Invoice alive seconds. Default: 24 hour
    paymentType: str = 'debit'  # Payment type. Enum: "debit" "hold". Default: 'debit'
    qrId: str = ''  # QR cashier ID to set the payment amount on existing QR cashiers


@dataclass
class StatusInvoiceData(BaseDataclass):
    invoiceId: str
