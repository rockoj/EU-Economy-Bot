##this files is where the database stores info about money





#general form of a wallet will be
#{
#   "name"   :"eulerthedestroyer",
#   "id"     :464954455029317633,
#   "type"   :"personal",
#   "balance": 5
#}
import PyMongo
from pymongo import MongoClient
import pprint
import methods

client = MongoClient('ADIPAT FILL THIS IN')
db = client.database


def send(guild, from_wallet, to_wallet, amount):
    guild_collection =db[guild]
    from_wallet_id = methods.get_wallet(guild, from_wallet)
    to_wallet_id =methods.get_wallet(guild, to_wallet)
    if(from_wallet_id[0] and to_wallet_id[0])
        sender_account = guild_collection.find_one(posts.find_one({"id": from_wallet_id[1]}))
        reciever_account = guild_collection.find_one(posts.find_one({"id": to_wallet_id[1]}))
        if(sender_account is not None):
            if(reciever_account is not None):
                if(sender_account["balance"] > amount):

                else:
                    return (False, "insufficent funds")
            else:
                return (False, "reciever account not found")   
        else:
           return (False, "sender account not found") 
    else:
        return (False, "cannot find wallet")


    pass

def get_balance(guild,wallet):
    pass
def alter_money(guild, amount,wallet):
    pass
def set_money(guild, amount, wallet):
    pass