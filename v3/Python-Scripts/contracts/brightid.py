from . import utils


def addContext(context, private_key):
    func = utils.contracts['brightid'].functions.addContext(context)
    tx_hash = utils.send_transaction(func, 0, private_key)
    return tx_hash

def addNodeToContext(context, node_address, private_key):
    node_address = utils.w3.toChecksumAddress(node_address)
    func = utils.contracts['brightid'].functions.addNodeToContext(context, node_address)
    tx_hash = utils.send_transaction(func, 0, private_key)
    return tx_hash

def register(context, contextIds, v, r, s, private_key):
    func = utils.contracts['brightid'].functions.register(context, contextIds, v, r, s)
    tx_hash = utils.send_transaction(func, 0, private_key)
    return tx_hash

def isContext(context):
    func = utils.contracts['brightid'].functions.isContext(context)
    resp = utils.send_eth_call(func)
    return resp

def isNodeInContext(context, node_address):
    func = utils.contracts['brightid'].functions.isNodeInContext(context, node_address)
    resp = utils.send_eth_call(func)
    return resp

def isUniqueHuman(ethAddress, context):
    ethAddress = utils.w3.toChecksumAddress(ethAddress)
    func = utils.contracts['brightid'].functions.isUniqueHuman(ethAddress, context)
    resp = utils.send_eth_call(func)
    return resp
