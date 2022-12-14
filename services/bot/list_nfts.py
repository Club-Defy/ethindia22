import json

import discord
import requests

from config.config import fetch_owned_nfts
from services.bot.transfer import get_address_from_ens


def list_erc721(address):
    url = fetch_owned_nfts
    headers = {"accept": "application/json"}
    response = requests.get(url, params={"owner": get_address_from_ens(address), "withMetadata": "true", "pageSize": 10}, headers=headers)
    data = response.json()
    nft_list_response = []
    if data["ownedNfts"]:
        for nft in data["ownedNfts"]:
            embed = discord.Embed(
                title=nft["contract"]["address"],
                url=nft["media"][0]["gateway"])\
                .add_field(name="TokenId", value=int(nft["id"]["tokenId"], 16))\
                .set_thumbnail(url=nft["media"][0]["gateway"])
            nft_list_response.append(embed)

    return nft_list_response
