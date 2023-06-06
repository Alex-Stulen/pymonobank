import requests

from pymonobank.core.api import MonoApi
from pymonobank.request import RequestMethods


__all__ = (
    'MonoMerchant',
)


class MonoMerchant(MonoApi):
    MERCHANT_INFO = MonoApi.BASE_URL + '/api/merchant/details'

    def get_merchant_info(self) -> requests.Response:
        """
        Returns information about the merchant

        :return: requests.Response
        """

        return self.request(
            url=self.MERCHANT_INFO,
            method=RequestMethods.GET
        )
