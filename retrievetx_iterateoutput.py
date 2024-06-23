from bitcoin.rpc import RawProxy

p = RawProxy()

# Alice tx ID
txid = "466200308696215bbc949d5141a49a4138ecdfdfaa2a8029c1f9bcecd1f96177"

# Retrieve raw tx in hex
raw_tx = p.getrawtransaction(txid)
print(raw_tx)

# Decode tx hex into JSON object
decoded_tx = p.decoderawtransaction(raw_tx)
print(decoded_tx)

# Retrieve each output from tx
for output in decoded_tx['vout']:
    print(output['scriptPubKey']['address'], output['value'])