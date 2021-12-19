from brownie import Contract, interface, multicall


def main():
    price_feed = Contract.from_abi(
        "feed",
        "0xaEA2808407B7319A31A383B6F8B60f04BCa23cE2",
        interface.AggregatorV3Interface.abi,
    )
    rounds = []
    latest_round = price_feed.latestRoundData()[0]
    multicall(address="0x5BA1e12693Dc8F9c48aAD8770482f4739bEeD696")
    with multicall:
        for round_id in range(latest_round, latest_round - 50, -1):
            round_data = price_feed.getRoundData(round_id)
            rounds.append(round_data)
    print(rounds)
