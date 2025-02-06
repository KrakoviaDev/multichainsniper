


# 📖 Introduction
The **FASTEST** Solana bot on GitHub

<img src="https://files.catbox.moe/uvignr.gif" width="400" alt="image">


# ✨ Quickstart

This project has been made for Python 3.11

## 🛠️ Installation

**Install Python 3.11** [Python 3.11.](https://www.python.org/downloads/)
**IMPORTANT**: When installing Python, tick the box "Add python to path" and "Use admin privileges when installing py.exe".

**Open your terminal/cmd**

💾 **Clone this repository**
```sh
git clone https://github.com/KrakoviaDev/solana-raydium-sniper
```

💾 **Navigate to the repository**
```sh
cd solana-raydium-sniper
```
💻 **Install/upgrade pip =**
```sh
python -m pip install --upgrade pip
```
💻 **Install the required libs**
```sh
pip install -r requirements.txt
```
▶️ **Start**
```sh
python main.py
```
![image](https://files.catbox.moe/we7imi.png)
![image](https://files.catbox.moe/l02bx1.png)
# 🤖 Sniper Bot

### ⚙️ How it works
The bot continually sends requests to [Solana].<br>
If the token is available to purchase, the transaction will execute quickly.<br>
Please note that only tokens with sufficient liquidity and on-chain metadata are listed in Jupiter API: min. 250$ liquidity and buy/sell price impact are below 30%.<br>
When these criteria are met, it will take a few minutes to automatically add the token.<br>

### 🆕 Add a token to snipe
- Add as many wallets as necessary
- Token/Project name
- Token Address
- Amount ($) to buy
- Take Profit ($)
- Stop Loss ($)
- Slippage (%)

If token has a launch date:
- Month
- Day
- Hours
- Minutes

### 🔭 Watch token
You can watch your trading position by selecting the token.<br>

### ✍🏻 Edit tokens
You can modify token info as follow:
- Name
- Address
- Selected Wallet
- Buy Amount
- Take Profit
- Stop Loss
- Slippage
- Launch date
- Delete

# Q&A
### Where are my private keys?
*Your private keys are stored in `wallets.json`.*
### Is there any fees when swapping using the bot?
*There are no additional fees when performing swaps via the CLI; the costs should be the same as using the Jupiter UI.*
### Does sniper bot remains running if I close it?
*If you close the terminal, the sniper bot will stop running.* 



# MY OTHER PROJECT FOR SALE: Multichainsniper
Multi chain and multi wallet sniper that works on a variety of decentralized exchanges as well. Optimized methods are used in order to make this one of the fastest, if not the fastest sniper on the market

## Interested in buying?
Sales have reopened. Message me on telegram if you are interested
- [Telegram](https://t.me/nonlinearlogic)


### Supported chains and exchanges
- Ethereum
    - Uniswap
    - Sushiswap

- Binance smart chain
    - Pancakeswap
    - Sushiswap
    - Apeswap
    - Backeryswap

- Polygon Matic
    - Quickswap
    - Apeswap
    - Defyn

- Kucoin Community Chain
    - Kuswap
    - KoffeSwap

- Okex Chain
    - CherrySwap

- Avalanche Mainnet C-Chain
    - Pangolin
    - Trader Joe

- Fantom Opera
    - Spirit Swap
    - Spooky Swap
    - Protofi

- Cronos Mainnet beta
    - Meerkat
    - VVS Finance
    - Cronaswap

- Harmony chain shard 0
    - Viper

- Metis Andromeda Mainnet
    - Netswap
    - Tethys


### Innovative UI
The bot has a UI which runs in the terminal, this allows you to run the bot on remote servers without needing a display server or having to play with virtual displays as you would with normal UIs.

![Loading screen](https://i.imgur.com/Rave54x.png)
![Working screen](https://i.imgur.com/Kl8FY6u.png)

### Current features
- Multi wallet support
- Support for custom pairs (Tokens that are paired to a different coin than the default one of the exchange)
- Instant buy functionality, you can make the bot Instantly skipping it's normal flow in case something changes after you've started it.
- Automatically detect owner, max buy, trading open functions and sell triggering functions (ex. mint, blacklist and so on)
- Mempool scan for liquidity scanning & trading open scanning
- Option to send multiple buy transactions at the same time (99% all get in the same block at relatively near positions from each other, depends also on the node you use)
- Honeypot prevention, you can set the bot to check if the token is a honeypot before buying.
- Max buy tax and max sell tax prevention, the bot will only sell if the current tax is below the amount you set.
- Anti-bot prevention, options to skip blocks/seconds after liquidity detection, option to skip blocks/seconds after trading enable detection, minimum liquidity check (to be added in v1.0.1) 
- Anti rug

### Changelogs

#### Version 1.0.0
- Initial release
- Added TUI (Text user interface), it's like GUI but you can run your bot in the terminal)
- Added support for multiple wallets
- Added automatic trading enable function detection
- Added automatic bad functions (sell triggering) detection
- Added automatic owner address detection
- Improved mempool speed and overall performance
- Improved sending transactions speed
- Option to change secondary wallets on your own

#### Version 1.0.1
- Fix small bugs from version 1.0.0
- Add option to set gas price and gas limit also from UI rather than config only
- Add netswap and Tethys on Metis chain

#### Version 1.0.2
- Support for ethereum chain and it's new gas system
- Support for buying exact amount of tokens
- Add missing chains and exchanges
- Fix bugs from version 1.0.1

#### Version 1.0.3
- Add rug pull prevention (sell when liquidity is about to be removed or when a bad function is about to be called on the token contract)
- Add option to scroll the token functions table at startup screen
- Add IPC node connection support
- Added anti rug system
- Improvements to mempool scan

#### version 1.1.0
- Implement minimum liquidity option
- Add everything related to selling the tokens, sell certain % of tokens, certain amounts of tokens. Sell based on take profit and stop loss


#### version 1.2.0
- Telegram scrapper added (features in telegram)


#### version 1.3.0
- Contract buy mode added (anti blacklist)
- You will have to deploy a contract on each corresponding chain!

#### version 1.3.1 
- Refactoring/performance improvements
