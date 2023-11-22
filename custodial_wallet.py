from cobo_custody.signer.local_signer import generate_new_key,LocalSigner
from cobo_custody.client import Client
from cobo_custody.config import DEV_ENV
from cobo_custody.signer.local_signer import LocalSigner
import time

api_secret, api_key = generate_new_key() # Generate api_secret and api_key
signer = LocalSigner(api_secret) # Initial singner
coin_code = "GETH"  # Your testing coin
amount = 10000000000000000  # Withdrawal amount：0.01GETH
to_address = "your address"  # Your external address

print("api_secret : " + api_secret)
print("api_key : " + api_key)


# Initialize Cobo Client
client = Client(signer=signer, env=DEV_ENV, debug=True)


# Check if GETH has been added in your wallet
response = client.get_coin_info(coin=coin_code)
print(f"Get Coin Info: {response.result}")


# Create GETH address
response = client.new_deposit_address(coin=coin_code)
print(f"New Deposit Address: {response.result}")


# Get deposit transaction
response = client.get_transactions_by_time(side="deposit", limit="1")
print(f"Get Transactions By Time: {response.result}")


# Withdraw 0.01GETH
request_id = f"ApiTransaction-{int(time.time() * 1000)}"    # Your custom request_id
response = client.withdraw(
    coin=coin_code,
    request_id=request_id,
    amount=amount,
    address=to_address,
)
print(f"Withdraw: {response.result}")


# Get transaction by request_id
response = client.get_transactions_by_request_ids(request_ids=request_id)
print(f"Get Transactions By Request Ids： {response.result}")




