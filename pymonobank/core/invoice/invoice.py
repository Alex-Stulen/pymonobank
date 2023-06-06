import requests

from pymonobank.core.api import MonoApi
from pymonobank.request import RequestMethods

from .schemas import InvoiceData, StatusInvoiceData


class MonoInvoice(MonoApi):
    CREATE = MonoApi.BASE_URL + '/api/merchant/invoice/create'
    STATUS = MonoApi.BASE_URL + '/api/merchant/invoice/status'

    def __init__(self, token: str):
        super().__init__(token=token)

    def create_invoice(self, invoice_data: InvoiceData) -> requests.Response:
        """
        Create invoice for payment

        :param invoice_data:
        :return: requests.Response
        """

        return self.request(
            url=self.CREATE,
            method=RequestMethods.POST,
            data=invoice_data.as_dict()
        )

    def invoice_status(self, invoice_data: StatusInvoiceData) -> requests.Response:
        """
        Method of checking the status of the account when the seller is out of sync or there is no webHookUrl
        when creating the account

        :param invoice_data:
        :return: requests.Response
        """

        return self.request(
            url=self.STATUS,
            method=RequestMethods.GET,
            params=invoice_data.as_dict()
        )
