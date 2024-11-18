class Urls:

    def __init__(self, base_url):
        self.base_url = base_url

    def url_admin(self, add_url="administration/"):
        return self.base_url + add_url

    def url_reg(self, add_url="/index.php?route=account/register"):
        return self.base_url + add_url

    def url_cataloge(self, add_url="/en-gb/catalog/"):
        return self.base_url + add_url


