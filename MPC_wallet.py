from cobo_custody.signer.local_signer import generate_new_key,LocalSigner
from cobo_custody.client.mpc_client import MPCClient
from cobo_custody.config import DEV_ENV
from cobo_custody.signer.local_signer import LocalSigner
import time

api_secret, api_key = generate_new_key() # Generate api_secret and api_key
signer = LocalSigner(api_secret) # Initial singner
coin_code = "GETH"  # Your testing coin
chain_code = "GETH"  # Your testing chain
amount = 10000000000000000  # Withdrawal amount：0.01GETH
from_address = "your mpc wallet address"  # Your MPC wallet address
to_address = "your address"  # Your external address

print("api_secret : " + api_secret)
print("api_key : " + api_key)


# Initialize Cobo Client
mpc_client = MPCClient(signer=LocalSigner(api_secret), env=DEV_ENV, debug=False)


# Create GETH address
response = mpc_client.generate_addresses(chain_code=chain_code, count=1)
print(f"New Deposit Address: {response.result}")


# Get deposit transaction
response = mpc_client.list_transactions(transaction_type=1000, order_by="created_time", order="DESC", limit=1)
print(f"Get Transactions By Time: {response.result}")

# Get estimated gas fee
response = mpc_client.estimate_fee(coin=coin_code, amount=1, address=to_address)
print(f"Get Estimated Gas Fee: {response.result}")

# Withdraw 0.01GETH
request_id = f"MPCTransaction-{int(time.time() * 1000)}"  # Your custom request_id
response = mpc_client.create_transaction(
    coin=coin_code,
    request_id=request_id,
    amount=amount,
    from_addr=from_address,
    to_addr=to_address,
)
print(f"Withdraw: {response.result}")

# Get transaction by request_id
response = mpc_client.transactions_by_request_ids(request_id)
print(f"Get Transactions By Request Ids： {response.result}")



