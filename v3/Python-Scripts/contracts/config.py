from web3.auto import w3

INFURA_URL = ''

BRIGHTID_NODE_URL = ''

private_key_1 = ''
private_key_2 = ''
private_key_3 = ''

ABIES = {
    'brightid':
        '[{"stateMutability": "nonpayable", "inputs": [], "type": "constructor", "payable": false}, {"inputs": [{"indexed": false, "type": "bytes32", "name": "context", "internalType": "bytes32"}, {"indexed": false, "type": "bytes32", "name": "contextId", "internalType": "bytes32"}, {"indexed": false, "type": "address", "name": "ethAddress", "internalType": "address"}], "type": "event", "name": "AddressLinked", "anonymous": false}, {"inputs": [{"indexed": true, "type": "bytes32", "name": "context", "internalType": "bytes32"}, {"indexed": true, "type": "address", "name": "owner", "internalType": "address"}], "type": "event", "name": "ContextAdded", "anonymous": false}, {"inputs": [{"indexed": true, "type": "bytes32", "name": "context", "internalType": "bytes32"}, {"indexed": false, "type": "address", "name": "nodeAddress", "internalType": "address"}], "type": "event", "name": "NodeFromContextRemoved", "anonymous": false}, {"inputs": [{"indexed": true, "type": "bytes32", "name": "context", "internalType": "bytes32"}, {"indexed": false, "type": "address", "name": "nodeAddress", "internalType": "address"}], "type": "event", "name": "NodeToContextAdded", "anonymous": false}, {"inputs": [], "constant": true, "name": "id", "outputs": [{"type": "uint256", "name": "", "internalType": "uint256"}], "stateMutability": "view", "payable": false, "type": "function"}, {"inputs": [{"type": "bytes32", "name": "context", "internalType": "bytes32"}], "constant": true, "name": "isContext", "outputs": [{"type": "bool", "name": "", "internalType": "bool"}], "stateMutability": "view", "payable": false, "type": "function"}, {"inputs": [{"type": "bytes32", "name": "context", "internalType": "bytes32"}, {"type": "address", "name": "nodeAddress", "internalType": "address"}], "constant": true, "name": "isNodeInContext", "outputs": [{"type": "bool", "name": "", "internalType": "bool"}], "stateMutability": "view", "payable": false, "type": "function"}, {"inputs": [{"type": "bytes32", "name": "context", "internalType": "bytes32"}, {"type": "bytes32[]", "name": "cIds", "internalType": "bytes32[]"}, {"type": "uint8", "name": "v", "internalType": "uint8"}, {"type": "bytes32", "name": "r", "internalType": "bytes32"}, {"type": "bytes32", "name": "s", "internalType": "bytes32"}], "constant": false, "name": "register", "outputs": [], "stateMutability": "nonpayable", "payable": false, "type": "function"}, {"inputs": [{"type": "address", "name": "ethAddress", "internalType": "address"}, {"type": "bytes32", "name": "context", "internalType": "bytes32"}], "constant": true, "name": "isUniqueHuman", "outputs": [{"type": "bool", "name": "", "internalType": "bool"}, {"type": "address[]", "name": "", "internalType": "address[]"}], "stateMutability": "view", "payable": false, "type": "function"}, {"inputs": [{"type": "bytes32", "name": "context", "internalType": "bytes32"}], "constant": false, "name": "addContext", "outputs": [], "stateMutability": "nonpayable", "payable": false, "type": "function"}, {"inputs": [{"type": "bytes32", "name": "context", "internalType": "bytes32"}, {"type": "address", "name": "nodeAddress", "internalType": "address"}], "constant": false, "name": "addNodeToContext", "outputs": [], "stateMutability": "nonpayable", "payable": false, "type": "function"}, {"inputs": [{"type": "bytes32", "name": "context", "internalType": "bytes32"}, {"type": "address", "name": "nodeAddress", "internalType": "address"}], "constant": false, "name": "removeNodeFromContext", "outputs": [], "stateMutability": "nonpayable", "payable": false, "type": "function"}]',
}

ADDRESSES = {
    'brightid':
    w3.toChecksumAddress(''),
}

GAS = 500 * 10**3
GAS_PRICE = 5 * 10**9
