from brownie import Contract, interface, multicall
from datetime import datetime
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def main():
    price_feed = Contract.from_abi(
        "feed",
        "0xaEA2808407B7319A31A383B6F8B60f04BCa23cE2",
        interface.AggregatorV3Interface.abi,
    )
    answers = []
    time_stamps = []
    latest_round = price_feed.latestRoundData()[0]
    multicall(address="0x5BA1e12693Dc8F9c48aAD8770482f4739bEeD696")
    with multicall:
        for round_id in range(latest_round, latest_round - 50, -1):
            round_data = price_feed.getRoundData(round_id)
            answers.append(round_data[1])
            time_stamps.append(datetime.fromtimestamp(round_data[3]))
    plt.plot(time_stamps, answers)
    plt.show()
