"""Object adapter converts a payment provider's API."""
class StripeLike:
    def charge(self, cents): return f"charged {cents} cents"
class PaymentAdapter:
    def __init__(self, provider): self.provider = provider
    def pay(self, dollars): return self.provider.charge(dollars * 100)

print(PaymentAdapter(StripeLike()).pay(12))
